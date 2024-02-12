# import csv

# name1 = 'Chynar'
# name2 = 'Eliza'
#
# with open('exemple.csv', 'w') as file:
#     writer = csv.writer(file)
#     writer.writerow(
#         [name1, name2]
#     )


# information = [
#     ['Name', 'Age', 'Salary', 'Position'],
#     ['Bektur', '66', '30 000', 'Pensia'],
#     ['Oliver', '41', '70 000', 'Buhgalter'],
#     ['Piter', '24', '110 000', 'Stamatolog'],
#     ['Ivan', '19', '-10 000', 'Treyder'],
#     ['Quin', '22', '75 000', 'Buhgalter'],
#     ['Sasuke', '28', '130 000', 'Stamatolog'],
#     ['Akula', '33', '80 000', 'Buhgalter'],
#     ['Adidas', '36', '4 000 000', 'Aktyor'],
#     ['Palto', '28', '5 000 000', 'Aktyor'],
#     ['Marat', '24', '6 000 000', 'Aktyor'],
#     ['Veronika', '85', '40 000', 'Pensia'],
#
#
#
#
# ]
# with open('exemple.csv', 'w', newline='') as file:
#     csv_w = csv.writer(file)
#     csv_w.writerows(information)
#
# with open('exemple.csv', 'r', encoding='utf-8') as file:
#     csv_r = csv.reader(file)
#     num = next(csv_r)
#     for i in csv_r:
#         Name, Age, Salary, Position = i
#         if int(Age) < 60:
#             print(f'Мое имя {Name}, мой возраст {Age}, Моя зарплата {Salary} мое должность {Position}')
        # elif int(Age) > 60:
        #     print(f'Мое имя {Name}, мой возрост {Age}, Мне получить {Position}, {Salary}'





# a = 20000
# b = 60
# def i(*args):
#     Name, Age, Salary, Position = b
#     if int(Age) > 60:
#         print('Вы на пенсию')
#     elif int(Age) < 60:
#         print(f'Мое имя {Name}, мой возраст {Age}, Моя зарплата {Salary} мое должность {Position}')



'''
тение и вывод данных:
 • Прочитайте содержимое CSV-файла и выведите его на экран.
 • Выведите только определенные столбцы (например, только имена и возраст).
  Фильтрация данных:
 • Найдите все строки с определенным значением в конкретном столбце (например, все строки, где возраст больше 25).
  Добавление данных:
 • Добавьте новую строку данных в CSV-файл.
  Обновление данных:
 • Измените значение в определенной ячейке (например, измените номер телефона для определенного человека).
  Удаление данных:
 • Удалите строки, соответствующие определенному условию (например, удалите все строки, где город - "Москва").
  Статистика:
 • Посчитайте средний возраст всех людей в файле.
 • Посчитайте количество людей в каждом городе.
  Сортировка:
 • Отсортируйте данные по возрасту в порядке убывания.
 • Отсортируйте данные по имени в алфавитном порядке.
  Создание нового файла:
 • Создайте новый CSV-файл и скопируйте в него только определенные столбцы из исходного файла.
  Работа с датами:
 • Если в данных есть столбец с датами, выведите людей, родившихся после определенной даты.
  Обработка ошибок:
 • Обработайте возможные ошибки при чтении и записи CSV-файлов.
Эти задачи позволят вам практиковаться в различных операциях с данными в формате CSV и развивать навыки работы с файлами и обработки данных.
'''
# import csv
#
#
# def i(file_n, file_i, file_v):
#     data = []
#     with open(file_n, 'r', encoding='utf-8') as file:
#         csv_r = csv.reader(file)
#         for n in csv_r:
#             if n[file_i] != file_v:
#                 data.append(n)
#
#     with open(file_n, 'w', newline='', encoding='utf-8') as file:
#         csv_w = csv.writer(file)
#         csv_w.writerows(data)