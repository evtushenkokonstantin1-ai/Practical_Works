#Из предложенного текстового файла (text18-6.txt) вывести на экран его содержимое,
#количество пробельных символов. Сформировать новый файл, в который поместить текст
#в стихотворной форме предварительно заменив все знаки пунктуации на знак «!».

f = open("text18-6.txt", "r", encoding="utf-16")
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

f = open("result.txt", "w", encoding="utf-16")

f.write(new_text)

f.close()

print("Файл создан")