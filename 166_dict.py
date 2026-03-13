# Write a program to find the maximum value in a dictionary. 
employ={"johan":3000,"rydham":50000, "harry":5000,"ranveer":2000}
# print(max(employ.values()))
max=employ["johan"] # 3000
name=""
sum=0
for key in employ:
    sum+=employ[key]
    if max<=employ[key]:
        max=employ[key]
        name=key
print(f"name = {name}\nsallary = {max}")
print(f"total sallary : {sum}")