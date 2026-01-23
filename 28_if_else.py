# Write a program to check whether a character is an alphabet or not. .
alpha=input("enter a alphabet : ")

# if alpha.lower() in "abcdefghijklmnopqrstuvwxyz":
#     print('char is alpha')
# else:
#     print('char is not alpha')

# if alpha>='a' and alpha<='z' or alpha>='A' and alpha<='Z':
#     print('char is alpha')
# else:
#     print('char is not alpha')

# if alpha.lower()>='a' and alpha.lower()<='z':
#     print('char is alpha')
# else:
#     print('char is not alpha')

if ord(alpha.lower())>=97 and ord(alpha.lower())<=122:
    print('char is alpha')
else:
    print('char is not alpha')