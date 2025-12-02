num = int(input("Введите четырехзначное число: "))

f_dig = num // 1000
s_dig = num % 1000 // 100
t_dig = num % 1000 % 100 // 10
fs_dig = num % 1000 % 100 % 10
rev_num = str(fs_dig) + str(t_dig) + str(s_dig) + str(f_dig)

print(num == rev_num)