# 1. Созадайте класс Image
#
# 2. У каждого экземпляра класса должно быть три собственных атрибута
# - resolution
# - title
# - extension
#
# 3. В классе должен быть метод resize, с помощью которого можно поменять
# разрешение изображения.
#
# 4*. В классе должен быть метод title_upper, с помощью которого можно
# имя файла записать в верхнем регистре.
#
# 5. Создайте несколько экземпляров класса Image и вызовите для каждого
# метод resize

class img:
    def __init__(self, resolution_width, resolution_height, title, extension):
        self.resolution_width = resolution_width
        self.resolution_height = resolution_height
        self.title = title
        self.extension = extension

    def resize(self, percent):
        self.resolution_width = int(self.resolution_width * percent) / 100
        self.resolution_height = int(self.resolution_height * percent) / 100
        return self.resolution_width, self.resolution_height

    def title_upper(self):
        return self.title.upper()

Image_sun = img(1920, 1080, 'sun', 'jpg')
Image_human = img(1920, 1080, 'hunan', 'png')
Image_animal = img(1920, 1080, 'animal', 'jpeg')

print(Image_sun.title_upper(), "- разрешение", Image_sun.resize(150))
print(Image_human.title_upper(), "- разрешение", Image_human.resize(200))
print(Image_animal.title_upper(), "- разрешение", Image_animal.resize(40))