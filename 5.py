class Stationery():
    def __init__(self, title):
        self.title = title

    def draw(self):
        print('Запуск отрисовки.')

class Pen(Stationery):
    def draw(self):
        print(f'{self.title} проводит тонкую синию линию')

class Pencil(Stationery):
    def draw(self):
        print(f'{self.title} провел тонкую серую линию')

class Handle(Stationery):
    def __init__(self, title, color):
        Stationery.__init__(self, title)
        self.color = color

    def draw(self):
        print(f'{self.title} провел толстую линию цвета "{self.color}"')

pen = Pen('Ручка')
pen.draw()

pencil = Pencil('Простой карандаш')
pencil.draw()

handle = Handle('Маркер', 'красный')
handle.draw()