num = int(input("Введите трехзначное число: "))
last_digit = num % 10
rest_digits = num // 10
print(last_digit, rest_digits, sep="")