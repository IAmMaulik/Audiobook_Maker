import PyPDF2
from time import sleep
from gtts import gTTS

book = open('example.pdf', 'rb')
out = open('output.txt', 'a')
pdfReader = PyPDF2.PdfFileReader(book)
pages = pdfReader.numPages
print("The number of pages in the pdf is: {}".format(pages))
print("Your PDF is being processed...")
for curr_page in range(0, pages):
    page = pdfReader.getPage(curr_page)
    text = page.extractText()
    out.write(text)
out.close()

print("Your Audibook is being created...")

with open("output.txt") as file:
    file = file.read()

speak = gTTS(file, lang='en')
speak.save('audiobook.mp3')
print("Successfully created the Audiobook")

sleep(7)
