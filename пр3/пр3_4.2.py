wave = float(input("Введите длинну волны: "))
if wave <= 450:
    print("Цвет: ", "Фиолетовый")
elif wave in range(450, 480):
    print("Цвет: ", "Синий")
elif wave in range(480, 510):
    print("Цвет: ", "Сине-зелёный")
elif wave in range(510, 550):
    print("Цвет: ", "Зелёный")
elif wave in range(550, 570):
    print("Цвет: ", "Жёлто-зелёный")
elif wave in range(570, 590):
    print("Цвет: ", "Жёлтый")
elif wave in range(590, 630):
    print("Цвет: ", "Оранжевый")
elif wave >= 630:
    print("Цвет: ", "Красный")