class Road():
    def __init__(self, length, width):
        self._length = length
        self._width = width

    def mass_calculation(self, mass_per_cm, thickness):
        print(f'Масса асфальта равняется {self._length * self._width * mass_per_cm * thickness/1000} тонн')


kad = Road(142200, 6)
kad.mass_calculation(13, 10)
