# Python file for interacting with the OpenAI Assistant (used by both teacher and student)

from openai import OpenAI
from dotenv import load_dotenv

class Tutor:

    def __init__(self):
        load_dotenv()
        self.bot = OpenAI() # defaults to using os environ variables OPENAI_API_KEY
        self.file_ids = []
        self.assistant = None
        

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
            model="gpt-4",
            file_ids=self.file_ids
        )
        return self.assistant.id


    def set_assistant(self, assistant_id):
        self.assistant = assistant_id

    def ask(self, message = "", message_type = "query"):
        if (self.assistant == None):
            print("Fatal Error! No assistant instance created!")
            return
        # Ask Assistant question