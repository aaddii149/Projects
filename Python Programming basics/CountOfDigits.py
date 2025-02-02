def count(num:int):
    i=0
    while (num!=0):
        num = num//10
        i += 1
    return i

num = input("Please input a positive integer:")
digits = count(int(num))
print("Number of digits in " + str(num) + " is " + str(digits))