#Даны три словаря на три элемента каждый. Объединить все словари в один. Вывести
#исходные словари и результирующий.

suka = {'jopa': 1, 'pidor': 2, 'ueban': 3}
bliad = {'suchka': 4, 'juchka': 5, 'xuilo': 6}
pizda = {'xui': 7, 'govno': 8, 'zalupa': 9}

result = {**suka, **bliad, **pizda}
print(result)
print(suka)
print(bliad)
print(pizda)