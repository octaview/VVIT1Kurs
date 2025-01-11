class UserAccount:
    def __init__(self, username, email, password):
        self.username = username
        self.email = email
        self.__password = password

    def set_password(self, new_password):
        self.__password = new_password

    def check_password(self, password):
        return self.__password == password

user = UserAccount("kirill", "kirill@gmail.com", "123123")
print(user.check_password("123123"))

user.set_password("qwe123123")
print(user.check_password("qwe123123"))
print(user.check_password("123123"))

# class Vehicle:
#     def __init__(self, make, model):
#         self.make = make
#         self.model = model
#
#     def get_info(self):
#         print('Марка: '+self.make+'.'+' Модель: '+self.model+'.')
#
#
# class Car(Vehicle):
#     def __init__(self, make, model, fuel_type):
#         super().__init__(make, model)
#         self.fuel_type = fuel_type
#
#     def get_info(self):
#         print('Марка: '+self.make+'.'+' Модель: '+self.model+'.'+'Тип топлива: '+self.fuel_type+'.')
#
#
# vehicle = Vehicle('Scoda', 'Octavia')
# vehicle.get_info()
#
# car = Car('VAZ', '2109', 'АИ-100')
# car.get_info()
