# Agency Flask Application

The Agency Flask Application is a robust web platform built with Flask, designed to manage user registrations, logins, and profile updates. It integrates a secure file upload system, allowing users to upload and manage resumes seamlessly. Leveraging Flask's flexibility and the power of SQLAlchemy, this application offers a solid foundation for any agency's personnel management needs. Targeted at recruitment agencies, HR departments, and freelancers, this application simplifies the process of managing candidate profiles and job applications, making it an ideal solution for small to medium-sized enterprises (SMEs) looking to streamline their hiring process.

## Features

- **User Authentication**: A secure login and registration system that leverages Flask and werkzeug's advanced Web Server Gateway Interface (WSGI) to ensures high standards of security while facilitating the creation and management of user sessions with ease.
- **Profile Management**: Users can update personal information, add a resume (docx or pdf with a 5mb limit), and update their schedule.
- **Resume Upload**: Secure upload feature for resumes, supporting PDF and DOCX formats, tied directly to the user's profile.
- **Scalable Database Architecture**: Utilizes the robustness of SQLAlchemy with the versatility of Amazon RDS, providing seamless scaling capabilities and reliable data storage and retrieval mechanisms.
- **Enhanced Security Measures**: Employs werkzeug for password hashing and also integrates comprehensive CSRF protection for all forms, ensuring that user credentials and data are managed with utmost security.

## Environment Configuration Guide

To ensure proper configuration of the project environment, it's essential to set up the .env file correctly. This file will store all sensitive and configuration-specific information, including database connections, mail server details, and AWS credentials. Please follow the instructions below to configure your .env file. **Note: For security reasons, it's crucial to keep your .env file out of version control. Ensure that .env is listed in your .gitignore file to prevent accidental upload of sensitive information to your Git repository. This practice helps in safeguarding your application's security credentials.**

### Database Configuration
Set up your database connection by specifying the following environment variables:

- SECRET_KEY: This is your application's secret key, used for cryptographic components.
- DATABASE_URL: The full URL to your database.

Example:

```shell
SECRET_KEY=your-database-secret-key-here
DATABASE_URL=your-database-url-here
```

### Mail Server Configuration

Configure your mail server settings with these variables:

- MAIL_SERVER: The SMTP server address for your email service.
- MAIL_PORT: The port your SMTP server uses for sending email.
- MAIL_USE_TLS: Specifies whether to use TLS. Set to true or false.
- MAIL_USERNAME: Your email account username. This may be the same as MAIL_DEFAULT_SENDER.
- MAIL_PASSWORD: The password for your email account.
- MAIL_DEFAULT_SENDER: The default sender email address. Typically, this is a support email tied to your website's domain.

Example:

```shell
MAIL_SERVER=your-mail-smtp-server-here
MAIL_PORT=your-mail-port-here
MAIL_USE_TLS=your-tls-boolean-here
MAIL_USERNAME=your-email-alias-here
MAIL_PASSWORD=your-password-to-default-sender-here
MAIL_DEFAULT_SENDER=your-default-sender-here
```

### AWS Configuration

For AWS services, define the following:

- AWS_ACCESS_KEY_ID: Your access key for AWS services.
- AWS_SECRET_ACCESS_KEY: Your secret access key for AWS services.

Example:

```shell
AWS_ACCESS_KEY_ID=your-access-key-here
AWS_SECRET_ACCESS_KEY=your-secret-access-key-here
```

### Amazon S3 Storage Configuration

If you're using S3 for storage, specify these variables:

- S3_BUCKET_NAME: The name of your S3 bucket.
- S3_REGION: The region your S3 bucket is located in.

Example:

```shell
S3_BUCKET_NAME="your-bucket-name-here"
S3_REGION=your-bucket-region-here
```

If configured properly, your .env should look as follows:

```shell
SECRET_KEY=your-database-secret-key-here
DATABASE_URL=your-database-url-here
MAIL_SERVER=your-mail-smtp-server-here
MAIL_PORT=your-mail-port-here
MAIL_USE_TLS=your-tls-boolean-here
MAIL_USERNAME=your-email-alias-here
MAIL_PASSWORD=your-password-to-default-sender-here
MAIL_DEFAULT_SENDER=your-default-sender-here
AWS_ACCESS_KEY_ID=your-access-key-here
AWS_SECRET_ACCESS_KEY=your-secret-access-key-here
S3_BUCKET_NAME="your-bucket-name-here"
S3_REGION=your-bucket-region-here
# Just replace the example content with your actual `.env` configuration instructions as needed.
```

## Database Models

The `models.py` file defines the SQLAlchemy ORM models that serve as the foundation for the application's database. It includes two main models: `User` and `Profile`. Below you can see the Entity-Relationship Diagram.

### Entity-Relationship Diagram
<p align="center">
  <img src="https://github.com/Xthe23/flask-agency/blob/main/Resources/QuickDBD-export.png" alt="ERD Diagram" width="600" height="600"/>
</p>

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

<figure>
  <table>
    <tr>
      <td><img src="https://github.com/Xthe23/flask-agency/blob/main/Resources/img1.png" alt="Profile View" width="400"/></td>
      <td><img src="https://github.com/Xthe23/flask-agency/blob/main/Resources/img2.png" alt="Registration Form" width="400"/></td>
    </tr>
    <tr>
      <td><img src="https://github.com/Xthe23/flask-agency/blob/main/Resources/img3.png" alt="Responsive Mobile View" width="400"/></td>
      <td><img src="https://github.com/Xthe23/flask-agency/blob/main/Resources/img4.png" alt="Profile Update Form" width="400"/></td>
    </tr>
    <tr>
      <td colspan="2"><img src="https://github.com/Xthe23/flask-agency/blob/main/Resources/img6.png" alt="Resume Upload Feature" width="400"/></td>
    </tr>
  </table>
  <figcaption>Leveraging Jinja tags, I implemented conditional logic to display the resume upload feature exclusively for users identified as either Workers or Clients on the profile route.</figcaption>
</figure>


## Technologies Used

- **SQLAlchemy**: For local DB testing.
- **AWS SDK for Python (Boto3)**.
- **Amazon Web Services**:
  - **Amazon RDS**: PostgresSQL Database
  - **Amazon S3**: Persistent File Storage System
  - **Amazon EC2**: Web Application Hosting
- **Flask**:
  - **Flask-Migrate**: For database migrations.
  - **Flask-Login**: For managing user sessions.
  - **Flask-WTF**: For form handling and CSRF protection.
- **werkzeug**: For password hash creation and checking.
