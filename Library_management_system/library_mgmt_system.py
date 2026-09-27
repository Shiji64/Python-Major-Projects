import sqlite3
from datetime import date

conn = sqlite3.connect("librarymgmt.db")
cursor = conn.cursor()

#Users table
cursor.execute('''
CREATE TABLE IF NOT EXISTS Users(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username VARCHAR UNIQUE,
    password TEXT,
    role TEXT
)
''')

#Books table
cursor.execute('''
CREATE TABLE IF NOT EXISTS Books(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT,
    authorname TEXT,
    category TEXT,
    total_copies INTEGER,
    available_copies INTEGER
)
''')

#Members table
cursor.execute('''
CREATE TABLE IF NOT EXISTS Members(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    phone TEXT,
    email TEXT UNIQUE
)
''')

#Borrowings table
cursor.execute('''
CREATE TABLE IF NOT EXISTS Borrowings(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    member_id INTEGER,
    book_id INTEGER,
    issue_date TEXT,
    return_date TEXT,
    status TEXT,
    FOREIGN KEY (member_id) REFERENCES Members(id),
    FOREIGN KEY (book_id) REFERENCES Books(id)
)
''')

conn.commit()
conn.close()


#Books menu
#Add book
def get_connection():
    conn = sqlite3.connect("librarymgmt.db")
    conn.execute("PRAGMA foreign_keys = ON")
    return conn

def addbook():
    conn = get_connection()
    cursor = conn.cursor()
    title = input("Enter book title: -").strip()
    authorname = input("Enter author name: -").strip()
    category = input("Enter book category: -").strip()
    if title == "" or authorname == "" or category == "":
        print("Book details cannot be empty!")
        conn.close()
        return
    #Check for duplicate books
    cursor.execute('''
        SELECT * FROM Books
        WHERE title = ? AND authorname = ?
    ''', (title, authorname))

    existing_book = cursor.fetchone()

    if existing_book:
        print("This book already exists in the library!")
        conn.close()
        return
    try:
        total_copies = int(input("Enter total number of copies: -"))
        if total_copies <= 0:
            print("Number of copies must be greater than 0")
            conn.close()
            return
        cursor.execute('''
                INSERT INTO Books(title,authorname,category,total_copies,available_copies)
                VALUES(?,?,?,?,?)
            ''',(title,authorname,category,total_copies,total_copies))
    
        conn.commit()
        print("Book added successfully!")
    except ValueError:
        print("Number of copies must be a number")
    conn.close()

#View all books
def viewbooks():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute('''SELECT * FROM Books''')
    books = cursor.fetchall()
    if books:
        print("----- Books List -----")
        for i in books:
            print(f"Book ID : {i[0]}")
            print(f"Book Title : {i[1]}")
            print(f"Author : {i[2]}")
            print(f"Category : {i[3]}")
            print(f"Available Copies : {i[5]}")
            print(f"Total Copies : {i[4]}")
            print("-"*20)
            
    else:
        print("No books in library!")
    conn.close()

#Search for a book
def searchbook():
    conn = get_connection()
    cursor = conn.cursor()
    try:

        book_id = int(input("Enter book id: "))

        cursor.execute('''
            SELECT * FROM Books WHERE id = ?
        ''',(book_id,))
        book = cursor.fetchone()
        if book:
            print("Book found!")
            print(f"Book Title : {book[1]}")
            print(f"Author : {book[2]}")
            print(f"Category : {book[3]}")
            print(f"Total Copies : {book[4]}")
            print(f"Available Copies : {book[5]}")
        else:
            print("Book not found ❌")
    except ValueError:
        print("Book Id must be a number!")
    conn.close()

#Update books details
def updatebookdetails():
    conn = get_connection()
    cursor = conn.cursor()
    try:

        book_id = int(input("Enter book id: "))
        title = input("Enter book title: -").strip()
        authorname = input("Enter author name: -").strip()
        category = input("Enter book category: -").strip()
        if title == "" or authorname == "" or category == "":
            print("Book details cannot be empty!")
            conn.close()
            return
        cursor.execute('''
            UPDATE Books SET title = ? , authorname = ? , category = ? WHERE id = ?
        ''',(title,authorname,category,book_id))
        if cursor.rowcount == 0:
            print("Book Id not found!")
        else:
            conn.commit()
            print("Book details updated")
    except ValueError:
            print("Book Id must be a number!")
    conn.close()

