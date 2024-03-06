from project.user import User


class Library:
    def __init__(self):
        self.user_records = []  # store users as objects
        self.books_available = {}  # {vazov: [pod igoto,...]}
        self.rented_books = {}  # ({Ivan: {book names: days to return}}

    def get_book(self, author, book_name, days_to_return, user: User):
        if book_name in self.books_available[author]:
            self.books_available[author].remove(book_name)
            user.books.append(book_name)

            if user.username in self.user_records:  # ako User go imame, slagame knigata s days to return
                self.rented_books[user.username][book_name] = days_to_return
            else:
                self.rented_books[user.username] = {
                    book_name: days_to_return}  # ako go nqmame, go syzdavame v rented books
            return f"{book_name} successfully rented for the next {days_to_return} days!"

        for data in self.rented_books.values():  # data is {book names: days to return}, to check days to be returned
            if book_name in data:
                return f'The book "{book_name}" is already rented and will be available in {data[book_name]} days!'

    def return_book(self, author, book_name, user: User):
        if book_name in user.books:  # ako sme q naeli knigata e returnvame i mahame ot spisycite
            user.books.remove(book_name)
            self.books_available[author].append(book_name)  # vryshtame q kym avaialable
            del self.rented_books[user.username][book_name]
        return f"{user.username} doesn't have this book in his/her records!"
