#wap to print english speling for given number.
d1 = {
    1: "one",
    2: "two",
    3: "three",
    4: "four",
    5: "five",
    6: "six",
    7: "seven",
    8: "eight",
    9: "nine",
    10: "ten",
    11: "eleven",
    12: "twelve",
    13: "thirteen",
    14: "fourteen",
    15: "fifteen",
    16: "sixteen",
    17: "seventeen",
    18: "eighteen",
    19: "nineteen",
    20: "twenty",
    30: "thirty",
    40: "forty",
    50: "fifty",
    60: "sixty",
    70: "seventy",
    80: "eighty",
    90: "ninety",
    100: "hundred",
    1000: "thousand",
}

num=int(input("enter a num : "))#100
if num in d1:
    print(d1[num])
else:
    if len(str(num))==2: # 78
        f=num//10 * 10
        s=num%10
        print(f"{d1[f]} {d1[s]}")
    elif len(str(num))==3:  # 567
        f=num//100 # 5
        s=num//10%10 *10  # 60
        t=num%10 # 7
        print(f"{d1[f]} hundred {d1[s]} {d1[t]}")
    elif len(str(num))==4:  # 5678
        f=num//1000 # 5
        s=num//100%10  # 6
        t=num//10%10*10 # 70
        fo=num%10
        print(f"{d1[f]} thousand {d1[s]} hundred {d1[t]}  {d1[fo]}")    