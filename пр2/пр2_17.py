num = int(input("Введите трехзначное число: "))
first_digit = num // 100
second_digit = num // 10 % 10
third_digit = num % 10
print(third_digit, second_digit, first_digit, sep="")