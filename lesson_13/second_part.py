# print(";".join(str(1 / x) for x in range(int(input()), int(input())+1)))

# interval = range(int(input()), int(input())+1)
# if 0 in interval:
#     print("Диапазон содержит 0")
# else:
#     print(";".join(str(1 / x) for x in interval))

# start = input()
# end = input()
# if not(start.lstrip('-').isdigit() and end.lstrip('-').isdigit()):
#     print("Необходимо ввести 2 числа")
# else:
#     interval = range(int(start), int(end)+1)
#     if 0 in interval:
#         print("Диапазон содержит 0")
#     else:
#         print(";".join(str(1 / x) for x in interval))

# BaseException
#  +-- SystemExit
#  +-- KeyboardInterrupt
#  +-- GeneratorExit
#  +-- Exception
#       +-- StopIteration
#       +-- StopAsyncIteration
#       +-- ArithmeticError
#       |    +-- FloatingPointError
#       |    +-- OverflowError
#       |    +-- ZeroDivisionError
#       +-- AssertionError
#       +-- AttributeError
#       +-- BufferError
#       +-- EOFError
#       +-- ImportError
#       |    +-- ModuleNotFoundError
#       +-- LookupError
#       |    +-- IndexError
#       |    +-- KeyError
#       +-- MemoryError
#       +-- NameError
#       |    +-- UnboundLocalError
#       +-- OSError
#       |    +-- BlockingIOError
#       |    +-- ChildProcessError
#       |    +-- ConnectionError
#       |    |    +-- BrokenPipeError
#       |    |    +-- ConnectionAbortedError
#       |    |    +-- ConnectionRefusedError
#       |    |    +-- ConnectionResetError
#       |    +-- FileExistsError
#       |    +-- FileNotFoundError
#       |    +-- InterruptedError
#       |    +-- IsADirectoryError
#       |    +-- NotADirectoryError
#       |    +-- PermissionError
#       |    +-- ProcessLookupError
#       |    +-- TimeoutError
#       +-- ReferenceError
#       +-- RuntimeError
#       |    +-- NotImplementedError
#       |    +-- RecursionError
#       +-- SyntaxError
#       |    +-- IndentationError
#       |         +-- TabError
#       +-- SystemError
#       +-- TypeError
#       +-- ValueError
#       |    +-- UnicodeError
#       |         +-- UnicodeDecodeError
#       |         +-- UnicodeEncodeError
#       |         +-- UnicodeTranslateError
#       +-- Warning
#            +-- DeprecationWarning
#            +-- PendingDeprecationWarning
#            +-- RuntimeWarning
#            +-- SyntaxWarning
#            +-- UserWarning
#            +-- FutureWarning
#            +-- ImportWarning
#            +-- UnicodeWarning
#            +-- BytesWarning
#            +-- EncodingWarning
#            +-- ResourceWarning

# try:
#     <код, который может вызвать исключения>
# except <КлассИсключения_1>:
#     <код обработки исключения>
# except <КлассИсключения_2>:
#     <код обработки исключения>
# ...
# else:
#     <код выполняется, если не вызвано исключение в блоке try>
# finally:
#     <код который выполняется всегда>



# try:
#     print(1/int(input()))
# except Exception:
#     print("Неизвестная ошибка")
# except ZeroDivisionError:
#     print("Ошбика деления на ноль")
# except ValueError:
#     print("Невозможно преобразовать строку в число")

# try:
#     print(1/int(input()))
# except ZeroDivisionError:
#     print("Ошбика деления на ноль")
# except ValueError:
#     print("Невозможно преобразовать строку в число")
# except Exception:
#     print("Неизвестная ошибка")
# else:
#     print("Операция выполнена успешно")
# finally:
#     print("Программа завершена.")

# try:
#     print(";".join(str(1 / x) for x in range(int(input()), int(input())+1)))
# except ZeroDivisionError:
#     print("Нельзя делить на ноль")
# except ValueError:
#     print("Необходимо 2 числа")

class NumbersError(Exception):
    pass

class EvenError(NumbersError):
    pass

class NegativeError(NumbersError):
    pass

def no_even(numbers):
    if all(x % 2 !=0 for x in numbers):
        return True
    raise EvenError("В списке не должно быть четных числел")

def no_negative(numbers):
    if all(x>=0 for x in numbers):
        return True
    raise NegativeError("В списке не должно быть отрицательных числе")

try:
    numbers = [int(x) for x in input().split()]
    if no_negative(numbers) and no_even(numbers):
        print(f"Сумма чисел {sum(numbers)}")
except NumbersError as e:
    print(f"Произошла ошибка {e}")
except Exception as e:
    print(f"Произошла непредвиденная ошибка {e}")

