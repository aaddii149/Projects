import math
def gcd(a:int, b:int) -> int:
    if (b == 0):
        return a
    else:
        return gcd(b, a%b)

print(gcd(12, 15))