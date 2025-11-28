num = int(input("Введите трехзначное число: "))
first_digit = num // 100
rest_digits = num % 100
print(rest_digits, first_digit, sep="")