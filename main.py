import os
import sys
from dotenv import load_dotenv
from google import genai
from google.genai import types
from config import SYSTEM_PROMPT
from functions.genai_function_schemas import schema_get_files_info, schema_get_file_content, schema_run_python_file, schema_write_file
from functions.call_function import call_function
from google.genai import errors

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

    try:
        for i in range(20):
            # Flag
            function_call_made = False

            # call the Gemini model
            response = client.models.generate_content(
                model='gemini-2.0-flash-001', 
                contents=messages,
                config=types.GenerateContentConfig(
                    tools=[available_functions],
                    system_instruction=SYSTEM_PROMPT),
            )

            for candidate in response.candidates:
                text_parts = []
                for part in candidate.content.parts:
                    if hasattr(part, 'function_call'):
                        if part.function_call is not None:
                            function_call_made = True

                            function_call_result = call_function(part.function_call, verbose)
                        
                            if not hasattr(function_call_result, 'parts') or len(function_call_result.parts) == 0:
                                raise Exception("Function call result is missing expected parts")
                            

                            response_dict = function_call_result.parts[0].function_response.response

                            if isinstance(response_dict, dict):
                                # Try to get the "result" key, else fall back to stringifying the dict
                                text = response_dict.get('result')
                                if text is None:
                                    # Maybe try another key or fallback to representing the dict
                                    text = str(response_dict)
                            else:
                                # If response is already a string (or something else), just use it directly
                                text = str(response_dict)

                            messages.append(types.Content(role="user", parts=[types.Part(text=text)]))

                    elif hasattr(part, 'text'):
                        text_parts.append(types.Part(text=part.text))

                if text_parts:
                    messages.append(types.Content(role="model", parts=text_parts))

            if not function_call_made:
                print("Final Response:")
                print(response.text)
                break

        if verbose:
            print("Prompt tokens:", response.usage_metadata.prompt_token_count)
            print("Response tokens:", response.usage_metadata.candidates_token_count)
    
    except errors.ClientError as e:
        print("API Error:", e)

if __name__ == "__main__":
    main()
