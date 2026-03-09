class LibraryBook:
    def __init__(self, title, writer, is_available=True):
        self.title = title
        self.writer = writer
        self.is_available = is_available

    def borrow_book(self):
        if self.is_available:
            self.is_available = False
            print(f"You borrowed '{self.title}' written by {self.writer}.")
        else:
            print(f"'{self.title}' is not available right now.")

    def give_back(self):
        if not self.is_available:
            self.is_available = True
            print(f"'{self.title}' has been returned to the library.")
        else:
            print(f"'{self.title}' was already in the library.")

    def show_details(self):
        status = "Available" if self.is_available else "Not Available"
        print(f"Title: {self.title} | Author: {self.writer} | Status: {status}")


b1 = LibraryBook("Godan", "Premchand")
b2 = LibraryBook("Malgudi Days", "R. K. Narayan", False)

b1.show_details()
b2.show_details()

b1.borrow_book()
b1.show_details()

b1.give_back()
b1.show_details()
