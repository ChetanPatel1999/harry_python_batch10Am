import time
import threading

def table2():
    for i in range(1,11): # 2
        print(f"{2} * {i} = {2*i}")
        

def table3():
    for i in range(1,11): # 2
        print(f"{3} * {i} = {3*i}" )
        

def table4():
    for i in range(1,11): # 2
        print(f"{4} * {i} = {4*i}" )
        


t1= threading.Thread(target=table2)
t2= threading.Thread(target=table3)
t3= threading.Thread(target=table4)


t1.start()
t2.start()
t3.start()





