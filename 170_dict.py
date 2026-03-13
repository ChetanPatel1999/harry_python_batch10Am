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
    100: "one hundred",
    200: "two hundred"
}

num=int(input("enter a num : "))#56
if num in d1:
    print(d1[num])
else:
    if len(str(num))==2:
        f=num//10 * 10
        s=num%10
        print(f"{d1[f]} {d1[s]}")
    else: #567
        f=num//100 * 100
        s=num//10%10 *10
        t=num%10
        print(f"{d1[f]} {d1[s]} {d1[t]}")