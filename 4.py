class Car():
    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        print(f'{self.name} начинает движение')

    def stop(self):
        print(f'{self.name} останавливается')

    def turn(self, direction):
        print(f'{self.name} совершает поворот {direction}')

    def show_speed(self):
        print(f'Текущая скорость автомобиля равна {self.speed}')

class TownCar(Car):
    def show_speed(self):
        if self.speed > 60:
            print(f'Скорость превышена на {self.speed - 60} и составляет {self.speed}!')
        else:
            print(f'Текущая скорость автомобиля равна {self.speed}')


class SportCar(Car):
    pass

class WorkCar(Car):
    def show_speed(self):
        if self.speed > 40:
            print(f'Скорость превышена на {self.speed - 40} и составляет {self.speed}!')
        else:
            print(f'Текущая скорость автомобиля равна {self.speed}')

class PoliceCar(Car):
    pass

lada = TownCar(183, 'Blue', 'Седан', False)
lada.show_speed()

ferrari = SportCar(320, 'Red', 'Ferrari Roma', False)
ferrari.show_speed()
print(ferrari.name)

jac = WorkCar(13.5, 'Yellow', 'JAC', False)
jac.show_speed()

dps = PoliceCar(150, 'White', 'Патрульный автомобиль', True)
print(dps.is_police)