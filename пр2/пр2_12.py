num = int(input("Введите двузначное число: "))
first_digit = num // 10
second_digit = num % 10
sum = first_digit + second_digit
prod = first_digit * second_digit
print(sum, prod)