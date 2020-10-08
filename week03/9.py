d = dict()
n = int(input())
for i in range(n):
    s = input().split()
    for w in s:
        d[w] = d.get(w, 0) + 1
max_value = max(d.values())
print(min([i for i,j in d.items() if j == max_value]))