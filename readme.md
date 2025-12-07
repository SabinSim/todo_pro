

### 📄 README.md (Copy & Paste)


# Todo Pro - Authentication Based Task Management System

![Python](https://img.shields.io/badge/Python-3.9-blue?style=for-the-badge&logo=python&logoColor=white)
![Flask](https://img.shields.io/badge/Flask-2.3-lightgrey?style=for-the-badge&logo=flask&logoColor=white)
![Bootstrap](https://img.shields.io/badge/Bootstrap-5-purple?style=for-the-badge&logo=bootstrap&logoColor=white)
![SQLite](https://img.shields.io/badge/SQLite-Data-003B57?style=for-the-badge&logo=sqlite&logoColor=white)

**Todo Pro** is not just another todo list. It is a fully functional, authentication-based task management system built with **Python Flask**. 

This project demonstrates a robust backend architecture using **Blueprints** and the **Service Layer Pattern** to ensure scalability, maintainability, and clean code principles (Separation of Concerns).

---

## 🚀 Live Demo
You can view the live deployed application here:
**[Link to your Render App](https://sabin-todo-pro.onrender.com)** *(Note: Hosted on Render Free Tier. Initial loading may take up to 30-50 seconds due to cold start.)*

---

## 🔑 Key Features

### 1. User Authentication (Security)
- **Secure Sign-up & Login:** Password hashing using `werkzeug.security`.
- **Session Management:** Flask-Session based user persistence.
- **Authorization:** Route protection (decorators) ensuring users can only access their own data.

### 2. Task Management (CRUD)
- **Create:** Add tasks with priority, category, and deadlines.
- **Read:** View tasks with visual indicators for overdue or high-priority items.
- **Update:** Edit task details or toggle completion status.
- **Delete:** Remove tasks with confirmation safeguards.

### 3. Data Visualization
- **Dashboard:** Provides statistics on completed vs. pending tasks.
- **Categorization:** Visual breakdown of tasks by category.

### 4. UI/UX
- **Responsive Design:** Built with **Bootstrap 5** for mobile and desktop.
- **Interactive Feedback:** Flash messages for actions (success, error, warnings).
- **Consistent Theme:** Custom Indigo-Purple branding with card-based layout.

---

## 🏗️ System Architecture

This project moves away from the monolithic `app.py` structure often seen in tutorials. Instead, it adopts a modular architecture suitable for scalable applications.

### Folder Structure
```text
TODO_PRO/
├── app.py                  # Application Factory & Entry Point
├── config.py               # Configuration (Dev/Prod split)
├── init_db.py              # Database Initialization Logic
├── todo_pro.db             # SQLite Database
│
├── auth/                   # [Module] Authentication
│   ├── routes.py           # Controller (Handles HTTP Requests)
│   ├── services.py         # Service Layer (Business Logic & DB interactions)
│   └── templates/          # Views (Login/Signup Forms)
│
├── todo/                   # [Module] Task Management
│   ├── models.py           # DB Connection Handler
│   ├── routes.py           # Controller
│   ├── services.py         # Service Layer (CRUD Logic)
│   └── templates/          # Views (Index, Edit, Stats)
│
└── templates/              # Shared Layouts
    └── layout/
        └── base.html       # Base Template with Navbar & Footer
````

### Design Pattern: Service Layer

I implemented a **Service Layer** (`services.py`) to separate business logic from the route handlers (`routes.py`).

  - **Routes:** Only handle HTTP requests, input validation, and rendering templates.
  - **Services:** Handle database queries, calculations, and core logic.
  - **Benefit:** This makes the code reusable, easier to test, and highly maintainable.

-----

## 🛠️ Tech Stack

  - **Backend:** Python, Flask (Blueprints)
  - **Database:** SQLite (Relational DB)
  - **Frontend:** Jinja2 Templates, Bootstrap 5, Custom CSS
  - **Deployment:** Render (Cloud), Gunicorn (WSGI Server)
  - **Version Control:** Git, GitHub

-----

## 💻 How to Run Locally

### 1\. Clone the repository

```bash
git clone [https://github.com/SabinSim/todo-pro.git](https://github.com/SabinSim/todo-pro.git)
cd todo-pro
```

### 2\. Create a Virtual Environment

```bash
# macOS/Linux
python3 -m venv venv
source venv/bin/activate

# Windows
python -m venv venv
venv\Scripts\activate
```

### 3\. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4\. Run the Application

```bash
python app.py
```

Visit `http://127.0.0.1:5000` in your browser.

-----

## 📈 Future Improvements

  - [ ] Migrate database from SQLite to **PostgreSQL** for production.
  - [ ] Add **Unit Tests** (pytest) for critical service functions.
  - [ ] Build a **RESTful API** endpoint for mobile integration.
  - [ ] Add email notifications for approaching deadlines.

-----

## 👨‍💻 Author

**Sabin Sim** *Aspiring Backend Engineer based in Switzerland.* Passionate about building clean, scalable web applications and mastering software architecture.

-----

