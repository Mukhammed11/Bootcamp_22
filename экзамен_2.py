'''     •	Задача о банковском счете: Создайте класс BankAccount,
 который имеет атрибуты balance (баланс) и методы для deposit (внесения средств) и withdraw
 (снятия средств). Ограничьте сумму снятия, чтобы она не могла превышать текущий баланс.
•	Создайте класс Book с атрибутами название, автор и год издания.
Создайте методы для вывода информации о книге.
Затем создайте список книг и реализуйте метод для поиска книг по автору или году издания.
•	Создайте классы для моделирования товаров в магазине и корзины для покупок.
Покупатель должен иметь возможность добавлять товары в корзину и рассчитывать общую стоимость.
•	Создайте классы Bank и Customer, чтобы моделировать банковский аккаунт.
Каждый клиент банка может иметь несколько счетов,
и банк должен предоставлять методы для открытия новых счетов, внесения и снятия средств. '''




class BankAccount:
    def __init__(self):
        self.klient = {}

    def account(self, client, number, balance):
        if client in self.klient:
            self.klient[client][number] = balance
        else:
            self.klient[client] = {number: balance}

    def deposit(self, klients, nums, kolichestvo):
        if klients in self.klient and nums in self.klient[klients]:
            self.klient[klients][nums] += kolichestvo
        else:
            print("Неверные данные для внесения средств")

    def withdraw(self, clients, nam, kolichestvo):
        if clients in self.klient and nam in self.klient[clients]:
            if kolichestvo <= self.klient[clients][nam]:
                self.klient[clients][nam] -= kolichestvo
                return f'остаток на счету: {self.klient[clients][nam]}'
            else:
                return f'Недостаточно средств на счету'
        else:
            return f'Неверные данные для снятия средств'


bank = BankAccount()
bank.account('Мухаммед', '50 000', 1000)
bank.deposit('Мухаммед', '50 000', 500)
result = bank.withdraw('Мухаммед', '50 000', 500)
print(result)

