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
    for i in range(2, 1 + int(math.sqrt(a))):
        if (a % i == 0):
            return False
    return True

print(check2(3))