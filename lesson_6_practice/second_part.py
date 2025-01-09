#Пропуск слов с определенной длиной(4)
# text = "This is a simple Python string example"
# new_text = text.split()

# for word in new_text:
#     if len(word)>4:
#         print(word)

#Пропуск символов по условию
# text = "This is a simple Python string example"
# result = ""

# for char in text:
#     if char.lower() == 'a':
#         continue
#     result+=char
# print(result)

#У вас есть список из видов мороженого. Найдите, есть ли в меню мороженое "ванильное".
# menu = ["шоколадное", "клубничное", "ванильное", "фисташковое"]

# if "ванильное" in menu:
#     print("Yes")
# else:
#     print("No")

#У вас есть список городов и их температур. Найдите город с самой высокой температурой.
# cities = ["Москва", "Сочи", "Якутск", "Казань"]
# temperatures = [-5, 15, -30, -2]
# max_temp = max(temperatures)
# id_max_temp = temperatures.index(max_temp)
# print(cities[id_max_temp])

# max_temp = temperatures[0]
# max_city = cities[0]

# for i in range(1, len(temperatures)):
#     if temperatures[i] > max_temp:
#         max_temp = temperatures[i]
#         max_city = cities[i]

# print(max_city, max_temp)

#У вас есть список животных. Посчитайте, сколько раз каждое животное встречается.
animals = ["слон", "тигр", "слон", "зебра", "тигр", "тигр", "зебра"]

# unique_animals = []
# counts = []

# for animal in animals:
#     if animal not in unique_animals:
#         unique_animals.append(animal)
#         counts.append(1)
#     else:
#         index = unique_animals.index(animal)
#         counts[index] += 1

# for i in range(len(unique_animals)):
#     print(f"{unique_animals[i]}: {counts[i]}")


#print(animals.count("слон")) #доп способ

# from collections import Counter
# print(Counter(animals))
