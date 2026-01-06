class Book:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year

    def __str__(self):
        return f"Title: {self.title}, Author: {self.author}, Year: {self.year}"


class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)
        print("✅ Book added successfully.")

    def remove_book(self, title):
        for book in self.books:
            if book.title == title:
                self.books.remove(book)
                print("❌ Book removed successfully.")
                return
        print("⚠ No book found with that title.")

    def search_book(self, title):
        for book in self.books:
            if book.title == title:
                print("📘 Book found:")
                print(book)
                return
        print("⚠ No book found with that title.")

    def show_all_books(self):
        if not self.books:
            print("📭 No books in the library.")
        else:
            print("📚 List of all books:")
            for book in self.books:
                print(book)


def main():
    library = Library()

    while True:
        print("\n--- Library Menu ---")
        print("1: Add a book")
        print("2: Remove a book")
        print("3: Search for a book")
        print("4: Show all books")
        print("0: Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            title = input("Enter book title: ")
            author = input("Enter author name: ")
            year = int(input("Enter publication year: "))
            book = Book(title, author, year)
            library.add_book(book)

        elif choice == "2":
            title = input("Enter the title of the book to remove: ")
            library.remove_book(title)

        elif choice == "3":
            title = input("Enter the title of the book to search: ")
            library.search_book(title)

        elif choice == "4":
            library.show_all_books()

        elif choice == "0":
            print("👋 Goodbye!")
            break

        else:
            print("❗ Invalid option. Please try again.")


if __name__ == "__main__":
    main()
