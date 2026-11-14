import sqlite3
from functools import wraps
from flask import Blueprint, render_template, redirect, url_for, session, flash
from app.database.db import get_db

user = Blueprint('user', __name__)

# Reusable login protection
def login_required(view):
    @wraps(view)
    def wrapped_view(*args, **kwargs):
        if 'user_id' not in session:
            flash("Please log in to continue.", "error")
            return redirect(url_for('auth.login'))

        return view(*args, **kwargs)
    
    return wrapped_view

        
# dashboard route
@user.route('/dashboard')
@login_required
def dashboard():
    return render_template('user/user-dashboard.html')




@user.route('/user-space')
@login_required
def user_space():
   
    db = get_db()
   
    try:
        posts = db.execute(
            """
            SELECT
                p.post_id,
                p.user_id,
                p.post_title,
                p.post_content,
                p.post_image,
                p.created_at,
                ui.username
            FROM posts AS p
            LEFT JOIN user_info AS ui
            ON p.user_id = ui.user_id
            ORDER BY p.created_at DESC
            """
        ).fetchall()
   
        # posts = db.execute(
        #     """
        #     SELECT * FROM posts
        #     ORDER BY created_at DESC
        #     """
        # ).fetchall()
   
        print("Number of posts:", len(posts))
        print("Post records:", [dict(p) for p in posts])
   
        flash('Welecome User', 'success')
        return render_template('user/user-space.html', posts = posts)
       
    except sqlite3.Error:
        flash("Something went wrong!", "error")
        return redirect(url_for('auth.login'))