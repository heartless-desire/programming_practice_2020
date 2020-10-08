xa, ya, xb, yb = list(map(float, input().split()))
print((lambda x1, y1, x2, y2: ((x1-x2)**2 + (y1-y2)**2)**.5)(xa, ya, xb, yb))