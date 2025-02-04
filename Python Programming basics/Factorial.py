def factorial(num:int) -> int:
    fact = 1
    while (num > 1):
        fact *= num
        num -= 1
    
    return fact

num = input("Please enter an integer: ")
fact = factorial(int(num))
print("Factorial of " + num + " is " + str(fact))
