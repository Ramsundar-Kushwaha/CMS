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
    

@post.route('/delete-post/<int:post_id>', methods=['POST'])
def remove_post(post_id):
    if 'username' not in session:
        return redirect(url_for('auth.login'))


    if request.method == 'POST':
        query = """
        DELETE FROM posts
        WHERE post_id = ? AND user_id = ?"""

        post_id = post_id

        try:
            db = get_db()

            db.execute(query, (post_id, session['user_id']))

            db.commit()

            db.close()

            return redirect(url_for('user.dashboard'))
        
        except sqlite3.Error as e:
            print('Database error while delete in post method!', e)
            return render_template('errors/500.html')


@post.route('/update-post')
def update_post():
    if 'username' not in session:
        return redirect(url_for('auth.login'))

    return render_template('user/update-post.html')