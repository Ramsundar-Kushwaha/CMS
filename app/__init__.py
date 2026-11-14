import os
from dotenv import load_dotenv
from flask import Flask, redirect, url_for

# Load variables from the project's .env file
load_dotenv()

def create_app():
    app = Flask(
        __name__,
        template_folder='templates',
        static_folder='static',
        instance_relative_config=True
    )

    secret_key = os.getenv('SECRET_KEY')
    if not secret_key:
        raise RuntimeError('SECRET_KEY is missing. Check your .env file.')

    app.config['SECRET_KEY'] = secret_key

    # Create the instances directory if it doesn't exist
    os.makedirs(app.instance_path, exist_ok=True)

    # SQLite database location
    app.config["DATABASE"] = os.path.join(
        app.instance_path, "cms.db"
    )

    # Initialize database connection management
    from app.database.db import init_app as init_db_app
    from app.database.db import init_db

    init_db_app(app)

    # Register existing blueprits
    from app.routes.auth import auth
    from app.routes.user import user
    from app.routes.connection import connection
    from app.routes.post import post


    app.register_blueprint(auth, url_prefix='/auth')
    app.register_blueprint(user, url_prefix='/user')
    app.register_blueprint(connection, url_prefix='/connection')
    app.register_blueprint(post, url_prefix='/post')


    # Redirect to auth urls
    @app.route('/')
    @app.route('/login')
    def login_redirect():
        return redirect(url_for('auth.login'))
    
    @app.route('/signup')
    def signup_redirect():
        return redirect(url_for('auth.signup'))


    @app.route('/logout')
    def logout_redirect():
        return redirect(url_for('auth.logout'))

    # Redirect to user urls
    @app.route('/dashboard')
    def dashboard_redirect():
        return redirect(url_for('user.dashboard'))

    @app.route('/user-space')
    def user_space_redirect():
        return redirect(url_for('user.user_space'))
    
    # Create tables if they don't exist
    with app.app_context():
        init_db()

    return app