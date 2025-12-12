def AddRightDigit(D, K):
    res = 0
    res = str(K) + str(D)
    return res

D = int(input("Введите число D: "))
K = int(input("Введите число K: "))
print(AddRightDigit(D, K))