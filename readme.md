MasterMind

Welcome to mastermind game, my version of the game is developed using Django, Python, JavaScript and Ajax.

Game offers user default and custom version default version is just basic version of mastermind game.

In customized game users have option to adjust difficulty level up or down based on the settings they choose.

Game provides results of user input in color coded response where:
    1) red circle is correct number in correct position
    2) yellow circle is correct number in incorrect position
    3) white blank circle is wrong number
    4) order of circles is not same as user input

Installation guide:
    1) Create new directory anywhere in your system
    2) cd into newly created directory and clone github repo using terminal/command prompt or download code files from github and move them into newly created directory
    github repo: https://github.com/beqasabana/MasterMind
    note: pip3 and python 3 is required for game to run please refer to official sources for installation guide
    3) using terminal cd into same directory where game source code was cloned/downloaded
    4) lunch virtual environment using terminal command: pipenv shell
    5) we need to install requests library and django before we can run the game use following command: 
        pipenv install django request
    6) once django and requests packages are installed successfully cd into cloned/downloaded mastermind directory where main_app, manage.py and mastermind files are located
    7) to lunch the web app run following command: python manage.py runserver

    note: if django on your system is not configured to run on port 8000 use following command: python manage.py runserver 8000

    note: if static files cant load please clear your browsers cached images and files
