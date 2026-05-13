#Приложение для туристического агентства ТУР. Таблица Турист должна
#содержать следующую информацию о клиентах турфирмы: Код клиента, Клиент
#(Фамилия), Телефон, Название страны, Регион, Продолжительность поездки, Стоимость
#путевки.

import sqlite3 as sq
with sq.connect('Tour.db') as con:
    cur = con.cursor()
    cur.execute("""CREATE TABLE IF NOT EXISTS users (
        client_id INTEGER PRIMARY KEY AUTOINCREMENT,
        phone_number TEXT NOT NULL,
        last_name TEXT NOT NULL,
        region TEXT NOT NULL,
        tour_time TEXT NOT NULL,
        price INTEGER NOT NULL
    )""")

con.commit()