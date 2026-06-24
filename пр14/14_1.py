#В соответствии с номером варианта перейти по ссылке https://uicookies.com/wp-content/uploads/2019/05/Reg-Form-v5.jpg
# на прототип. Реализовать его в IDE PyCharm Community с применением пакета tk. Получить интерфейс максимально
#приближенный к оригиналу (см. таблицу 1).

import tkinter as tk
from tkinter import ttk

BG_PAGE = "#4E54F3"
BG_ENTRY = "#EAEAEA"
FONT_BOLD = ("Arial", 10, "bold")
FONT_SUB = ("Arial", 8)

root = tk.Tk()
root.title("Event Registration Form")
root.geometry("800x650")
root.configure(bg=BG_PAGE)

card = tk.Frame(root, bg="white")
card.place(relx=0.5, rely=0.5, anchor="center", width=550, height=550)

header = tk.Frame(card, bg="#1A1A1A")
header.place(x=0, y=0, relwidth=1, height=50)
tk.Label(header, text="EVENT REGISTRATION FORM", font=("Arial", 12, "bold"), fg="white", bg="#1A1A1A").pack(expand=True)

content = tk.Frame(card, bg="white")
content.place(x=40, y=80, width=470, height=450)
content.columnconfigure(0, minsize=110)
content.columnconfigure(1, weight=1)

def create_entry(parent):
    return tk.Entry(parent, font=("Arial", 11), bg=BG_ENTRY, fg="#333333", bd=0,
                    highlightthickness=8, highlightbackground=BG_ENTRY, highlightcolor=BG_ENTRY)


def create_double_fields(row_num, label_text, sub1, sub2):
    tk.Label(content, text=label_text, font=FONT_BOLD, bg="white", fg="#333333").grid(row=row_num, column=0,
                                                                                      sticky="nw", pady=10)

    frame = tk.Frame(content, bg="white")
    frame.grid(row=row_num, column=1, sticky="ew", pady=10)
    frame.columnconfigure((0, 1), weight=1)

    e1, e2 = create_entry(frame), create_entry(frame)
    e1.grid(row=0, column=0, sticky="ew", padx=(0, 10))
    e2.grid(row=0, column=1, sticky="ew")

    tk.Label(frame, text=sub1, font=FONT_SUB, fg="#888888", bg="white").grid(row=1, column=0, sticky="w", pady=(2, 0))
    tk.Label(frame, text=sub2, font=FONT_SUB, fg="#888888", bg="white").grid(row=1, column=1, sticky="w", pady=(2, 0))
    return e1, e2

ent_first, ent_last = create_double_fields(0, "Name", "First Name", "Last Name")
ent_area, ent_phone = create_double_fields(3, "Phone", "Area Code", "Phone Number")

entries = {}
for i, field in enumerate(["Company", "Email"], start=1):
    tk.Label(content, text=field, font=FONT_BOLD, bg="white", fg="#333333").grid(row=i, column=0, sticky="w", pady=10)
    entries[field] = create_entry(content)
    entries[field].grid(row=i, column=1, sticky="ew", pady=10)

tk.Label(content, text="Subject", font=FONT_BOLD, bg="white", fg="#333333").grid(row=4, column=0, sticky="w", pady=10)
ttk.Style().theme_use('clam')
ttk.Style().configure("TCombobox", fieldbackground=BG_ENTRY, background=BG_ENTRY, borderwidth=0, arrowsize=12)

combo_subject = ttk.Combobox(content, values=["Option 1", "Option 2", "Option 3"], font=("Arial", 10), state="readonly",
                             style="TCombobox")
combo_subject.set("Choose option")
combo_subject.grid(row=4, column=1, sticky="ew", pady=10, ipady=4)

tk.Label(content, text="Are you an existing customer?", font=FONT_BOLD, bg="white", fg="#333333").grid(row=5, column=0, columnspan=2, sticky="w", pady=(15, 5))
radio_frame = tk.Frame(content, bg="white")
radio_frame.grid(row=6, column=0, columnspan=2, sticky="w")

radio_var = tk.StringVar(value="None")
tk.Radiobutton(radio_frame, text="Yes", variable=radio_var, value="Yes", bg="white", fg="#333333",
               font=("Arial", 10)).grid(row=0, column=0, padx=(0, 20))
tk.Radiobutton(radio_frame, text="No", variable=radio_var, value="No", bg="white", fg="#333333",
               font=("Arial", 10)).grid(row=0, column=1)

tk.Button(
    content, text="REGISTER", bg="#FF4A5A", fg="white", font=FONT_BOLD, bd=0,
    activebackground="#E0404F", activeforeground="white", cursor="hand2", width=15, height=2
).grid(row=7, column=0, sticky="w", pady=(20, 0))

root.mainloop()