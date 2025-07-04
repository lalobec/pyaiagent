import os
from google.genai import types


def get_files_info(working_directory, directory=None):
    abs_working = os.path.abspath(working_directory)
    if directory is None:
        abs_dir = abs_working
    else:
        abs_dir = os.path.abspath(os.path.join(working_directory, directory))
    # print(abs_working)
    # print(abs_dir)
    if os.path.commonpath([abs_dir, abs_working]) != abs_working:
        return f'Error: Cannot list "{abs_dir}" as it is '\
            'outside the permitted working directory'
    if not os.path.isdir(abs_dir):
        return f'Error: "{abs_dir}" is not a directory'

    try:
        # print("------ Console print ------")
        dir_content = os.listdir(abs_dir)
        info_data = ""
        for file in dir_content:
            abs_file_dir = os.path.join(abs_dir, file)
            info_data += f'{file}: file_size={os.path.getsize(abs_file_dir)} '\
                'bytes, is_dir = {os.path.isdir(abs_file_dir)}\n'

        return info_data

    except Exception as e:
        return f"Error: Something bad happened {e}"


schema_get_files_info = types.FunctionDeclaration(
    name="get_files_info",
    description="Lists files in the specified directory along with their\
     sizes, constrained to the working directory.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "directory": types.Schema(
                type=types.Type.STRING,
                description="The directory to list files from, relative to\
                the working directory. If not provided, lists files in the\
                working directory itself.",
            ),
        },
    ),
)
