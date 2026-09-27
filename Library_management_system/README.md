# Library Management System

A command-line Library Management System developed in Python using SQLite.

## Project Overview

This project manages books, members, users, and borrowing records in a library. It provides user registration and login with Admin and Staff roles, along with functions for adding, viewing, searching, updating, issuing, returning, and tracking library records.

The project demonstrates Python functions, loops, conditional statements, input validation, exception handling, SQLite database operations, and basic role-based menus.

## Features Implemented

- SQLite database creation
- User registration and login
- Admin and Staff roles
- Add, view, search, update, and delete books
- Add, view, search, update, and delete members
- Duplicate book checking
- Duplicate member email checking
- Duplicate username checking
- Issue books to members
- Return issued books
- Track issue date and return date
- Maintain available and total book copies
- Prevent issuing unavailable books
- Prevent the same member from borrowing the same book twice while it is already issued
- View borrowing records
- Basic input validation and exception handling

## Database Tables

The program automatically creates the following SQLite tables when it starts:

### Users

Stores:

- User ID
- Username
- Password
- Role

### Books

Stores:

- Book ID
- Title
- Author name
- Category
- Total copies
- Available copies

### Members

Stores:

- Member ID
- Name
- Phone number
- Email ID

### Borrowings

Stores:

- Borrowing ID
- Member ID
- Book ID
- Issue date
- Return date
- Status

The Borrowings table uses foreign keys connected to the Members and Books tables.

## Project Files

```text
Library_Management_System/
|
|-- library_mgmt_system.py
|-- librarymgmt.db
|-- README.md
```

`librarymgmt.db` is created automatically when the program is run for the first time.

## Requirements

- Python 3.x
- No external Python packages are required

The project uses Python standard-library modules:

```python
import sqlite3
from datetime import date
```

## How to Run

1. Keep `library_mgmt_system.py` in the project folder.
2. Open Command Prompt or Terminal inside the folder.
3. Run:

```bash
py library_mgmt_system.py
```

You can also use:

```bash
python library_mgmt_system.py
```

if `python` is configured on your system.

## Main Menu

When the program starts, the following options are available:

```text
1. Register
2. Login
3. Exit
```

A new user must register before logging in.

During registration, the user can choose either:

```text
1. Admin
2. Staff
```

## Admin Functions

An Admin can:

- Add Book
- View Books
- Search Book
- Update Book
- Delete Book
- Add Member
- View Members
- Search Member
- Update Member
- Delete Member
- Issue Book
- Return Book
- View Borrowings
- Logout

## Staff Functions

A Staff user can:

- View Books
- Search Book
- Add Member
- View Members
- Search Member
- Issue Book
- Return Book
- View Borrowings
- Logout

## Book Issue Process

To issue a book, the program:

1. Checks whether the Member ID exists.
2. Checks whether the Book ID exists.
3. Checks whether a copy is available.
4. Checks whether the same member already has the same book issued.
5. Creates a borrowing record.
6. Stores the current date as the issue date.
7. Reduces the available book count by one.

## Book Return Process

To return a book, the program:

1. Checks for an active borrowing record.
2. Stores the current date as the return date.
3. Changes the borrowing status from `Issued` to `Returned`.
4. Increases the available book count by one.

## Input Validation

The program includes validation for:

- Empty book details
- Empty member details
- Empty username or password
- Duplicate usernames
- Duplicate member email IDs
- Duplicate books
- Invalid numeric IDs
- Invalid menu options
- Invalid number of book copies
- Unavailable books
- Missing members or books
- Duplicate active borrowing records

## Notes

- The database file is stored locally as `librarymgmt.db`.
- Foreign key support is enabled when database connections are opened through `get_connection()`.
- This project is designed as a command-line educational application.
- User passwords are stored as entered in the local database; password hashing is not implemented in this version.

## Author

Python Project  
Library Management System
