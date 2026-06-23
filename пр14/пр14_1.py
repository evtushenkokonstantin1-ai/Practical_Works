import tkinter as tk

def check_numbers():
    try:
        a = int(entry_a.get())
        b = int(entry_b.get())

        condition = (a % 2 == 0 or b % 2 == 0)

        if condition:
            lbl_result.config(text="Результат: True (есть четное число)", fg="green")
        else:
            lbl_result.config(text="Результат: False (оба числа нечетные)", fg="red")

    except ValueError:
        lbl_result.config(text="Ошибка: Введите корректные целые числа!", fg="orange")

root = tk.Tk()
root.title("Проверка четности")
root.geometry("400x250")
root.configure(pady=20, padx=20)

tk.Label(root, text="Введите число A:", font=("Arial", 10)).pack(anchor="w", pady=(0, 2))
entry_a = tk.Entry(root, font=("Arial", 10))
entry_a.pack(fill="x", pady=(0, 10))

tk.Label(root, text="Введите число B:", font=("Arial", 10)).pack(anchor="w", pady=(0, 2))
entry_b = tk.Entry(root, font=("Arial", 10))
entry_b.pack(fill="x", pady=(0, 15))

btn_check = tk.Button(root, text="Проверить условие", font=("Arial", 10, "bold"), command=check_numbers)
btn_check.pack(fill="x", ipady=5, pady=(0, 15))

lbl_result = tk.Label(root, text="Результат: ", font=("Arial", 11, "bold"))
lbl_result.pack(pady=5)

root.mainloop()