def add_book(catalog, book_id, title, author, year):
    catalog[book_id] = (title, author, year)


def borrow_book(catalog, borrowed_books, book_id):
  
    if book_id in catalog and book_id not in borrowed_books:
        borrowed_books.append(book_id)
        print(f"Book {book_id} borrowed successfully.")
    else:
        print(f"Cannot borrow Book {book_id}.")


def return_book(borrowed_books, book_id):
    if book_id in borrowed_books:
        borrowed_books.remove(book_id)
        print(f"Book {book_id} returned successfully.")
    else:
        print(f"Book {book_id} was not borrowed.")
  


def show_available(catalog, borrowed_books):
    print("\nAvailable Books:")
    for book_id, details in catalog.items():
        if book_id not in borrowed_books:
            title, author, year = details
            print(f"ID: {book_id}, Title: {title}, Author: {author}, Year: {year}")


def main():
    catalog = {}
    borrowed_books = []
    members = set()

    # Add 4 books
    add_book(catalog, 1, "1984", "George Orwell", 1949)
    add_book(catalog, 2, "Alice's Adventures in Wonderland", "Lewis Carroll.", 1960)
    add_book(catalog, 3, "The Great Gatsby", "F. Scott Fitzgerald", 1925)
    add_book(catalog, 4, "Pride and Prejudice", "Jane Austen", 1813)

    # Register 3 members 
    register_member(members, 101)
    register_member(members, 102)
    register_member(members, 103)
    register_member(members, 101) 

    # Borrow 2 books
    borrow_book(catalog, borrowed_books, 1)
    borrow_book(catalog, borrowed_books, 3)

    # Return 1 book
    return_book(borrowed_books, 1)

    # Show available books
    show_available(catalog, borrowed_books)

    # Display members
    print("\nRegistered Members:", members)

if __name__ == "__main__":
    main()
