x = int(input("Введите координату X: "))
y = int(input("Введите координату Y: "))

if x == 0 and y == 0:
    print(0)
elif x != 0 and y == 0:
    print(1)
elif x == 0 and y != 0:
    print(2)
elif x != 0 and y != 0:
    print(3)