class Person:
    def __init__(self, name, age):
        self._name = name
        self.age = age

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, x):
        self._name = x




#     def get_name(self):
#         return self.name
#
#     def set_name(self, a):
#         self.name = a
#
#     def get_age(self):
#         return self.age
#
#     def set_age(self, c):
#         self.age = c
#
#
a = Person('Mukhammed', "18")
print(a.name)
a.name = 'Akula'
print(a.name)
# print(a.get_name())
# a.set_name('Akula')
# print(a.get_name())
# print(a.get_age())
# print(a.set_age('17'))
# print(a.get_age())

