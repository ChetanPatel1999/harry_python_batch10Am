#welcome to my home
# count character in every word in given string
s=input("enter a string :")
list1=s.split()
print("string each word character count :")
for ele in list1:
    print(f"{ele} = {len(ele)}")
