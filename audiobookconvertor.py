import pyttsx3 # lib for text to speech
import PyPDF3 # lib for pdf accesing
book = open('object_oriented_python_tutorial.pdf','rb') # varible to store and open file in reading mode
pdfreader= PyPDF3.PdfFileReader(book) # storing the info in pdfreader
pages = pdfreader.numPages # fro thr object pdfreader etracting the number of pages
# print(pages)
speaker = pyttsx3.init() # initializing the object of python text to speech
for i in range(7,pages): # loop for accecing the pages
    page = pdfreader.getPage(i) # varible to store the page
    text = page.extractText() # extracting the page tet
    speaker.say(text) # function .say for generation
    speaker.runAndWait() # function for running


