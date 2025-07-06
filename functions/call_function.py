from google.genai import types
from functions.get_files_info import get_files_info
from functions.get_file_content import get_file_content
from functions.write_file import write_file
from functions.run_python import run_python_file

functions = ['check_if_in_directory', 'get_file_content', 'get_files_info', 'run_python_file', 'write_file']
working_dir = './calculator'

def call_function(function_call_part, verbose=False):
    if verbose:
        print(f"Calling function: {function_call_part.name}({function_call_part.args})")
    else:
        print(f" - Calling function: {function_call_part.name}")

    function_name = function_call_part.name
    if function_name in functions:
        if 'file_path' in function_call_part.args:
            file_path = function_call_part.args['file_path']
        if 'directory' in function_call_part.args:
            directory = function_call_part.args['directory']
        if 'content' in function_call_part.args: 
            content = function_call_part.args['content']

        if function_name == 'check_if_in_directory':
            pass
        elif function_name == 'get_file_content':
            function_result = get_file_content(working_dir, file_path=file_path)
        elif function_name == 'get_files_info':
            function_result = get_files_info(working_dir, directory=directory)
        elif function_name == 'run_python_file':
            function_result = run_python_file(working_dir, file_path=file_path)
        elif function_name == 'write_file':
            arg2 = function_call_part.args['content']
            function_result = write_file(working_dir, file_path=file_path, content=content)

        return types.Content(
            role="tool",
            parts=[
                types.Part.from_function_response(
                    name=function_name,
                    response={"result": function_result},
                )
            ],
        )


    else:
        return types.Content(
        role="tool",
        parts=[
            types.Part.from_function_response(
                name=function_name,
                response={"error": f"Unknown function: {function_name}"},
            )
        ],
    )
