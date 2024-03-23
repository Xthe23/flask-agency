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
