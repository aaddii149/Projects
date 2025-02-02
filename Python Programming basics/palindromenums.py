def palindrome(num:int):
    rev = 0
    num1 = num
    while (num1 != 0):
        rev = rev*10 + num1%10
        num1 = num1//10

    if (rev== num):
        return(True)
    else:
        return(False)
    
num = input("Please input a positive integer:")
check = palindrome(int(num))
if (check):
    print(num + " is a Palindrome")
else:
    print(num + " is not a Palindrome")

