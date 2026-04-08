#write object(int, float, list , tuple ,dictionary ) data in file
import pickle
file=open(r"C:\Users\PC\Desktop\mayank\data.txt","wb")
# l1=(12,34,56)
l1={"hindi":78,"math":80}
pickle.dump(l1,file)
file.close()
print("object write succfully")