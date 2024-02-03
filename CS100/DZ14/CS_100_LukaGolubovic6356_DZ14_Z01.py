class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def perimeter(self):
        return 2 * (self.length + self.width)

    def area(self):
        return self.length * self.width

    def display(self):
        print(f"Dužina: {self.length}")
        print(f"Širina: {self.width}")
        print(f"Obim: {self.perimeter()}")
        print(f"Površina: {self.area()}")
        print()


class Parallelepipede(Rectangle):
    def __init__(self, length, width, height):
        super().__init__(length, width)
        self.height = height

    def volume(self):
        return self.length * self.width * self.height

    def display(self):
        super().display()
        print(f"Visina: {self.height}")
        print(f"Zapremina: {self.volume()}")


pravougaonik = Rectangle(5, 8)
pravougaonik.display()

paralelepiped = Parallelepipede(3, 4, 6)
paralelepiped.display()

