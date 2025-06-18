import os

def check_if_in_directory(working_directory, file_path, dir):
    parent = os.path.abspath(working_directory)
    child = os.path.abspath(dir)
    if not child.startswith(parent):
        print(f'Error: Cannot read "{file_path}" as it is outside the permitted working directory')
        return False
    
    else: 
        return True

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