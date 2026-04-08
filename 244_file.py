#write object(int, float, list , tuple ,dictionary ) data in file
import pickle
file=open(r"C:\Users\PC\Desktop\mayank\data.txt","rb")
l1= pickle.load(file)
print(l1)
file.close()