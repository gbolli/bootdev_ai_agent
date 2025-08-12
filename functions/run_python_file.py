import os
import sys
import subprocess

def run_python_file(working_directory, file_path, args=[]):
    path = os.path.join(working_directory, file_path)
    abs_path = os.path.abspath(path)
    wd_abs_path = os.path.abspath(working_directory)

    if not abs_path.startswith(wd_abs_path):
        return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'
    
    if not os.path.isfile(abs_path):
        return f'Error: File "{file_path}" not found.'
    
    if not abs_path.endswith('.py'):
        return f'Error: "{file_path}" is not a Python file.'

    try:
        command = [sys.executable, abs_path] + args
        result = subprocess.run(command, timeout=30, capture_output=True, text=True)
        if result.returncode != 0:
            return f'Error: running file "{file_path}": {result.stderr}. Process exited with code {result.returncode}'
        if not result.stdout:
            return f'No output produced.'

        result_string = f"STDOUT: {result.stdout}, STDERR: {result.stderr}"
        return result_string
    except Exception as e:
        return f"Error: executing Python file: {e}"