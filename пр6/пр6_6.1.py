a = int(input("Введите первый элемент: "))
b = int(input("Введите второй элемент: "))

list = [a, b]

count_num = a + b

while len(list) < 10:
    list.append(count_num)
    count_num += list[-1]
print(list)