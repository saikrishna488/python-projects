from PyPDF2 import PdfReader

reader = PdfReader('r.pdf')
pages = len(reader.pages)

#no of pages
print(pages)

text = ""

for i in range(pages):
    text += reader.pages[i].extract_text()

print(text)