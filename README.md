# Customer Relationship Manager using Django
This project is a Customer Relationship Management (CRM) system implemented using Django. It allows users to manage customer records, including adding, updating, and deleting records. Users can also register and log in to the system to access these features.

## Features
* User registration and authentication.
* Display a list of customer records on the homepage.
* View detailed information of a specific customer record.
* Add new customer records.
* Update existing customer records.
* Delete customer records.

## Installation
1. Clone this repository to your local machine:
```git clone https://github.com/sankarXace/CRM-django.git```

2. Navigate to the project directory:
```cd CRM-django```

3. Create a virtual environment to make sure the dependencies not to install globally. Read the docs on how to create virtualenv [click here](https://docs.python.org/3/library/venv.html)

4. Install the required dependencies:
```pip install -r requirements.txt```

5. Run the migrations to set up the database:
```python manage.py migrate```

6. Create a superuser to access the Django admin panel:
```python manage.py createsuperuser```

7. Start the development server:
```python manage.py runserver```

8. Open your web browser and go to **http://127.0.0.1:8000/** to access the CRM application.

9. Another thing is you need to install Mysql Server [download here](https://dev.mysql.com/downloads/mysql/)
10. I'd prefer you to set username to 'root' in mysql configuration.


## Usage
1. Register a new user account to log in.
2. Log in using your registered credentials.
3. Upon logging in, you'll be redirected to the homepage displaying a list of customer records.
4. Click on a customer record to view its details.
5. To add a new customer record, click on the "Add Record" button and fill in the required information.
6. To update an existing customer record, click on the "Update" button next to the record and make the necessary changes.
7. To delete a customer record, click on the "Delete" button next to the record.



