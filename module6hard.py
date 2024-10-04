from math import pi


class Figure:
    sides_count = 0

    def __init__(self, color, *sides):
        self.__color = list(color)
        if len(sides) == self.sides_count:
            self.__sides = list(sides)
        else:
            self.__sides = [1] * self.sides_count
        self.filed = False

    def get_color(self):
        return self.__color

    def __is_valid_color(self, r, g, b):
        if (0 <= r <= 255 and 0 <= g <= 255 and 0 <= b <= 255
                and isinstance(r, int)
                and isinstance(g, int)
                and isinstance(b, int)):
            return r, g, b
        else:
            return self.__color

    def set_color(self, r, g, b):
        self.__color = list(self.__is_valid_color(r, g, b))
        return self.__color

    def __is_valid_sides(self, *sides):
        for side in sides:
            if not isinstance(side, int) or side <= 0:
                return False
            return len(sides) == self.sides_count

    def get_sides(self):
        return self.__sides

    def __len__(self):
        return sum(self.__sides)

    def set_sides(self, *new_sides):
        if self.__is_valid_sides(*new_sides):
            self.__sides = list(new_sides)
            return self.__sides


class Circle(Figure):
    sides_count = 1

    def __init__(self, color, *sides):
        super().__init__(color, *sides)
        self.__radius = sides[0] / (2 * 3.14)

    def get_square(self):
        return pi * self.__radius ** 2


class Triangle(Figure):
    sides_count = 3

    def __init__(self, color, *sides):
        super().__init__(color, *sides)

    def get_square(self):
        p = (self._Figure__sides[0] + self._Figure__sides[1] + self._Figure__sides[2]) / 2
        return ((p * (p - self._Figure__sides[0]) * (p - self._Figure__sides[1]) *
                 (p - self._Figure__sides[2]))) ** 0.5


class Cube(Figure):
    sides_count = 12

    def __init__(self, color, *sides):
        super().__init__(color, *sides)
        self._Figure__sides = list(sides) * self.sides_count

    def get_volume(self):
        return self._Figure__sides[0] ** 3


circle1 = Circle((200, 200, 100), 10)  # (Цвет, стороны)
cube1 = Cube((222, 35, 130), 6)
triangle1 = Triangle((66, 33, 22), 3, 4, 5)

# print(circle1.__dict__)
# print(cube1.__dict__)
# print(triangle1.__dict__)

# Проверка на изменение цветов:
circle1.set_color(55, 66, 77)  # Изменится
# print(f'Было [200, 200, 100], -> [55, 66, 77], стало {circle1.get_color()}')
print(circle1.get_color())
cube1.set_color(300, 70, 15)  # Не изменится
# print(f'Было [222, 35, 130], -> [300, 70, 15], стало {cube1.get_color()}')
print(cube1.get_color())

# Проверка на изменение сторон:
cube1.set_sides(5, 3, 12, 4, 5)  # Не изменится
print(cube1.get_sides())
circle1.set_sides(15)  # Изменится
print(circle1.get_sides())

# Проверка периметра (круга), это и есть длина:
print(len(circle1))
# print(len(cube1))
# print(len(triangle1))

# Проверка площади (круга):
# print(circle1.get_square())
# Проверка объёма (куба):
print(cube1.get_volume())
# Проверка площади (треугольника):
# print(triangle1.get_square())
