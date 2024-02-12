"""
ООП- обьектно ориентированное программирование:
                                                Инкапсуляция;
                                                Полиморфизм;
                                                Наследование;

                Наследование
                     /\
        родительский>||<дочерний
"""
"""
(def) snake_case - hello_world
(class) CamelCase - HelloWorld
"""

# class Adam:
#     """адамдын тузулушу"""
#     def __init__(self, name: str, age: int, gender: str):
#         self.name = name
#         self.age = age
#         self.gen = gender
#
#     def info(self):
#         """маалымат"""
#         return f'{self.name}, {self.age}, {self.gen}'
#
#
# class Chynar(Adam):
#     def __init__(self):
#         super().__init__('CHynar', 61, 'woman')
#
#
# class Kyzy(Adam):
#     def __init__(self):
#         super().__init__('Alina', 20, 'woman')
#
#
# adam = Adam('Adam', 0, 'none')
# ch = Chynar()
# k = Kyzy()
# print(adam.info())
# print(k.info())
# print(ch.name)


# class House:
#     """Уйдун макети"""
#     def __init__(self, prospect, number):
#         """Уйдун тузулушу"""
#         self.prospekt = prospect
#         self.num = number
#         self.age = 0
#
#
#     def stoyka(self):
#         """Уйдун курулушу"""
#         print(f'{self.prospekt} кочосундогу {self.num}- уй бутту')
#
#     def age_of_house(self, years):
#         """Курулган жылы"""
#         self.age += years
#         print(f'{years} жыл болду курулганына!')
#
#
# class Manas(House):
#     """Жаны курулуш"""
#     def __init__(self, street, num1, prospekt):
#         super().__init__(prospekt, num1)
#         self.street = street
#
# manas = Manas('пр.Манас', 64.1, 'пр.Чуй')
# manas.stoyka()
# print(manas.street, manas.prospekt)
# print(manas.num)























