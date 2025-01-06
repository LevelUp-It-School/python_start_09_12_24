# for i in range(1, 6):
#     for j in range(5 - i):
#         print(" ", end='')
#     for j in range(2*i-1):
#         print("*", end = '')
#     print()

for i in range(5, 0, -1):
    for j in range(i):
        print("*", end = '')
    print()

for i in range(5):
    for j in range(7):
        if i==0 or i==4 or j==0 or j==6:
            print("#", end='')
        else:
            print(' ', end = '')
    print()