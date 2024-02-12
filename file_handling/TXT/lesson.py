'''           Eсли  файл сушествует, данные в нем будут перезаписаны.
    'x' -> открывает файл на запись. Если файл уже существует, операция будет ошибкой.
    'a' -> открывает файл и дозаписывает в него данные, не стирая предыдущие.
           Создает новый файл , если он не существует.
    't' -> открывает файл как текстовый. (значения по умолчанию)
    'b' -> открывет файл в бинарном / двоичном режиме.
    '+' -> Позволяет работать с файлом как для записи так и для чтения
'''

"r -> read"
# hi = open('lesson.txt', 'r', encoding='utf-8')
# print(hi.read())
# print(hi.read(3))
# print(hi.read(4))
# hi.seek(0)
# print(hi.read(8))
# hi.close()

"w -> write"
# with open('lesson.txt', 'w') as file:
#     file.write('hello world')

"a -> append"
# with open('filename.txt', 'a') as file:
#     file.write('\nNew data append')

# with open('lesson.txt', 'rt') as file:
#     content = file.read()
#     print(content)

# try:
#     with open('example.txt', 'x') as file:
#         file.write('new file created')
# except FileExistsError as F:
#     print('file allready exist', F)


# with open('/Users/askatkulmanov/Desktop/BOOTCAMP/Bootcamp_22/comprehension/lesson.txt', 'r') as file:
#     print(file.read())


with open('python.txt', '+a', encoding='utf-8') as file:
    file.write('\nLolkiula')
print(file)