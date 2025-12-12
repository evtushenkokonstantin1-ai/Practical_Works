def line():
    sym = str(input("Введите символ: "))
    c_sym = int(input("Введите количество символов: "))
    p_line = sym * c_sym
    return p_line

print(line())