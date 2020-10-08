n = list(map(int, input().split()))
max_i, min_i = n.index(max(n)), n.index(min(n))
n[max_i], n[min_i] = n[min_i], n[max_i]
print(n)