#Delete a book details
def deletebook():
    conn = get_connection()
    cursor = conn.cursor()
    try:

        book_id = int(input("Enter book id: "))
        # Check borrowing history
        cursor.execute('''
            SELECT * FROM Borrowings WHERE book_id = ?
        ''', (book_id,))

        borrowing = cursor.fetchone()

        if borrowing:
            print("This book cannot be deleted because borrowing records exist!")
            conn.close()
            return
        ch = input("Are u sure u want to delete this book \nY/N").lower()
        if ch == "y":
            cursor.execute('''
                DELETE FROM Books WHERE id = ?
            ''',(book_id))
            if cursor.rowcount == 0:
                print("Book Id not found!")
            else:
                conn.commit()
                print("Book deleted!!!")
        elif ch == "n":
            print("Book not deleted") 
        else:
            print("Invalid option! Please enter Y or N.")
    except ValueError:
                print("Book Id must be a number!")
    conn.close()


#Members
#Add member details

def addmembers():
    conn = get_connection()
    cursor = conn.cursor()
    membername = input("Enter member name: -").strip()
    phone = input("Enter member phone no: -").strip()
    email = input("Enter member email id: -").strip()
    if membername == "" or phone == "" or email == "":
        print("Member details cannot be empty!")
        conn.close()
        return
     # Check duplicate email
    cursor.execute('''
        SELECT * FROM Members WHERE email = ?
    ''', (email,))

    existing_member = cursor.fetchone()

    if existing_member:
        print("This email ID is already registered!")
        conn.close()
        return
    cursor.execute('''
                INSERT INTO Members(name,phone,email)
                VALUES(?,?,?)
            ''',(membername,phone,email))
    
    conn.commit()
    print("Member details added successfully!")
    # except ValueError:
    #     print("Number of copies must be a number")
    conn.close()

#View all members
def viewmembers():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute('''SELECT * FROM Members''')
    members = cursor.fetchall()
    if members:
        print("----- Members Details -----")
        for i in members:
            print(f"Member ID : {i[0]}")
            print(f"Member Name : {i[1]}")
            print(f"Phone : {i[2]}")
            print(f"Email : {i[3]}")
            print("-"*20)
            
    else:
        print("No members in library!")
    conn.close()

#Search for a member
def searchmember():
    conn = get_connection()
    cursor = conn.cursor()
    try:

        m_id = int(input("Enter member id: "))

        cursor.execute('''
            SELECT * FROM Members WHERE id = ?
        ''',(m_id,))
        member = cursor.fetchone()
        if member:
            print("Member found!")
            print(f"Member Name : {member[1]}")
            print(f"Phone : {member[2]}")
            print(f"Email : {member[3]}")
        else:
            print("Member not found ❌")
    except ValueError:
        print("Member Id must be a number!")
    conn.close()

#Update Members details
def updatememberdetails():
    conn = get_connection()
    cursor = conn.cursor()
    try:

        m_id = int(input("Enter member id: "))
        membername = input("Enter member name: -").strip()
        phone = input("Enter member phone no: -").strip()
        email = input("Enter member email id: -").strip()
        if membername == "" or phone == "" or email == "":
            print("Member details cannot be empty!")
            conn.close()
            return
        # Check duplicate email
        cursor.execute('''
            SELECT * FROM Members
            WHERE email = ? AND id != ?
        ''', (email, m_id))

        existing_member = cursor.fetchone()

        if existing_member:
            print("This email ID is already registered!")
            conn.close()
            return
        cursor.execute('''
            UPDATE Members SET name = ? , phone = ? , email = ? WHERE id = ?
        ''',(membername,phone,email,m_id))
        if cursor.rowcount == 0:
            print("Member Id not found!")
        else:
            conn.commit()
            print("Member details updated")
    except ValueError:
        print("Member Id must be a number!")
    conn.close()

