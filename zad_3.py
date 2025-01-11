class Property:
    def __init__(self, area: str, rooms: int, price: str, address: str):
        self.area = area
        self.rooms = rooms
        self.price = price
        self.address = address

    def __str__(self):
        return f"{self.area} {self.rooms} {self.price} {self.address}"


class House(Property):
    def __init__(self, area: str, rooms: int, price: str, address: str, plot: int):
        super().__init__(area, rooms, price, address)
        self.plot = plot

    def __str__(self):
        return super().__str__() + f' {self.plot}'


class Flat(Property):
    def __init__(self, area: str, rooms: int, price: str, address: str, floor: int):
        super().__init__(area, rooms, price, address)
        self.floor = floor

    def __str__(self):
        return super().__str__() + f' {self.floor}'


house = House('150', 5, '100000', 'Katowice', 840)
print(house)

flat = Flat('79', 4, '100000', 'Roma', 79)
print(flat)
