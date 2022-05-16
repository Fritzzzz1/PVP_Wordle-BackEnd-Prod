To run a local copy of the app :

## Clone repository : 
git clone https://github.com/Fritzzzz1/PVP_Wordle-BackEnd-Prod

## Make a new virtual environment
mkvirtualenv <project_name> // virtualenv <project_name>

## Activate virtual environment
workon <project_name> // ./scripts/activate.ps1

## Install requirements
pip install -r requirements.txt

## create .env file and add SECRET_KEY= '<Your Secret Key>'

## Start the development server
python manage.py runserver
