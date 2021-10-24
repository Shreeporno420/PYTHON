import pyttsx3
import PyPDF2
book= open('opp.pdf','rb')
pdf_Reader= PyPDF2.PdfFileReader(book)
pages=pdf_Reader.numPages
print(pages)
freind= pyttsx3.init()
for num in range(1,pages):
    page= pdf_Reader.getPage(num)
    text= page.extractText()
    freind.say(text)
    freind.runAndWait()