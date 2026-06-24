#Из исходного текстового файла (ip_address.txt) из раздела «Зарезервированные
#адреса» перенести в первый файл строки с ненулевыми первым и вторым октетами,
#а во второй – все остальные. Посчитать количество полученных строк в каждом
#файле.

import re

f = open("ip_address.txt", "r")
text = f.readlines()
f.close()

f1 = open("file1.txt", "w")
f2 = open("file2.txt", "w")

count1 = 0
count2 = 0
shablon = r"\d+\.\d+\.\d+\.\d+"
start = False

for line in text:
    ip = re.search(shablon, line)

    if ip:
        address = ip.group()
        octets = address.split(".")

        if octets[0] != "0" and octets[1] != "0":
            f1.write(line)
            count1 += 1

        else:
            f2.write(line)
            count2 += 1

f1.close()
f2.close()

print("Строк в первом файле: ", count1)
print("Строк во втором файле: ", count2)