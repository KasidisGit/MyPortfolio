# MyPortfolio

Requirements:
- An installation of Python and Virtual Environment.
- An installation of Django in your virtual Environment.

Run Script:
```
git clone https://github.com/KasidisGit/MyPortfolio.git
cd path/to/MyPortfolio
python -m venv <name_of_virtualenv>
source <name_of_virtualenv>/bin/activate
pip install django
python manage.py migrate
python manage.py makemigrations
python manage.py runserver
```
Go to http://127.0.0.1:8000/
