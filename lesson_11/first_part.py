#lambda x: x>0

# def only_pos(x):
#     return x > 0
# 
# result = filter(only_pos, [-1, 5, 6, -10, 0])
# print(", ".join(str(x) for x in result))

# result = filter(lambda x: x>0, [-1, 5, 6, -10, 0])
# print(", ".join(str(x) for x in result))

# result = map(lambda x: x**2, range(5))
# print(", ".join(str(x) for x in result))

# lines =['abcd', 'ab', 'ba', 'abcdef']
# print(sorted(lines, key=lambda line: (-len(line), line)))

# lines =['abcd', 'ab', 'ba', 'acde']
# print(min(lines, key=lambda line: (-len(line), line)))

# result = (x for x in [-1, 5, 6, -10, 0] if x>0)
# print(", ".join(str(x) for x in result))

# 1. O! = 1
# 2. n!=1*2*3*...*n, n>0

# def summ(n):
#     answer = 0
#     for i in range(n+1):
#         answer += i
#     return answer
# print(summ(5))


# def fact(n):
#     factorial = 1
#     for i in range(2, n+1):
#         factorial *= i 
#     return factorial

# print(fact(5))

# 1. O! = 1
# 2. n!=(1*2*3*...*(n-1))*n = n(n-1)

# def fact(n):
#     if n==0:
#         return 1
#     return fact(n-1)*n

# print(fact(5))

# 1. Первые два числа равны единице
# 2. n-е число Фибоначчи равно сумме двух предыдущих, то есть fib(n) = fib(n-1) + fib(n-2), где 
# n - индекс числа последовательности.

# 1 1 2 3 5 8 13 21 34...
from timeit import timeit

# def fib(n):
#     global count
#     count +=1
#     if n in (0, 1):
#         return 1
#     return fib(n-1)+fib(n-2)
# count = 0
# print(fib(35))
# #print(f"Среднее время вычисления: " f"{round(timeit('fib(35)', number=10, globals=globals())/10, 3)} сек.")
# print(f"Количество вызовов рекурсивной функции равно: {count}")

# def fib(n):
#     f_1, f=1, 1
#     for i in range(n-1):
#         f_1, f = f, f_1+f
#     return f

# print(f"Среднее время вычисления: " f"{round(timeit('fib(35)', number=10, globals=globals())/10, 6)} сек.")

from sys import setrecursionlimit
setrecursionlimit(2000)

# def fib(n):
#     global count
#     count +=1
#     if n not in cash:
#         cash[n] = fib(n-1)+fib(n-2)
#     return cash[n]

# count = 0
# cash = {0:1, 1:1}

# # print(fib(35))
# print(f"Среднее время вычисления: " f"{round(timeit('fib(1000)', number=10, globals=globals())/10, 6)} сек.")
# # print(f"Количество вызовов рекурсивной функции равно: {count}")

from functools import lru_cache

@lru_cache(maxsize=1000)
def fib(n):
    if n in (0,1):
        return 1
    return fib(n-1)+fib(n-2)

print(f"Среднее время вычисления: " f"{round(timeit('fib(35)', number=10, globals=globals())/10, 6)} сек.")
