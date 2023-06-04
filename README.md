# INSTALLATION
## REQUIREMENTS
### Already installed :
- Python
- A local web server with MySQL
### 1 - Create a folder and open it in your IDE (VS Code for example)
### 2 - Open a terminal and clone the project
```
git clone https://github.com/TommyPREEL/EventImmediat.git
```
### 3 - Go inside
```
cd EventImmediat
```
### 4 - Install the dependencies
```
pip install -r requirements.txt
```
### 5 - Create a database in your web server named "event_immediat"

### 6 - Generate a secret key for the application
### Type in a terminal 
```
python manage.py shell
```
### This will open a python shell
### Then type those commands :
```
from django.core.management.utils import get_random_secret_key
print(get_random_secret_key())
```
### The generated key is the new secret key for the application

### 7 - Configure the .env file
```
SECRET_KEY=                 #the new secret key
DB_NAME=event_immediat      #the database name
DB_USER=root                #the admin user of your web server
DB_PASS=                    #the admin password of your web server
```
### 8 - Do a migration
```
python manage.py migrate
```
### 9 - Create a superuser
```
python manage.py createsuperuser
```
### 10 - Start the server 
```
python manage.py runserver
```
# ROLES & PERMISSIONS

# User 
## Not logged in :
### Can : 
### - See the home page
### - See the events list
### - Sign in
### - Log in

## Logged in :
### Can : 
### - See the home page
### - See the events list
### - See the "My Events" page
### - Log out
### - Participate to an event
### - Cancel his participation to an event

# Staff
## Has the same permissions that a logged in user 
### Can : 
### - Create a new event
### - Edit his own events
### - Delete his own events
### - See the participants list of his own events

# Admin
## Has the same permissions that a staff
### Can :
### - Edit/delete all events
### - See the participants list of all events