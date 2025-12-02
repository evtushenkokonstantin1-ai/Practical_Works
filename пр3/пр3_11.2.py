import random
num = random.randint(1, 999)
print("Число: ", num)

if num % 2 == 0 and num // 100 > 0:
    print("Чётное трёхзначное число")
elif num % 2 == 1 and num // 100 > 0:
    print("Нечётное трёхзначное число")
elif num % 2 == 0 and num // 100 == 0 and num // 10 > 0:
    print("Чётное двузначное число")
elif num % 2 == 1 and num // 100 == 0 and num // 10 > 0:
    print("Нечётное двузначное число")
elif num % 2 == 0 and num // 100 == 0 and num // 10 == 0:
    print("Чётная цифра")
elif num % 2 == 1 and num // 100 == 0 and num // 10 == 0:
    print("Нечётная цифра")