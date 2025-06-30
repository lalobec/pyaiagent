import os
import sys
from dotenv import load_dotenv
from google import genai
from google.genai import types
from prompts import system_prompt
from call_function import available_functions, call_function


def main():
    load_dotenv()
    if len(sys.argv) == 1:
        print("No argument given...")
        sys.exit(1)

    user_prompt = sys.argv[1]
    verbose = "--verbose" in sys.argv

    api_key = os.environ.get("GEMINI_API_KEY")
    client = genai.Client(api_key=api_key)

    if verbose:
        print(f"User prompt: {user_prompt}\n")

    messages = [
        types.Content(role="user", parts=[types.Part(text=user_prompt)]),
    ]

    for i in range(20):
        if i == 19:
            print("Maximum iterations reached, exiting the program...")
            sys.exit(1)

        try:
            final_response = generate_content(client, messages, verbose)
            if final_response:
                print(final_response)
                break
        except Exception as e:
            print(f'Error in generate_content function: {e}')


def generate_content(client, messages, verbose):
    response = client.models.generate_content(
        model="gemini-2.0-flash-001",
        contents=messages,
        config=types.GenerateContentConfig(
            tools=[available_functions],
            system_instruction=system_prompt),
    )

    if verbose:
        print(f"Prompt tokens: {response.usage_metadata.prompt_token_count}")
        print(f"Response tokens:\
        {response.usage_metadata.candidates_token_count}")

    if response.candidates:
        for response_candidate in response.candidates:
            # print("respp")
            # print(response_candidate.content)
            # print(f'number of messages {len(messages)}')
            messages.append(response_candidate.content)
            # print(f'number of messages {len(messages)}')

    if not response.function_calls:
        return response.text

    function_responses = []
    for function_call_part in response.function_calls:
        # print(f"Calling function: {function_call_part.name}"
        #      f"({function_call_part.args})")
        function_call_result = call_function(function_call_part, verbose)
        # print("The second step for adding the types.Content from the call")
        # print(type(function_call_result))
        if (
                not function_call_result.parts
                or not function_call_result.parts[0].function_response
        ):
            raise Exception("empty function call result")
        try:
            if verbose:
                print(f"-> {function_call_result.parts[0].function_response.response}")
        except Exception as e:
            raise f'whhaaaaat is going ooonnn...!!!! {e} !!'
        function_responses.append(function_call_result.parts[0])

    if not function_responses:
        raise Exception("no function responses generated, exiting the program")

    messages.append(types.Content(role="tool", parts=function_responses))


if __name__ == "__main__":
    main()
