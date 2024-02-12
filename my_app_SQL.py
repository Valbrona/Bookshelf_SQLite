from utils import my_database_SQL

user_choice = """
-> 'a' to add a new book
-> 'l' to list all books
-> 'r' to mark a book as read
-> 'd' to delete a book
-> 'q' to quit

Your choice: """

def menu():
    my_database_SQL.create_book_table()
    user_input = input(user_choice)
    while user_input != "q":
        if user_input == "a":
            prompt_add_book()
        elif user_input == "l":
            list_books()
        elif user_input == "r":
            prompt_read_books()
        elif user_input == "d":
            prompt_delete_book()
        else:
            print("Unknown command. Please try again.")
        user_input = input(user_choice)


def prompt_add_book():
    name = input("Please type the name of the desired book: ").title()
    author = input("Please type the name of the author: ").title()

    while name.isnumeric() or author.isnumeric():
        print("^" * 20)
        print("Please provide a book and author name.")
        name = input("Please type the name of the desired book: ").title()
        author = input("Please type the name of the author: ").title()

    my_database_SQL.add_book(name, author)


def list_books():
    books = my_database_SQL.get_all_books()
    num = 0
    print("*" * 10, "Your book collection:", "*" * 10)
    for book in books:
        read = "read" if book["read"] else "not read"
        num += 1
        print(f"{num}.{book["name"]} written by {book["author"]} -> STATUS: {read}.")

def prompt_read_books():
    user_input =  input("Please write the name of the book you want to mark as 'read': ").title()

    my_database_SQL.mark_book_as_read(user_input)


def prompt_delete_book():
    user_input = input("Type in the name of the book you want to remove: ").title()

    my_database_SQL.delete_book(user_input)

menu()