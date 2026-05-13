import sqlite3 as sq
with sq.connect('Tour.db') as con:
    cur = con.cursor()

    while True:
        print("Выберите действие: \n1. Добавить \n2. Поиск \n3. Редактировать \n4. Удаление \n5. Выход")
        choice = int(input("Выбор действия 1-5: "))

        if choice == 1:
            for i in range(10):
                phone_number = str(input('Введите номер телефона клиента: '))
                last_name = str(input('Введите фамилию клиента: '))
                region = str(input('Введите регион клиента: '))
                tour_time = str(input('Введите продолжительность поездки: '))
                price = int(input('Введите цену тура: '))

                cur.execute("""
                INSERT INTO users (phone_number, last_name, region, tour_time, price) 
                VALUES (?, ?, ?, ?, ?) """, (phone_number, last_name, region, tour_time, price))
        elif choice == 2:
            print("Поиск \n1. По фамилии \n2. По номеру телефона \n3. По id")
            choice_sel = int(input("Введите номер критерия: "))
            if choice_sel == 1:
                last_name = str(input("Введите нужную фамилию: "))
                cur.execute("""SELECT * FROM users WHERE last_name = ?""", (last_name,))
            elif choice_sel == 2:
                phone_number = str(input('Введите номер телефона клиента: '))
                cur.execute("""SELECT * FROM users WHERE phone_number = ?""", (phone_number,))
            elif choice_sel == 3:
                client_id = int(input('Введите id клиента: '))
                cur.execute("""SELECT * FROM users WHERE client_id = ?""", (client_id,))
            rows = cur.fetchall()
            print("Результат: ")
            for row in rows:
                print(row)
        elif choice == 3:
            print("Редактирование: \n1. По id \n2. По номеру телефона \n3. По фамилии \n4. По региону \n5. По продолжительности поездки \n6. По цене тура")
            choice_upd = int(input("Введите номер критерия: "))
            if choice_upd == 1:
                client_id = int(input('Введите id клиента: '))
                cur.execute("""UPDATE users SET client_id = ?""", (client_id,))
            if choice_upd == 2:
                phone_number = str(input('Введите номер телефона клиента: '))
                cur.execute("""UPDATE users SET client_id = ?""", (phone_number,))
            if choice_upd == 3:
                last_name = str(input('Введите фамилию клиента: '))
                cur.execute("""UPDATE users SET client_id = ?""", (last_name,))
            if choice_upd == 4:
                region = str(input('Введите регион клиента: '))
                cur.execute("""UPDATE users SET client_id = ?""", (region,))
            if choice_upd == 5:
                tour_time = str(input('Введите продолжительность поездки: '))
                cur.execute("""UPDATE users SET client_id = ?""", (tour_time,))
            if choice_upd == 6:
                price = int(input('Введите цену тура: '))
                cur.execute("""UPDATE users SET client_id = ?""", (price,))

        elif choice == 4:
            print("Удаление: \n1. По id \n2. По номеру телефона \n3. По фамилии \n4. По региону \n5. По продолжительности поездки \n6. По цене тура")
            choice_del = int(input("Введите номер критерия: "))
            if choice_del == 1:
                cur.execute("""DELETE FROM users WHERE client_id = ?""", (client_id,))
            if choice_del == 2:
                cur.execute("""DELETE FROM users WHERE phone_number = ?""", (phone_number,))
            if choice_del == 3:
                cur.execute("""DELETE FROM users WHERE last_name = ?""", (last_name,))
            if choice_del == 4:
                cur.execute("""DELETE FROM users WHERE region = ?""", (region,))
            if choice_del == 5:
                cur.execute("""DELETE FROM users WHERE tour_time = ?""", (tour_time,))
            if choice_del == 6:
                cur.execute("""DELETE FROM users WHERE price = ?""", (price,))
            print("Успешно удалено!")

        elif choice == 5:
            break