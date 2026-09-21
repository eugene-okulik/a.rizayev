

class Book:
    page_material = 'бумага'
    text_exists = True

    def __init__(self, name, author, page_count, isbn, reserved):
        self.name = name
        self.author = author
        self.page_count = page_count
        self.isbn = isbn
        self.reserved = reserved


book_1 = Book('Идиот', 'Достоевский', 550, '123123', False)
book_2 = Book('Сказка о Рыбаке и рыбке', 'Пушкин', 25, '232323', False)
book_3 = Book('1984', 'Оруэлл', 660, '234253', False)
book_4 = Book('Дети капитана Гранта', 'Верн', 440, 'T2323', True)
book_5 = Book('Граф Монте Кристо', 'Дюма', 770, '8787878', False)

books = [book_1, book_2, book_3, book_4, book_5]


def print_book(book_to_print):
    print(f'Название: {book_to_print.name}, Автор: {book_to_print.author},'
          f' страниц: {book_to_print.page_count}, материал: {book_to_print.page_material}'
          + (', зарезервирована' if book_to_print.reserved else ''))


for book in books:
    print_book(book)


class SchoolBook(Book):
    def __init__(self, name, author, page_count, isbn, reserved, subject, grade, tasks_presented):
        super().__init__(name, author, page_count, isbn, reserved)
        self.subject = subject
        self.grade = grade
        self.tasks_presented = tasks_presented

    def print_info(self):
        print(f'Название: {self.name}, Автор: {self.author}, страниц: {self.page_count}, предмет: {self.subject},'
              f' класс: {self.grade}' + (', зарезервирована' if self.reserved else ''))


book_6 = SchoolBook('География для детей', 'Дятлов', 110,
                    'IO2323', True, 'География', 5, True)
book_7 = SchoolBook('Математика для детей', 'Воробьев', 105,
                    'IO2623', False, 'Математика', 6, True)
book_8 = SchoolBook('Ботаника для детей', 'Синицын', 103,
                    'IO2923', False, 'Ботаника', 7, False)

school_books = [book_6, book_7, book_8]

for book in school_books:
    book.print_info()
