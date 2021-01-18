# Bank security console

Bank security console is site, which you can connect to remote database with all visits and passcards of workers of your bank.

### How to install

First of all, we should have the python upper 3.5.0 and manager pip. 
You have to install all requirements from requirements.txt

```
pip install -r requirements.txt
```

After that you can run it from you local server with
```
python manage runserver 0.0.0.0:8080
```

### .env
The console uses variables of enviroment. You should create file .env in root directory and use the next variables:

```
DB_PORT - port to your database
DB_NAME - name of your database
DB_USER - user of your database
DB_PASSWORD - password of your database
SECRET_KEY - secret key for Django
DEBUG - True (debug mode), False (production mode)
```
### Project Goals

The code is written for educational purposes on online-course for web-developers [dvmn.org](https://dvmn.org/).
