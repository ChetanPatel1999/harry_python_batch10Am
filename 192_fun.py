def listSum(lst):
    sum=0
    for num in lst:
        sum+=num
    return sum    



marks=[12,34,56,78]
gameScore=[4,5,2,7]
attendence=[8,6,4,2,4,56,78]

print(f"sum of marks : {listSum(marks)}")
print(f"sum of gameScore : {listSum(gameScore)}")
print(f"sum of attendence : {listSum(attendence)}")
