from zad_1 import Student


class Library:
    def __init__(
        self, city: str, street: str, zip_code: str, open_hours: str, phone: str
    ):
        self.city = city
        self.street = street
        self.zip_code = zip_code
        self.open_hours = open_hours
        self.phone = phone

    def __str__(self):
        return (
            f"{self.city} {self.street} {self.zip_code} {self.open_hours} {self.phone}"
        )


class Employee:
    def __init__(
        self,
        first_name: str,
        last_name: str,
        hire_date: str,
        birth_date: str,
        city: str,
        street: str,
        zip_code: str,
        phone: str,
    ):
        self.first_name = first_name
        self.last_name = last_name
        self.hire_date = hire_date
        self.birth_date = birth_date
        self.city = city
        self.street = street
        self.zip_code = zip_code
        self.phone = phone

    def __str__(self):
        return f"{self.first_name} {self.last_name} {self.hire_date} {self.city} {self.street} {self.zip_code} {self.phone}"


class Book:
    def __init__(
        self,
        library: Library,
        publication_date: str,
        author_name: str,
        author_surname: str,
        number_of_pages: str,
    ):
        self.library = library
        self.publication_date = publication_date
        self.author_name = author_name
        self.author_surname = author_surname
        self.number_of_pages = number_of_pages

    def __str__(self):
        return f"{self.library} {self.publication_date} {self.author_name} {self.author_surname} {self.number_of_pages}"


class Order:
    def __init__(
        self, employee: Employee, student: Student, books: list[Book], order_date
    ):
        self.employee = employee
        self.student = student
        self.books = books
        self.order_date = order_date

    def __str__(self):
        books_list = "\n".join(str(book) for book in self.books)
        return f"{self.employee} {self.student} {books_list} {self.order_date}"


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

order = Order(employee, student, [book, book1, book2, book4], order_date="1990-01-10")
print(order)

order1 = Order(
    employeeRoma, student1, [book1, book2, book3, book4], order_date="2000-01-10"
)
print(order1)
