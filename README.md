# CMS
Content Management System (semester mini project)


# Content Management System (CMS)

## About the Project

This is a simple Content Management System (CMS) developed using **Python, Flask, SQLite, HTML, CSS, and JavaScript**.

The main purpose of this project is to allow users to create, manage, and share their posts through a simple web application.

Users can create an account, log in securely, create posts, and manage their content.

## Features

- **User Registration:** Users can create a new account.
- **User Login:** Registered users can log in to their accounts.
- **User Dashboard:** Users can access their personal dashboard.
- **Create Posts:** Users can create posts with a title, content, and image URL.
- **View Posts:** Users can view available posts.
- **Session Management:** Flask sessions are used to manage user login status.
- **Database Management:** SQLite is used to store user information and posts.

## Technologies Used

- **Python** – Backend programming.
- **Flask** – Web application framework.
- **SQLite** – Database management.
- **HTML** – Web page structure.
- **CSS** – Web page styling.
- **JavaScript** – Frontend functionality.

## Project Structure

```text
CMS/
│
├── app/
│   ├── database/       # Database connection and queries
│   ├── functions/      # Reusable application functions
│   ├── routes/         # Application routes and blueprints
│   ├── static/
│   │   ├── css/        # CSS files
│   │   └── script/     # JavaScript files
│   ├── templates/
│   │   ├── auth/       # Login and registration pages
│   │   ├── errors/     # Error pages
│   │   └── user/       # User dashboard and post pages
│   └── __init__.py     # Flask application factory
│
├── instance/           # Application database
├── venv/               # Python virtual environment
├── config.py           # Application configuration
├── run.py              # Application entry point
├── .env                # Environment variables
├── .gitignore          # Files ignored by Git
└── README.md           # Project documentation
```

## Installation and Setup

Follow these steps to run the project on your computer.

### 1. Clone the Repository

```bash
git clone <your-repository-url>
```

### 2. Open the Project Directory

```bash
cd CMS
```

### 3. Create a Virtual Environment

```bash
python -m venv venv
```

### 4. Activate the Virtual Environment

For Windows:

```bash
venv\Scripts\activate
```

### 5. Install Dependencies

```bash
pip install flask python-dotenv
```

### 6. Run the Application

```bash
python run.py
```

### 7. Open in Browser

Visit:

```text
http://127.0.0.1:5000/
```

## Future Improvements

Some features that I would like to add in the future:

- Edit existing posts.
- Delete posts.
- Upload images directly.
- User profile management.
- Search and filter posts.
- Like and comment functionality.
- Improve the user interface and responsiveness.

## Learning Purpose

This project is developed as a practical learning project to improve my understanding of Python, Flask, database management, backend development, and web application architecture.

---

**Developed with Python and Flask.**