import os
import sys
from dotenv import load_dotenv
from google import genai
from google.genai import types

from functions.get_files_info import schema_get_files_info
from functions.get_file_content import schema_get_file_content
from functions.run_python import schema_run_python
from functions.write_file import schema_write_file


flags = ['--verbose']

#Hardcoded prompt that instructs the LLM on what to do
system_prompt = """
You are a helpful AI coding agent.

When a user asks a question or makes a request, make a function call plan. You can perform the following operations:

- List files and directories
- Read file contents
- Execute Python files with optional arguments
- Write or overwrite files

All paths you provide should be relative to the working directory. You do not need to specify the working directory in your function calls as it is automatically injected for security reasons.
"""


def read_arguments():
    argument = sys.argv[1:]
    load_dotenv()

    if len(argument) >= 1:
        messages = [types.Content(role="user", parts=[types.Part(text=argument[0])])]
        flag = ''
        if len(argument) > 1:
            flag = argument[1]
        api_key = os.environ.get("GEMINI_API_KEY")

        #List of available functions
        available_functions = types.Tool(
            function_declarations=[
                schema_get_files_info,
                schema_get_file_content,
                schema_run_python,
                schema_write_file
            ]
        )

        client = genai.Client(api_key=api_key)
        response = client.models.generate_content(
            model="gemini-2.0-flash-001",
            contents=messages,
            config=types.GenerateContentConfig(
                tools=[available_functions], system_instruction=system_prompt
            )
        )
        #print(response.text)
        for func in response.function_calls:
            print(f"{func.name}: ({func.args})")

        if flag in flags:
            print("User prompt: " + argument[0])
            print("Prompt tokens: " + str(response.usage_metadata.prompt_token_count))
            print("Response tokens: " + str(response.usage_metadata.candidates_token_count))

    else:
        print('Please input just 1 prompt in quotation marks')
        exit(1)

def main():
    read_arguments()

main()