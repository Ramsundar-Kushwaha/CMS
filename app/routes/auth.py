import sqlite3
from flask import Blueprint, render_template, redirect, url_for, request, session, flash
from werkzeug.security import generate_password_hash, check_password_hash
from app.database.db import get_db


auth = Blueprint('auth', __name__)

@auth.route("/signup", methods=['GET', 'POST'])
def signup():
    if request.method == 'GET':
        return render_template("auth/signup.html")

    # Read from data
    dob = request.form.get('DOB', "").strip()
    gender = request.form.get('gender', "").strip()
    first_name = request.form.get('first-name', "").strip()
    middle_name = request.form.get('middle-name', "").strip()
    last_name = request.form.get('last-name', "").strip()
    username = request.form.get('username', "").strip()
    phone = request.form.get('phone-number', "").strip()
    email = request.form.get('email', "").strip().lower()
    password = request.form.get('pass', "")
    confirm_password = request.form.get('confirm-pass', "")

    if not all([first_name, last_name, email, username, phone, password]):
        flash("Please fill in all required fields.", "error")
        return redirect(url_for("auth.signup"))


    if not password == confirm_password:
        flash("Password mismatch.", "error")
        return redirect(url_for("auth.signup"))


    # Hash the password before storing it
    password_hash = generate_password_hash(password)

    db = get_db()

    try:
        # Both inserts succeed together or roll back together

        with db:
            cursor = db.execute(
                """
                INSERT INTO users (
                    first_name,
                    middle_name,
                    last_name,
                    email,
                    password_hash,
                    date_of_birth,
                    gender
                )
                VALUES (?, ?, ?, ?, ?, ?, ?)
                """,
                (
                    first_name,
                    middle_name,
                    last_name,
                    email,
                    password_hash,
                    dob or None,
                    gender or None
                )
            )

            user_id = cursor.lastrowid

            db.execute(
                """
                    INSERT INTO user_info (
                        user_id,
                        phone_number,
                        username
                    )
                    VALUES (?, ?, ?)
                """,
                (
                    user_id,
                    phone or None,
                    username
                )
            )

        flash("Account created successfully. Please log in.", "success")
        return redirect(url_for("auth.login"))

    except sqlite3.IntegrityError:
        flash(
            "That email, username, or phone number may already be registered.", "error"
        )

        return redirect(url_for("auth.signup"))


# login route
@auth.route('/')
@auth.route('/login', methods = ['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username', "").strip().lower()
        password = request.form.get('pass', "")

        db = get_db()

        user = db.execute(
            """
            SELECT
                u.user_id,
                u.first_name,
                u.email,
                u.password_hash,
                ui.username
            FROM users AS u JOIN user_info AS ui
                ON u.user_id = ui.user_id
            WHERE ui.username = ?
            """,
            (username,)
        ).fetchone()

        if user and check_password_hash(user['password_hash'], password):
            session.clear()
            session['user_id'] = user['user_id']
            session['username'] = user['username']

            return redirect(url_for("user.user_space"))
        
        flash("Invalid username or password.", "error")

    return render_template("auth/login.html")


# logout
@auth.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('auth.login'))