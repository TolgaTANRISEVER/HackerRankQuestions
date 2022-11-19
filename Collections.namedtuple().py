# #solution tips ctrl+/ quickly comment and code
"""
Python supports a type of container dictionaries called “namedtuple()” present in the module, “collections“.
Like dictionaries, they contain keys that are hashed to a particular value.
But on contrary, it supports both access from key-value and iteration, the functionality that dictionaries lack.

Tuple veri yapısı Python dilinde çokca kullanılır.
Dil bize kullandığımız tuple yapılarını isimlendirme imkanını sağlamak için NamedTuple yapısını sunuyor.
NamedTuple arkaplanda sizin verdiğiniz isim ve alan adlarını kullanarak sıradan bir sınıf yapısı oluşturuyor.
"""
# from collections import namedtuple
# Point = namedtuple('Point','x,y')
# pt1 = Point(1,2)
# pt2 = Point(3,4)
# dot_product = (pt1.x * pt2.x) +( pt1.y * pt2.y )
# print(dot_product)

# from collections import namedtuple
# Car = namedtuple('Car','Price Mileage Colour Class')
# xyz = Car(Price = 100000, Mileage = 30, Colour = 'Cyan', Class = 'Y')
# print(xyz)
# Car(Price=100000, Mileage=30, Colour='Cyan', Class='Y')
# print(xyz.Class)



from collections import namedtuple
N = int(input())
Students = namedtuple('Students', list(input().split()))
total_marks = 0
a=[]
for _ in range(N):
    student = Students(*input().split())
    a.append(list(student))
    total_marks += int(student.MARKS)
print("{:.2f}".format(total_marks / N))
print(a)


# from collections import namedtuple
# N, Student = int(input()), namedtuple('Student', input().strip().split())
# print(sum([float(m.MARKS) for m in [Student(*input().split()) for i in range(N)]])/N)
