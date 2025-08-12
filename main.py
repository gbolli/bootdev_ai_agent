import os
import sys
from dotenv import load_dotenv
from google import genai
from google.genai import types
from config import SYSTEM_PROMPT
from functions.genai_function_schemas import schema_get_files_info, schema_get_file_content, schema_run_python_file, schema_write_file


def main():

    # check if a prompt is provided
    if len(sys.argv) < 2:
        print("No arguments provided. Please include a prompt.")
        sys.exit(1)

    # get the user prompt from command line arguments
    user_prompt = sys.argv[1]
    messages = [
        types.Content(role="user", parts=[types.Part(text=user_prompt)]),
    ]

    # check for verbose mode
    verbose = "--verbose" in sys.argv
    if verbose:
        print("Verbose mode is ON")
        print("User prompt:", user_prompt)

    # set up genai client
    load_dotenv()
    api_key = os.environ.get("GEMINI_API_KEY")
    client = genai.Client(api_key=api_key)
    available_functions = types.Tool(
        function_declarations=[
            schema_get_files_info,
            schema_get_file_content,
            schema_run_python_file,
            schema_write_file,
        ]
    )

    # call the Gemini model
    response = client.models.generate_content(
        model='gemini-2.0-flash-001', 
        contents=messages,
        config=types.GenerateContentConfig(
            tools=[available_functions],
            system_instruction=SYSTEM_PROMPT),
    )

    # print the response
    if response.function_calls:
        for function_call_part in response.function_calls:
            print(f"Calling function: {function_call_part.name}({function_call_part.args})")
    else:
        print(response.text)

    if verbose:
        print("Prompt tokens:", response.usage_metadata.prompt_token_count)
        print("Response tokens:", response.usage_metadata.candidates_token_count)
    

if __name__ == "__main__":
    main()
