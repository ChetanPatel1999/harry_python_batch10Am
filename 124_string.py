#   Write a program to find the largest word in a string.
#hello i am student of 12th class
s="hello i am chetann patel student of 12th class"
list1=s.split()
#["hello","i","am","student","of ","12th","class"]
largest=list1[0]
for ele in list1:
    if len(largest)<len(ele):
        largest=ele  # student
print("largest word :- ",largest)        
