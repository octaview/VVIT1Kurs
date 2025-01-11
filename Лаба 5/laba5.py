# Задание 1
class Book:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year
    def get_info(self):
        print('Название книги: ', self.title, ', Автор: ', self.author, ', Год издания: ', self.year, sep='')
class Book1(Book):
    def __init__(self, title, author, year):
        super().__init__(title, author, year)

book1 = Book1('я русский', 'шаманчик связывай', '2024')
book1.get_info()
book = Book("Гойда", "Охлобыстин", 2024)
book.get_info()


# # Задание 2
# class Circle:
#     def __init__(self, radius):
#         self.radius = radius
#     def get_radius(self):
#         return self.radius
#     def set_radius(self, new_radius):
#         self.radius = new_radius
#
# circle = Circle(5)
# print('старт радиус:', circle.get_radius())
# circle.set_radius(10)
# print('новый радиус:', circle.get_radius())
