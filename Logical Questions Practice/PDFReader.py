import PyPDF2
import pyttsx3

#Open the file in read mode
file = open('Python Programming by John Zelle.pdf', 'rb')

#Reading the file using PyPDF2 package
pdfreader = PyPDF2.PdfFileReader(file)

#Extracting Text from PDF and saving it in a ".txt" file
str = ""
for i in range(9, 19):
    str += pdfreader.getPage(i).extractText()
with open("Python Zelle.txt", "w", encoding="utf-8") as f:
    f.write(str)

#displaying number of pages in the PDF
pages = pdfreader.numPages
print(pages)

#Initializing the inbuilt speaker using pyttsx3 package
speaker = pyttsx3.init()
rate = speaker.getProperty('rate')
print(rate)

#Used for loop to let the say method say everything till mentioned
#range is not mentioned (can be changed as per the use)
for num in range(9):
    page = pdfreader.getPage(9)
    text = page.extractText()
    speaker.say(text)
    speaker.runAndWait()