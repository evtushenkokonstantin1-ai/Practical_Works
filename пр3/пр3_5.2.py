num = int(input("Введите трехзначное число: "))

suit = num // 100
dignity = num % 100

if suit == 1 and dignity == 11:
    print("Валет пик")
elif suit == 2 and dignity == 11:
    print("Валет треф")
elif suit == 3 and dignity == 11:
    print("Валет бубен")
elif suit == 4 and dignity == 11:
    print("Валет червов")
elif suit == 1 and dignity == 12:
    print("Дама пик")
elif suit == 2 and dignity == 12:
    print("Дама треф")
elif suit == 3 and dignity == 12:
    print("Дама бубен")
elif suit == 4 and dignity == 12:
    print("Дама червов")
elif suit == 1 and dignity == 13:
    print("Король пик")
elif suit == 2 and dignity == 13:
    print("Король треф")
elif suit == 3 and dignity == 13:
    print("Король бубен")
elif suit == 4 and dignity == 13:
    print("Король червов")
elif suit == 1 and dignity == 14:
    print("Туз пик")
elif suit == 2 and dignity == 14:
    print("Туз треф")
elif suit == 3 and dignity == 14:
    print("Туз бубен")
elif suit == 4 and dignity == 14:
    print("Туз червов")