from library import Library
from employee import Employee
from book import Book
from order import Order
from zad_1.student import Student


def main():
    libKatowice = Library("Katowice", "Lubuska", "40-100", "8-20", "5463728983")
    libRoma = Library("Roma", "Carlitto", "00-001", "10-14, 16-18", "+395463728983")

    book = Book(libKatowice, "15.01.2002", "Adam", "Mickiewicz", "200")
    book1 = Book(libKatowice, "15.05.2202", "Król", "Julian", "200")
    book2 = Book(libKatowice, "15.11.2022", "Skipper", "Pingwin", "200")
    book3 = Book(libRoma, "29.09.2018", "Juliusz", "Cezar", "200")
    book4 = Book(libRoma, "31.02.2012", "Maximus Decimus", "Meridus", "200")

    employee = Employee(
        "Adam",
        "Adam",
        "2002-01-10",
        "2002-01-10",
        "Godula",
        "Godulska",
        "40-400",
        "51515151",
    )
    employee1 = Employee(
        "Wojtek",
        "Wojtek",
        "2022-02-10",
        "1997-01-10",
        "Warszawa",
        "Katowicka",
        "40-401",
        "51515151",
    )
    employeeRoma = Employee(
        "Mario",
        "Buffon",
        "1992-11-11",
        "1990-01-10",
        "Rome",
        "Legions",
        "40-400",
        "51515151",
    )

    student = Student("Juliusz", "49")
    student1 = Student("Tomasz", "55")

    order = Order(
        employee, student, [book, book1, book2, book4], order_date="1990-01-10"
    )
    print(order)

    order1 = Order(
        employeeRoma, student1, [book1, book2, book3, book4], order_date="2000-01-10"
    )
    print(order1)


if __name__ == "__main__":
    main()
