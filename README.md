Setup Guide
===========

 - Make a folder (fx. leapkit)

 - Create a virtual environment: ```virtualenv epita-venv```(På arch: ```virtualenv epita-venv/python2``` )
 - Start a project with the code: ```django-admin.py startproject leapkit```
 - Go into this new folder and delete the folder with the name leapkit
 - ```git clone git@github.com:martinnj/leapkit```
 - ```cd leapkit```
 - ```vagrant up```
 - ```vagrant ssh```
 - ```sudo ./postinstall.sh```
 - ```cd /vagrant/```
 - ```./leapkit/01_setup.sh```


Database Setup
==============
 - ```sudo -u postgres psql```
 - ```postgres=# create user leapkit_user createdb createuser password '12345q';```
 - ```postgres=# create database leapkit_db owner leapkit_user;```
 - ```./leapkit/02_db.sh```

Populate Database
=================
**TODO: Get data to the tables (instritutions are missing for instance.)**

Starting Leapkit Solution
=========================
 - ```./manage.py runserver 0.0.0.0:8080```
 - Kan herefter tilgås på [http://localhost:8080/](http://localhost:8080/)







Django
======

This repository is meant as a working environment for the EPITA 2014 RIP project.

Getting started
--------

To get started with this project work you need to do the following

1. Install **python 2.7** on your computer
2. Install **pip**
3. Install **virtualenv**
4. Create a virtual environment: **virtualenv epita-venv**
5. Start a project with the code: **django-admin.py startproject choose-a-name** (e.g leapkit)
6. Go into this new folder and delete the folder with the name you just chose (e.g leapkit)
7. Start git, and pull everything from this repository
8. Write: **pip install -r requirements.txt** to install all the needed external apps

Database
--------
The database is currently SQLlite since this makes it easier to work on on multiple computers

Name           |Value
:---           |:---:
User name:     |test
Email: 		   |test@test.dk
Password:	   |test


Important Information
---------------------

Bootstrap and JQuery is installed as apps, because it makes it easier to allow their usage in all parts of the websites.

In all apps there is a test directory, all test made should be put into this directory and be named "test_" + name of the
part of the program it test (e.g **test_model**, **test_view**).

All apps contain a folder called **static**. This is for static files such as **CSS**, **JavaScript**, **Images** etc. However, they need to be placed inside another folder with the same name as the app itself. I have added such a folder already. If custom CSS is needed it would then have to be placed inside a folder called **css**.

All **HTML** files will need to be put inside the **templates folder**, also included in all apps. If any of the html folders are used as templates, they should be included in a folder called **_layouts** inside **templates**.

For specific information about django, most can be found on djangos website:
https://docs.djangoproject.com/en/1.6/contents


### Other notes

In the template folder of each app, there is a folder called _layout. In this there will be a base template for all views in the given app. I recommend that all CSS files and JS files should be loaded from this template. It means that all CSS files and JS files are loaded once, which might cause a loading spike once, but it is faster than loaded a new file in every template. On top of this, it will enable us to use some cool JavaScript that makes the website look more responsive, by starting the loading process as soon as the mouse hovers over a link. (http://www.instantclick.io)


### Information sources

#### Working with the views

1. https://docs.djangoproject.com/en/1.6/topics/templates/ (Information about how to design flexible templates)
2. https://docs.djangoproject.com/en/1.6/topics/http/shortcuts/ (Shortcut functions that makes it easy to do regular tasks)
3. https://docs.djangoproject.com/en/1.6/topics/class-based-views/ (How to use class based views)
4. https://docs.djangoproject.com/en/1.6/topics/forms/ (Working with forms in Django)
5. https://docs.djangoproject.com/en/1.6/topics/pagination/ (Pagination in Django)
6. https://docs.djangoproject.com/en/1.6/howto/static-files/ (Working with static files)

#### Third party libraries used

1. http://django-crispy-forms.readthedocs.org/en/latest/index.html (making it easier to manage forms)
2. http://django-floppyforms.readthedocs.org/en/latest/ (improving form layout)
3. http://django-braces.readthedocs.org/en/latest/index.html (Making plugin mixing easy)
4. http://south.readthedocs.org/en/latest/ (Improving database management)


1. http://quilljs.com/ (For great styling messages)


#### Bootstrap design inspiration

1. http://builtwithbootstrap.com/
2. http://lovebootstrap.com/
3. http://spyrestudios.com/40-websites-built-with-the-twitter-bootstrap-framework/
4. http://designgeekz.com/15-best-bootstrap-tools-for-designers/
5. http://untame.net/2012/09/15-incredible-sites-built-with-twitter-bootstrap/


#### Email

1. https://docs.djangoproject.com/en/1.6/topics/email/ (Sending emails with Django)

#### Login and security

1. https://docs.djangoproject.com/en/1.6/topics/auth/ (User Authentication)
2. https://docs.djangoproject.com/en/1.6/topics/http/sessions/ (Working with sessions in Django)
3. https://docs.djangoproject.com/en/1.6/topics/security/ (Security in Django)

#### Working with files

1. https://docs.djangoproject.com/en/1.6/topics/http/file-uploads/ (File uploading)
2. https://docs.djangoproject.com/en/1.6/topics/files/ (Handle files)

#### Testing in Django
1. https://docs.djangoproject.com/en/1.6/topics/testing/overview/
https://docs.djangoproject.com/en/1.6/topics/testing/tools/
https://docs.djangoproject.com/en/1.6/topics/testing/advanced/

Selenium is installed and can be used for testing, for more information and tutorials, here are some links:

1. http://lincolnloop.com/blog/introduction-django-selenium-testing/
2. http://blog.wercker.com/2013/11/28/django-selenium.html
3. http://www.realpython.com/blog/python/django-1-6-test-driven-development/

#### Multiple languages

1. https://docs.djangoproject.com/en/1.6/topics/i18n/translation/#translating-url-patterns (Best practises for multiple languages)

#### Comments
1. https://code.djangoproject.com/wiki/UsingFreeComment (Django's build in comment library)


#### Searching
1. http://haystacksearch.org

### Payment systems that work in Denmark

1. 2Checkout
2. Authorize.net
3. **Braintree**
4. ePay
5. PAYMILL
6. Quickpay
7. WorldPay

I personally have only heard good things about **Braintree**, and there is no cost for the first 50.000$ the company makes.

https://www.braintreepayments.com/docs/python/guide/overview (Working with Braintree in Python)



Commands that are good to know
-------------------------------

1. **django-admin.py startproject name-of-project**
2. **python manage.py startapp name-of-app**
3. **python manage.py syncdb** (To sync the database)
4. **python manage.py test** (to run standard django tests)
6. **python manage.py test --settings=leapkit.settings.testing** (to make sure to use the settings defined in testing.py)
6. **coverage run manage.py test** (better way to run tests)
7. **coverage report** (To create a report showing how much of the program your tests covers)
8. **coverage html** (to create a html site showing which parts of your code is tested and which parts that still need to be tests)

## Git Commands

1. **git init** (to create a git repository)
2. **git remote add origin https://github.com/MVilstrup/EPITA.git** (To add the remote branch with the name origin)
3. **git pull origin** (To pull all the code from github to your folder)
4. **git push -u origin master** (To push your changes to github, for the first time)
5. **git push origin master** (to push your changes to github the rest of the project)


