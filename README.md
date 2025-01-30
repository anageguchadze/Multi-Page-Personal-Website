# Multi-Page-Personal-Website

Project Overview

This is a simple Django project with basic pages, including Home, About, Contact, and a Thank You page. The project follows the MVC pattern, utilizing Django's built-in URL routing, views, and template system.

Features:
Home Page
About Page
Contact Page with a simple form
Thank You Page after form submission

Installation
Make sure you have Python and Django installed.
pip install django
Clone the Repository
git clone https://github.com/anageguchadze/Multi-Page-Personal-Website.git
cd Multi-Page-Personal-Website

Run Migrations
python manage.py migrate
Run Development Server
python manage.py runserver
Open your browser and go to http://127.0.0.1:8000/

Project Structure:
my_project/
│── my_app/
│   ├── templates/
│   │   ├── home.html
│   │   ├── about.html
│   │   ├── contact.html
│   │   ├── thank_you.html
│   ├── views.py
│   ├── urls.py
│── my_project/
│   ├── settings.py
│   ├── urls.py
│── manage.py

Git Usage

Initialize Git Repository

git init
git add .
git commit -m "Initial commit"
git branch -M main
git remote add origin https://github.com/anageguchadze/Multi-Page-Personal-Website.git
git push -u origin main

Common Git Commands

Add changes: git add .

Commit changes: git commit -m "your message"

Push to remote: git push origin main

Pull latest changes: git pull origin main

License

This project is open-source. Modify and use it as needed.
