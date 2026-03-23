# Variable-Length Arguments 
#  **kwargs - These are Keyword Arguments.  

# its create dictionary using passing  key-value data
def display(*a,**data):  
    print(data)
    print(a)


display(12,67,89,name="sahaj",rno=101,per=56.78)    