# countries = {country: capital for country, capital in [("Россия", "Москва"), ("Беларусь", "Минск"), ("Сербия", "Белград")]}
# print(countries)

# numbers = (int(input()) for i in range(5))
# print(numbers)

# from sys import getsizeof

# numbers_iter =(i for i in range(10 ** 6))
# print(getsizeof(numbers_iter))

# numbers_list = list(range(10 **6))
# print(getsizeof(numbers_list))

# from timeit import timeit

# print(round(timeit("s = '; '.join(str(x) for x in range(10 ** 7))", number = 10), 3))
# print(round(timeit("s = '; '.join([str(x) for x in list(range(10 ** 7))])", number = 10), 3))

# x = 5
# print(id(x))
# x = 10
# print(id(x))

# x = 1
# y = x

# print(id(x))
# print(id(y))
# print(x is y)

# x = [el ** 2 for el in range(5)]
# y = [el ** 2 for el in range(5)]
# print(x is y)
# print(x == y)

# numbers = [1, 2, 3]
# print(id(numbers))

# # numbers += [4]
# # print(id(numbers))

# numbers = numbers + [4]
# print(id(numbers))

# x = [1, 2, 3]
# y = x

# print (x is y)
# x[0] = 0

# print(x)
# print(y)
# print(x is y)

# x = [1, 2, 3]
# y = x[:]

# print (x is y)
# x[0] = 0

# print(x)
# print(y)
# print(x is y)

# numbers = [[1, 2, 3],
#            [4, 5, 6],
#            [7, 8, 9]]

# numbers_copy = numbers[:]
# numbers_copy = [element[:] for element in numbers]
# print([numbers_copy[i] is numbers[i] for i in range(len(numbers))])

from copy import deepcopy

numbers = [[1, 2, 3],
           [4, 5, 6],
           [7, 8, 9]]
# numbers_copy = numbers.copy()
# print(numbers is numbers_copy)
# numbers_copy = deepcopy(numbers)
# print([numbers_copy[i] is numbers[i] for i in range(len(numbers))])

# numbers = [1, 2, 3, 6, 8, 4, 55]
# threshold = 5
# numbers_new = [i**2 for i in numbers if i>threshold]
# print(numbers_new)

# words = ['banana', 'strawberry', 'apple', 'pineapple', 'plum']
# dct = {word: len(word) for word in words}
# print(dct)

numbers = [1, 3, 5, 15, 16]
gen = ("FizzBuzz" if num % 3 == 0 and num % 5 == 0
        else "Fizz" if num % 3 == 0
        else "Buzz" if num % 5 == 0 
        else num for num in numbers)
for value in gen:
    print(value)