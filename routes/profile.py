from flask import Blueprint, render_template, redirect, url_for, flash, request
from flask_login import login_required, current_user
from werkzeug.datastructures import FileStorage
from werkzeug.utils import secure_filename
import os
from project.models import db, Profile
from project.forms import UploadForm
from flask import current_app
from flask import session

profile_bp = Blueprint('profile', __name__)


def validate_file(file, username):
    """
    Validates the uploaded file based on its type and size.

    Args:
        file (FileStorage): The uploaded file object.
        username (str): The username of the user uploading the file.

    Returns:
        str: The generated secure filename for the uploaded file.

    Raises:
        ValueError: If the file type is not allowed or if the file size exceeds the limit.
    """
    allowed_file_types = {'pdf', 'docx'}
    file_ext = file.filename.rsplit('.', 1)[1].lower()
    if file_ext not in allowed_file_types:
        raise ValueError(
            'File type not allowed. Please upload a PDF or DOCX file.')

    # Validate file size
    if file.content_length > 5 * 1024 * 1024:  # 5 MB limit
        raise ValueError(
            'File size exceeds 5MB. Please upload a smaller file.')

    # Generate a secure filename that is unique to the user but consistent for their uploads
    secure_filename_base = secure_filename(username)
    object_name = f"{secure_filename_base}_resume.{file_ext}"

    return object_name


# def save_resume(resume_file, username):
#     """
#     Save the resume file uploaded by the user LOCALLY. Great for development and testing.

#     Parameters:
#     - resume_file (FileStorage): The resume file to be saved.
#     - username (str): The username of the user.

#     Returns:
#     - str: The filename of the saved resume.

#     Raises:
#     - ValueError: If the file type is not allowed or if the file size exceeds the limit.
#     """
#     allowed_file_types = {'pdf', 'docx'}
#     file_ext = resume_file.filename.rsplit('.', 1)[1].lower()
#     if file_ext not in allowed_file_types:
#         raise ValueError(
#             'File type not allowed. Please upload a PDF or DOCX file.')

#     if resume_file.content_length > 5 * 1024 * 1024:  # 5 MB limit
#         raise ValueError(
#             'File size exceeds 5MB. Please upload a smaller file.')

#     # Generate a secure filename that is unique to the user but consistent for their uploads
#     secure_filename_base = secure_filename(username)
#     resume_filename = f"{secure_filename_base}_resume.{file_ext}"
#     file_path = os.path.join('uploads', resume_filename)

#     # Save the file
#     resume_file.save(file_path)
#     return resume_filename


@profile_bp.route('/profile', methods=['GET', 'POST'])
@login_required
def profile():
    """
    View function for the profile page.

    This function handles GET and POST requests to the '/profile' route. It allows users to view and update their profile information.

    Returns:
        If the request method is GET:
            A rendered template 'profile.html' with the profile form and existing profile data.
        If the request method is POST:
            - If the form data is valid and the profile is successfully updated:
                A flash message indicating the successful update and a redirect to the profile page.
            - If there are errors during the update process:
                A flash message indicating the error and a redirect to the profile page.
    """
    form = UploadForm()
    existing_profile = Profile.query.filter_by(
        email=current_user.email).first()
    if form.validate_on_submit():
        try:
            # Process file upload if a file was provided
            resume_filename = None
            if form.resume.data:
                resume_filename = form.resume.data.filename
                file = form.resume.data
                if isinstance(file, FileStorage):
                    # Validate the file and get the object name
                    object_name = validate_file(
                        file, current_user.username)
                    # Save the file to S3 bucket. Configured in app.py.
                    current_app.s3_client.upload_fileobj(
                        file, current_app.config['S3_BUCKET_NAME'], object_name)

            if not existing_profile:
                # Create a new profile if it doesn't exist
                existing_profile = Profile(
                    email=current_user.email,
                    resume_filename=resume_filename,  # Use the variable storing the processed filename
                    address=form.address.data,
                    city=form.city.data,
                    state=form.state.data,
                    zip_code=form.zip_code.data,
                    phone=form.phone.data,
                    schedule_monday=form.schedule_monday.data,
                    schedule_tuesday=form.schedule_tuesday.data,
                    schedule_wednesday=form.schedule_wednesday.data,
                    schedule_thursday=form.schedule_thursday.data,
                    schedule_friday=form.schedule_friday.data,
                    schedule_saturday=form.schedule_saturday.data,
                    schedule_sunday=form.schedule_sunday.data,
                    start_date=form.start_date.data,
                    end_date=form.end_date.data
                )
                db.session.add(existing_profile)

            # Update the profile information
            if resume_filename:
                existing_profile.resume_filename = resume_filename
            existing_profile.address = form.address.data
            existing_profile.city = form.city.data
            existing_profile.state = form.state.data
            existing_profile.zip_code = form.zip_code.data
            existing_profile.phone = form.phone.data
            existing_profile.schedule_monday = form.schedule_monday.data
            existing_profile.schedule_tuesday = form.schedule_tuesday.data
            existing_profile.schedule_wednesday = form.schedule_wednesday.data
            existing_profile.schedule_thursday = form.schedule_thursday.data
            existing_profile.schedule_friday = form.schedule_friday.data
            existing_profile.schedule_saturday = form.schedule_saturday.data
            existing_profile.schedule_sunday = form.schedule_sunday.data
            existing_profile.start_date = form.start_date.data
            existing_profile.end_date = form.end_date.data

            db.session.commit()
            flash('Profile updated successfully!', 'success')
        except ValueError as e:
            # Handle errors from save_resume (e.g., invalid file type or size)
            flash(str(e), 'danger')

        return redirect(url_for('profile.profile'))

    return render_template('profile.html', form=form, existing_profile=existing_profile)
