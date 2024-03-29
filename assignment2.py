from abc import ABC, abstractmethod
from typing import List, Dict

class Item(ABC):
    def __init__(self, title: str, author: str, item_id: str):
        self.title = title
        self.author = author
        self.item_id = item_id

    @abstractmethod
    def display(self):
        pass

class Book(Item):
    def __init__(self, title: str, author: str, item_id: str, isbn: str):
        super().__init__(title, author, item_id)
        self.isbn = isbn

    def display(self):
        print(f"Book: {self.title} by {self.author}, ISBN: {self.isbn}")

class CD(Item):
    def __init__(self, title: str, author: str, item_id: str, duration: int):
        super().__init__(title, author, item_id)
        self.duration = duration

    def display(self):
        print(f"CD: {self.title} by {self.author}, Duration: {self.duration} minutes")

class User(ABC):
    def __init__(self, user_id: str, name: str):
        self.user_id = user_id
        self.name = name

    @abstractmethod
    def access_catalog(self, catalog):
        pass

class Librarian(User):
    def access_catalog(self, catalog):
        catalog.display_items()

class Catalog:
    def __init__(self):
        self.items = {}

    def add_item(self, item: Item):
        self.items[item.item_id] = item

    def display_items(self):
        for item in self.items.values():
            item.display()

def librarian_cli():
    catalog = Catalog()
    catalog.add_item(Book("The Great Gatsby", "F. Scott Fitzgerald", "1", "1234567890"))
    catalog.add_item(CD("Dark Side of the Moon", "Pink Floyd", "2", 42))

    librarian = Librarian("lib1", "Alice")
    print("Welcome, Librarian!")
    while True:
        command = input("Enter command (list, exit): ").strip().lower()
        if command == "list":
            librarian.access_catalog(catalog)
        elif command == "exit":
            break

librarian_cli()
