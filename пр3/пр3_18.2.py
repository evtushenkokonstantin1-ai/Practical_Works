num1 = int(input("Введите число A: "))
num2 = int(input("Введите число B: "))
num3 = int(input("Введите число C: "))

s_num = (num1 + num2 + num3)
min_num = min(num1, num2, num3)
max_num = max(num1, num2, num3)
mid = s_num - min_num - max_num
print("Среднее число: ", mid)