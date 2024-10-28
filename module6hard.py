
class Figure:
    sides_count = 0

    def __init__(self, __sides, __color, filled = False):
            self.__sides = __sides
            self.__color = __color
            self.filled = filled

    def get_color(self):
        return self.__color

    def __is_valid_color(self, new_color):
        valid = 0
        for i in new_color:
            if i > 0 and i < 255:
                valid += 1
            else:
                continue
        if valid == 3:
            print(f'Верный формат цвета')
            return True
        else:
            print(f'Недопустимый формат цвета')
            return False

    def set_color(self, new_color):
        valid = self._Figure__is_valid_color((new_color))
        if valid:
            self.__color = new_color
            print(f'Цвет изменён на новый')
        else:
            print(f'Цвет не может быть изменён на новый, неверный формат')

    def __is_valid_sides(self, new_sides):
        a = self.sides_count
        valid = 0
        if a == len(new_sides):
            for i in new_sides:
                if i > 0 and type(i) == int:
                    valid += 1
                else:
                    continue
            if valid == a:
                self.__sides = new_sides
                return True
            else:
                return False
        else:
            return False

    def get_sides(self):
        return self.__sides

    def __len__(self):
        P = 0
        for i in self.__sides:
            P += i
        return P

    def set_sides(self, new_sides):
        valid = self._Figure__is_valid_sides(new_sides)
        if valid:
            print(f"Стороны изменены")
            self.__sides = new_sides
            return self.__sides
        else:
            print(f"Стороны не могут быть изменены")

class Circle(Figure):
    sides_count = 1
    __radius = 0

    def __init__(self, __sides, __color, filled = False):
        super().__init__(__sides, __color, filled)
        self._Circle__radius = self._Figure__sides / (2 * 3.14)

    def __len__(self):
        return self._Figure__sides

    def __is_valid_sides(self, new_sides):
        if new_sides > 0 and type(new_sides) == int:
            return True
        else:
            return False

    def set_sides(self, new_sides):
        valid = self._Circle__is_valid_sides(new_sides)
        if valid:
            print(f"Стороны изменены")
            self._Figure__sides = new_sides
            return self._Figure__sides
        else:
            print(f"Стороны не могут быть изменены")

    def get_square(self):
        return 3.14 * self._Circle__radius**2

class Triangle(Figure):
    sides_count = 3

    def __init__(self, __sides, __color, filled = False):
        super().__init__(__sides, __color, filled)

    def get_square(self):
        p = 0
        S = 1
        for i in self._Figure__sides:
            p += i
        p /= 2

        for i in self._Figure__sides:
            S *= (p - i)
        S *= p
        return (S**0.5)

class Cube(Figure):
    sides_count = 12

    def __init__(self, __sides, __color, filled = False):
        super().__init__(__sides, __color, filled)

        self._Figure__sides = self.sides_count * [self._Figure__sides]

    def get_volume(self):
        V = (self._Figure__sides[1])**3
        return V

f1 = Figure([2, 2, 2, 2], [152, 65, 65])
print(f1.get_color())
f1._Figure__is_valid_color((255, 65, 257))
f1.set_color((158, 75, 65))
print(f1.get_sides())
print(len(f1))

c1 = Circle(12, (12, 56, 234))
print(c1.get_sides())
print(c1._Circle__radius)
c2 = Circle(14, (12, 51, 234))
print(c2._Circle__radius)
print(c1.get_square())

t1 = Triangle([12, 6, 7], (12, 51, 234))
print(t1.get_square())

C1 = Cube(3, (12, 56, 234))
print(C1._Figure__sides)
print(C1.get_volume())

print(t1.get_sides())
print(t1.get_color())
print(len(t1))

c1.set_color((12, 56, 234))
c1._Figure__is_valid_color((12, 56, 234))

Figure.sides_count = 4
f1.set_sides([12, 2, 5, 1])

print(t1._Figure__is_valid_sides([12, 56, 234]))
t1.set_sides([12, 56, 12])
print(f'Стороны куба изменены: {C1.set_sides([3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3])}')

print(c1._Circle__is_valid_sides(13))
print(f'Сторона круга изменена: {c1.set_sides(12)}')

