# Python file for the student side of Artificial Teaching Assistant

'''
Creates Threads to interact with Assistant.
Assistant cites files used for knowledge retrieval

Threads persist throughout usage
'''
from scripts.tutor import Tutor

tutor: Tutor = None

def extract_message(openai_message):
    return openai_message[0].text.value

def ask_tutor(message):
    tutor.ask(message)
    messages_full = tutor.retrieve_run()
    messages = []
    for thread in messages_full:
        messages.append(thread.content[0].text.value)
    print(messages_full)
    return messages
    # return messages_full


def start_assistant(assistant_id):
    global tutor
    if assistant_id == None: 
        print("Fatal error! No assistant exists for this class")
    tutor = Tutor()
    tutor.set_assistant(assistant_id)

def run_user_bot(assistant_id):
    start_assistant(assistant_id)

# if __name__=='__main__':
#     start_assistant()
#     ask_tutor("I don't understand the concept of message passing. Could you explain it to me?")
