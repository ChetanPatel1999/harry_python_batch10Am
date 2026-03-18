# Create a set using user input until user enters 0.
s1=set()
while True:
    s1.add(int(input("enter elemenet : ")))
    if 0 in s1:
        s1.remove(0)
        break
print(s1)    