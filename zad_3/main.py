from flat import Flat
from house import House


def main():
    house = House("150", 5, "100000", "Katowice", 840)
    print(house)

    flat = Flat("79", 4, "100000", "Roma", 79)
    print(flat)


if __name__ == "__main__":
    main()
