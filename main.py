import os
import sys
from dotenv import load_dotenv
from google import genai
from google.genai import types

flags = ['--verbose']

def main():
    argument = sys.argv[1:]
    load_dotenv()

    if len(argument) >= 1:
        messages = [types.Content(role="user", parts=[types.Part(text=argument[0])])]
        flag = ''
        if len(argument) > 1:
            flag = argument[1]
        api_key = os.environ.get("GEMINI_API_KEY")

        client = genai.Client(api_key=api_key)

        response = client.models.generate_content(
            model="gemini-2.0-flash-001",
            contents=messages,
        )
        print(response.text)
        
        if flag in flags:
            print("User prompt: " + argument[0])
            print("Prompt tokens: " + str(response.usage_metadata.prompt_token_count))
            print("Response tokens: " + str(response.usage_metadata.candidates_token_count))

    else:
        print('Please input just 1 prompt in quotation marks')
        exit(1)

main()