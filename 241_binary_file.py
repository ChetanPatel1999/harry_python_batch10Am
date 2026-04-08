#write your file handling code with statement
#with statement close your file automaticaly

with open(r"C:\Users\PC\Desktop\Demo\photo.png","rb") as file:
    imageData=file.read()

with open(r"C:\Users\PC\Desktop\mayank\photo.png","wb") as file:
    file.write(imageData)

