deldichoalhecho
===============

Deldichoalhecho is a promise tracker application.

This is intended to be a django-app and also a site by itself that allows 
citizens to create promises made by an authority and keep track of their 
fulfillment, this project is inspired by deldichoalhecho.cl.

This version handles multi-instances. For a single instance version, see 
https://github.com/ciudadanointeligente/check-it

[![Build Status](https://travis-ci.org/ciudadanointeligente/deldichoalhecho.svg?branch=master)](https://travis-ci.org/ciudadanointeligente/deldichoalhecho)
[![Coverage Status](https://coveralls.io/repos/ciudadanointeligente/deldichoalhecho/badge.png?branch=master)](https://coveralls.io/r/ciudadanointeligente/deldichoalhecho?branch=master)
[![Dependency Status](https://www.versioneye.com/user/projects/56a2489c9b5998003c000025/badge.svg?style=flat)](https://www.versioneye.com/user/projects/56a2489c9b5998003c000025)
[![Code Issues](https://www.quantifiedcode.com/api/v1/project/8c60078cc0c04ec284a7e93d89459491/badge.svg)](https://www.quantifiedcode.com/app/project/8c60078cc0c04ec284a7e93d89459491)

## Installation

The installation requires certain software to be installed in your machine

## Requirements

- [Python](https://www.python.org/)
- [virtualenv](https://pypi.python.org/pypi/virtualenv)
- [virtualenvwrapper](https://pypi.python.org/pypi/virtualenvwrapper)
- [Django 1.8](https://docs.djangoproject.com/en/1.8/)

## Steps

* Clone the project

```
git clone https://github.com/ciudadanointeligente/deldichoalhecho.git
```

* Create a virtualenv and enter the directory

```
mkvirtualenv deldichoalhecho
cd deldichoalhecho
```

* Install the project requirements

```
pip install -r requirements.txt
```

* Create your own config file. Here you can edit the configuration for your specific implementation

```
cp project_site/local_settings.demo.py project_site/local_settings.py 
```

And then edit that file.

* Install migrations

```
python manage.py migrate
```

* Managing static files

```
python manage.py collectstatic
```

* Run server

```
python manage.py runserver
```

And now you can access it at [http://localhost:8000](http://localhost:8000).

## Deploy to Heroku

This app can be deployed to [heroku](http://heroku.com) to do so you need to create an account and install the [heroku toolbelt](https://toolbelt.heroku.com/), then you need to create an app and relate a database for it (for example [heroku postgres](https://postgres.heroku.com) which has a free layer).

Then you can publish your project by doing

```
git push heroku master
```

After that you need to sync the database by doing


```
heroku run ./manage.py syncdb
```

And run the migrations


```
heroku run ./manage.py migrate
```

## Thanks

This project is inspired by:

* [Promesometro](http://promesometro.pe/)

* [PolitiFact | Tracking politicians' promises](http://www.politifact.com/truth-o-meter/promises/)

## TODO

* Write documentation about themeing
* Write documentation about using deldichoalhecho in another django app

