import os
from config import MAX_CHAR_LIMIT

def get_file_content(working_directory, file_path):
    path = os.path.join(working_directory, file_path)
    abs_path = os.path.abspath(path)
    wd_abs_path = os.path.abspath(working_directory)

    if not abs_path.startswith(wd_abs_path):
        return f'Error: Cannot read "{file_path}" as it is outside the permitted working directory'
    
    if not os.path.isfile(abs_path):
        return f'Error: File not found or is not a regular file: "{file_path}"'
    
    try:
        with open(abs_path, 'r') as file:
            content = file.read()
            #file_string = content[:MAX_CHAR_LIMIT]
            if len(content) > MAX_CHAR_LIMIT:
                content = content[:MAX_CHAR_LIMIT] + f'[...File "{file_path}" truncated at 10000 characters].'
        return content
    except Exception as e:
        return f'Error: reading file "{file_path}": {str(e)}'