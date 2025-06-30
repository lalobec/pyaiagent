import os
from google.genai import types


def write_file(working_directory, file_path, content):
    abs_working = os.path.abspath(working_directory)
    abs_file_path = os.path.abspath(os.path.join(working_directory, file_path))
    if os.path.commonpath([abs_file_path, abs_working]) != abs_working:
        return f'Error: Cannot write to "{file_path}" as it is outside the permitted working directory'
    os.makedirs(os.path.dirname(abs_file_path), exist_ok=True)
    try:
        with open(abs_file_path, 'w') as f:
            f.write(content)
        return f'Successfully wrote to "{file_path}" ({len(content)} characters written)'
    except Exception as e:
        return f'Error: Something bad happened in the write_file function {e}'


schema_write_file = types.FunctionDeclaration(
    name="write_file",
    description="Create a file or overwrite if exists with the content\
    argument",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="If the file_path does not exist, create it",
            ),
            "content": types.Schema(
                type=types.Type.STRING,
                description="This is the content to write in the file",
            ),
        },
    ),
)
