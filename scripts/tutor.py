# Python file for interacting with the OpenAI Assistant (used by both teacher and student)

from openai import OpenAI
from dotenv import load_dotenv
import time

class Tutor:

    def __init__(self):
        load_dotenv()
        self.bot = OpenAI() # defaults to using os environ variables OPENAI_API_KEY
        self.file_ids = []
        self.assistant = None
        self.thread = None # Conversation (thread) to assistant
        self.run = None 
        

    # Uploads a powerpoint or textbook to OpenAI
    ''' textbook_path = path to .pdf textbook
        powerpoint_path = path to .pptx slides '''
    def upload_file(self, filepath = "knowledge.pdf"):
        file_object = self.bot.files.create(
            file=open(filepath, "rb"),
            purpose="assistants"
        )
        self.file_ids.append(file_object.id)


    '''
    module_name = Name of module (e.g. 'Operations Management')
    teaching_level = 'university', 'high school', 'junior school'
    assistant_name = Name of assistant for OpenAI
    '''
    def create_assistant(self, module_name, assistant_name="Tutor", teaching_level="university"):
        assistant_prompt = "You are a teaching assistant teaching a {0} level course in {1}. Use your knowledge base to best answer student questions about the course.".format(teaching_level, module_name)
        self.assistant = self.bot.beta.assistants.create(
            name=assistant_name,
            instructions=assistant_prompt,
            tools=[{"type": "retrieval"}],
            model="gpt-4-turbo-preview",
            file_ids=self.file_ids
        )
        return self.assistant.id


    def set_assistant(self, assistant_id):
        self.assistant = self.bot.beta.assistants.retrieve(assistant_id)

    def start_thread(self):
        if self.thread == None: 
            self.thread = self.bot.beta.threads.create()

    # Add message to Thread, and creates a Run
    def ask(self, message = ""):
        if (self.assistant == None):
            print("Fatal Error! No assistant instance created!")
            return
        
        self.start_thread()
        self.bot.beta.threads.messages.create(
            thread_id=self.thread.id,
            content=message,
            role='user'
        )
        
        self.run = self.bot.beta.threads.runs.create(
            thread_id=self.thread.id,
            assistant_id=self.assistant.id
        )
    
    def retrieve_run(self):
        if self.run == None:
            print("Error! There is no run instance running!")
            return None
        
        self.run = self.bot.beta.threads.runs.retrieve(
            thread_id=self.thread.id, 
            run_id=self.run.id
        )

        print(self.run)
        print("--"*10)

        status = self.run.status
        if status == 'cancelled' or status == 'expired' or status == 'failed' or status == 'cancelled':
            print("Error! Run has not completed")
            return None
        
        if self.run.status != 'completed':
            time.sleep(1) # Sleep for some time then recursively call
            return self.retrieve_run()
        
        messages = self.bot.beta.threads.messages.list(
            thread_id=self.thread.id
        )

        return messages.data