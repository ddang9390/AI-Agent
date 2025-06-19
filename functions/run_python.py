import os
import subprocess
from google.genai import types

schema_run_python = types.FunctionDeclaration(
    name="run_python_file",
    description="Runs the mentioned python file",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="The python file that will be ran",
            ),
        },
    ),
)

def check_if_in_directory(working_directory, file_path, dir):
    parent = os.path.abspath(working_directory)
    child = os.path.abspath(dir)
    if not child.startswith(parent):
        print(f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'
)
        return False
    
    else: 
        return True
    
def run_python_file(working_directory, file_path):
    dir = os.path.join(working_directory, file_path)

    if not check_if_in_directory(working_directory, file_path, dir):
        return 
    
    if not os.path.exists(dir):
        print(f'Error: File "{file_path}" not found.')
        return
    
    if not (dir.endswith(".py")):
        print(f'Error: "{file_path}" is not a Python file.')
        return
    
    try:
        process = subprocess.run(["python3", dir], timeout=30, capture_output=True, text=True)
        if process.stdout:
            print(f"STDOUT: {process.stdout}")
        if process.stderr:
            print(f"STDERR: {process.stderr}")

        if process.stderr == None and process.stdout == None:
            print("No output produced")
        if process.returncode != 0:
            print(f"Process exited with code {process.returncode}")

    except:
        raise f"Error: executing Python file: {file_path}"

