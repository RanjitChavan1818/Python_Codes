# ===== Library Management System =====

# 1. Add Book
# 2. Display All Books
# 3. Search Book
# 4. Borrow Book
# 5. Return Book
# 6. Exit


class Book:
    def __init__(self, b_name, author, price, publish_date):
        self.author = author
        self.b_name = b_name
        self.price  = price
        self.publish_date = publish_date
        self.isborrowed=False
        

    def display(self):
        print(f"Book Name:{self.b_name}")
        print(f"Author Name:{self.author}")
        print(f"Published date:{self.publish_date}")
        print(f"Price :{self.price}")
        print()


    # def search_book(self):
    #     pass

    def borrow_book(self):
        self.isborrowed=True

    def return_book(self):
        self.isborrowed=False




library=[]
# book=Library()

while True:
    print("1. Add Book")
    print("2. Display All Books")
    print("3. Search Book")
    print("4. Borrow Book")

    print("5. Exit")

    ch=int(input("Enter a choice:"))
    match ch:
        case 1:
            b_name=input("Enter Book Name:")
            author=input("Enter author name:")
            price=int(input("Enter price of book:"))
            publish_date=input("Enter publishing date:(year/day/month)")
            b=Book(b_name,author,price,publish_date)
            library.append(b)
            print("Book Successfully Added..")

        case 2:
            for b in library:
                b.display()
                print()

        case 3:
            book_name=input("Enter Book name to search:")
            for b in library:
                if b.b_name==book_name:
                    if b.isborrowed:
                        print("Hey, Book is already borrowed")
                    else:
                        
                        print("Book is available")
                    break
            else:
                print("Book not found")

        case 4:
            book_name=input("Enter Book name to borrow:")
            for b in library:
                if b.b_name==book_name:
                    if b.isborrowed:
                        print("Hey, Book is already borrowed")
                    else:
                        b.borrow_book()
                        print("Print Book Borrowed Successfully")
                    break
            else:
                print("Book not found")

        case 5:
            b_name=input("Enter book , which returning..")
            for b in library:
                if b.b_name==b_name:
                    if b.isborrowed:
                        b.return_book()
                        print("Book is returned successfuuly..")
                    else:
                        print('Book is not currently borrowed')
                    break
            else:
                print("Book Not from this library")

        case 6:
            print("Application is closing....")
            break

        case _:
            print("Invalid choice!")





