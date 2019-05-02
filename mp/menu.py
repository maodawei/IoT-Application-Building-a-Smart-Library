from cloud_db import cloud_db

class Menu:
    def main(self):
        with cloud_db() as db:
            #Order we create tables is important
            db.createBookTable()
            db.createLmsUserTable()
            db.createBorrowTable()
            
        self.runMenu()

    def runMenu(self):
        while(True):
            print()
            print("1. List Books")
            print("2. Insert Book")
            print("3. Quit")
            print("4. Search book by title")
            selection = input("Select an option: ")
            print()

            if(selection == "1"):
                self.listBooks()
            elif(selection == "2"):
                self.insertBook()
            elif(selection == "3"):
                print("Goodbye!")
                break
            else:
                print("Invalid input - please try again.")

    def listBooks(self):
        print("--- Books ---")
        print("{:<15} {}".format("Book ID", "Title"))
        with cloud_db() as db:
            for book in db.getBooks():
                print("{:<15} {}".format(book[0], book[1]))

    def insertBook(self):
        print("--- Insert Book ---")
        title = input("Enter the title of the new book: ")
        author = input("Enter the author's name: ")
        pDate = input("Enter the date of the new book y-m-d")
        with cloud_db() as db:
            if(db.insertBook(title, author, pDate)):
                print("{} inserted successfully.".format(title))
            else:
                print("{} failed to be inserted.".format(title))

    def searchBookByTitle(self):
        searchTerm = input("Enter your search term for the book: ")
        print("--- Books ---")
        print("{:<15} {}".format("Book ID", "Title"))
        with cloud_db() as db:
            for book in db.getBooksByTitle(searchTerm):
                print("{:<15} {}".format(book[0], book[1]))

if __name__ == "__main__":
    Menu().main()