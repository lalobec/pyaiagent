import os
import subprocess

from google.genai import types


def run_python_file(working_directory, file_path):
    abs_working = os.path.abspath(working_directory)
    abs_file_path = os.path.abspath(os.path.join(working_directory, file_path))
    if os.path.commonpath([abs_file_path, abs_working]) != abs_working:
        return f'Error: Cannot execute "{file_path}" as it is outside'\
            'the permitted working directory'
    if not os.path.exists(abs_file_path):
        return f'Error: File "{file_path}" not found.'
    if not abs_file_path.endswith(".py"):
        return f'Error: "{abs_file_path}" is not a Python file.'
    # print("Processing file in a particular way...")
    # print(abs_file_path)
    try:
        test = subprocess.run(["python", abs_file_path], capture_output=True,
                              timeout=30)
        print(test.stdout)
        print(test.stderr)
        output = f'STDOUT: {test.stdout}, STDERR: {test.stderr}'
        if test.returncode != 0:
            output += f'\nProcess exited with code {test.returncode}'
        return output
    except Exception as e:
        return f"Error: executing Python file: {e}"


schema_run_python_file = types.FunctionDeclaration(
    name="run_python_file",
    description="Executes a Python file within the working directory and returns the output from the interpreter.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="This is the python file to execute",
            ),
            "args": types.Schema(
                type=types.Type.ARRAY,
                items=types.Schema(
                    type=types.Type.STRING,
                    description="Optional arguments to pass to the Python file.",
                ),
                description="Optional arguments to pass to the Python file.",
            ),
        },
        required=["file_path"],
    ),
)
