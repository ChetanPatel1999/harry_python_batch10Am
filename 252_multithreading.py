import time
import threading

def table(num):
    for i in range(1,11): # 2
        print(f"{num} * {i} = {num*i}")
t1= threading.Thread(target=table,args=[2])
t2= threading.Thread(target=table,args=[3])
t3= threading.Thread(target=table,args=[4])

t1.start()
t1.join()

t2.start()
t3.start()





