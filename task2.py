# Задача 18: Требуется найти в массиве A[1..N] самый близкий по величине элемент к заданному числу X.
# Пользователь в первой строке вводит натуральное число N – количество элементов в массиве.
# В последующих  строках записаны N целых чисел Ai. Последняя строка содержит число X
# *Пример:*

# 5
# 1 2 3 4 5
# 6
# -> 5

import random

n = int(input("Введите количество элементов в массиве: "))

lst = [random.randint(1, n) for i in range(n)]
print(*lst)

nearUp = max(lst)
nearDown = min(lst)


x = int(input("Введите число X: "))
for i in lst:
    if i < x and i > nearDown < x:
        nearDown = i
    elif i > x and i < nearUp:
        nearUp = i

if nearDown == x:
    print(f"{x} < {nearUp}")
elif nearUp == x:
    print(f"{nearDown} < {x}")
else:
    print(f"{nearDown} < {x} < {nearUp}")
