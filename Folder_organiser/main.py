import os

files = os.listdir()
files.remove("main.py")

# create folder func
def createFolders(fname):
    if not os.path.exists(fname):
        os.mkdir(fname)

# move folder func
def move(foldername, files):
    for file in files:
        os.replace(file,f"{foldername}/{file}")
   

# creating folders
createFolders("images")
createFolders("documents")
createFolders("others")

# file extensions
imagesExtension = ['.png', '.jpeg', '.jpg']
documentsExtension = ['.pdf','.pptx','.txt','.docx']

#categorizing files
images = [file for file in files if os.path.splitext(file)[1].lower() in imagesExtension]
documents = [file for file in files if os.path.splitext(file)[1].lower() in documentsExtension]
others = []

for file in files:
    exten = os.path.splitext(file)[1].lower()
    if exten not in imagesExtension and exten not in documentsExtension:
        if os.path.isfile(file):
            others.append(file)

# organising files
move("images",images)
move("documents",documents)
move("others",others)

print("Files are organised")