# imports 
import os
import openai
from dotenv import load_dotenv 
import time

# constants

MODEL_GPT = 'gpt-4o-mini'
MODEL_LLAMA = 'llama3.2'
MAX_RETRIES = 3
RETRY_DELAY = 2

# set up environment
load_dotenv()  # load environment variables from .env file
openai.api_key = os.getenv("OPENAI_API_KEY")

if not openai.api_key:
    print("Error: OPENAI_API_KEY environment variable not set.")
    print("Please create a .env file with your OpenAI API key in the format: OPENAI_API_KEY=your_api_key_here")
    sys.exit(1)

def get_code_explanation(question):
    """
    Send a coding question to GPT and get a detailed explanation with code.
    Implements retry logic with exponential backoff.
    """
    for attempt in range(MAX_RETRIES):
        try:
            print(f"\n💻 Analyzing your code...\n")
            
            # Create the chat completion with streaming
            response = openai.chat.completions.create(
                model=MODEL_GPT,
                messages=[
                    {"role": "system", "content": "You are a helpful programming assistant. Explain code clearly with examples, highlighting best practices and potential improvements."},
                    {"role": "user", "content": question}
                ],
                temperature=0.3,
                stream=True
            )
            
            # Process the streaming response
            collected_response = ""
            print("\n--- EXPLANATION ---\n")
            
            for chunk in response:
                if chunk.choices and chunk.choices[0].delta.content:
                    content = chunk.choices[0].delta.content
                    print(content, end="", flush=True)
                    collected_response += content
            
            print("\n\n--- END OF EXPLANATION ---\n")
            return collected_response
            
        except Exception as e:
            wait_time = RETRY_DELAY * (2 ** attempt)
            print(f"Error: {e}. Retrying in {wait_time} seconds...")
            time.sleep(wait_time)
    
    print("Failed to get a response after multiple attempts.")
    return None

# here is the question; type over this to ask something new

question = """
Please explain what this code does and why:
yield from {book.get("author") for book in books if book.get("author")}
"""

# Get gpt-4o-mini to answer, with streaming
if __name__ == "__main__":
    print("\n🤖 Programming Assistant Tool 🤖")
    print("--------------------------------")
    
    while True:
        # Display the current question
        print(f"\nCurrent question:\n{question}")
        print("\nOptions:")
        print("1. Answer this question")
        print("2. Enter a new question")
        print("3. Quit")
        
        choice = input("\nEnter your choice (1-3): ")
        
        if choice == '1':
            get_code_explanation(question)
        elif choice == '2':
            print("\nEnter your new question (type 'END' on a new line when finished):")
            new_question = ""
            while True:
                line = input()
                if line == "END":
                    break
                new_question += line + "\n"
            if new_question.strip():
                question = new_question
        elif choice == '3':
            print("\nThank you for using the Programming Assistant Tool. Goodbye!")
            break
        else:
            print("\nInvalid choice. Please select 1, 2, or 3.")

