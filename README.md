# Game-Social 
A Video Game fan community Site. Users can create groups on various Gaming topics 
(e.g. Call of Duty, Halo and Battlefield. Users can then create posts in groups their apart of. 
## Installation
### These are required to run the server 
```
pip install django ( Django 2.0 - current version should work )
pip install django-braces
pip install django-bootstrap3
```
## Usage
To run the app use command 
```
python manage.py runserver
```
## Restful Urls
* List of Users:
    * GET http://127.0.0.1:8000/accounts/users/

* A Specific User 
    * GET http://127.0.0.1:8000/accounts/users/id/
* List of Groups:
    * GET http://127.0.0.1:8000/groups/list
