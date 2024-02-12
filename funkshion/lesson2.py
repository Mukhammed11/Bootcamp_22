"""

*args -> tuple
**kwargs -> dict

"""


# def func1(z, y, g):
#     return z + y + g
#
#
# print(func1(10, 20, 30))

"--------------------------------------------------"


# def func(x, y=20, z=30):
#     return x + y + z
#
#
# print(func(30, y=20, z=80))
"--------------------------------------------------"

"-------------*args--------------------------------"
# def my_args(*args):
#     print(args)
#
#
# my_args(1, 2, 3, 4, 5, 6,  7, 8,)

"-----------**kwargs-------------------------------"
# def my_kwargs(**kwargs):
#     name = []
#     for k, v in kwargs.items():
#         name.append(v)
#         print(name)
#
#
#
# my_kwargs(alina="Kbazova")

"------------*args, **kwargs-----------------------"
# def my_func(*args, **kwargs):
#     for i in args:
#         for k, v in kwargs.items():
#             print(f'Hi {k}{v} good luck')
#         print(i, end=' ')
#
#
# my_func(1, Altyn='Beyshekeev')

def b(*args, **kwargs):
    return args, kwargs


nam = b(5000)
nemo = b({})

num = input('Как вас зовут: ')
nums = input('Сколько у вас зарплата: ')

# print(f'Привет ', (num))
# print(f'Зарплата 5000', (nums))

print(('Привет'), num)
print(('Зарплата'), nam)
