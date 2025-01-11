# #задание 1
# def greet(a):
#     print('Приветствую, ', a)
# greet('Колян')
#
# def square(a):
#     return(a**2)
# print(square(4))
#
# def max_of_two(a, b):
#     return(max(a, b))
# print(max_of_two(1, 2))
#
# #задание 2
# def describe_person(name, age=30):
#     print('Имя:', name)
#     print('Возраст:', age)
# describe_person('Толян')
# describe_person('Вовчик', '25')
#
# #задание 3
# def is_prime(a):
#     for i in range(2, int(a**0.5)+1):
#         if a%i==0:
#             return False
#     return True
# print(is_prime(4))
# print(is_prime(3))