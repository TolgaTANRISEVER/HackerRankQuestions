from collections import OrderedDict
N=int(input())

orders = OrderedDict()


for _ in range(N):
    item_name, sep, net_price = input().rpartition(" ")
    orders[item_name] = orders.get(item_name, 0) + int(net_price)
for item in orders:
    print(item, orders[item])
print(orders.items(),orders.keys(),orders.values())

