def gcd(*couple:tuple):
    a, b = couple
    while a != 0 and b != 0:
        if a > b:
            a = a % b
        else:
            b = b % a
    return a+b
