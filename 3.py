class Worker:
    def __init__(self, name, surname, position, **income):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = income

    def info(self):
        print(self.name, self.surname, self.position, self._income)

class Position(Worker):
    def get_full_name(self):
        print(f'Полное имя сотрудника - {self.name} {self.surname}')

    def get_total_income(self):
        print(f'Годовой доход работника составляет {list(self._income.values())[0] * 12 + list(self._income.values())[1]}')

vasya = Position('Vasiliy', 'Ivanov', 'Povar', wage = 100, income = 10)
vasya.get_full_name()
vasya.get_total_income()