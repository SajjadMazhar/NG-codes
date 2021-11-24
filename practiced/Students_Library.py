class Library:

    def __init__(self, availBooks):
        self.availBooks = availBooks
        self.issuedBooks = {}

    def lendBook(self, requestedBook, recever):
        if requestedBook in self.availBooks:
            self.availBooks.remove(requestedBook)
            self.issuedBooks[requestedBook] = recever
            print("The book is given to you!")
        else:
            print("The book is not available at this moment")

    def displayBooks(self, count):
        print("The available books are: ")
        for book in self.availBooks:
            print(f"{count}- {book}")
            count += 1

    def returnBook(self, book, userName):
        if book in self.availBooks:
            print("The book was already returned!!")
        else:
            self.availBooks.append(book)
            print("Thanks to return the book")
            del self.issuedBooks[book]


    def addBooks(self, book):
        if book in self.availBooks:
            print("The book is already there in the library")
        else:
            self.availBooks.append(book)
            print("Thank you for adding a new book!")

    def showIssuedBooks(self):
        print(self.issuedBooks)


print("-----------------Welcome to Sajjad's library---------------")
lib = Library(['Physics', 'Chemistry', 'Mathematics', 'Literature', 'History', 'Geography'])
isOpen = True
while isOpen:
    print("""
            
            1- to see the available books
            2- to request and lend a book
            3- return a book
            4- add a new book to the library
            5- Show issued books
            6- exit the programme
            
    """)
    choice = int(input("Enter your choice: "))
    if choice == 1:
        count = 1
        lib.displayBooks(count)
    elif choice == 2:
        requestedBook = input("Enter the name of the book you want to lend: ")
        receverName = input("Enter your name: ")
        lib.lendBook(requestedBook.title(), receverName)
    elif choice == 3:
        book = input("What book do you want to return: ")
        user = input("What is your name: ")
        lib.returnBook(book.title(), user)
    elif choice == 4:
        new_book = input(
            "Enter the Name of the book you want to add to this library: ")
        lib.addBooks(new_book.title())
    elif choice == 5:
        lib.showIssuedBooks()
    else:
        isOpen = False
