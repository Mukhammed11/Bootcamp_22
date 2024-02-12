# class Human:
#     _age = 0    # private
#     __age = 0   # protected
#     age = 0     # public
#
#
# num = Human()
# num.__age = 10
# num._age = 20
# num.age = 30
#
# print(num.__age, num._age, num.age)

# '''private'''
#
#
# class Human:
#     def __init__(self):
#         self._private = 0
#
#     def Adam(self, private):
#         self._private = private
#
#     def Akula(self):
#         return self._private
#
#
# human = Human()
#
# human.Adam(25)
# print("Возрост :", human.Akula())
#
#
#
# '''protected'''
#
#
# class Human:
#     def __init__(self):
#         self.__protected = 0
#
#     def Adam(self, protected):
#         self.__protected = protected
#
#     def Akula(self):
#         return self.__protected
#
# human = Human()
#
# human.Adam(25)
# print("Возрост :", human.Akula())
#
#
# '''public'''
#
#
# class Human:
#     def __init__(self):
#         self.public = 0
#
#     def Adam(self, public):
#         self.public = public
#
#     def Akula(self):
#         return self.public
#
#
# human = Human()
#
# human.Adam(25)
# print("Возрост :", human.Akula())


class MBank:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.__balance = 0
        self.__vip = False
        self.s_l = 0

    def verifications(self):
        self.__vip = True

    def get__cash(self):
        return f'balance: {self.__balance}'

    def set__cash(self, x):
        self.__balance += x

    def info(self):
        return f'name: {self.name}, surname: {self.surname}'

    def komissia(self, a):
        if a <= 50000:
            return a * 0.03
        else:
            return 100 + a * 0.012

    def dordoi(self, x):
        if self.__balance >= x:
            if x <= 50000 and self.s_l + x <= 50000:
                self.__balance -= x
                return f'Udacha ostatok {self.get__cash() } som! '
            else:
                if self.__vip:
                    self.__balance -= x
                    return f'Balance jetti {self.get__cash()} som'
                else:
                    return 'sende VIP jok!'
        else:
            return f'У тебя не хватит деньги, на балансе есть только {self.__balance} сом! '


a = MBank('Mukhammed', 'Nematzhonov')
a.set__cash(100000)
print(a.info())
# a.verifications()
# print(a.dordoi(58000))
print(a.get__cash())