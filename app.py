from flask import Flask, render_template, redirect, request, url_for
from flask_login import LoginManager
from flask_mail import Mail, Message
from .models import db, User, Profile
from .routes import auth_bp, profile_bp
import os
from dotenv import load_dotenv
from flask_tailwind import Tailwind
import boto3


app = Flask(__name__, static_folder='static')
tailwind = Tailwind(app)

# Load the .env file
load_dotenv()
# Database setup
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['MAIL_SERVER'] = os.getenv('MAIL_SERVER')
app.config['MAIL_PORT'] = int(os.getenv('MAIL_PORT'))
app.config['MAIL_USE_TLS'] = os.getenv('MAIL_USE_TLS') == 'True'
app.config['MAIL_USERNAME'] = os.getenv('MAIL_USERNAME')
app.config['MAIL_PASSWORD'] = os.getenv('MAIL_PASSWORD')
app.config['MAIL_DEFAULT_SENDER'] = os.getenv('MAIL_DEFAULT_SENDER')

# Retrieve S3 configuration from environment variables
app.config['AWS_ACCESS_KEY_ID'] = os.getenv('AWS_ACCESS_KEY_ID')
app.config['AWS_SECRET_ACCESS_KEY'] = os.getenv('AWS_SECRET_ACCESS_KEY')
app.config['S3_BUCKET_NAME'] = os.getenv('S3_BUCKET_NAME')
app.config['S3_REGION'] = os.getenv('S3_REGION')

# Initialize the boto3 client with your S3 configuration
app.s3_client = boto3.client(
    's3',
    aws_access_key_id=app.config['AWS_ACCESS_KEY_ID'],
    aws_secret_access_key=app.config['AWS_SECRET_ACCESS_KEY'],
    region_name=app.config['S3_REGION']
)

mail = Mail(app)

db.init_app(app)


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


@app.route('/submit_form', methods=['POST'])
def submit_form():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        message = request.form['message']

        # Prepare the email message
        subject = f"New contact form submission from {name}"
        body = f"Name: {name}\nEmail: {email}\nMessage: {message}"

        # Using MAIL_DEFAULT_SENDER for simplicity, assuming it's defined in your .env
        recipient = os.getenv('MAIL_DEFAULT_SENDER')
        msg = Message(subject, recipients=[recipient], body=body)
        mail.send(msg)

        return redirect(url_for('thank_you'))


@app.route('/thank_you')
def thank_you():
    return render_template('thank_you.html')


@app.route('/login')
def login():
    return redirect('login')


@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/legal')
def legal():
    return render_template('legal.html')


if __name__ == '__main__':
    app.run(debug=False)
