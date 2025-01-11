# #задание 1
# def chtenie_faila(filename = 'example.txt', tip_chteniya='whole'):
#     f=open(filename)
#     if tip_chteniya=='whole':
#         print(f.read())
#     if tip_chteniya=='line_by_line':
#         for i in f:
#             print(str(i))
#
# chtenie_faila('example.txt', 'line_by_line')

# #задание 2
# def write_to_new():
#     text = input('Введите текст:')
#     f = open('user_input.txt', 'w')
#     f.write(text)
# def add_to_old():
#     text = input('Введите текст:')
#     f = open('user_input.txt', 'a')
#     f.write('\n' + text)

#задание 3
def chtenie_faila(filename = 'example.txt', tip_chteniya='whole'):
    try:
        f = open(filename)
        if tip_chteniya=='whole':
            print(f.read())
        if tip_chteniya=='line_by_line':
            for i in f:
                print(str(i))
    except FileNotFoundError:
        print('Файл не найден.')

chtenie_faila('example.txt', 'line_by_line')

