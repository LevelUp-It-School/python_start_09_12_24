# import itertools

# print(itertools.product("ABC", repeat=2))

# from itertools import product

# print(product("ABC", repeat=2))

### count(start, step)

# from itertools import count

# for value in count(0, 0.1):
#     if value <=1:
#         print(round(value, 1))
#     else:
#         break

# from itertools import cycle

# max_len = 10
# s = ''
# for letter in cycle('ABC'):
#     if len(s)<max_len:
#         s+=letter
#     else:
#         break

# print(s)

# from itertools import repeat

# result = list(repeat("ABC", 5))
# print(result)

# from itertools import accumulate

# for value in accumulate([1,2,3,4,5]):
#     print(value)

#from itertools import chain

# values = list(chain("АБВ", "ГДЕЁ", "ЖЗИЙК"))
# print(values)

# values = list(chain.from_iterable(["АБВ", "ГДЕЁ", "ЖЗИЙК"]))
# print(values)

# from itertools import product

# # values = list(product([1, 2, 3], "АБВГ"))
# # print(values)

# values = list(product([1, 2, 3], "АБВГ", repeat=2))
# print(values)

# from itertools import permutations

# values = list(permutations("АБВ"))
# print(values)     

# from itertools import combinations

# values = list(combinations("АБВГД", 2))
# print(values)

# from itertools import combinations_with_replacement

# values = list(combinations_with_replacement("АБВ", 3))
# print(values)


# from itertools import combinations

# result = list(combinations([1,2,3,4], 2))

# print(result)

#Условие: Пользователь вводит несколько строк, содержащих слова. Для каждой строки найдите уникальные слова.

# from sys import stdin

# lines = stdin.read().split("\n")
# # print([lines])
# for line in lines:
#     unique_words = set(line.split())
#     print(", ".join(unique_words))