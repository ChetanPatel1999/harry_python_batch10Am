#  Write a program to count frequency of each word in a sentence using dictionary. 
s= "indore ujjain indore ram  shyam ram indore"
d1={}
l1=s.split()
for word in l1 :
    if word not in d1:   
        d1[word]=1
    else:
        d1[word]=d1[word]+1
print(s)  
print(d1)      