# Numbers API

### Endpoints

- POST unpaired/ - send array

##### request data
```
{
    "data": [1, 5, 3, 5, 3, 1, 6]
}
```
##### response data
```
{
    "answer": 6
}
```

- GET statistic/ - get results
##### response data
```
[
    {
        "number": 6,
        "count": 1
    }
]
```

### Installing
1. Clone project
```
git clone git@github.com:arseniysychev/numbers_api.git
```
2. Enter cloning folder 
```
cd numbers_api
```
3. Create environments file ".env" with env variables
- DJANGO_SETTINGS_MODULE - django settings module
- SECRET_KEY - A secret key for a particular Django installation. This is used to provide cryptographic signing, and should be set to a unique, unpredictable value.

example
```
DJANGO_SETTINGS_MODULE=project.settings.production
SECRET_KEY=v733e&jnd7@-a*q$9zps$-a06vtj(pks$h(k36!x&1*p@u3uh+
```
4. Create virtualenv
```
python3 -m venv .venv
```
5. Activate created virtualenv
```
source .venv/bin/activate
```
6. Install requirements for project
```
pip install -r requirements.txt
```
7. Make migrations
```
./manage.py makemigrations
```
8. Apply migrations
```
./manage.py migrate
```
9. Run django tests
```
./manage.py test
```
10. Run django server
```
./manage.py runserver
```