#Delete a member details
def deletemember():
    conn = get_connection()
    cursor = conn.cursor()
    try:

        m_id = int(input("Enter member id: "))
        # Check whether member exists
        cursor.execute('''
            SELECT * FROM Members WHERE id = ?
        ''', (m_id,))
        member = cursor.fetchone()
        if not member:
            print("Member Id not found!")
            conn.close()
            return
        # Check borrowing history
        cursor.execute('''
            SELECT * FROM Borrowings WHERE member_id = ?
        ''', (m_id,))
        borrowing = cursor.fetchone()
        if borrowing:
            print("This member cannot be deleted because borrowing records exist!")
            conn.close()
            return
        ch = input("Are u sure u want to delete this member \nY/N").lower()
        if ch == "y":
            cursor.execute('''
                DELETE FROM Members WHERE id = ?
            ''',(m_id))
            if cursor.rowcount == 0:
                print("Member Id not found!")
            else:
                conn.commit()
                print("Member deleted!!!")
        elif ch == "n":
            print("Member not deleted") 
        else:
            print("Invalid option! Please enter Y or N.")
    except ValueError:
                print("Member Id must be a number!")
    conn.close()

# User Registration
def registeruser():
    conn = get_connection()
    cursor = conn.cursor()
    username = input("Enter username: ").strip()
    password = input("Enter password: ").strip()
    if username == "" or password == "":
        print("Username and password cannot be empty!")
        conn.close()
        return
    # Check duplicate username
    cursor.execute('''
        SELECT * FROM Users WHERE username = ?
    ''', (username,))
    existing_user = cursor.fetchone()
    if existing_user:
        print("Username already exists!")
        conn.close()
        return

    print("Choose your user role")
    print("1. Admin")
    print("2. Staff")
    role_choice = input("Enter your choice: ").strip()

    if role_choice == "1":
        role = "Admin"
    elif role_choice == "2":
        role = "Staff"
    else:
        print("Invalid role selection!")
        conn.close()
        return
    cursor.execute('''
        INSERT INTO Users(username, password, role)
        VALUES(?,?,?)
    ''', (username, password, role))

    conn.commit()
    print("User registered successfully!")
    conn.close()

# User Login
def loginuser():
    conn = get_connection()
    cursor = conn.cursor()
    username = input("Enter username: ").strip()
    password = input("Enter password: ").strip()
    if username == "" or password == "":
        print("Username and password cannot be empty!")
        conn.close()
        return
    cursor.execute('''
        SELECT * FROM Users
        WHERE username = ? AND password = ?
    ''', (username, password))
    user = cursor.fetchone()
    if user:
        print(f"\nLogin successful! Welcome {user[1]}")
        print(f"Role: {user[3]}")
        role = user[3]
        conn.close()
        if role == "Admin":
            adminmenu()
        elif role == "Staff":
            staffmenu()
    else:
        print("Invalid username or password!")
        conn.close()


# Issue a book
def issuebook():
    conn = get_connection()
    cursor = conn.cursor()
    try:
        m_id = int(input("Enter member ID: "))
        b_id = int(input("Enter book ID: "))

        # Check member exists
        cursor.execute('''
            SELECT * FROM Members WHERE id = ?
        ''', (m_id,))

        member = cursor.fetchone()

        if not member:
            print("Member ID not found!")
            conn.close()
            return

        # Check book exists
        cursor.execute('''
            SELECT * FROM Books WHERE id = ?
        ''', (b_id,))

        book = cursor.fetchone()

        if not book:
            print("Book ID not found!")
            conn.close()
            return

        # Check book availability
        if book[5] <= 0:
            print("No copies of this book are currently available!")
            conn.close()
            return

        # Check whether same member already borrowed same book
        cursor.execute('''
            SELECT * FROM Borrowings
            WHERE member_id = ? AND book_id = ? AND status = ?
        ''', (m_id, b_id, "Issued"))

        existing_borrowing = cursor.fetchone()

        if existing_borrowing:
            print("This member has already borrowed this book!")
            conn.close()
            return

        issue_date = date.today().isoformat()

        # Add borrowing record
        cursor.execute('''
            INSERT INTO Borrowings
            (member_id, book_id, issue_date, return_date, status)
            VALUES(?,?,?,?,?)
        ''', (m_id, b_id, issue_date, None, "Issued"))

        # Reduce available copies
        cursor.execute('''
            UPDATE Books
            SET available_copies = available_copies - 1
            WHERE id = ?
        ''', (b_id,))

        conn.commit()

        print("Book issued successfully!")
        print(f"Member : {member[1]}")
        print(f"Book : {book[1]}")
        print(f"Issue Date : {issue_date}")

    except ValueError:
        print("Member ID and Book ID must be numbers!")

    conn.close()


