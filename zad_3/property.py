class Property:
    def __init__(self, area: str, rooms: int, price: str, address: str):
        self.area = area
        self.rooms = rooms
        self.price = price
        self.address = address

    def __str__(self):
        return f"{self.area} {self.rooms} {self.price} {self.address}"
