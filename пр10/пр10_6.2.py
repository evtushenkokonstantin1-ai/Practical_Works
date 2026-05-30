f = open("text18-6", "r", encoding="utf-8")
text = f.read()
f.close()

print(text)

spaces = 0

for symbol in text:
    if symbol.isspace():
        spaces += 1

print("Количество пробельных символов:", spaces)

punctuation = ".,:;!?-«»()"

new_text = ""

for symbol in text:
    if symbol in punctuation:
        new_text += "!"
    else:
        new_text += symbol

f = open("result.txt", "w", encoding="utf-8")

f.write(new_text)

f.close()

print("Файл result.txt создан")