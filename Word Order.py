from collections import OrderedDict

words = OrderedDict()
for _ in range(int(input())):
    word = input()
    words[word] = words.get(word, 0) + 1
print(word)
print(words)
print(len(words))
print(*words.values())


# 4
# bcdef
# abcdefg
# bcde
# bcdef
