import os
import sys
from dotenv import load_dotenv
from google import genai
from google.genai import types
from config import SYSTEM_PROMPT


def main():
    print("Hello from ai-agent!")

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

    # call the Gemini model
    response = client.models.generate_content(
        model='gemini-2.0-flash-001', 
        contents=messages,
        config=types.GenerateContentConfig(system_instruction=SYSTEM_PROMPT),
    )

    # print the response
    print(response.text)

    if verbose:
        print("Prompt tokens:", response.usage_metadata.prompt_token_count)
        print("Response tokens:", response.usage_metadata.candidates_token_count)
    

if __name__ == "__main__":
    main()
