from random import *
class library:

    def  __init__(self,books,record,copy_books):
        self.books=books
        self.record=record
        self.copy_books=copy_books

    def display_book(self):
        while True:
            print("1. All Books of the Library \n2. Issued Books\n3. Available books\n4. Return to Main Menu\n")
            try:
                disp=int(input("\nEnter your choice :"))
            except ValueError as e:
                print("ENTER A VALID INTEGER!\n")
            if disp==1:
                for i in self.copy_books:
                    print(i,end=", ")
                print()
            elif disp==2:
                if (self.record.values()):
                    for i in self.record.values():
                        print(i,end=", ")
                    print()
                else:
                    print("No Books Issued!\n")
            elif disp==3:
                if (self.books):
                    for i in self.books:
                        print(i,end=", ")
                    print()
                else:
                    print("No Books Available\n")
            elif disp==4:
                break
            else:
                print("Enter a Valid choice!")

    def issue_book(self):

        name=input("Enter Your ID : ")
        check=input("Enter name of the book you want to issue : ")
        if name in self.record.keys():
            print("Issuing More Than One Book is Not Allowed")
        else:
            if check in self.books:
                self.record[name]=check
                self.books.remove(check)
                print("Book Issued Successfully\n")
            else:
                print("Book Not Available!\n")

    def donate_book(self):
        d_book=input("Enter the name of book you want to donate : ")
        self.books.append(d_book)
        self.copy_books.append(d_book)
        print("Thank You For The Donation\n")

    def return_book(self):
        r_name=input("Enter your ID : ")
        if r_name in self.record.keys():
            r_book = input("Enter the name of book which you want to return: ")
            if self.record[r_name]==r_book:
                if r_book in self.record.values():
                    self.books.append(r_book)
                    del self.record[r_name]
                    print("Book Returned Successfully\n")
                else:
                    print("Book Name Not Matched\n")
            else:
                print("Record not found!\n")
        else:
            print("Record Not Found!\n")

def execute():

    books=["Anna Karenina", "To Kill a Mockingbird", "The Great Gatsby", "One Hundred Years of Solitude", "A Passage to India", "Invisible Man", "Don Quixote"]
    copy_books=books[:]

    record = {}
    obj=library(books,record,copy_books)

    print("\nWELCOME TO THE LIBRARY!\n\nRules to be followed:-\n1. You can issue only one book at a time.\n2. Proper silence should be maintained\n3. Kindly return the book once you're done with your work\n\n")
    print("YOU CAN MAKE YOUR CHOICE FROM 1 - 5")

    while True:
        print("\n1. Display Books \n2. Issue Book\n3. Donate a book\n4. Return a book\n5. Exit\n")
        try:
            choice=int(input("Enter your choice :"))
            if choice==5:
                break
            elif choice==1:
                obj.display_book()
            elif choice==2:
                obj.issue_book()
            elif choice==3:
                obj.donate_book()
            elif choice==4:
                obj.return_book()
            else:
                print("INVALID CHOICE! CHOOSE A NUMBER FROM 1-5")

        except ValueError as e:
            print("PLEASE ENTER A VALID INTEGER NUMBER FROM 1-5!!")


execute()