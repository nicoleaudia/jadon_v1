# Python file for the student side of Artificial Teaching Assistant

'''
Creates Threads to interact with Assistant.
Assistant cites files used for knowledge retrieval

Threads persist throughout usage
'''
from tutor import Tutor

assistant_id = None
tutor: Tutor = None

def extract_message(openai_message):
    return openai_message.content[0].text.value

def ask_tutor(message):
    tutor.ask(message)
    messages_full = tutor.retrieve_run()
    messages = map(messages_full, extract_message) # Messages to render to screen [need roles]

def start_assistant():
    if assistant_id == None: 
        print("Fatal error! No assistant exists for this class")
    tutor = Tutor()
    tutor.set_assistant(assistant_id)