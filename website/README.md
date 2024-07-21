# Django Project Setup Guide

This guide will walk you through setting up our Django project on your local machine. Follow these steps carefully to ensure a smooth setup process.

## Prerequisites

Before you begin, make sure you have the following installed:
- Python (3.8 or higher)
- Git
- pip (Python package manager)

## Setup Steps

### 1. Clone the Repository

First, clone the project repository to your local machine:

```
git clone https://github.com/Kebaso-J/iGrow.git
```

### 2. Navigate to the Project Directory

Change into the website project directory:

```
cd ./iGrow/website
```

### 3. Create a Virtual Environment (Optional but Recommended)

It's best practice to use a virtual environment to keep your project dependencies isolated:

```
python -m venv venv
```

Activate the virtual environment:

- On macOS and Linux:
  ```
  source venv/bin/activate
  ```
- On Windows:
  ```
  venv\Scripts\activate
  ```

### 4. Install Dependencies

Install the required packages using pip:

```
pip install -r requirements.txt
```

### 5. Set Up the Database

Run migrations to set up your database schema:

```
python manage.py makemigrations && python manage.py migrate
```

### 6. Start the Development Server

Launch the Django development server:

```
python manage.py runserver
```

### 7. Access the Application

Open your web browser and navigate to:

```
http://localhost:8000
```

You should now see the Django application running.

## Additional Information

- To create a superuser for the Django admin interface, run:
  ```
  python manage.py createsuperuser
  ```

- Check `settings.py` for any environment-specific configurations you might need to adjust.

## Troubleshooting

If you encounter any issues during setup, please:
1. Ensure all prerequisites are correctly installed.
2. Check that you're in the correct directory when running commands.
3. Verify that your virtual environment is activated.

For further assistance, please open an issue in the GitHub repository or contact the project maintainers.

