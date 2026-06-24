#Составить генератор (yield), который переведёт
# символы строки из нижнего регистра в верхний
def nizhni_express (stroka):
    for letter in stroka:
        yield letter.lower()

bar = ""

for letter in nizhni_express("ТиХИй ДеН"):
    bar += letter
print(bar)