# #solution tips ctrl+/ quickly comment and code
from collections import Counter
X=input()
size=input().split()
N=int(input())
buyer=[]
for i in range(N):
    buyer.append(input().split())
shoes=Counter(size)
money=0
for i in buyer:
    if i[0] in shoes.keys() and shoes[i[0]] != 0:
        money+=int(i[1])
        shoes[i[0]]-=1
# print(money)

#----------------------------------------------------------------
#What is the counter()

from collections import Counter

myList = [1,1,2,3,4,5,3,2,3,4,2,1,2,3]
print(Counter(myList))
Counter({2: 4, 3: 4, 1: 3, 4: 2, 5: 1})

print(Counter(myList).items())
[(1, 3), (2, 4), (3, 4), (4, 2), (5, 1)]

print(Counter(myList).keys())
[1, 2, 3, 4, 5]

print(Counter(myList).values())
[3, 4, 4, 2, 1]

# counter yapısında liste içerisindeki verileri
#sayarak adet sayısına göre collections.Counter
#tipinde bir veriye dönüştürür tupple vari bir kullanımı vardır.

print(dir(Counter))# ile kullanılabilen fonksiyonlar görebiliriz.

