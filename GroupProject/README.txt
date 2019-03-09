you will need to install python which should include pip before you can start

Directions might be different on a windows computer. You van visit the Django site for more information.
( Here's a link to a youtube video on django install for Windows user: https://youtu.be/MEcWRk9w0t0 )

P.S. You need to install Python before installing Django. The website has information also on this. 

How to install Django 

pip install django



How to install virtualenv 

Pip install virtualenv


How to start virtual environment - need to do this before you start the dango sever

cd to …Cosc484/Group project
source env/bin/activate (This is not needed in Windows if you follow the instruction in the youtube video)

You should see (env) before your command prompt 


How to Start app

cd MessageApp
python3 manage.py migrate (for Windows: python manage.py migrate)
python3 manage.py runserver (for Windows: python manage.py migrate)

If you get no errors then go to your browser and type in 127.0.0.1:8000

You should see project set up page