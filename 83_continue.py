#wap to print square 1 to 20 but skip 12,13,14. 
for i in range(1,21):
    if i>=12 and i<=14:
        continue
    print(f"sqaure of {i}={i*i}")