from flask import Blueprint, render_template, redirect, url_for, flash
from flask_login import login_user, logout_user, login_required, current_user
from werkzeug.security import generate_password_hash, check_password_hash
from ..models import db, User
from ..forms import RegistrationForm, LoginForm
from flask import session

auth_bp = Blueprint('auth', __name__)


@auth_bp.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    print(form.data)
    if form.validate_on_submit():
        # Check if email already exists in the database
        email = User.query.filter_by(email=form.email.data.lower()).first()
        username = User.query.filter_by(username=form.username.data).first()
        if email:
            flash(
                'Email already in use. Please use a different email address or log in.', 'danger')
            return redirect(url_for('auth.register'))
        elif username:
            flash(
                'Username already in use. Please choose a different username or log in.', 'danger')
            return redirect(url_for('auth.register'))
        # Proceed with creating a new user if email is not in use
        hashed_password = generate_password_hash(form.password.data)
        user = User(
            username=form.username.data,
            email=form.email.data.lower(),
            password_hash=hashed_password,
            role=form.role.data
        )
        db.session.add(user)
        try:
            db.session.commit()
            flash('Account created successfully!', 'success')
            return redirect(url_for('auth.login'))
        except Exception as e:
            db.session.rollback()
            flash('An error occurred. Please try again.', 'danger')
    return render_template('register.html', form=form)


@auth_bp.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('profile.profile'))

    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data.lower()).first()
        if user and check_password_hash(user.password_hash, form.password.data):
            login_user(user)
            flash('Login successful!', 'success')
            return redirect(url_for('profile.profile'))
        else:
            flash('Invalid username or password. Please try again.', 'danger')
    return render_template('login.html', form=form)


@auth_bp.route('/logout')
@login_required
def logout():
    # Clear the presigned_url from the session
    session.pop('presigned_url', None)
    logout_user()
    flash('You have been logged out.', 'success')
    return redirect(url_for('auth.login'))
