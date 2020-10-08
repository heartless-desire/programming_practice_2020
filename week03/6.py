n = list(map(int, input().split()))
a = set()
for i in n:
    if i in a:
        print("YES")
    else:
        print("NO")
        a.add(i)
