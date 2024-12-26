'''for i in range(26):
    for j in range(26):
        print(f"{chr(ord('a')+i)}{chr(ord('a')+j)}")'''

# print(ord("a"))
# print(ord("b"))
# print(ord("c"))
# print(chr(97))
# print(chr(98))
# print(chr(99))
#print(chr(ord("a")+11))
#((2 + 2) + 2)

'''password = 'right_password'

while True:
    if input("Введите пароль: ") == password:
        print("Пароль принят")
        break'''

'''flag = False
for i in range(26):
    for j in range(26):
        text = f"{chr(ord('a')+i)}{chr(ord('a')+j)}"
        if text == "ya":
            print(text)
            flag = True
            break
        print(text)
    if flag:
        break'''
'''for i in range(26):
    for j in range(26):
        if i == j:
            continue
        print(f"{chr(ord('a')+i)}{chr(ord('a')+j)}")'''
'''for i in range(26):
    for j in range(26):
        if i != j:
            print(f"{chr(ord('a')+i)}{chr(ord('a')+j)}")'''

'''while (text := input("введите строку (СТОП для остановки): ")) != "СТОП":
    if text == 'ignore_else':
        break
else:
    print("Цикл завершен")'''
# 1. Построить треугольник, где строки содержат цифры от 1 до номера строки

'''for i in range(1, 6):
    for j in range(1, i+1):
        print(j, end = '')
    print()
'''

# 2. Вывести квадрат из # размером 4х4
'''for i in range(4):
    for j in range(4):
        print('#', end = '')
    print()'''
# 3. Построить треугольник, начиная с 5 звездочек.
# *****  
# ****  
# ***  
# **  
# *  
'''brick = '*'
size = 5
while size > 0:
    print(brick * size)
    size -= 1'''

'''for i in range(5, 0, -1):
    for j in range(i):
        print("*", end = '')
    print()'''

for row in range(5):
    for column in range(7):
        if row==0 or row==4 or column==0 or column==6:
            print('#', end='')
        else:
            print(' ', end = '')
    print()