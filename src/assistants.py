#!/usr/bin/env python3
import os
import json
import sqlite3
import sys
from openai import OpenAI

# Configuration loading
def load_configuration():
    home_directory = os.path.expanduser("~")
    config_path = os.path.join(home_directory, '.gpt-assistants-config.json')
    if not os.path.exists(config_path):
        raise FileNotFoundError(f"Configuration file not found at {config_path}")
    with open(config_path) as f:
        return json.load(f)

config = load_configuration()

# Ensure OPENAI_API_KEY is set
api_key = config.get("OPENAI_API_KEY")
if not api_key:
    raise EnvironmentError("OPENAI_API_KEY not set in the configuration file.")

client = OpenAI(api_key=api_key)

# Database setup
conn = sqlite3.connect('conversations.db')
c = conn.cursor()
c.execute('''CREATE TABLE IF NOT EXISTS conversations
             (id INTEGER PRIMARY KEY, thread_id TEXT, messages TEXT)''')
conn.commit()

def get_assistant_config(agent_name):
    return config.get("assistants", {}).get(agent_name)

def save_conversation(thread_id, messages):
    c.execute("INSERT INTO conversations (thread_id, messages) VALUES (?, ?)", (thread_id, json.dumps(messages)))
    conn.commit()
    return c.lastrowid

def get_conversation(conversation_id):
    c.execute("SELECT thread_id, messages FROM conversations WHERE id=?", (conversation_id,))
    row = c.fetchone()
    if row:
        return row[0], json.loads(row[1])
    return None, []

def interact_with_assistant(assistant_config, start_message, conversation_id=None):
    if conversation_id:
        thread_id, _ = get_conversation(conversation_id)
    else:
        # Create a new thread
        thread = client.beta.threads.create()
        thread_id = thread['id']

    message = client.beta.threads.messages.create(
        thread_id=thread_id,
        role="user",
        content=start_message,
    )

    # Get or create assistant
    assistant = client.beta.assistants.create(
        name="Custom Assistant",
        instructions=assistant_config.get('instructions', "Interact with users."),
        model=assistant_config.get('model', "gpt-4"),
    )

    # Create a run
    run = client.beta.threads.runs.create(
        thread_id=thread_id,
        assistant_id=assistant['id'],
    )

    # Retrieve all the messages in the thread
    messages = client.beta.threads.messages.list(thread_id=thread_id)

    if conversation_id:
        return thread_id, messages
    else:
        conversation_id = save_conversation(thread_id, messages['data'])
        return conversation_id, messages

def main():
    if len(sys.argv) < 3:
        print("Usage: gpt-assist <assistant_name> <message>")
        sys.exit(1)

    agent_name = sys.argv[1]
    message = ' '.join(sys.argv[2:])
    assistant_config = get_assistant_config(agent_name)

    if not assistant_config:
        raise ValueError(f"No configuration found for '{agent_name}'.")

    new_conversation_id, messages = interact_with_assistant(assistant_config, message)
    print(f"New conversation started with ID: {new_conversation_id}")

    for message in messages['data']:
        if message['role'] == 'user':
            print("You:", message['content']['text']['value'])
        else:
            print("Assistant:", message['content']['text']['value'])

if __name__ == "__main__":
    main()
