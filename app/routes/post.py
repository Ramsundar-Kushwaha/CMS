import sqlite3
from flask import Blueprint, render_template, redirect, url_for, session, request, flash
from app.database.db import get_db


post = Blueprint('post', __name__)


@post.route('/create-post', methods=['GET', 'POST'])
def create_post():

    # Check authentication
    if 'user_id' not in session:
        return redirect(url_for('auth.login'))

    if request.method == 'POST':

        # Get form data
        title = request.form.get('title', '').strip()
        content = request.form.get('content', '').strip()
        img = request.form.get('img', '').strip()

        # Get logged-in user's ID
        user_id = session['user_id']

        # Validate input
        if not all([title, content, img]):
            flash("All feilds are required", "error")
            return redirect(url_for('post.create_post'))

        db = get_db()

        try:
            db.execute(
                """
                INSERT INTO posts (
                    user_id,
                    post_title,
                    post_content,
                    post_image
                )
                VALUES (?, ?, ?, ?)
                """,
                (user_id, title, content, img)
            )

            db.commit()

            flash("Post created successfully!", "success")
            return redirect(url_for('post.create_post'))


        except sqlite3.Error:
            db.rollback()
            flash("Something went wrong while creating your post.", "error")
            return redirect(url_for('post.create_post'))
    
    return render_template('user/create-post.html')

@post.route('/delete-post')
def delete_post():
    if 'username' not in session:
        return redirect(url_for('auth.login'))
    
    return "delete post"

@post.route('/update-post')
def update_post():
    if 'username' not in session:
        return redirect(url_for('auth.login'))

    return render_template('user/update-post.html')
    
    return "update post"

@post.route('/view-post')
def view_post():
    if 'username' not in session:
        return redirect(url_for('auth.login'))
    
    return "view post"