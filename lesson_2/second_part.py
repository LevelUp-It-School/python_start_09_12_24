'''import random

secret = random.randint(1, 10)
guess = int(input("Угадайте число от 1 до 10: "))

if guess == secret:
    print("Поздравляем, вы угадали!!!")
elif guess > secret:
    print("Ваше число больше загаданного!")
else:
    print("Ваше число меньше загадонного")'''\
    

a = int(input('enter num: '))
dev_by_3 = a % 3
dev_by_5 = a % 5
if dev_by_3 == 0 and dev_by_5 == 0:
    print('FizzBuzz')
elif dev_by_5 == 0:
    print('Buzz')
elif dev_by_3 == 0:
    print('Fizz')
else:
    print(a)