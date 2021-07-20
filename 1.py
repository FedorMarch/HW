from sys import argv

_, hours, wage_rate, prize = argv

print(f'При выработке {hours} часов, ставке {wage_rate} рублей и премии {prize} рублей расчетная заработная плата составляет {int(hours) * int(wage_rate) + int(prize)} рублей')