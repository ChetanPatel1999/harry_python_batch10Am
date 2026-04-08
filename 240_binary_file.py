#binary file 
file= open(r"C:\Users\PC\Desktop\Demo\fox.jpg","rb")
imageData=file.read()
print(imageData)
file.close()
file=open(r"C:\Users\PC\Desktop\mayank\fox.jpg","wb")
file.write(imageData)
file.close()