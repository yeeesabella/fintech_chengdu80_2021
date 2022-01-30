# Introduction
This is the submission from National University of Singapore for Chengdu80 Fintech Competition 2021.

# Set up
Run the following commands to run on virtual environment.
```python3 -m venv .venv
source .venv/bin/activate

pip install -r requirements.txt
python manage.py makemigrations

python manage.py migrate
python manage.py collectstatic
python manage.py runserver```
