num = int(input("Введите трехзначное число: "))
last_digit = num % 100 % 10
middle_digit = num // 10 % 10
print(last_digit, middle_digit)