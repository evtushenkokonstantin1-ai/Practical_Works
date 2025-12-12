num = int(input("Введите целое число: "))
dig = 0

while num > 0:
    print(num % 10)
    num = num // 10
