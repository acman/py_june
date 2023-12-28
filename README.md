# py_june

## Project overview
This project is python help forum. It is a place where you can ask questions about python and get answers 
from other users.

## Technologies
* Python 3.12.1
* Django 5.0.2
* Materialize 1.0.0
* PostgreSQL 13.4
* AWS
* Terraform

## Setup
* pyenv install $(cat .python-version)
* pyenv virtualenv $(cat .python-version) py_june
* pyenv activate py_june
* pip install -r requirements.txt
* python manage.py migrate
* python manage.py loaddata categories.json
* python manage.py collectstatic
* python manage.py runserver
* open http://localhost:8000
* python manage.py createsuperuser

## Before commit
Check code style  
`make lint`
Check types
`make mypy`

## License
[MIT](https://choosealicense.com/licenses/mit/)

## Contact
lambda.py.inc@gmail.com
