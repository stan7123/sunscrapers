# Currency README

Application fetches data about currencies rates and provides API endpoint with this data. 

Rates are fetched regularly from: https://www.ecb.europa.eu/home/html/rss.en.html

### Data fetching
Fetching is done by Python scheduler initialized during app init.
Other options of periodic fetching:
* If there was Celery already in the project, I would use Celery's periodic task for this to not introduce another lib/tech. Running celery just for this simple task would be overkill in my opinion.
* Use cron or windows scheduler (os dependent)

## Development environment installation

### System requirements
* Python >=3.6

### Create virtualenv
* `python -m venv /path/to/venv`

### Install python dependencies
* `pip install -r requirements.txt`

### Run database migrations
./manage.py migrate

### Create admin account
./manage.py createsuperuser

### Run server
./manage.py runserver --noreload (to not start many schedulers)

### Run tests
...

## API

### Example API call for
Write about API here or give link to swagger... 
* `curl -H "Content-Type: application/json" -X POST -d '{"email":"alama@kotaduzego.pl","username":"alama","password1":"XYab31415","password2":"XYab31415"}' 127.0.0.1:8000/api/v1/register/`

