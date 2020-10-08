max1 = int(input())
max2 = int(input())
if max1 < max2:
    max1, max2 = max2, max1
x = int(input())
while x:
    if x > max1:
        max1, max2 = x, max1
    elif x > max2:
        max2 = x
    x = int(input())
print(max2)