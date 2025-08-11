import os

def write_file(working_directory, file_path, content):
    path = os.path.join(working_directory, file_path)
    abs_path = os.path.abspath(path)
    wd_abs_path = os.path.abspath(working_directory)

    if not abs_path.startswith(wd_abs_path):
        return f'Error: Cannot write to "{file_path}" as it is outside the permitted working directory'
    
    if not os.path.exists(os.path.dirname(abs_path)):
        try:
            os.makedirs(os.path.dirname(abs_path))
        except Exception as e:
            return f'Error: creating directories for "{file_path}": {str(e)}'

    try:
        with open(abs_path, 'w') as file:
            file.write(content)
        return f'Successfully wrote to "{file_path}" ({len(content)} characters written)'
    
    except Exception as e:
        return f'Error: writing to file "{file_path}": {str(e)}'