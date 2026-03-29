# Buyer Portal

A simple property browsing app where users can register, log in, view properties, and save their favourites.

Built with Django + Django REST Framework for the backend and plain HTML/JS for the frontend.

---

## What it does

- Register and log in as a buyer
- Browse a list of properties
- Add or remove properties from your favourites
- Your favourites are private — other users can't see them

---

## Project Structure

```
buyer_portal/
├── config/          # Django project settings and URLs
├── accounts/        # Register and login (JWT auth)
├── properties/      # Property listing
├── favourites/      # Add/remove/list favourites
├── frontend/        # Plain HTML pages (login, register, dashboard)
└── manage.py
```

---

## Setup

Make sure you have Python installed, then:

```bash
# Install dependencies
pip install -r requirements.txt

# Run migrations
python manage.py migrate

# Create an admin user (to add properties)
python manage.py createsuperuser

# Start the server
python manage.py runserver
```

---

## Adding Properties

Go to `http://127.0.0.1:8000/admin/` and log in with your superuser account. Add a few properties from there so they show up on the dashboard.

---

## Using the App

1. Open `frontend/register.html` in your browser
2. Create an account
3. You'll be redirected to `login.html` — log in
4. On the dashboard you'll see all properties
5. Click "Add to Favourites" on any property
6. Switch to the "My Favourites" tab to see your saved ones
7. Click "Remove Favourite" to remove one

---

## API Endpoints

| Method | URL | Description |
|--------|-----|-------------|
| POST | `/api/accounts/register/` | Create account |
| POST | `/api/accounts/login/` | Get JWT tokens |
| GET | `/api/properties/` | List all properties |
| GET | `/api/favourites/` | List my favourites |
| POST | `/api/favourites/add/` | Add a favourite |
| DELETE | `/api/favourites/<id>/remove/` | Remove a favourite |

All endpoints except register and login require a JWT token in the header:
```
Authorization: Bearer <access_token>
```

---

## Notes

- The frontend uses `localStorage` to store the JWT token
- SQLite is used as the database (no extra setup needed)
- `CORS_ALLOW_ALL_ORIGINS = True` is set for local development only
