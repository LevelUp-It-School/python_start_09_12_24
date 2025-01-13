# countries_and_capitals = [("Россия", "Москва"),("США","Вашингтон"),("Франция","Париж")]
# for country in countries_and_capitals:
#     if "Франция" == country[0]:
#         print(country[1])
#         break

from itertools import zip_longest


countries_and_capitals = {"Россия": "Москва",
                          "США": "Вашингтон",
                          "Франция": "Париж"}
# print(countries_and_capitals["Франция"])
# countries_and_capitals["Сербия"] = "Белград"
# print(countries_and_capitals)

# d = {"key": "old_value"}
# d['key'] = "new_value"
# print(d['not_existed_key'])
# if "Сербия" in countries_and_capitals:
#     print(countries_and_capitals["Сербия"])
# else:
#     print("Страна пока отсутствует в словаре")

# for country in countries_and_capitals:
#     print(f"У страны {country} столица - {countries_and_capitals[country]}")

# countries = dict()
# country = input()
# str_number = 0

# while country != "СТОП":
#     if country not in countries:
#         countries[country] = [str_number]
#     else:
#         countries[country].append(str_number)
#     str_number+=1
#     country = input()

# for country in countries:
#     print(f"{country}: {countries[country]}")

d = {"a":1, "b":2, "c":3}
#print(len(d))
#del d['b']
#d.clear()
#d_new = d.copy()
#print(d.get('е'), "Ключа нет")

#for key, value in d.items():
#     print(key, value)
# for key in d.keys():
#      print(key)

#print(d.keys())
# for value in d.values():
#      print(value)

# print(d.values())

# x = d.pop("a")
# print(x)
# print(d)

# countries = dict()
# country = input()
# str_number = 0

# while country != "СТОП":
#     countries[country] = countries.get(country, []) + [str_number]
#     str_number+=1
#     country = input()

# for country in countries:
#     print(f"{country}: {countries[country]}")

# x = []
# x = x + [5]
# print(x)

#zipped = list(zip([0,1,2], '012', ('zero', 'one', 'two')))
#zipped = list(zip('012'))
#zipped = list(zip([0,1,2], '012', {0:'zero', 1:'one', 2:'two'}))
#zipped = list(zip([0,1,2], '012', {0:'zero', 1:'one', 2:'two'}.values()))
#zipped = list(zip([0,1,2], '012', ('zero', 'one', 'two')))
#
# print(zipped)
zipped_longest = list(zip_longest([0,1,2], '0123456789', ('zero', 'one', 'two', 'three'), fillvalue="???"))
print(zipped_longest)

