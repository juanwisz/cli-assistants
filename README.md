# cli-assistants
A small yet powerful script to invoke OpenAI Assistants through our CLI.

GPT-Assistants CLI
GPT-Assistants CLI is a command-line interface that allows you to interact with various GPT-powered assistants for different tasks, such as cooking advice or software installation guidance, directly from your terminal.

Installation
To install GPT-Assistants CLI, run:

bash
Copy code
pip install gpt-assistants-cli
Configuration
Before using the assistants, you need to configure your assistants and set your OpenAI API key. Follow these steps:

Create a configuration file named .gpt-assistants-config.json in your home directory.
Add your assistants and your OpenAI API key to the configuration file. Here's an example:
json
Copy code
{
    "OPENAI_API_KEY": "your_openai_api_key_here",
    "assistants": {
        "cook": {
            "model": "text-davinci-003",
            "instructions": "Provide cooking instructions."
        },
        "software": {
            "model": "text-davinci-003",
            "instructions": "Provide software installation instructions."
        }
    }
}
Replace your_openai_api_key_here with your actual OpenAI API key.

Usage
Once configured, you can invoke an assistant by simply calling it from your command line. For example:

To get cooking advice:

bash
Copy code
gpt-assist 'cook' 'How do I make spaghetti carbonara?'
To get software installation help:

bash
Copy code
gpt-assist 'software' 'How do I install Git on Ubuntu?'
License
Specify your project's license here.

Adjusting the Code
To meet the above user-friendly approach, the code needs to:

Automatically load the configuration from the .gpt-assistants-config.json file in the user's home directory.
Accept the assistant's name (e.g., 'cook', 'software') as the first argument, making it easy to switch between different assistants.
Handle the rest of the command line input as the query to be sent to the selected assistant.
The entry point in setup.py should be adjusted to something like:

python
Copy code
entry_points={
    'console_scripts': [
        'gpt-assist=your_package.script:main',
    ],
},
And the main function in the script should be updated to parse the assistant's name as the first argument and the rest of the command line input as the query. It should also load the configuration from the user's home directory automatically.
