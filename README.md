# TBC Django Bookstore Project

Welcome to the Django Bookstore Project! This is a simple web application built using Django framework that allows users to view book data from a virtual bookstore.

## Features

- Book JSON data: Users can view a JSON list of available books with details such as title, author, price, page count and category.
- Pre-populated database: The project comes with a database of books to view and test and with a superuser. 
- Admin panel: Admin users can add, edit, and delete books.

## Admin Panel
- Admin Credentials: **username** - admin | **password** - admin123
- Admin Users can add books, search them based on title and author, and filter them by category.

## Installation

1. Clone the repository:

```bash
git clone https://github.com/Lasha-Nikolaishvili/tbc-django-project.git
```

2. Navigate into the project directory:

```bash
cd tbc-django-project
```

3. Install dependencies:

```bash
pip install -r requirements.txt
```

4. Apply database migrations:

```bash
python manage.py migrate
```

5. Run the development server:

```bash
python manage.py runserver
```

The application should now be accessible at `http://localhost:8000`.

## Usage

- Visit `http://localhost:8000/books` in your web browser to access the bookstores list of books.
- Visit `http://localhost:8000/books/:book_id` in your web browser to access a book at a specific id.
- Admin users can access the admin panel at `http://localhost:8000/admin` to manage books, and users.