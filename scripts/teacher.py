# Python file for the teacher side of Artificial Teaching Assistant

'''
Takes uploaded files (slides.pptx, textbook.pdf) and generates a GPT Assistant for use 
by students
'''

from tutor import Tutor

assistant_id = None # we would keep this in a database ordinarily
module_name = "Operations Management" # input text filed
teaching_level = "university" # radio buttons (pre-selected)

def powerpointUploaded():
    return False

def textbookUploaded():
    return True

def uploadFiles(tutor):
    if powerpointUploaded(): 
        tutor.upload_file("scripts/files/slides.pdf")
    if textbookUploaded(): 
        tutor.upload_file("scripts/files/textbook.pdf")

# Called when teacher wishes to create an assistant
def create_assistant():
    global assistant_id, module_name, teaching_level
    # Get teacher to upload desired files
    tutor = Tutor()
    uploadFiles(tutor)
    # Create assistant when required
    if assistant_id != None: tutor.set_assistant(assistant_id)
    else: assistant_id = tutor.create_assistant(teaching_level=teaching_level, module_name=module_name)

    print("Succesfully loaded assistant with id {}".format(assistant_id))


if __name__=="__main__":
    create_assistant()