# View all borrowing records
def viewborrowings():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute('''
        SELECT Borrowings.id,
               Members.name,
               Books.title,
               Borrowings.issue_date,
               Borrowings.return_date,
               Borrowings.status
        FROM Borrowings
        JOIN Members ON Borrowings.member_id = Members.id
        JOIN Books ON Borrowings.book_id = Books.id
    ''')

    borrowings = cursor.fetchall()

    if borrowings:
        print("----- Borrowing Details -----")

        for i in borrowings:
            print(f"Borrowing ID : {i[0]}")
            print(f"Member Name : {i[1]}")
            print(f"Book Title : {i[2]}")
            print(f"Issue Date : {i[3]}")
            print(f"Return Date : {i[4]}")
            print(f"Status : {i[5]}")
            print("-" * 20)

    else:
        print("No borrowing records found!")

    conn.close()


# Return a book
def returnbook():
    conn = get_connection()
    cursor = conn.cursor()
    try:
        br_id = int(input("Enter borrowing ID: "))
        cursor.execute('''
            SELECT * FROM Borrowings
            WHERE id = ? AND status = ?
        ''', (br_id, "Issued"))

        borrowing = cursor.fetchone()

        if not borrowing:
            print("Active borrowing record not found!")
            conn.close()
            return

        b_id = borrowing[2]
        return_date = date.today().isoformat()

        # Update borrowing record
        cursor.execute('''
            UPDATE Borrowings
            SET return_date = ?, status = ?
            WHERE id = ?
        ''', (return_date, "Returned", br_id))

        # Increase available copies
        cursor.execute('''
            UPDATE Books
            SET available_copies = available_copies + 1
            WHERE id = ?
        ''', (b_id,))

        conn.commit()

        print("Book returned successfully!")
        print(f"Return Date : {return_date}")

    except ValueError:
        print("Borrowing ID must be a number!")

    conn.close()



#Admin Menu options
def adminmenu():
    while True:
        print("----- ADMIN MENU -----")
        try:
            ch = int(input("1. Add Book\n2. View Books\n3. Search Book\n4. Update Book\n5. Delete Book\n6. Add Member\n7. View Members\n8. Search Member\n9. Update Member\n10. Delete Member\n11. Issue Book\n12. Return Book\n13. View Borrowings\n14. Logout"))
            if ch == 1:
                addbook()
            elif ch == 2:
                viewbooks()
            elif ch == 3:
                searchbook()
            elif ch == 4:
                updatebookdetails()
            elif ch == 5:
                deletebook()
            elif ch == 6:
                addmembers()
            elif ch == 7:
                viewmembers()
            elif ch == 8:
                searchmember()
            elif ch == 9:
                updatememberdetails()
            elif ch == 10:
                deletemember()
            elif ch == 11:
                issuebook()
            elif ch == 12:
                returnbook()
            elif ch == 13:
                viewborrowings()
            elif ch == 14:
                print("Logged out successfully!")
                break
            else:
                print("Invalid option!")
        except ValueError:
            print("Please enter a valid number!")
            continue

#Staff menu options
def staffmenu():
    while True:
        print("----- STAFF MENU -----")
        try:
            ch = int(input("1. View Books\n2. Search Book\n3. Add Member\n4. View Members\n5. Search Member\n6. Issue Book\n7. Return Book\n8. View Borrowings\n9. Logout"))
            if ch == 1:
                viewbooks()
            elif ch == 2:
                searchbook()
            elif ch == 3:
                addmembers()
            elif ch == 4:
                viewmembers()
            elif ch == 5:
                searchmember()
            elif ch == 6:
                issuebook()
            elif ch == 7:
                returnbook()
            elif ch == 8:
                viewborrowings()
            elif ch == 9:
                print("Logged out successfully!")
                break
            else:
                print("Invalid option!")
        except ValueError:
            print("Please enter a valid number!")
            continue

#Main function
def main():
    while True:
        print("Welcome to Library management system")
        try:
            ch = int(input("1. Register\n2. Login\n3. Exit"))
            if ch == 1:
                registeruser()
            elif ch == 2:
                loginuser()
            elif ch == 3:
                print("Thank you for using Library Management System!")
                break
            else:
                print("Invalid option!")
        except ValueError:
            print("Please enter a valid number!")
            continue

main()

