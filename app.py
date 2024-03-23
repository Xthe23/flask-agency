from flask import Flask, render_template, redirect
from flask_login import LoginManager
from .models import db, User, Profile
from .routes import auth_bp, profile_bp
import os
from dotenv import load_dotenv


app = Flask(__name__, static_folder='static')
# Load the .env file
load_dotenv()
# Database setup
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


db.init_app(app)


print(app.config['SQLALCHEMY_DATABASE_URI'])

# # This is where you would create the database tables
# Only run once when creating tables..
# with app.app_context():
#     db.create_all()


# # Login manager setup
login_manager = LoginManager()
login_manager.login_view = 'auth.login'
login_manager.init_app(app)


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


# Register blueprints
app.register_blueprint(auth_bp)
app.register_blueprint(profile_bp)


@app.route('/')
def main_page():
    return render_template('homepage.html')


@app.route('/login')
def login():
    return redirect('login')


if __name__ == '__main__':
    app.run(debug=True)
