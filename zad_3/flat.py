from property import Property


class Flat(Property):
    def __init__(self, area: str, rooms: int, price: str, address: str, floor: int):
        super().__init__(area, rooms, price, address)
        self.floor = floor

    def __str__(self):
        return super().__str__() + f" {self.floor}"
