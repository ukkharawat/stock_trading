# Stock Trading:: Backend


## Feature

``` bash
  1. Display stock in graph
  2. Buy Stock
  3. Sell Stock
  4. Portfolio page
```

## Prerequisite

### Python3 based on [Anaconda3](https://www.anaconda.com/download/)
##### pip install package==version [pip3 for linux]
``` bash 
  django: 2.0.2
  djangorestframework 3.7.7  
  django-cors-headers 2.1.0  
  bcrypt 3.1.4
  psycopg2-binary
```

## Database setup
```bash
  apt-get -y install postgresql postgresql-contrib
  sudo su - postgres
  psql
  CREATE DATABASE DB_NAME;
  CREATE USER USER_NAME WITH PASSWORD YOUR_PASSWORD; \\MUST CHANGE IN SETTINGS
  \q
  exit
```

## Build Setup

``` bash
# run in local
  python manage.py runserver [port: optional]
  
# change model
  python manage.py makemigrations
  
# apply model
  python manage.py migrate
 
# create superuser (Require runserver)
  prthon manage.py createsuperuser 
```
