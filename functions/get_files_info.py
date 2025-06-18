import os

MAX_CHARS = 10000

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

def write_file(working_directory, file_path, content):
    dir = os.path.join(working_directory, file_path)

    if check_if_in_directory(working_directory, file_path, dir):
        if os.path.isdir(dir):
            print(f'Error: "{file_path}" is a directory, not a file')
            return
        
        if not os.path.exists(dir):
            with open(dir, "x") as f:
                f.write("")

        with open(dir, "w") as f:
            f.write(content)
            print(f'Successfully wrote to "{file_path}" ({len(content)} characters written)')