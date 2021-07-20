from time import sleep


class TrafficLight():
    def __init__(self, durability):
        self.durability = int(durability)  # сколько итераций может проработать светофор

    __color = (('Красный', 7), ('Желтый', 2), ('Зеленый', 9))

    def running(self):
        for _ in range(self.durability):
            for current_color in self.__color:
                print(f'Цвет светофора - {current_color[0]}')
                sleep(current_color[1])
        print(f'Светофор отработал {self.durability} итераций и сгорел')


svetofor = TrafficLight(2)
svetofor.running()
