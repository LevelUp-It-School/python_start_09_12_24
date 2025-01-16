# numbers = []
# for i in range(5):
#     numbers.append(int(input()))
# print(numbers)

# numbers = [int(input()) for i in range(5)]
# avg = sum(numbers) / len(numbers)
# numbers = [element for element in numbers if element > avg]
# print(numbers)
# print(avg)

# newlist = []
# for element in numbers:
#     newlist.append(element**2)

# numbers = [int(input()) for i in range(5)]
# numbers = [element for element in numbers if element > sum(numbers) / len(numbers)] #неправильный пример
# print(numbers)
# print(avg)

#print(input().split())

# matrix = [[int(x) for x in input().split()] for i in range(5)]
# print(matrix)

#zeros = [[0] * 5] * 5 #НЕВЕРНАЯ ЗАПИСЬ
# print(zeros)
# zeros[0][0] = 1
# print(zeros)

# zeros = [[0] * 5 for i in range(5)]
# print(zeros)
# zeros[0][0] = 1
# print(zeros)

# text = "Строка символов"
# codes = [ord(symbol) for symbol in text]
# print(codes)

countries = {'Россия':["русский"],
            'Беларусь':["беларусский", "русский"],
            "Бельгия":["немецкий", "французский", "нидерландский"],
            "Вьетнам": ["вьетнамский"]}
multiple_lang = [country for country, lang in countries.items() if len(lang)>1]
print(multiple_lang)