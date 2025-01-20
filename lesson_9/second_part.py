# file_in = open(r"C:\Users\azubochenko\Desktop\Новая папка\python_start_09_12_24\lesson_9\input_1.txt", encoding="UTF-8")
# #Windows - cp-1251

# for line in file_in:
#     print(line)
# file_in.close()
FILE_PATH = r"C:\Users\azubochenko\Desktop\Новая папка\python_start_09_12_24\lesson_9\input_1.txt"
# with open(FILE_PATH, encoding="UTF-8") as file_in:
#     for line in file_in:
#         print(line.rstrip("\n"))

# with open(FILE_PATH, encoding="UTF-8") as file_in:
#     lines = file_in.readlines()
# print(lines)

# with open(FILE_PATH, encoding="UTF-8") as file_in:
#     symbols = file_in.read()
# print([symbols])


# with open('lesson_9/output_1.txt', "w", encoding="UTF-8") as file_out:
#     n = file_out.write("Это первая строка\nА вот это вторая\nИ третья - последняя строка")
# print(n)

# lines = ["Это первая строка\n", "А вот это вторая\n", "И третья - последняя строка"]
# with open('lesson_9/output_2.txt', "w", encoding="UTF-8") as file_out:
#     file_out.writelines(lines)

# with open("lesson_9/output_3.txt", "w", encoding="UTF-8") as file_out:
#     print("Вывод в файл с помощью функции print()", file = file_out)