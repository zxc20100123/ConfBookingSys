# Conference Room Booking System

A room booking system built using Django framework. It is designed for employees to book a conference room at their selected date time. Features include room booking and manage upcoming reservations.

## Installation

Python, Django and other required modules need to be installed
```python
pip install -r requirements.txt
```

## Set Up

Before running the project, there are few things need to be done first.

Firstly, you'll need a **secret key** for the django project. See how to get one **[here](https://stackoverflow.com/questions/4664724/distributing-django-projects-with-unique-secret-keys)**.\
Secondly, you'll need to sign up on **[Cloudinary](https://cloudinary.com/)** to obtain your cloud where you'll be storing medias.\
Lastly, create a **.env** file in the root folder of the project with:
```
SECRET_KEY = 'your_secret_key'

CLOUD_NAME = 'your_cloud_name'
API_KEY = 'your_api_key'
API_SECRET = 'your_api_secret'
```

## Usage

Open cmd and cd to where the project folder and run:
```python
python manage.py runserver
```

Date and time field currently works on:
:heavy_check_mark: Chrome\
:heavy_check_mark: Edge\
:x: Firefox

## Login

Open a browser and go to **[http://127.0.0.1:8000/home](http://127.0.0.1:8000/home)**, where you'll be redirect to login page and asked to log in or register.

You can also create an admin account by typing the following command in cmd:
```python
python manage.py createsuperuser
```

## Screenshots

![home](https://res.cloudinary.com/dys4hxaoi/image/upload/v1657538702/github_readme_img/home_jxkhwv.png)
![search](https://res.cloudinary.com/dys4hxaoi/image/upload/v1657538704/github_readme_img/search_ao1p00.png)
![history](https://res.cloudinary.com/dys4hxaoi/image/upload/v1657538702/github_readme_img/history_cub6aa.png)
![admin](https://res.cloudinary.com/dys4hxaoi/image/upload/v1657538702/github_readme_img/admin_ciocmh.png)
![admin_room](https://res.cloudinary.com/dys4hxaoi/image/upload/v1657538702/github_readme_img/admin_room_qvte6n.png)
![admin_roombooked](https://res.cloudinary.com/dys4hxaoi/image/upload/v1657538702/github_readme_img/admin_roombooked_dkyzfu.png)


