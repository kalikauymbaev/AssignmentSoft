# Subsystems: BookInventory and UserManagement
class BookInventory:
    def __init__(self):
        self.books = [
            {"id": 1, "title": "1984", "author": "George Orwell", "available": True},
            {"id": 2, "title": "The Great Gatsby", "author": "F. Scott Fitzgerald", "available": False}
        ]

    def search_books(self, title=None, author=None):
        results = []
        for book in self.books:
            if (title and title in book["title"]) or (author and author in book["author"]):
                results.append(book)
        return results

    def check_availability(self, book_id):
        for book in self.books:
            if book["id"] == book_id:
                return book["available"]
        return False

class UserManagement:
    def borrow_book(self, user_id, book_id):
        return f"User {user_id} borrowed book {book_id}"

    def return_book(self, user_id, book_id):
        return f"User {user_id} returned book {book_id}"

# Facade: LibraryFacade
class LibraryFacade:
    def __init__(self):
        self.inventory = BookInventory()
        self.users = UserManagement()

    def borrow_book(self, user_id, book_id):
        if self.inventory.check_availability(book_id):
            return self.users.borrow_book(user_id, book_id)
        else:
            return "Book is not available"

    def return_book(self, user_id, book_id):
        return self.users.return_book(user_id, book_id)

    def search_books(self, title=None, author=None):
        return self.inventory.search_books(title, author)

    def check_book_availability(self, book_id):
        availability = self.inventory.check_availability(book_id)
        return "Available" if availability else "Not Available"

# Main Testing Script
def main():
    # Create an instance of the facade
    library_system = LibraryFacade()

    # Test searching for books
    print("Search Results for '1984':", library_system.search_books(title="1984"))
    print("Search Results for authors containing 'Fitzgerald':", library_system.search_books(author="Fitzgerald"))

    # Test checking availability
    print("Availability of Book ID 1:", library_system.check_book_availability(1))
    print("Availability of Book ID 2:", library_system.check_book_availability(2))

    # Test borrowing and returning books
    print(library_system.borrow_book(1001, 1))  # Should succeed
    print(library_system.borrow_book(1002, 2))  # Should fail - not available
    print(library_system.return_book(1001, 1))

if __name__ == "__main__":
    main()
