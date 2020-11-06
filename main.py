import pyttsx3
import PyPDF2
book = open('example.pdf', 'rb')
pdfReader = PyPDF2.PdfFileReader(book)
pages = pdfReader.numPages
print("The number of pages in the pdf is: {}".format(pages))
speaker = pyttsx3.init()
for curr_page in range(0, pages):
    page = pdfReader.getPage(curr_page)
    text = page.extractText()
    speaker.say(text)
    speaker.runAndWait()