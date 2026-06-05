class book:
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages
    def read(self):
        return print("Название:", self.title, "Написал:", self.author, self.pages, "страниц")
    def write(self):
        self.title = str(input("Введите название книги: "))
        self.author = str(input("Введите автора: "))
        self.pages = int(input("Введите количество страниц: "))
        return print("Название:", self.title, "Написал:", self.author, self.pages, "страниц")

crime_and_punishment = book("Преступление и наказание", "Ф.М.Достоевский", 672)
crime_and_punishment.write()