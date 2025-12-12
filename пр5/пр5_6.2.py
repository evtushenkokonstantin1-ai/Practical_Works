def InvertDigits(K):
    res = 0
    while K > 0:
        l_dig = K % 10
        res = res * 10 + l_dig ##Двигаю последнюю цифру влево
        K = K // 10
    return res

for res in range(5): ##Цикл позволяет пользователю вводить 5 чисел,
    K = int(input("Введите число: ")) ##которые переворачиваются с помощью вызова функции
    print(InvertDigits(K))