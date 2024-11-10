#We create the class book
class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.is_borrowed = False

#We Mark the book borrowed
    def mark_as_borrowed(self):
        if not self.is_borrowed:
            self.is_borrowed = True
            return True
        return False

# We mark the book as returned.
#  To  make sure that a book which is not borrowed in the first place to be marked as returned(since this will mark all  books as returned) We have an if statement for is_borrowed such that we confirm first if it was ever borrowed if it is false we just return false
    def mark_as_returned(self):
        if self.is_borrowed:
            self.is_borrowed = False
            return True
        return False

#Class to include members
class LibraryMember:
    def __init__(self, name, member_id):
        self.name = name
        self.member_id = member_id
        self.borrowed_books = []

#function to borrow book
    def borrow_book(self, book):
        if book.mark_as_borrowed():
            self.borrowed_books.append(book)
            print(f"{self.name} borrowed '{book.title}' by {book.author}.")
        else:
            print(f"'{book.title}' is already borrowed by another member.")
# Function to return booka and then mark them as returned
    def return_book(self, book):
        if book in self.borrowed_books:
            if book.mark_as_returned():
                self.borrowed_books.remove(book)
                print(f"{self.name} returned '{book.title}'.")
        else:
            print(f"{self.name} does not have '{book.title}' borrowed.")

#Function to display borrowed books
    def list_borrowed_books(self):
        if self.borrowed_books:
            print(f"{self.name} has borrowed the following books:")
            for book in self.borrowed_books:
                print(f"- {book.title} by {book.author}")
        else:
            print(f"{self.name} has not borrowed any books.")


# I will be instanciating to see How it behaves
# I have made the functionality of borrowing and returnign books interactive by use  of input function and also you can print list of borrowed books
def main():
    books = []
    members = {}

    # Adding sample books and members for demonstration
    books.append(Book("Man's Search for meaning", " Victor Frankl"))
    books.append(Book("The Book of John", "Saint John "))

    member = LibraryMember("Wayne", "101")
    members["101"] = member

    while True:
        print("\nLibrary Management System")
        print("1. Borrow a book")
        print("2. Return a book")
        print("3. List borrowed books for a member")
        print("4. Exit")
        
        choice = input("Enter your choice: ")
        
        if choice == "1":
            # Borrowing a book
            member_id = input("Enter member ID: ")
            title = input("Enter book title to borrow: ")
            
            member = members.get(member_id)
            if member:
                book = next((b for b in books if b.title == title and not b.is_borrowed), None)
                if book:
                    member.borrow_book(book)
                else:
                    print(f"'{title}' is either not available or already borrowed.")
            else:
                print("Invalid member ID.")
        
        elif choice == "2":
            # Returning a book
            member_id = input("Enter member ID: ")
            title = input("Enter book title to return: ")
            
            member = members.get(member_id)
            if member:
                book = next((b for b in member.borrowed_books if b.title == title), None)
                if book:
                    member.return_book(book)
                else:
                    print(f"'{title}' is not in {member.name}'s borrowed books.")
            else:
                print("Invalid member ID.")
        
        elif choice == "3":
            # Listing borrowed books for a member
            member_id = input("Enter member ID: ")
            member = members.get(member_id)
            if member:
                member.list_borrowed_books()
            else:
                print("Invalid member ID.")


        elif choice == "4":
            print("Exiting the Library Management System.")
            break
        else:
            print("Invalid choice. Please try again.")

# Run the main function to  start the instanciate the Applicarion
main()