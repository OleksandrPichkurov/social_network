# social_network

## Table of contents
* [General info](#general-info)
* [Technologies](#technologies)
* [Setup](#setup)


## General info
This is a training project. It implements the functionality of social networks, such as:

1. Token authentication(JWT).
* api/token/
* api/token/refresh/ 
2. Login and logout page.
* api-auth/login/
* api-auth/logout/
3. User registrations and activity(last login, last request to the service).
* api/users/signup/
* api/users/activity/
* api/users/activity/(user id)/
4. Post creation and extra action(like, unlike).
* api/posts/
* api/posts/(post id)/
* api/posts/(post id)/like/
* api/posts/(post id)/unlike/
5. Analytics about how many likes were made every day in the desired period of time.
* api/analitics/?date_from=2021-01-01&date_to=2021-03-15

	
## Technologies
Project is created with:
* Django==3.0
* djangorestframework==3.12.2
* djangorestframework-simplejwt == 4.6.0
	
## Setup
To run this project, clone it locally using:

```
$ git clone https://github.com/OleksandrPichkurov/social_network.git
$ pip3 install -r requirements.txt
```

Run migration
```
$ python3 manage.py migrate
```