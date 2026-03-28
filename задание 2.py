class Черепашка:
    def __init__(self, x=0, y=0, s=1):
        self.x = x
        self.y = y
        self.s = s

    def go_up(self):
        self.y += self.s

    def go_down(self):
        self.y -= self.s

    def go_left(self):
        self.x -= self.s

    def go_right(self):
        self.x += self.s

    def evolve(self):
        self.s += 1

    def degrade(self):
        if self.s - 1 <= 0:
            raise ValueError("s не может стать меньше или равно 0")
        self.s -= 1

    def count_moves(self, x2, y2):
        distance_x = abs(x2 - self.x)
        distance_y = abs(y2 - self.y)

        steps_x = (distance_x + self.s - 1) // self.s
        steps_y = (distance_y + self.s - 1) // self.s

        return steps_x + steps_y