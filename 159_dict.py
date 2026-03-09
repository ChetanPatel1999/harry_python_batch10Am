dict1 = {  
    "brand": "Ford",  
    "electric": False,  
    "year": 1964,  
    "colors": ["red", "white", "blue"] }

# print(dict1)

for key in dict1:
    print(key," = ",dict1[key])
    if key == "colors":
        for color in dict1["colors"]:
            print(color)