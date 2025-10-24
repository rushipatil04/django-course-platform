# Django Course Platform

[![Python Version](https://img.shields.io/badge/python-3.11+-blue.svg)](https://www.python.org/downloads/)
[![Django Version](https://img.shields.io/badge/django-4.2.7-green.svg)](https://www.djangoproject.com/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

A full-featured, production-ready web application for a Free & Paid Course System. This platform allows users to register, browse courses, purchase paid courses via a manual payment verification system, and access their enrolled content. It also includes a comprehensive admin dashboard for managing users, courses, and purchase requests.

## ✨ Key Features

### 👤 User Features
- **Authentication:** Secure user registration with email/password and login.
- **User Profiles:** A personal dashboard showing profile information and enrolled courses.
- **Course Discovery:**
  - Homepage with sections for Featured, Free, and Paid courses.
  - A dedicated "All Courses" page with search and filtering by category and price.
  - Detailed course pages with full descriptions, syllabus, and purchase options.
- **Paid Course Purchase Flow:**
  - Simple QR code-based payment system (e.g., for UPI in India or other merchant QR codes).
  - Users can upload a payment screenshot to verify their purchase.
  - The status of a purchase (Pending, Approved, Rejected) is shown on the user's dashboard.
- **Access Control:** Users can only access content for free courses or paid courses for which their purchase has been approved by an admin.
- **My Courses Page:** A centralized location for users to access all their enrolled courses with one click.

### ⚙️ Admin Features
- **Secure Admin Panel:** Uses the built-in Django Admin for core data management (Users, Courses, Categories, Content).
- **Custom Admin Dashboard:**
  - A user-friendly dashboard at `/admin-dashboard/` for day-to-day operations.
  - Analytics widgets showing total users, courses, and pending purchases.
  - **Purchase Management:** View pending purchase requests with screenshot previews. Approve or reject requests with comments.
- **Content Management:** Admins can create, edit, and manage courses, categories, and individual content items (videos, PDFs) through the Django Admin interface.

## 🔧 Tech Stack

- **Backend:** Django, Python
- **Database:** SQLite3 (for development), configured for easy migration to PostgreSQL.
- **Frontend:** Django Template Language, Bootstrap 5
- **Authentication:** Django's built-in authentication system.
- **File Storage:** Local file storage for development (for `media` files like screenshots and thumbnails).
- **QR Codes:** `qrcode` library for dynamic generation of payment QR codes.

## 📂 Project Structure

course_platform/
├── accounts/ # Handles user registration, login, and profiles
├── courses/ # Manages Course, Category, and Content models
├── purchases/ # Manages Purchase requests and admin approval views
├── core/ # For core project files, can be used for management commands
├── courseplatform/ # Main Django project settings and URLs
├── media/ # Directory for user-uploaded files
├── static/ # Directory for static files (CSS, JS)
├── templates/ # Contains all HTML templates for the site
├── create_sample_data.py # Script to populate the database with dummy data
├── manage.py # Django's command-line utility for management tasks
└── requirements.txt # Lists all Python package dependencies


## 🚀 Getting Started

Follow these instructions to get the project up and running on your local machine for development and testing.

### 1. Prerequisites

- [Python 3.11+](https://www.python.org/downloads/)
- [Git](https://git-scm.com/) (for cloning the repository)

### 2. Installation on macOS

1.  **Clone the repository:**
    ```bash
    git clone https://github.com/your-username/course-platform.git
    cd course-platform
    ```

2.  **Create and activate a virtual environment:**
    A virtual environment keeps your project's dependencies separate from other projects.
    ```bash
    python3 -m venv venv
    source venv/bin/activate
    ```

3.  **Install the required dependencies:**
    This command reads the `requirements.txt` file and installs all necessary packages.
    ```bash
    pip install -r requirements.txt
    ```

4.  **Apply database migrations:**
    This command creates the database schema based on your models.
    ```bash
    python manage.py migrate
    ```

5.  **Create a superuser account:**
    This account will have full administrative privileges.
    ```bash
    python manage.py createsuperuser
    ```
    Follow the prompts to set a username, email, and a strong password.

6.  **Populate the database with sample data (Recommended):**
    This script creates sample categories and courses to make the site feel alive.
    ```bash
    python create_sample_data.py
    ```

### 3. Running the Application

1.  **Start the development server:**
    ```bash
    python manage.py runserver
    ```

2.  **Access the website:**
    Open your web browser and navigate to `http://127.0.0.1:8000`.

## 🖥️ Site Usage

- **Main Website:** `http://127.0.0.1:8000`
  - Browse courses, register, and log in.

- **Django Admin Panel:** `http://127.0.0.1:8000/admin`
  - Login with your superuser credentials.
  - Use this for deep management: adding course content (videos, PDFs), editing categories, and managing user accounts directly.

- **Custom Admin Dashboard:** `http://127.0.0.1:8000/admin-dashboard/`
  - You must be logged in as an admin to access this.
  - This is the main hub for reviewing and approving/rejecting course purchase requests.

### Testing the Purchase Flow
1.  Register a new, non-admin user account.
2.  Navigate to a paid course and click "Purchase Course".
3.  On the payment page, upload any image file as a "payment screenshot" and submit.
4.  Log in as the admin and go to the **Admin Dashboard** to see the pending request.
5.  Approve the request.
6.  Log back in as the user. You will now have access to the course via the "My Courses" page.

## 💡 Future Improvements

-   **Dockerization:** Containerize the application with Docker and Docker Compose for easy setup and deployment.
-   **REST API:** Implement a RESTful API using Django REST Framework for a potential SPA frontend (React/Vue) or mobile app.
-   **Unit Tests:** Add comprehensive unit and integration tests for critical application flows like registration and purchasing.
-   **CI/CD:** Set up a GitHub Actions workflow to automatically run tests on every push or pull request.
-   **Real Email Notifications:** Integrate an email service like SendGrid or Mailgun for sending transactional emails (e.g., on purchase approval).

## 📄 License

This project is licensed under the MIT License.