
steps to run the project

git clone https://github.com/learnkvl/aifeglobal.git

pip install -r requirements.txt

write/copy  .env file in backend project folder 

run 
python manage.py runserver







steps to create From starting any project

create a project folder with project name

create an vitual environment 
python -m venv env

Activate the environment
source env/Scripts/activate

install required libraries

if we are creating a Django project first time 
pip install Django

django-admin startproject backend .

pip install required frameworks,corsheader based on what you want
we have settings.py in project there we have to edit some names

if we have project/or cloned git repository 
pip install -r requirements.txt

after that create an app according to our project
python manage.py startapp accounts

python manage.py startapp aife

write models in models.py in app folders write the fields which are required to show,filter etc in admin file

python manage.py makemigrations
python manage.py migrate

python manage.py runserver

write views according to our requirement

write urls in that app

write urls in main project folder backend also 

create templates folder  in project app put your templates .html

create static folder in that put your images 

python manage.py createsuperuser

python manage.py collectstatic

run 
python manage.py runserver


How to Set Up and Run the Project Locally

Follow these detailed steps to get the project up and running on your local machine.


1. Create a Project Folder

Start by creating a new folder for your project:

```bash
mkdir aifeglobal
cd aifeglobal

2. Create a Virtual Environment
A virtual environment helps isolate dependencies:

python -m venv env

 3. Activate the Virtual Environment
On Windows:

env\Scripts\activate

 4. Install Required Libraries
If you're starting from scratch:


pip install Django

If you've cloned the project:


pip install -r requirements.txt

Install other required libraries like:


pip install djangorestframework django-cors-headers

 5. Start a New Django Project (if needed)

django-admin startproject backend .

 6. Configure settings.py
In backend/settings.py:

Add your apps to INSTALLED_APPS

Add 'corsheaders.middleware.CorsMiddleware' to MIDDLEWARE

Configure STATIC_URL, TEMPLATES, and ALLOWED_HOSTS

Link your database or environment settings if needed

7. Create Django Apps
Create apps according to the project requirements:


python manage.py startapp accounts
python manage.py startapp aife

8. Define Models
In each app’s models.py, define the required database structure:

 9. Make and Apply Migrations

python manage.py makemigrations
python manage.py migrate

Create Views and URL Routes
Define logic in views.py of each app.

Create an urls.py file inside each app to handle routing.

In backend/urls.py, include your app URLs:



 11. Templates and Static Files
In each app, create a templates/ folder and add your .html files.

Create a static/ folder to store images, CSS, JS, etc.

Update settings.py:


STATICFILES_DIRS = [BASE_DIR / "static"]
TEMPLATES[0]['DIRS'] = [BASE_DIR / 'templates']

12. Create Superuser
To access the admin panel:

python manage.py createsuperuser

 13. Collect Static Files
To prepare static files for deployment:

python manage.py collectstatic

write build files

write velcel.json file

14. Run the Development Server

python manage.py runserver

Then visit:

http://127.0.0.1:8000/

http://127.0.0.1:8000/admin




