#1. Средствами языка Python сформировать текстовый файл (.txt), содержащий
#последовательность из целых положительных и отрицательных чисел. Сформировать
#новый текстовый файл (.txt) следующего вида, предварительно выполнив требуемую
#обработку элементов:
#Исходные данные:
#Количество элементов:
#Произведение элементов:
#Повторяющиеся элементы:
#Количество повторяющихся элементов:
#Элементы больше 5 увеличены в два раза:

with open('6.1.txt', 'r') as f:
    nums = list(map(int, f.read().split()))

    count = len(nums)

prod = 1
for i in nums:
    prod *= i

rep = []
for i in nums:
    if nums.count(i) > 1:
        rep.append(i)

rep_c = len(rep)

modified = []
for i in nums:
    if i > 5:
        modified.append(i * 2)
    else:
        modified.append(i)

with open('6.2_final.txt', 'w', encoding='utf-8') as f:
    f.write(f'Количество элементов: {nums}\n')
    f.write(f'Произведение элементов: {prod}\n')
    f.write(f'Повторяющиеся элементы: {rep}\n')
    f.write(f'Количество повторяющихся элементов: {rep_c}\n')
    f.write(f'Элементов больше 5 увеличены в 2 раза: {modified}\n')
