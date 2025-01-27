# def decorator(old_func):
#     def new_func():
#         return old_func()

# @decorator
# def func():
#     ...
# # print(func)
# # func = decorator(func)
# # print(func)


# def count(f):
#     total = 0

#     def decorated(*args, **kwargs):
#         nonlocal total
#         total+=1
#         return f(*args, **kwargs), total
#     return decorated

# @count
# def hello(name):
#     return f"Hello {name}!!!"

# print(hello("Пользователь_1"))        
# print(hello("Пользователь_2"))


# squares = (i**2 for i in range(10))
# print(squares)

# def fib(n):
#     n_1, n_2 = 1, 1
#     for i in range(n):
#         yield n_1
#         n_1, n_2 = n_2, n_1+n_2

# print(", ".join(str(x) for x in fib(10)))

#Напишите функцию list_sum(numbers) которая с использованием рекурсии вычисляет сумму элементов списка.

# def list_sum(numbers):
#     if not numbers:
#         return 0 
#     return numbers[0] + list_sum(numbers[1:])

# print(list_sum([1,2,3,4,5]))

# words = ["пицца", "бургер", "пепперони", "суши", "макароны", "сыр"]
# pizza_filter = filter(lambda x: 'пицца' in x or "пепперони" in x or "сыр" in x, words)

# print(list(pizza_filter))

# wrong_calculator = lambda a, b: a+b+42

# print(wrong_calculator(15,5))

laziness_level = lambda tasks: "Ленивый" if tasks < 15 else "Трудолюбивый"
print(laziness_level(20))