import os

def get_files_info(working_directory, directory="."):
    path = os.path.join(working_directory, directory)

    abs_path = os.path.abspath(path)
    wd_abs_path = os.path.abspath(working_directory)

    if not abs_path.startswith(wd_abs_path):
        return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'
    
    if not os.path.isdir(path):
        return f'Error: {directory}" is not a directory'
    
    dir_contents = os.listdir(path)
    if not dir_contents:
        return f'No files found in directory "{directory}"'
    
    dir_info = map(lambda item: f" - {item}: file_size={os.path.getsize(os.path.join(path, item))} bytes, is_dir={os.path.isdir(os.path.join(path, item))}", dir_contents)

    return "\n".join(dir_info)