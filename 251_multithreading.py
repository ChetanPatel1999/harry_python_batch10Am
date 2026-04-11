import time
def table(num):
    for i in range(1,11):
        print(f"{num} * {i} = {num*i}" )
        time.sleep(0.2)



table(2)
table(3)
table(4)