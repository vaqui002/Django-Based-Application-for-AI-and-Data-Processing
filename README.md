# Django Project Setup Guide

This guide will walk you through setting up and running a Django project on your local machine.

## Prerequisites
Before proceeding, ensure you have the following installed on your system:
- **Python 3.x** (Download from [python.org](https://www.python.org/downloads/))
- **pip** (Python package manager, usually included with Python)
- **Virtualenv** (for creating a virtual environment)

### Check Installation
To verify that these are installed, run the following commands in your terminal or command prompt:
```sh
python --version
pip --version
virtualenv --version
```
If any of these commands return an error, install the missing software before proceeding.

## Step 1: Clone the Project
Download the project repository to your local machine.

### Option 1: Clone with Git
If you have **Git** installed, run the following commands in your terminal:
```sh
git clone https://github.com/vaqui002/Django-Project.git
cd Django-Project
```

### Option 2: Download as ZIP
If you don’t have Git:
1. Download the project as a ZIP file from the repository.
2. Extract the contents.
3. Open the extracted folder in your terminal or command prompt.

## Step 2: Set Up a Virtual Environment
A virtual environment helps isolate project dependencies from the rest of your system.

### Create a Virtual Environment
In the project folder, run:
```sh
virtualenv venv
```
This creates a **venv** folder containing the virtual environment.

### Activate the Virtual Environment
#### On Windows:
```sh
venv\Scripts\activate
```
#### On macOS/Linux:
```sh
source venv/bin/activate
```
Once activated, you should see **(venv)** in your terminal prompt, indicating the virtual environment is active.

## Step 3: Install Dependencies
Install the required libraries and dependencies:
```sh
pip install -r requirements.txt
```

## Step 4: Run Database Migrations
Set up the database and apply migrations:
```sh
python manage.py migrate
```
This command creates the necessary database tables based on your Django models.

## Step 5: Collect Static Files
If your project includes static files (CSS, JavaScript, images), collect them into a single location:
```sh
python manage.py collectstatic
```
When prompted, confirm by typing **yes**.

## Step 6: Start the Development Server
Run the Django development server:
```sh
python manage.py runserver
```
Now, open your web browser and go to [http://127.0.0.1:8000/](http://127.0.0.1:8000/) to access the application.

## Troubleshooting
### 1. Port Already in Use
If you see an error that the port is in use, start the server on a different port:
```sh
python manage.py runserver 8080
```
### 2. Missing Dependencies
If you encounter missing dependencies, run:
```sh
pip install -r requirements.txt
```
### 3. Database Errors
If you have database-related issues:
- Ensure you have run `python manage.py migrate`.
- Check your database settings in **settings.py**.

## Step 7: Deactivate the Virtual Environment
When you're done, deactivate the virtual environment:
```sh
deactivate
```
This returns you to your system’s default Python environment.

## Additional Notes
### For Production Use
This guide is for local development. For deploying to a production server, configure:
- A secure database
- A web server (e.g., Nginx, Apache)
- HTTPS settings

## Conclusion
Congratulations! You have successfully set up the Django project on your local machine. You can now start developing and testing your application. If you encounter any issues, refer to this guide or seek support.

