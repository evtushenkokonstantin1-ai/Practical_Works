#Приложение для туристического агентства ТУР. Таблица Турист должна
#содержать следующую информацию о клиентах турфирмы: Код клиента, Клиент
#(Фамилия), Телефон, Название страны, Регион, Продолжительность поездки, Стоимость
#путевки.

import sqlite3 as sq
import tkinter as tk
from tkinter import messagebox

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

def add_client():
    phone_number = ent_phone.get()
    last_name = ent_name.get()
    region = ent_region.get()
    tour_time = ent_time.get()
    price = ent_price.get()

    with sq.connect('Tour.db') as con:
        cur = con.cursor()
        cur.execute("""
        INSERT INTO users (phone_number, last_name, region, tour_time, price) 
        VALUES (?, ?, ?, ?, ?) """, (phone_number, last_name, region, tour_time, int(price or 0)))

    messagebox.showinfo("Успех", "Клиент успешно добавлен!")
    for e in (ent_phone, ent_name, ent_region, ent_time, ent_price):
        e.delete(0, tk.END)


def search_client():
    val = ent_crit.get()
    txt_output.delete("1.0", tk.END)  # Очищаем поле вывода

    with sq.connect('Tour.db') as con:
        cur = con.cursor()
        cur.execute("""SELECT * FROM users WHERE last_name = ? OR phone_number = ? OR client_id = ?""", (val, val, val))
        rows = cur.fetchall()

    txt_output.insert(tk.END, "Результат:\n")
    for row in rows:
        txt_output.insert(tk.END, f"{row}\n")


def edit_client():
    c_id = ent_crit.get()
    val = ent_name.get()

    if not c_id:
        messagebox.showwarning("Ошибка", "Введите ID клиента в поле 'Критерий / ID'!")
        return

    with sq.connect('Tour.db') as con:
        cur = con.cursor()
        cur.execute("""UPDATE users SET last_name = ? WHERE client_id = ?""", (val, int(c_id)))

    messagebox.showinfo("Успех", "Данные (фамилия) успешно обновлены!")


def delete_client():
    val = ent_crit.get()

    with sq.connect('Tour.db') as con:
        cur = con.cursor()
        cur.execute("""DELETE FROM users WHERE client_id = ? OR phone_number = ? OR last_name = ?""", (val, val, val))

    messagebox.showinfo("Успех", "Успешно удалено!")

root = tk.Tk()
root.title("Управление Tour.db")
root.geometry("450x620")
root.configure(padx=20, pady=15)

tk.Label(root, text="Фамилия клиента:", font=("Arial", 10)).pack(anchor="w", pady=(5, 2))
ent_name = tk.Entry(root, font=("Arial", 10))
ent_name.pack(fill="x", pady=(0, 5))

tk.Label(root, text="Номер телефона:", font=("Arial", 10)).pack(anchor="w", pady=(5, 2))
ent_phone = tk.Entry(root, font=("Arial", 10))
ent_phone.pack(fill="x", pady=(0, 5))

tk.Label(root, text="Регион:", font=("Arial", 10)).pack(anchor="w", pady=(5, 2))
ent_region = tk.Entry(root, font=("Arial", 10))
ent_region.pack(fill="x", pady=(0, 5))

tk.Label(root, text="Продолжительность поездки:", font=("Arial", 10)).pack(anchor="w", pady=(5, 2))
ent_time = tk.Entry(root, font=("Arial", 10))
ent_time.pack(fill="x", pady=(0, 5))

tk.Label(root, text="Цена тура:", font=("Arial", 10)).pack(anchor="w", pady=(5, 2))
ent_price = tk.Entry(root, font=("Arial", 10))
ent_price.pack(fill="x", pady=(0, 10))

tk.Frame(root, height=1, bg="darkgrey").pack(fill="x", pady=5)
tk.Label(root, text="Критерий / ID для поиска, изменения и удаления:", font=("Arial", 10, "bold"), fg="blue").pack(
    anchor="w", pady=(5, 2))
ent_crit = tk.Entry(root, font=("Arial", 10), bg="#FFFFE0")
ent_crit.pack(fill="x", pady=(0, 10))

btn_add = tk.Button(root, text="1. Добавить", font=("Arial", 10), command=add_client)
btn_add.pack(fill="x", pady=2)

btn_search = tk.Button(root, text="2. Поиск", font=("Arial", 10), command=search_client)
btn_search.pack(fill="x", pady=2)

btn_edit = tk.Button(root, text="3. Редактировать (меняет фамилию по ID)", font=("Arial", 10), command=edit_client)
btn_edit.pack(fill="x", pady=2)

btn_delete = tk.Button(root, text="4. Удаление", font=("Arial", 10), command=delete_client)
btn_delete.pack(fill="x", pady=2)

btn_exit = tk.Button(root, text="5. Выход", font=("Arial", 10, "bold"), fg="white", bg="#FF4A5A", command=root.quit)
btn_exit.pack(fill="x", pady=(10, 10))

txt_output = tk.Text(root, height=8, font=("Arial", 10))
txt_output.pack(fill="both", expand=True)

root.mainloop()