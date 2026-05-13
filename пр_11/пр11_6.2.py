##Составить генератор  (yield), который переведёт
# символы строки из нижнего регистра в верхний
def nizhni_express (stroka):
    for char in stroka:
        yield char.lower()

bar = ""

for char in nizhni_express("Бар НиЖнИй ЭкСпреСС"):
    bar += char
print(bar)