with open('suka_1.txt', 'r') as f:
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

with open('suka_final.txt', 'w', encoding='utf-8') as f:
    f.write(f'Количество элементов: {nums}\n')
    f.write(f'Произведение элементов: {prod}\n')
    f.write(f'Повторяющиеся элементы: {rep}\n')
    f.write(f'Количество повторяющихся элементов: {rep_c}\n')
    f.write(f'Элементов больше 5 увеличены в 2 раза: {modified}\n')
