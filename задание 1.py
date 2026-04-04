class Касса:
    def __init__(self, initial_amount=0):
        self.money = initial_amount

    def top_up(self, x):
        if x < 0:
            raise ValueError("Сумма пополнения не может быть отрицательной")
        self.money += x

    def count_1000(self):
        thousands = self.money // 1000
        print(f"Целых тысяч в кассе: {thousands}")
        return thousands

    def take_away(self, x):
        if x < 0:
            raise ValueError("Сумма изъятия не может быть отрицательной")
        if x > self.money:
            raise ValueError(f"Недостаточно денег в кассе. Доступно: {self.money}, запрашивается: {x}")
        self.money -= x
        print(f"Из кассы изъято {x}. Остаток: {self.money}")

cassa = Касса()
cassa.top_up(int(input("Введите сумму пополнения: ")))
cassa.count_1000()
cassa.take_away(int(input("Введите сумму изъятия: ")))
cassa.count_1000()
