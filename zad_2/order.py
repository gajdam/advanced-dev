class Order:
    def __init__(
        self, employee, student, books: list, order_date
    ):
        self.employee = employee
        self.student = student
        self.books = books
        self.order_date = order_date

    def __str__(self):
        books_list = "\n".join(str(book) for book in self.books)
        return f"{self.employee} {self.student} {books_list} {self.order_date}"
