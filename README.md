# Programming Assistant Tool

A Python-based interactive tool that uses OpenAI's GPT models to explain code snippets and answer programming questions with detailed explanations.

## Overview

This tool serves as your personal programming assistant, leveraging the power of OpenAI's language models to:
- Explain complex code snippets
- Answer technical programming questions
- Provide best practices and potential improvements
- Deliver explanations in real-time with a streaming interface

## Features

- **Interactive CLI Interface**: Simple menu-driven interaction
- **Real-time Responses**: Streaming API integration shows answers as they're generated
- **Robust Error Handling**: Implements retry logic with exponential backoff
- **Environment Variable Support**: Securely manages API keys
- **Customizable**: Easily modified to use different models or adjust parameters

## Installation

1. Clone the repository:
   ```
   git clone https://github.com/yourusername/programming-assistant-tool.git
   cd programming-assistant-tool
   ```

2. Install the required dependencies:
   ```
   pip install openai python-dotenv
   ```

3. Create a `.env` file in the root directory with your OpenAI API key:
   ```
   OPENAI_API_KEY=your_api_key_here
   ```

## Usage

1. Run the program:
   ```
   python code_assistant.py
   ```

2. Choose from the menu options:
   - **Option 1**: Answer the current programming question
   - **Option 2**: Enter a new question
   - **Option 3**: Quit the application

3. When entering a new question, type your code or question and type `END` on a new line when finished.

## Example

The tool comes with a default question:
```python
yield from {book.get("author") for book in books if book.get("author")}
```

Selecting Option 1 will provide a detailed explanation of this code's functionality, including what it does, how it works, and potential use cases.

## Advanced Configuration

You can modify the following constants in the code:
- `MODEL_GPT`: Change the OpenAI model (default: 'gpt-4o-mini')
- `MAX_RETRIES`: Adjust the number of retry attempts for API calls
- `RETRY_DELAY`: Modify the base delay between retries

## Requirements

- Python 3.6+
- OpenAI API key
- internet connection

## License

MIT

## Contributing

Contributions, issues, and feature requests are welcome!
