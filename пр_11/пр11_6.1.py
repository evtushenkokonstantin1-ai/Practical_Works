##Даны температуры за месяц март. Необходимо найти количество положительных
# и отрицательных значений температур в месяце, самую низкую и самую высокую
# температуры, а также среднемесячное значение температуры.

import random

t_march = [random.randint(-15,30) for element in range(31)]

count_pos = 0
count_neg = 0

for element in t_march:
    if element > 0:
        count_pos += 1
    elif element < 0:
        count_neg += 1


mx = max(t_march)
mn = min(t_march)
avg = sum(t_march) / len(t_march)

print(count_pos, count_neg, mx, mn, avg)