import json
import os
from pathlib import Path
from typing import List, Dict

def process_chat_messages(chat_data: Dict) -> List[Dict]:
    """
    Extract and format relevant messages from chat data.
    Only process messages from visitors ('v') and agents ('a').
    Starts with a system message that defines the AI model's behavior.
    
    Args:
        chat_data (Dict): Raw chat data from Tawk.to export
        
    Returns:
        List[Dict]: Formatted messages ready for OpenAI training
    """
    # Start with system message - customize this for your use case
    conversation = [{
        "role": "system",
        "content": """You are a customer service agent who will respond in the most helpful 
        and specific way possible. If you don't know the answer, you'll acknowledge that 
        and offer to forward the question to the team for follow-up via email or WhatsApp."""
    }]
    
    messages = chat_data.get('messages', [])
    
    for msg in messages:
        sender_type = msg.get('sender', {}).get('t')
        message_content = msg.get('msg', '').strip()
        
        # Skip empty messages or system messages
        if not message_content or sender_type == 's':
            continue
            
        # Map sender type to OpenAI roles
        role = 'user' if sender_type == 'v' else 'assistant' if sender_type == 'a' else None
        
        if role:
            conversation.append({
                "role": role,
                "content": message_content
            })
    
    return conversation

def create_jsonl_conversation(messages: List[Dict]) -> Dict:
    """
    Create a formatted conversation entry for the JSONL file.
    
    Args:
        messages (List[Dict]): List of processed messages
        
    Returns:
        Dict: Formatted conversation ready for JSONL output
    """
    return {
        "messages": messages
    }

def process_chat_files(root_path: str, output_dir: str):
    """
    Process all JSON chat files in the given directory structure and create JSONL files.
    
    Args:
        root_path (str): Path to directory containing exported chat files
        output_dir (str): Directory where JSONL files will be saved
    """
    # Create output directory if it doesn't exist
    os.makedirs(output_dir, exist_ok=True)
    
    # Counter for file naming
    file_counter = 1
    
    # Walk through all directories
    for root, _, files in os.walk(root_path):
        for file in files:
            if file.endswith('.json'):
                input_path = os.path.join(root, file)
                
                try:
                    # Read and parse JSON file
                    with open(input_path, 'r', encoding='utf-8') as f:
                        chat_data = json.load(f)
                    
                    # Process messages
                    conversation_messages = process_chat_messages(chat_data)
                    
                    # Skip empty conversations or conversations with only system message
                    if len(conversation_messages) <= 1:
                        continue
                    
                    # Create conversation in required format
                    conversation = create_jsonl_conversation(conversation_messages)
                    
                    # Create output filename with padded number
                    output_filename = f"{str(file_counter).zfill(5)}chat.jsonl"
                    output_path = os.path.join(output_dir, output_filename)
                    
                    # Write to JSONL file
                    with open(output_path, 'w', encoding='utf-8') as f:
                        json.dump(conversation, f, ensure_ascii=False)
                        f.write('\n')
                    
                    print(f"Processed: {input_path} -> {output_filename}")
                    
                    # Increment counter
                    file_counter += 1
                    
                except Exception as e:
                    print(f"Error processing {input_path}: {str(e)}")

def main():
    # Define the input and output paths - customize these for your setup
    input_path = "./tawkto_exports"  # Directory containing exported chat JSON files
    output_dir = "processed_chats"    # Directory where JSONL files will be saved
    
    print("Starting chat processing...")
    process_chat_files(input_path, output_dir)
    print("Processing complete!")

if __name__ == "__main__":
    main()
