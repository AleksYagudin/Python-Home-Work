#Напишите программу, которая принимает на вход цифру, обозначающую день недели, и проверяет, является ли этот день выходным.

#day = int(input("Введите номер дня недели : "))

#if day != 6 and day !=7:
#    print("Рабочий")
#else:
#    print("Выходной")

#Напишите программу, которая принимает на вход координаты точки (X и Y), причём X ≠ 0 и Y ≠ 0 и выдаёт номер четверти плоскости, в которой находится эта точка (или на какой оси она находится).

# x = int(input("введите X : "))
# y = int(input("введите Y : "))

# if x > 0 and y >0:
#     print ("1")
# if x < 0 and y > 0:
#     print("2")
# if x < 0 and y < 0:
#     print("3")
# if x > 0 and y < 0:
#     print(4)

#Напишите программу, которая по заданному номеру четверти, показывает диапазон возможных координат точек в этой четверти (x и y).

# number = int(input("Введите номер четверти : "))

# if number == 1:
#     print("x(0 ; + ∞) , y(0 ; + ∞)")
# if number == 2:
#     print("x(- ∞ ; 0) , y(0 ; + ∞)")
# if number == 3:
#     print("x(- ∞ ; 0) , y(- ∞ ; 0)")
# if number == 4:
#     print("x(0 ; + ∞) , y(- ∞ ; 0)")


#Напишите программу, которая принимает на вход координаты двух точек и находит расстояние между ними в 2D пространстве.

# import math

# x1 = int(input("Введите x1 : "))
# y1 = int(input("Введите y1 : "))
# x2 = int(input("Введите x2 : "))
# y2 = int(input("Введите y2 : "))

# x = x2 - x1
# y = y2 - y1
# z = x * x + y * y

# r = math.sqrt(z)
# print(round(r, 2))


#Напишите программу для. проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.

# x = int(input('Введите число x '))
# y = int(input('Введите число y '))
# z = int(input('Введите число z '))

# a = x * y * z
# b = x + y + z

# if a > 0:
#     a = 0
# elif a < 1:
#     a = 1
# if b > 0:
#     b = 0
# elif b < 1:
#     b = 1

# if a == b:
#     print('Утверждение истинно')
# elif a != b:
#     print('Утверждение ложно')