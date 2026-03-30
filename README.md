🏠 Buyer Portal – Property Listing & Favourites System

📌 Overview

This project is a Django-based web application developed as part of a take-home assessment.

It implements a buyer portal where users can register, log in, browse property listings, and manage their favourite properties. The primary focus is on backend architecture, authentication, and user-specific data handling.

---

🚀 Live Application

👉 https://home-assessment.onrender.com

---

📂 GitHub Repository

👉 https://github.com/Sujitapatel11/home-assessment

---

🔗 LinkedIn

👉 https://www.linkedin.com/in/suji57

---

🛠️ Tech Stack

- Backend: Django (Python)
- Frontend: HTML, CSS (Django Templates)
- Database: SQLite
- Deployment: Render (Gunicorn)
- Version Control: Git & GitHub

---

✨ Features

🔐 Authentication

- User registration and login
- Secure password handling using Django authentication system

🏡 Property Listings

- View available properties
- Each property includes:
  - Title
  - Description
  - Price
  - Location

❤️ Favourites System

- Add properties to favourites
- Remove properties from favourites
- Each user can only access their own favourites

🧑‍💼 Admin Panel

- Manage users, properties, and favourites
- Add/update/delete property listings via Django admin

---

🧠 Core Concepts Implemented

- RESTful backend structure using Django
- User-specific data isolation
- Secure authentication flow
- Relational data modeling (User ↔ Property ↔ Favourite)
- Deployment using Gunicorn on Render

---

⚙️ Project Structure

home-assessment/
│
├── accounts/        # User authentication
├── properties/      # Property models & logic
├── favourites/      # Favourite functionality
├── config/          # Django settings & WSGI
├── templates/       # Frontend templates
│
├── manage.py
├── requirements.txt
└── README.md

---

⚙️ Setup Instructions (Local Development)

1. Clone the repository

git clone https://github.com/Sujitapatel11/home-assessment.git
cd home-assessment

2. Create virtual environment

python -m venv venv
venv\Scripts\activate   # Windows

3. Install dependencies

pip install -r requirements.txt

4. Apply migrations

python manage.py migrate

5. Run the server

python manage.py runserver

---

🔑 Admin Access

To access the admin panel:

/admin

Create a superuser locally:

python manage.py createsuperuser

👉 Admin credentials are not shared publicly for security reasons.

---

🌐 Deployment Details

- Deployed on Render
- Uses Gunicorn as WSGI server
- Environment variables used for secure configuration
- Free-tier deployment (may take a few seconds to wake up)

---

📌 Key Highlights

- Clean and modular Django project structure
- Functional CRUD operations
- Secure authentication system
- Proper user-level data access control
- End-to-end deployment

---

⚠️ Notes

- SQLite is used for simplicity (not production-grade)
- UI is intentionally minimal (focus on backend logic)
- Static/media handling can be extended for production use

---

👨‍💻 Author

Sujita Patel
CSE Student | Backend Developer

🔗 LinkedIn: https://www.linkedin.com/in/suji57