# #solution tips ctrl+/ quickly comment and code
from collections import defaultdict
d = defaultdict(list)
n, m = map(int,input().split())
for i in range(n): d[input()].append(i+1)
for j in range(m): print(*d.get(input(),[-1]))
#run and show other fonk
for i in dir(defaultdict):
    print(i)
#defaultdict aracı, Python'un koleksiyon sınıfındaki bir kapsayıcıdır.
# Her zamanki sözlük (dict) kabına benzer,ancak tek fark, o anahtar henüz
# ayarlanmamışsa bir defaultdict'in varsayılan bir değere sahip olmasıdır.
# Bir defaultdict kullanmadıysanız, o anahtarın var olup olmadığını kontrol etmeniz ve yoksa,
# istediğiniz gibi ayarlamanız gerekir.
from collections import defaultdict
d = defaultdict(list)
d["a"].append(1+1)
print(d.keys())
