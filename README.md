# Vehicle Tracker

Vehicle Tracker takes your data, determines your vehicle type and displays summary of your data in an elegant pie chart.

# Features!

  - Import a XML file and watch it magically convert to relevant data
  - Summary of all the vehicles in your data
  - History of your uploaded files so you can view them anytime.

### Tech

Vehicle Tracker uses a number of open source projects to work properly:

* [Django] - Framework for building webapps in Python.
* [W3.CSS] - UI template in HTML,CSS and JS

### Installation

Vehicle Tracker requires Python3 to run. If you have a Linux machine, dont worry your good to go. If not, please refer https://www.python.org/downloads/

Create a virtual env
```sh
$ cd Vehicle-Tracker/
~/Vehicle-Tracker (master) $ python3 -m venv env
~/Vehicle-Tracker (master) $ ls
env  requirements.txt  src
```
You will notice an env folder has been created.

Now we need to activate our virtual environment using following:
```sh
~/Vehicle-Tracker (master) $ source env/bin/activate
```

Note: In case you need to deactivate the virtual environment or no longer need it just run `deactivate` like this:
```
(env) ~/Vehicle-Tracker (master) $ deactivate
```

We notice `(env)` in the path name of our terminal. Now we have successfully activated our virtual environment. Lets install the required packages via `requirements.txt` file
```sh
(env) ~/Vehicle-Tracker (master) $ pip install -r requirements.txt
Collecting Django==2.0.7 (from -r requirements.txt (line 1))
  Using cached https://files.pythonhosted.org/packages/ab/15/cfde97943f0db45e4f999c60b696fbb4df59e82bbccc686770f4e44c9094/Django-2.0.7-py3-none-any.whl
Collecting jsonfield==2.0.2 (from -r requirements.txt (line 2))
  Using cached https://files.pythonhosted.org/packages/39/ab/00f09d604f1d659831cc4d7f26419bbf2bd70852951a4f77691bd78f527e/jsonfield-2.0.2-py2.py3-none-any.whl
Requirement already satisfied (use --upgrade to upgrade): pkg-resources==0.0.0 in ./env/lib/python3.5/site-packages (from -r requirements.txt (line 3))
Collecting pytz==2018.5 (from -r requirements.txt (line 4))
  Using cached https://files.pythonhosted.org/packages/30/4e/27c34b62430286c6d59177a0842ed90dc789ce5d1ed740887653b898779a/pytz-2018.5-py2.py3-none-any.whl
Installing collected packages: pytz, Django, jsonfield
Successfully installed Django-2.0.7 jsonfield-2.0.2 pytz-2018.5
(env) ~/Vehicle-Tracker (master) $ pip list
Django (2.0.7)
jsonfield (2.0.2)
pip (8.1.1)
pkg-resources (0.0.0)
pytz (2018.5)
setuptools (20.7.0)
```

Check if the packages installed in pip list are same as yours. We need these files for running the project.

Now we need to migrate our Database and runserver. Follow these steps:
```sh
(env) ~/Vehicle-Tracker (master) $ cd src/
(env) ~/Vehicle-Tracker/src (master) $ python3 manage.py migrate
Operations to perform:
  Apply all migrations: admin, auth, contenttypes, core, sessions
Running migrations:
  Applying contenttypes.0001_initial... OK
  Applying auth.0001_initial... OK
  Applying admin.0001_initial... OK
  Applying admin.0002_logentry_remove_auto_add... OK
  Applying contenttypes.0002_remove_content_type_name... OK
  Applying auth.0002_alter_permission_name_max_length... OK
  Applying auth.0003_alter_user_email_max_length... OK
  Applying auth.0004_alter_user_username_opts... OK
  Applying auth.0005_alter_user_last_login_null... OK
  Applying auth.0006_require_contenttypes_0002... OK
  Applying auth.0007_alter_validators_add_error_messages... OK
  Applying auth.0008_alter_user_username_max_length... OK
  Applying auth.0009_alter_user_last_name_max_length... OK
  Applying core.0001_initial... OK
  Applying core.0002_report... OK
  Applying core.0003_vehicle_report... OK
  Applying sessions.0001_initial... OK
(env) ~/Vehicle-Tracker/src (master) $ python3 manage.py runserver
Performing system checks...

System check identified no issues (0 silenced).
July 21, 2018 - 06:39:24
Django version 2.0.7, using settings 'vehicle_tracker.settings'
Starting development server at http://127.0.0.1:8000/
Quit the server with CONTROL-C.
```

If you see `Starting development server at http://127.0.0.1:8000/` this means our server is now hosted on localhost at port 8000. Now we can go to `localhost:8000` and browse the webapp.

### Running Tests

Unit tests are written in `tests.py` and can be run by `python3 manage.py test`
```sh
(env) ~/projects/Vehicle-Tracker/src (master) $ python3 manage.py test
Creating test database for alias 'default'...
System check identified no issues (0 silenced).
.....
----------------------------------------------------------------------
Ran 5 tests in 0.016s

OK
Destroying test database for alias 'default'...
````
