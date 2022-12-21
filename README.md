# IndStats

Applicatiesysteem voor het indienen van paspoort- en visumaanvragen.

Functionaliteit:

* Gebruikerslogin
* Applicatie list view
* Applicatie creation form
* Statistics

## Demo

Het e.e.a. uitleggen over:

* Frontend
* Urls
* Views
* Database tables

## Run lokaal

### Setup virtual env

```bash
git clone https://github.com/jerwinwieser/indstats.git
cd indstats
python3 -m venv env
source env/bin/activate
pip3 install -r requirements.txt
```

### Run server

```bash
python3 manage.py migrate
python3 manage.py runserver
```

## Zie remote

[indstats.herokuapp.com](https://indstats.herokuapp.com/)
