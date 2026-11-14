from flask import Blueprint, render_template, redirect, url_for, session


connection = Blueprint('connection', __name__)


# contact route
@connection.route('/connections')
def connections():
    if 'username' not in session:
        return redirect(url_for('auth.login'))
    
    return "your connections"