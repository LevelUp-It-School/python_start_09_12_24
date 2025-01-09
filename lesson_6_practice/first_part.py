#Найдите первую заглавную букву в строке text. Если её нет, выведите сообщение, что заглавных букв нет.
# text = "Hello world"

# found = False
# for char in text:
#     if char.isupper():
#         print(f"Первая щаглавная буква: {char}")
#         found = True
#         break
# if not found:
#     print("Нет заглавных букв")
#Удалите все восклицательные знаки только в конце строки, но не в середине.
# text = "!!!Hello!!! world!!!"
# while text.endswith('!'):
#     text=text[:-1]
# print(text)

#Удаление чисел из строки
# text = "Python 3.9 is awesome 2025"
# result = ''

# for char in text:
#     if not char.isdigit():
#         result += char
# print(result)

#Подсчет гласных и согласных
# text = "Hello world23213  2323"
# vowels = 'aeiou'
# vowels_counter = 0
# consonant_counter = 0

# for char in text:
#     if char.isalpha():
#         if char.lower() in vowels:
#             vowels_counter += 1
#         else:
#             consonant_counter += 1

# print (f'Согласных = {consonant_counter}, гласных = {vowels_counter}')

