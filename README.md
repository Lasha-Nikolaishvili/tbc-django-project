# TBC Django Bookstore Project

Welcome to the Django Bookstore Project! This is a simple web application built using the Django framework that allows users to view book and author data from a virtual bookstore.

## Features

- Books listing: Users can view a paginated list of available books with details such as title, author, price, page count, and category.
- Author JSON data: Users can view a JSON list of book authors with details such as first_name, last_name, nationality, and age.
- Pre-populated database: The project comes with a database of books and authors to view and test with a superuser. 
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

- Visit `http://localhost:8000/books` in your web browser to access the bookstore's list of books.
- Visit `http://localhost:8000/books/:book_id` in your web browser to access a book at a specific id.
- Visit `http://localhost:8000/authors` in your web browser to access the bookstore's list of authors.
- Visit `http://localhost:8000/authors/:author_id` in your web browser to access an author at a specific ID along with their book listings.
- Admin users can access the admin panel at `http://localhost:8000/admin` to manage books and users.
