# Check if two sets are equal. 
s1={1,2,3}
s2={2,3,1}

if len(s1)!=len(s2):
    print("set is different")
else:
    for i in s1:
        if i not in s2:
            print("set is different")
            break
    else:
        print("set is sem")



# if s1==s2:
#     print("set is same")
# else:
#     print("set is different")    

# if s1.issubset(s2) and s2.issubset(s1):
#     print("set is same")
# else:
#     print("set is different")    
