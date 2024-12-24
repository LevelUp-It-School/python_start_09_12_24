# saved_pwd = "right_password"
# while input("Введите пароль для входа: ") != saved_pwd: 
# 	pass
# print("Пароль верный. Вход разрешён.")

'''name = input("Введите имя: ")
while name != "СТОП":
    print(f"Привет, {name}!")
    name = input("Введите имя: ")
print("Программа завершена.")'''

'''while (name := input("Введите имя: ")) != "СТОП":
    print(f"Привет, {name}!")
print("Программа завершена.")
'''

'''k = int(input("Введите начало диапазона: "))
n = int(input("Введите конец диапазона: "))
for i in range(k, n+1):
    print(i)'''

'''n = int(input("Введите конец диапазона: "))
for i in range(1, n+1, 2):
    print(i)'''

'''n = int(input("Введите первое число: "))
for i in range(n, -1, -1):
    print(i)'''
'''
for i in "Hello world":
    if i == "o":
        continue
    print(i*2)'''

for i in "Hello world":
    if i == "o":
        break
    print(i*2)
