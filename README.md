# Currency README

Application fetches data about currencies rates and provides API endpoint with current rates data. 
(I made design decision to make available only last rates via API).
Rates are fetched regularly from: https://www.ecb.europa.eu/home/html/rss.en.html

Project uses Sqlite DB.

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

### Clone repo
`git clone https://github.com/stan7123/sunscrapers.git .`

### Install python dependencies
* `pip install -r requirements.txt`

### Run database migrations
python manage.py migrate

### Create admin account
python manage.py createsuperuser

### Run server
python manage.py runserver --noreload (avoid running many schedulers)

### Run tests
TODO

## API

### Example API call for
Just call `http://localhost:8000/api/v1/currency/` to see the list or `http://localhost:8000/api/v1/currency/[BASE_TICKER]/[TARGET_TICKER]/` for specific rate.


### Settings
You can configure interval for rates fetching in settings under: `RATES_FETCH_INTERVAL_IN_MINUTES`

#TODO:
* Tests for fetching data - no more logic to test actually
* Maybe put out some swagger API description. Although for these a simple endpoints it seems redundant.
