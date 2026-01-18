
# Leot Project

Leot Project is a Django web application designed to [briefly state purpose: e.g., manage contacts, track tasks, or handle inventory].  
It demonstrates backend development skills, CRUD operations, user authentication, and a GitHub-ready project structure.

---

## Features

- User authentication (signup, login, logout)  
- Admin dashboard for managing app data  
- CRUD operations for main models (Contacts, Tasks, Products)  
- Interactive forms with validation  
- Search and filter functionality  
- Mobile-friendly, responsive pages  
- SQLite database with Django ORM  
- Clean GitHub repo with `.gitignore` and `requirements.txt`

---

## Screenshots

#### Homepage
![Homepage](screenshots/homepage.png)

#### Contact / Form Page
![Contact Page](screenshots/contact.png)

#### Admin Dashboard
![Admin Dashboard](screenshots/admin.png)

---

## Setup Instructions

1. **Clone the repository**

```bash
git clone https://github.com/your-username/LeotProject.git
cd LeotProject
```

2. **Create a virtual environment**

```bash
python -m venv virt_leot
```

3. **Activate the virtual environment**

- Windows (PowerShell): `.irt_leot\Scripts\Activate.ps1`  
- Windows (Command Prompt): `.irt_leot\Scriptsctivate.bat`  
- Mac/Linux: `source virt_leot/bin/activate`

4. **Install dependencies**

```bash
pip install -r requirements.txt
```

5. **Apply migrations**

```bash
python manage.py makemigrations
python manage.py migrate
```

6. **Run the server**

```bash
python manage.py runserver
```

7. Open your browser at `http://127.0.0.1:8000/`

---

## Technologies Used

- Python 3.x  
- Django 4.x  
- SQLite  
- HTML, CSS  
- Git & GitHub

---

## Author

**Emeka Dennis**  
[GitHub](https://github.com/your-username)  
your.email@example.com
