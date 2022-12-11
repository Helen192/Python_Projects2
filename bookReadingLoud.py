import pyttsx3
import PyPDF2

book = open('Beginning Azure Cognitive Services.pdf', 'rb')
pdfReader = PyPDF2.PdfFileReader(book)
num_pages = pdfReader.numPages
print(num_pages)

# create voice 
emma = pyttsx3.init()  # object emma
voices = emma.getProperty('voices')   #get voice in library
emma.setProperty('voice', voices[0].id)  # set voice to voice of a woman

# reading book from the first page to the end:
for num in range(0, num_pages):
    page = pdfReader.getPage(num)  # want to read the page num in file pdf of object book
    text = page.extract_text() # get text in page 23
    emma.say(text)
    emma.runAndWait()



