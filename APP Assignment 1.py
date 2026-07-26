class Book:
    def __init__(self,title,author,isbn):
        self.title=title
        self.author=author
        self.isbn=isbn
        self.is_borrowed=False #a new book added to the library is not immediately borrowed which is why this is defined as "False"

    def borrow(self): #checks whether a book is borrowed or not
        if self.is_borrowed == True:
            print("Is",self.title,"already borrowed? :",self.is_borrowed) #"True" will be printed here
            print(self.title,"is NOT available to borrow")
            print("____________________________________")
          
        else:
            print("Is",self.title,"already borrowed? :",self.is_borrowed) #"False" will be printed here
            print(self.title,"is available to borrow")

    def return_book(self):
        if self.is_borrowed == True: 
            print(self.title,"can be returned.") #if book was borrowed, it can be returned       
        else:
            print(self.title,"was NOT borrowed.")

class Patron:
    def __init__(self,name,patron_id):
        self.name=name
        self.patron_id=patron_id
        self.borrowed=[] #stores all books borrowed by a patron

    def borrow_book(self,book):
        if book in self.borrowed:
            print(book.title,"has already been borrowed.") #if book is already in [], it can't be borrowed again
            print("____________________________________")
        else:
            self.borrowed.append(book) #add book to be borrowed in self.borrowed=[]
            book.is_borrowed = True
            print(book.title,"Borrowed Successfully!")
            print("____________________________________")

    def return_book(self,book):
        if book in self.borrowed:
            self.borrowed.remove(book) #a book can be returned only if it had been borrowed
            book.is_borrowed = False
            print(book.title,"Returned Successfully!")
            print("____________________________________")
        else:
            print(book.title,"book was NOT borrowed.")
            print("____________________________________")

class Library:
    def __init__(self):
        self.books=[] #stores added books in the library
        self.patrons=[] #stores registered patrons

    def add_book(self,book):
        if book in self.books:
            print(book.title,"is already present in the library.")
            print("____________________________________")
            
        else:
            self.books.append(book)
            print(book.title, "added to library.")
            print("____________________________________")

    def register_patron(self,patron):
        if patron in self.patrons:
            print(patron.name,"is already registered.")
            print("____________________________________")
        else:    
            self.patrons.append(patron)
            print(patron.name,"registered successfully!")
            print("____________________________________")

    def borrow_book(self,patron,book):
        if book in self.books:
            book.borrow() #checks and prints the status

            if book.is_borrowed == False:
                patron.borrow_book(book)
        else:
            print(book.title, "cannot be borrowed.")
            print("____________________________________")

    def return_book(self, patron, book):
        if book in patron.borrowed:
            book.return_book() #uses return_book from Book class
            patron.return_book(book) #uses return_book from Patron class
        else:
            print(patron.name,"has not borrowed",book.title,".")
            print("____________________________________")

    def display_books(self):
        print("Library Books:")
        for book in self.books:
            print("Title:", book.title)
            print("Author:", book.author)
            print("ISBN:", book.isbn)
            if book.is_borrowed == True:
                print("Status: Borrowed")
            else:
                print("Status: Available")
            print("____________________________________")

    def display_patrons(self):
        print("Patrons:")
        for patron in self.patrons:
            print("Name:",patron.name,"| ID:",patron.patron_id)
            if patron.borrowed:
                print(" Borrowed Books:")
                for book in patron.borrowed:
                    print("  -", book.title)
            else:
                print("No books borrowed.")
        print("____________________________________")
        
library = Library() #create library object

#create book objects
book1 = Book("Good Omens", "Neil Gaiman", "101")
book2 = Book("Heated Rivalry", "Rachel Reid", "102")
book3 = Book("Python Programming", "Guido van Rossum", "103")

#add books to library
library.add_book(book1)
library.add_book(book2)
library.add_book(book3)

#create patron objects
patron1 = Patron("Alice", "P001")
patron2 = Patron("Bob", "P002")

#register patrons to library
library.register_patron(patron1)
library.register_patron(patron2)

#borrow books from library
library.borrow_book(patron1, book1)
library.borrow_book(patron2, book2)
library.borrow_book(patron1, book2)
library.borrow_book(patron2, book3)

#display information
library.display_books()
library.display_patrons()

#return book to library
library.return_book(patron1, book1)