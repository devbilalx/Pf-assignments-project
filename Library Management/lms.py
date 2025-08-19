books = {
    "HarryPotter": [101, "J.K. Rowling", "Issued"],
    "PythonBasics": [102, "John Smith", "Available"],
    "C++Guide": [103, "Sara Khan", "Issued"],
    "DataScience101": [104, "Ali Raza", "Available"],
    "MachineLearningIntro": [105, "Emily Brown", "Available"]
}
def menu():
    while True:
        userInput=input("Please Enter 1. Add a book 2. View all books 3. Search for a book 4. Issue a book 5. Return a book 6. Exit : \n")

        if userInput not in["1","2","3","4","5","6"]:
            print("Invalid Operation")
        else:
            if userInput=="1":
                BookId=input("Please Enter book Id")
                Title=input("Please Enter Title")
                AuthorName=input("Please Enter AuthorName")
                addbook(BookId,Title,AuthorName)
            elif userInput=="2":
                viewbooks()
            elif userInput=="3":
                search=input("Please Enter Book To Search")
                searchbook(search)
            elif userInput=="4":
                idbook=int(input("Please Enter book Id"))
                issuebook(idbook)
            elif userInput=="5":
                idbook=input("Please Enter book Id")
                retrnbook(idbook)
            elif userInput=="6":
                break


def issuebook(bookid):
    if isinstance(bookid,int):
        for title in books:
            id=books[title][0]
            status=books[title][2]
            if id==bookid and status=="Available":
                books[title][2]="Issued"
                print(f"Book '{title}' issued successfully.") 
                break
            elif id==bookid and status=="Issued":
                print("Book already issued")
                break

        else:
            print("Not found")
    else:
        print("Book ID should be in integer")


def searchbook(bookToSearch):
    if bookToSearch in books:
        detail=books[bookToSearch]
        print(f"Book Name is {bookToSearch}, Book ID is {detail[0]}, Author Name is {detail[1]}, Avalibility: {detail[2]}")

    else:
        nbookToSearch=str(bookToSearch)

        for title in books:
            detail=books[title]
            strid=str(detail[0])
            if nbookToSearch==strid:
                print(f"Book Name is {title}, Book ID is {detail[0]}, Author Name is {detail[1]}, Avalibility: {detail[2]}")
                break
        else:
            print("Book Not Found")


def viewbooks():
    if len(books)==0:
        print("No books available")
    else:
        for title in books:
            detail=books[title]
            print(f"Book Name is {title}, Book ID is {detail[0]}, Author Name is {detail[1]}, Avalibility: {detail[2]}")


def addbook(BookId,Title,AuthorName):
    for title in books:
        idbook=books[title][0]
        if str(idbook)==BookId:
            print("This book already exist so cannot add it.")
            break
    else:
        bookDetails=[int(BookId),AuthorName,"Available"]
        books[Title]=bookDetails

def retrnbook(bookId):
    for title in books:
        detail=books[title]
        if str(bookId)==str(detail[0]):
            if detail[2]=="Issued":
                detail[2]="Available"
                print(f"Book '{title}' returned successfully.")
                break
            else:
                print(f"Book {title} already Available")
                break
    else:
        print("Book you entered is not from our library")

menu()


        



  