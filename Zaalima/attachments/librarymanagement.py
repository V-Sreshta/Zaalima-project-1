# Book class
class Book:
    def __init__(self, title, author, isbn):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.is_issued = False

    def show_details(self):
        status = "Issued" if self.is_issued else "Available"
        print(f"{self.title} by {self.author} (ISBN: {self.isbn}) - {status}")

# Library class
class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)
        print(f"Book '{book.title}' added successfully.\n")

    def issue_book(self, isbn):
        for book in self.books:
            if book.isbn == isbn:
                if not book.is_issued:
                    book.is_issued = True
                    print(f"You have issued: {book.title}\n")
                else:
                    print(f"Book '{book.title}' is already issued.\n")
                return
        print("Book not found.\n")

    def return_book(self, isbn):
        for book in self.books:
            if book.isbn == isbn:
                if book.is_issued:
                    book.is_issued = False
                    print(f"Book '{book.title}' returned successfully.\n")
                else:
                    print(f"Book '{book.title}' was not issued.\n")
                return
        print("Book not found.\n")

    def show_books(self):
        if not self.books:
            print("Library is empty.\n")
        else:
            print("\nBooks in the Library:")
            for book in self.books:
                book.show_details()
            print()

# Main Program
library = Library()

while True:
    print("----- Library Menu -----")
    print("1. Add Book")
    print("2. Issue Book")
    print("3. Return Book")
    print("4. Show All Books")
    print("5. Exit")

    choice = input("Enter your choice (1-5): ")

    if choice == '1':
        title = input("Enter book title: ")
        author = input("Enter author name: ")
        isbn = input("Enter ISBN number: ")
        new_book = Book(title, author, isbn)
        library.add_book(new_book)

    elif choice == '2':
        isbn = input("Enter ISBN to issue: ")
        library.issue_book(isbn)

    elif choice == '3':
        isbn = input("Enter ISBN to return: ")
        library.return_book(isbn)

    elif choice == '4':
        library.show_books()

    elif choice == '5':
        print("Exiting Library System. Goodbye!")
        break

    else:
        print("Invalid choice. Please try again.\n")