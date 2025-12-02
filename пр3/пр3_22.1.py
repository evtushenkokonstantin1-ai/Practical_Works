num = int(input("Введите трехзначное число: "))

f_dig = num // 100
s_dig = num % 100 // 10
t_dig = num % 100 % 10

print(f_dig < s_dig < t_dig)