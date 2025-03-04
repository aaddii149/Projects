def gcd(a:int, b:int) -> int:
    if (b == 0):
        return a
    else:
        return gcd(b, a%b)
    
def lcm(a:int, b:int) -> int:
    return int((a*b)/gcd(a, b))

print(lcm(4,6))