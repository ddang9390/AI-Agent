import os

MAX_CHARS = 10000

#Schema that tells the LLM how to use the function
schema_get_files_info = types.FunctionDeclaration(
    name="get_files_info",
    description="Lists files in the specified directory along with their sizes, constrained to the working directory.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "directory": types.Schema(
                type=types.Type.STRING,
                description="The directory to list files from, relative to the working directory. If not provided, lists files in the working directory itself.",
            ),
        },
    ),
)

def get_files_info(working_directory, directory=None):
    dir = os.path.join(working_directory, directory)
    if os.path.isdir(dir):
        parent = os.path.abspath(working_directory)
        child = os.path.abspath(dir)
        if child.startswith(parent):
            print_directory_contents(dir)
        else:
            print(f'Error: Cannot list "{directory}" as it is outside the permitted working directory')
    else:
        print(f'Error: "{directory}" is not a directory')

def print_directory_contents(dir):
    dir_contents = os.listdir(dir)
    for x in dir_contents:
        path = os.path.join(dir, x)

        name = x
        size = os.path.getsize(path)
        is_dir = os.path.isdir(path)
        print(f"- {name}: file_size={size} bytes, is_dir={is_dir}")

