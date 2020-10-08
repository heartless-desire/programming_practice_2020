from collections import defaultdict as def_dict
from sys import stdin as s_in

purchases = def_dict(lambda: def_dict(int))
for l in s_in.readlines():
    client, purchase, val = l.split()
    purchases[client][purchase] += int(val)

for client in purchases:
    print(client + ":\n")
    for purchase in purchases[client]:
        print("\t" + purchase + " : " + purchases[client][purchase])