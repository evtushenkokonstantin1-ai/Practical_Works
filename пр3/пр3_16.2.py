from operator import index

num1 = int(input("Введите число A: "))
num2 = int(input("Введите число B: "))
num3 = int(input("Введите число C: "))

list1 = [num1, num2, num3]
if num1 != num2 == num3:
    print(1)
elif num2 != num1 == num3:
    print(2)
elif num1 == num2 != num3:
    print(3)