# Tawk.to Chat to OpenAI Training Converter

Convert your Tawk.to chat history into OpenAI-compatible training data for fine-tuning custom chat models.

## Overview

This Python script helps you transform exported chat histories from [Tawk.to](https://www.tawk.to/) (a free live chat widget) into the JSONL format required for OpenAI's fine-tuning process. This enables you to create custom AI models trained on your actual customer service conversations.

## Features

- Processes multiple JSON chat files from Tawk.to exports
- Converts chat messages into OpenAI's required JSONL format
- Maintains conversation flow between customers and agents
- Configurable system instructions for model behavior
- Handles nested directory structures
- Generates sequentially numbered output files

## Prerequisites

- Python 3.6+
- Tawk.to account with chat history
- Basic understanding of OpenAI's fine-tuning process

## Installation

1. Clone this repository:
```bash
git clone https://github.com/yourusername/tawkto-openai-converter.git
cd tawkto-openai-converter
```

2. No additional dependencies required (uses standard Python libraries)

## Usage

1. **Export Your Tawk.to Chats:**
   - Log into your [Tawk.to Dashboard](https://dashboard.tawk.to)
   - Go to "Inbox"
   - Select conversations (max 50 per page)
   - Click "Export" button at the top
   - Download the ZIP file from your email
   - Extract the ZIP file(s) to a directory

2. **Run the Script:**
```bash
python chat_converter.py
```

3. **Configure the Script:**
   - Open `chat_converter.py`
   - Modify the input and output paths in the `main()` function
   - Customize the system message in `process_chat_messages()` function

## Output Format

The script generates JSONL files with this structure:
```json
{
    "messages": [
        {
            "role": "system",
            "content": "You are a customer service agent who will respond..."
        },
        {
            "role": "user",
            "content": "Customer message here"
        },
        {
            "role": "assistant",
            "content": "Agent response here"
        }
    ]
}
```

## Customizing System Instructions

In the `process_chat_messages()` function, modify the system message to define how your AI model should behave. Example customizations:

```python
system_message = {
    "role": "system",
    "content": """You are a customer service agent who will:
    - Always be polite and professional
    - Follow company pricing: Basic($10), Pro($25), Enterprise($100)
    - Never offer discounts beyond 10%
    - Escalate technical issues to support@company.com
    - Operating hours: Mon-Fri 9am-5pm EST"""
}
```

## Limitations

- Tawk.to exports are limited to 50 conversations per download
- Large chat histories require multiple export operations
- Processing time depends on the number of chat files

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License - see the LICENSE file for details.
