num = int(input("Ввести трехзначное число: "))
first_digit = num // 100
second_digit = num // 10 % 10
third_digit = num % 10
sum = first_digit + second_digit + third_digit
prod = first_digit * second_digit * third_digit
print(sum, prod)