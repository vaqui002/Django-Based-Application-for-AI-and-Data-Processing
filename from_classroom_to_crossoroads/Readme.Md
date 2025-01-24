# Django Project Setup Guide

This guide will walk you through setting up and running the Django project on your local machine. 

## Prerequisites

Before setting up the project, please ensure that the following software is installed on your system:

- **Python 3.x** (Download from [python.org](https://www.python.org/downloads/))
- **pip** (Python package manager, usually installed with Python)
- **Virtualenv** (for creating a virtual environment)

### Check Installation

You can check if these are installed by running the following commands in your terminal or command prompt:

```bash
python --version
pip --version
virtualenv --version
```

If any of these commands return an error, please install the software before proceeding.

---

## Step 1: Clone the Project

Start by cloning the project repository to your local machine. You can either use Git to clone the project or download it as a ZIP file.

### Option 1: Clone with Git

If you have **Git** installed, open your terminal and run the following commands:

```bash
git clone https://github.com/vaqui002/Django-Project.git
cd yourproject
```

### Option 2: Download as ZIP

If you don’t have **Git**, you can simply download the project as a ZIP file. After downloading, extract the contents and open the extracted folder in your terminal or command prompt.

---

## Step 2: Set Up a Virtual Environment

To avoid conflicts with other Python projects, it’s recommended to set up a **virtual environment** for this project. This will ensure that the project dependencies are isolated from the rest of your system.

### Create a Virtual Environment

1. Open your terminal or command prompt in the project folder.
2. Run the following command to create a virtual environment:

```bash
virtualenv venv
```

This will create a `venv` folder in the project directory, which contains the virtual environment.

### Activate the Virtual Environment

- **On Windows**:

```bash
venv\Scripts\activate
```

- **On macOS/Linux**:

```bash
source venv/bin/activate
```

Once activated, you should see `(venv)` in your terminal prompt, indicating that the virtual environment is active.

---

## Step 3: Install Dependencies

Now that the virtual environment is set up, you can install the required dependencies for the project.

1. Run the following command to install the necessary libraries and dependencies listed in the `requirements.txt` file:

```bash
pip install -r requirements.txt
```

---

## Step 4: Run Database Migrations

To set up the database and apply all necessary migrations, run the following command:

```bash
python manage.py migrate
```

This command will create the necessary database tables and set up the structure based on the models defined in your Django project.

---

## Step 5: Collect Static Files

If your project includes static files (CSS, JavaScript, images), you need to collect them into a single location for easier access.

1. Run the following command:

```bash
python manage.py collectstatic
```

2. When prompted, confirm by typing `yes`.

This will gather all static files into a directory specified in your `settings.py` file.

---

## Step 6: Start the Development Server

Now that everything is set up, you can start the Django development server and view the application in your browser.

1. Run the following command to start the server:

```bash
python manage.py runserver
```

2. Open your web browser and go to `http://127.0.0.1:8000/` to access the application locally.

---

## Troubleshooting

Here are a few common issues and their solutions:

### 1. **Port Already in Use**

If you encounter an error that the port is already in use, you can start the server on a different port by running:

```bash
python manage.py runserver 8080
```

This will start the server on port `8080`.

### 2. **Missing Dependencies**

If you see an error about missing dependencies, try running the following command to install them:

```bash
pip install -r requirements.txt
```

### 3. **Database Errors**

If you experience issues with the database, ensure that you’ve run the `migrate` command and that your database settings are correct in `settings.py`.

---

## Step 7: Deactivate the Virtual Environment

Once you’re done working on the project, deactivate the virtual environment by running:

```bash
deactivate
```

This will return you to your system’s default Python environment.

---

## Additional Notes

- **For Production Use:** This guide is meant for local development. If you want to deploy the project to a production server, you’ll need to configure production-ready settings like a secure database, web server (e.g., Nginx, Apache), and HTTPS configuration.
  

## Conclusion

Congratulations! You’ve successfully set up the Django project on your local machine. You can now begin working with the application, running it locally, and making any modifications or tests. If you run into any issues during setup, refer to this guide or reach out for support.
