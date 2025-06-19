import os
from google.genai import types

MAX_CHARS = 10000

schema_get_file_content = types.FunctionDeclaration(
    name="get_file_content",
    description="Displays the content that is within the mentioned file",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="The file that will be read by the agent",
            ),
        },
    ),
)

def check_if_in_directory(working_directory, file_path, dir):
    parent = os.path.abspath(working_directory)
    child = os.path.abspath(dir)
    if not child.startswith(parent):
        print(f'Error: Cannot read "{file_path}" as it is outside the permitted working directory')
        return False
    
    else: 
        return True
    
def get_file_content(working_directory, file_path):
    dir = os.path.join(working_directory, file_path)

    if check_if_in_directory(working_directory, file_path, dir):
        if not os.path.isfile(dir):
            print(f'Error: File not found or is not a regular file: "{file_path}"')
        
        else:
            with open(dir, "r") as f:
                file_content_string = f.read()
    
                print(file_content_string[0:MAX_CHARS])
                if len(file_content_string) > MAX_CHARS:
                    print(f'[...File "{file_path}" truncated at 10000 characters]')