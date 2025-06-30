from google.genai import types
from functions.get_files_info import get_files_info, schema_get_files_info
from functions.get_file_content import get_file_content,schema_get_file_content
from functions.write_file import write_file, schema_write_file
from functions.run_python import run_python_file, schema_run_python_file

available_functions = types.Tool(
    function_declarations=[
        schema_get_files_info,
        schema_get_file_content,
        schema_run_python_file,
        schema_write_file,
    ]
)


def call_function(function_call_part, verbose=False):
    function_call_part.args["working_directory"] = "./calculator"
    if verbose:
        print(f"Calling function: "
              f"{function_call_part.name}({function_call_part.args})")
    else:
        print(f" - Calling function: {function_call_part.name}")

    if function_call_part.name == "get_files_info":
        result = get_files_info(**function_call_part.args)
    elif function_call_part.name == "get_file_content":
        result = get_file_content(**function_call_part.args)
    elif function_call_part.name == "write_file":
        result = write_file(**function_call_part.args)
    elif function_call_part.name == "run_python_file":
        result = run_python_file(**function_call_part.args)
    else:
        return types.Content(
            role="tool",
            parts=[
                types.Part.from_function_response(
                    name=function_call_part.name,
                    response={"error": f"Unknown function: \
                    {function_call_part.name}"},
                )
            ],
        )
    return types.Content(
        role="tool",
        parts=[
            types.Part.from_function_response(
                name=function_call_part.name,
                response={"result": result},
            )
        ],
    )
