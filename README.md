# Agency Flask Application

The Agency Flask Application is a robust web platform built with Flask, designed to manage user registrations, logins, and profile updates. It integrates a secure file upload system, allowing users to upload and manage resumes seamlessly. Leveraging Flask's flexibility and the power of SQLAlchemy, this application offers a solid foundation for any agency's personnel management needs.

## Features

- **User Authentication**: Secure login and registration system to manage user access.
- **Profile Management**: Users can update personal information and manage their profiles.
- **Resume Upload**: Secure upload feature for resumes, supporting PDF and DOCX formats, tied directly to the user's profile.
- **Database Integration**: Utilizes SQLAlchemy with a SQLite database for efficient data handling and storage.
- **Security**: Implements Flask-Bcrypt for password hashing, ensuring user credentials are securely managed.

## Technologies Used

- Flask
- SQLAlchemy
- Flask-Migrate for database migrations
- Flask-Login for managing user sessions
- Flask-WTF for form handling and CSRF protection
- Flask-Bcrypt for hashing and checking passwords securely

## Database Models

The `models.py` file defines the SQLAlchemy ORM models that serve as the foundation for the application's database. It includes two main models: `User` and `Profile`.

### User Model

The `User` model handles user information and authentication. It includes the following fields:

- `id`: The primary key for the user.
- `username`: A unique username for the user, required for login and identification.
- `email`: A unique email address for the user, required for login and identification.
- `password_hash`: A hashed password for secure authentication.
- `role`: A role assigned to the user to manage permissions within the application.

### Profile Model

The `Profile` model manages additional user details, allowing users to enrich their profiles with personal information and preferences. It includes fields such as:

- `id`: The primary key for the profile.
- `email`: A unique email address linked to the user's profile.
- `resume_filename`: The name of the uploaded resume file, if any.
- `address`, `city`, `state`, `zip_code`: Optional fields for the user's address.
- `phone`: An optional field for the user's phone number.
- `schedule_monday` to `schedule_sunday`: Boolean fields indicating availability for each day of the week.
- `start_date`, `end_date`: Optional fields indicating the preferred time range for activities or work.

These models are essential for the application's functionality, allowing for efficient data handling and storage. The use of Flask-SQLAlchemy simplifies database operations, making it straightforward to perform CRUD operations on these models.

Some images of the Agency Flask Web Application in Desktop and Mobile: Profile, Registration

![Img](https://github.com/Xthe23/flask-agency/blob/main/Resources/img1.png)
![Img](https://github.com/Xthe23/flask-agency/blob/main/Resources/img2.png)
![Img](https://github.com/Xthe23/flask-agency/blob/main/Resources/img3.png)
![Img](https://github.com/Xthe23/flask-agency/blob/main/Resources/img4.png)
![Img](https://github.com/Xthe23/flask-agency/blob/main/Resources/img6.png)

Leveraging Jinja tags, I implemented conditional logic to display the resume upload feature exclusively for users identified as either Workers or Clients on the profile route.
