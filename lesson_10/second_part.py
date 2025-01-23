# def list_modify_1(list_arg):
#     list_arg = [1,2,3,4]

# def list_modify_2(list_arg):
#     list_arg += [4]

# sample_1 = [1, 2, 3]
# sample_2 = [1, 2, 3]

# list_modify_1(sample_1)
# list_modify_2(sample_2)

# print(sample_1)
# print(sample_2)


# def inc():
#     global x
#     x += 1
#     print(f'Количество вызовов функции равно {x}.')

# x = 0
# inc()
# inc()
# inc()

# def f(count):
#     count += 1
#     print(f'Количество вызовов функции равно {count}.')
#     return count

# count_f = 0
# count_f = f(count_f)
# count_f = f(count_f)
# count_f = f(count_f)
# count_f = f(count_f)

# def final_price(price, discount=1):
#     final_price = price - price * discount / 100
#     return final_price

# print(final_price(1000, 5))
# print(final_price(1000))

# def add_value(x, list_arg = []):
#     list_arg += [x]
#     return list_arg

# print(add_value(0))
# print(add_value(0, [1, 2, 3]))
# print(add_value(1))

# def add_value(x, list_arg = None):
#     if list_arg is None:
#         list_arg = []
#     list_arg += [x]    
#     return list_arg

# print(add_value(0))
# print(add_value(0, [1, 2, 3]))
# print(add_value(1))

# def final_price(price, discount=1):
#     final_price = price - price * discount / 100
#     return final_price

# print(final_price(1000, discount=5))
# print(final_price(discount=5, price=1000))


# def final_price(*prices, discount=1):
#     return [price - price * discount / 100 for price in prices]
    

# print(final_price(1000, 15400, 600, 666, 56, discount=5))

# def final_price(*prices, discount=1, **kwargs):
#     low = kwargs.get("price_low", min(prices))
#     high = kwargs.get("price_high", max(prices))
#     return [price - price * discount / 100 for price in prices if low <= price <= high]
    

# print(final_price(1000, 15400, 600, 666, 56, discount=5))
# print(final_price(1000, 15400, 600, 666, 56, discount=5, price_low =200))
# print(final_price(1000, 15400, 600, 666, 56, discount=5, price_high =200))
# print(final_price(1000, 15400, 600, 666, 56, discount=5, price_low =200, price_high = 1500))


# def printc(arg1, arg2, *args, **kwargs):
#     print(" ".join([arg1]+[arg2]+list(args)+list(kwargs.values())))

# printc('1', '2', '3', '66', four = '4', five='5')

# def only_pos(x):
#     return x > 0

# result = filter(only_pos, [-1, 5, 6, -10, 0])
# print(", ".join(str(x) for x in result))

# result = filter(str.isalpha, '12323ABcd)()')
# print(" ".join(result))

# def square(x):
#     return x**2

# result = map(square, range(5))
# print(", ".join(str(x) for x in result))

# result = map(str.lower, ['avDDSD', 'sdRRRsds', "dfdfDFDFDGSDGDF"])
# print("\n".join(result))

numbers = list(map(int, input().split()))
