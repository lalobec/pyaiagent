def get_files_info(working_directory, directory=None):
    if directory not in working_directory:
        print(f'Error: Cannot list "{directory}" as it is outside the permitted working directory')
    if not directory.startswith("/"):
        print(f'Error: "{directory}" is not a directory')

    print(f'README.md: file_size={something} bytes, is_dir={os.path.isdir(directory)}')
    print(f'src: file_size={something} bytes, is_dir={os.path.isdir(directory)}')
    print(f'package.json: file_size={something} bytes, is_dir={os.path.isdir(directory)}')
