import re
from sys import stdin as s_in
d = dict()
n = s_in.read()
pat = r'\b[a-zA-Z0-9]+\b'
match = re.findall(pat, n)
for w in match:
    d[w] = d.get(w, 0) + 1
print(d)