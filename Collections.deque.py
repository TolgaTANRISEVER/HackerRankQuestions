from collections import deque
N=int(input())
d = deque()
for _ in range(N):
    method, *number = input().split()
    getattr(d,method)(*number)
    """
    #değişken ismi bilinmemesi durumunda bu kullanılabilir 
    method=append
    getattr(d,method)(*number)==d.append(number)
    """
print(*d)

# 6
# append 1
# append 2
# append 3
# appendleft 4
# pop
# popleft