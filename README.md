# django-imager
A simple image management website built in Python using the Django framework.

Once registered and logged-in, users can upload photos and albums.
Users can set their photo and album publication settings to public, shared, or private.
Users can share with photos or albums with persons they are "friends" with if photos or albums are set to "shared".

### Setup
Create an env.sh file and git ignore it. Add this information:

export DB_NAME=''
export DB_USER=''
export DB_PASSWORD=''
export DB_HOST='127.0.0.1'
export DB_PORT='5432'
export SECRET_KEY=''


Create a Postgres database
Pip install -r requirements.txt
Make migrations
This app will not work without a cache table. Be sure to "python manage.py createcachetable".



### Authors
Iris Carrera https://github.com/icarrera

Patrick Trompeter https://github.com/ptrompeter
