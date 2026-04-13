import time
import threading
def downlodeFile1():
    print("file1 download start ...")
    time.sleep(3)
    print("file1 downlode succefully")

def downlodeFile2():
    print("file2 download start ...")
    time.sleep(2)
    print("file2 downlode succefully")

def downlodeFile3():
    print("file3 download start ...")
    time.sleep(5)
    print("file3 downlode succefully") 



t1= threading.Thread(target=downlodeFile1)
t2= threading.Thread(target=downlodeFile2)
t3= threading.Thread(target=downlodeFile3)

t1.start()
t2.start()
t3.start()

t1.join()
t2.join()
t3.join()

print("all file download succefully")

# downlodeFile1()       
# downlodeFile2()       
# downlodeFile3()       
