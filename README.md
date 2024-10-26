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
- Creates fine-tuning ready JSONL files for OpenAI

## Prerequisites

- Python 3.6+
- Tawk.to account with chat history
- OpenAI account with API access
- Basic understanding of OpenAI's fine-tuning process

## Important Configuration

Before running the script, you must modify two key elements:

1. **File Paths**: In the `main()` function, update these variables:
```python
input_path = "./tawkto_exports"  # Directory containing your exported chat JSON files
output_dir = "processed_chats"   # Directory where JSONL files will be saved
```

2. **System Instructions**: In the `process_chat_messages()` function, customize this message:
```python
conversation = [{
    "role": "system",
    "content": """You are a customer service agent who will respond in the most helpful 
    and specific way possible. If you don't know the answer, you'll acknowledge that 
    and offer to forward the question to the team for follow-up via email or WhatsApp."""
}]
```

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

## Output Format

The script generates JSONL files where each line is a complete JSON object. Example format:

```
{"messages": [{"role": "system", "content": "You are a customer service agent..."}, {"role": "user", "content": "Customer message here"}, {"role": "assistant", "content": "Agent response here"}]}
{"messages": [{"role": "system", "content": "You are a customer service agent..."}, {"role": "user", "content": "Different customer message"}, {"role": "assistant", "content": "Different agent response"}]}
```

Note: Each line in the JSONL file is a complete, valid JSON object, with no commas between lines.

## Using Output Files with OpenAI Fine-tuning

The generated JSONL files are ready to use for OpenAI fine-tuning. To use them:

1. Go to [OpenAI Platform](https://platform.openai.com/finetune) or login to your OpenAI account and navigate to the fine-tuning section in the dashboard
2. Create a new fine-tuning job
3. Upload your JSONL files (you can upload multiple files)
4. Select your base model and configure training parameters
5. Start the fine-tuning process

Each JSONL file in your output directory is independently valid for fine-tuning. You can choose to:
- Upload all files for a comprehensive training dataset
- Select specific files based on conversation quality or topics
- Test fine-tuning with a subset of files before using the complete dataset

## Customizing System Instructions

The system message defines how your AI model should behave. Examples:

```python
# Example 1: E-commerce Support
"""You are a customer service agent for an e-commerce store who:
- Provides shipping information for US, Canada, and EU
- Handles returns within 30 days of purchase
- Can process refunds for orders under $500
- Escalates technical issues to support@company.com
- Operating hours: Mon-Fri 9am-5pm EST"""

# Example 2: Technical Support
"""You are a technical support agent who:
- Provides basic troubleshooting for our software
- Can reset user passwords and help with login issues
- Must verify user identity before providing account details
- Escalates server issues to DevOps team
- Never shares internal system information"""

# Example 3: Booking Service
"""You are a booking assistant who:
- Handles reservations for our 3 locations
- Follows pricing: Basic($50), Premium($100), VIP($200)
- Cannot offer discounts beyond 15%
- Must collect contact information for bookings
- Requires 24h notice for cancellations"""
```

## Limitations

- Tawk.to exports are limited to 50 conversations per download
- Large chat histories require multiple export operations
- Processing time depends on the number of chat files
- OpenAI may have size limits for individual fine-tuning files

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.
