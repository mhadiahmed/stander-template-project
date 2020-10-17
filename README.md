# follow the instractions


## create virtualenv

- clone the project to your pc

- install virtualenv if not in your system by execute the following command in cmd or powershell after run it as Administrator
  `pip install virtualenv`

- create virtual enviroment execute the following
    `virtualenv venv`

- activate virtual enviroment on windows execute the following
    `.\Scripts\activate`

- the install the requierments file
   `pip install -r requirements.txt`

- then run the migrations 
   `python manage.py migrate`

- create super user

    `python manage.py createsuperuser`

- finllay run the server
    `python manage.py runserver`