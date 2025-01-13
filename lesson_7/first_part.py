#vowels = {"а", "е", "ё", "и", "у", "о", "ы", "э", "ю", "я"}
# print(vowels)

# empty_set = set()
# print(len(vowels))

# word = "коллекция"
# letters = set(word)
# print(letters)

# for i in vowels:
#     print(i)

# vowels = {"а", "е", "ё", "и", "у", "о", "ы", "э", "ю", "я"}

# letter = input("Введите букву: ")
# if letter.lower() in vowels:
#     print("Гласная буква")
# else:
#     print("Согласная буква")

s_1 = {1, 2, 3}
s_2 = {3, 4, 5}
#s_union = s_1 | s_2
# s_union = s_1.union(s_2)
# print(s_union)
# s_intersection = s_1 & s_2
# s_intersection = s_1.intersection(s_2)
# print(s_intersection)
# s_dif = s_1 - s_2
# s_dif = s_1.difference(s_2)
# print(s_dif)
# s_sym_dif = s_1 ^ s_2
# s_sym_dif = s_1.symmetric_difference(s_2)
# print(s_sym_dif)

# vowels = {"а", "е", "ё", "и", "у", "о", "ы", "э", "ю", "я"}
# word = "коллекция"
# letters = set(word)
# print(", ".join(letters & vowels))

# s_1 = {1, 2, 3}
# s_2 = {3, 1, 2}
# print(s_1 == s_2)

#s_2 = {1, 2, 3}
#s_1 = {3, 1, 2, 4}
# print(s_1 >= s_2)

s = {4, 1, 2}
# s.add(10)
# print(s)
# s.remove(1)
# print(s)
# s.discard(5)
# print(s)
# x = s.pop()
# print(x)
# print(s)
s.clear()
print(s)