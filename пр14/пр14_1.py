from tkinter import *
from tkinter import ttk

root = Tk()
root.title("Registration")
root.geometry("1920x1080")
root.configure(bg="#6a5acd")

# --- КАРТОЧКА ---
frame = Frame(root, bg="white", padx=200, pady=280)
frame.place(relx=0.5, rely=0.5, anchor="center")

# --- СЕТКА (ВАЖНО) ---
frame.columnconfigure(0, weight=1)
frame.columnconfigure(1, weight=2)

# --- ЗАГОЛОВОК ---
Label(frame,text="EVENT REGISTRATION FORM",font=("Arial", 18, "bold"),bg="black",fg="white",).grid(row=0, column=0, columnspan=2, pady=(0, 200))

# --- ПОЛЯ ---
Label(frame, text="Name", bg="white").grid(row=1, column=0, sticky="w", pady=10)
Entry(frame).grid(row=1, column=1, sticky="ew", pady=10)

Label(frame, text="Company", bg="white").grid(row=2, column=0, sticky="w", pady=10)
Entry(frame).grid(row=2, column=1, sticky="ew", pady=10)

Label(frame, text="Email", bg="white").grid(row=3, column=0, sticky="w", pady=10)
Entry(frame).grid(row=3, column=1, sticky="ew", pady=10)

Label(frame, text="Phone", bg="white").grid(row=4, column=0, sticky="w", pady=10)
Entry(frame).grid(row=4, column=1, sticky="ew", pady=10)

# --- ВЫПАДАЮЩИЙ СПИСОК ---
Label(frame, text="Subject", bg="white").grid(row=5, column=0, sticky="w", pady=10)

combo = ttk.Combobox(frame, values=["Option 1", "Option 2", "Option 3"])
combo.grid(row=5, column=1, sticky="ew", pady=10)

# --- RADIO ---
Label(frame, text="Are you an existing customer?", bg="white").grid(
    row=6, column=0, columnspan=2, pady=(20, 10)
)

var = StringVar(value="Yes")
Radiobutton(frame, text="Yes", variable=var, value="Yes", bg="white").grid(row=7, column=0, sticky="w")
Radiobutton(frame, text="No", variable=var, value="No", bg="white").grid(row=7, column=1, sticky="w")

# --- РАСТЯГИВАЕМ НИЗ (чтобы кнопка ушла вниз) ---
frame.rowconfigure(8, weight=1)

# --- КНОПКА (ПРАВЫЙ НИЖНИЙ УГОЛ) ---
reg_button = Button(
    frame,
    text="REGISTER",
    bg="red",
    fg="white",
    width=20,
    height=2
)

reg_button.grid(row=9, column=1, sticky="e", pady=(30, 0))

root.mainloop()