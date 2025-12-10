num = int(input("Введите целое число: "))
dig = 0

while num > 0:
    num = num // 10
    str(num)
    dig += num
print(dig)