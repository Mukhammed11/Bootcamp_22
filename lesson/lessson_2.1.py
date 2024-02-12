# def a(*args, **kwargs):




# ('Osh' == 8, 'Jalal-Abad' == 4, 'Talas' == 7, 'Naryn' == 10, 'Yssyk-Kol' == 8, 'Batken' == -1, 'Chuy' == -3)



# print('Средняя Погода Кыргызстана:', max(a))
# def calculate(temperatures):
#     return sum(temperatures) / len(temperatures)
#
# obl = ['Чуй', 'Талас', 'Нарын', 'Баткен', 'Джалал-Абад', 'Ысык-Кол', 'Ош']
# temperatures = []
#
# for i in obl:
#     while True:
#         try:
#             temperature = float(input(f"Введите температуру {i}: "))
#             temperatures.append(temperature)
#             break
#         except ValueError:
#             print('число.')
#
# temp = calculate(temperatures)
#
# print(f" температура: {temp}")def addition(num_1, num_2):
#     return num_1 + num_2
#
#
# def multiplication(num_1, num_2):
#     return num_1 * num_2

while True:
    s = input("calculator (+, -, *, **, /, %): ")
    if s == '0':
        break
    if s in ('+', '-', '*', '**', '/', '%'):
        a = float(input("a = "))
        b = float(input("b = "))
        c = 2
        if s == '+':
            print("%.f" % (a + b))
        elif s == '%':
            print("%f" % (a % b))
        elif s == '-':
            print("%.f" % (a - b))
        elif s == '**':
            print("%.f" % (a ** c))
        elif s == '*':
            print("%.f" % (a * b))
        elif s == '/':
            if b != 0:
                print("%.f" % (a / b))
            else:
                print("Деление на ноль!")
                print("Исползуйте другие сифры!")
    else:
        print("Неверный знак операции!")
        print("Повторите еще раз!")