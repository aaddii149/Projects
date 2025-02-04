import math
#brute force
def check1(a:int) -> bool:
    if (a == 1):
        return False
    else:
        for i in range(2, a):
            if (a % i == 0):
                return False
    
    return True

print(check1(2))

#optimized
def check2(a:int) -> bool:
    if (a == 1):
        return False
    elif (a % 2 == 0 or a % 3 == 0):
        return False
    else:
        for i in range(5, int(math.sqrt(a)), 6):
            if(a % i == 0 or a % (i + 2) == 0):
                return False
    return True

print(check2(1031))