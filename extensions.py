'''
.png: image/png
.pdf: application/pdf
.txt: text/plain
.zip: application/zip
'''
file = input("File name: ").lower().strip()

if file.endswith(".gif"):
    print("image/gif")
if file.endswith(".jpg" ) or file.endswith(".jpeg"):
    print("image/jpeg")
if file.endswith(".pdf"):
    print("application/pdf")
if file.endswith(".png"):
    print("image/png")
if file.endswith(".zip"):
    print("application/zip")
if file.endswith(".txt"):
    print("text/plain")
else:
    print("application/octet-stream")        
    
       

