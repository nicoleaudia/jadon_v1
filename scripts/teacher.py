# Python file for the teacher side of Artificial Teaching Assistant

'''
Takes uploaded files (slides.pptx, textbook.pdf) and generates a GPT Assistant for use 
by students
'''

from tutor import Tutor

assistant_id = None
module_name = "Operations Management"
teaching_level = "university"

def powerpointUploaded():
    return False

def textbookUploaded():
    return True

def uploadFiles(tutor):
    if powerpointUploaded(): 
        tutor.upload_file("slides.pptx")
    if textbookUploaded(): 
        tutor.upload_file("textbook.pdf")
    

def main():
    tutor = Tutor()
    uploadFiles(tutor)
    if assistant_id != None: tutor.set_assistant(assistant_id)
    else: assistant_id = tutor.create_assistant(teaching_level=teaching_level, module_name=module_name)

    print("Succesfully loaded assistant with id {}".format(assistant_id))