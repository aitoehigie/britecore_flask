
# BriteCore FeatureRequests

Feature Request is a simple web application for making records of feature requests from IWS customers

## Tech Stack

* Server-Side: Python 3.6
* Microframework: Flask
* ORM: Sql-Alchemy (SQLite3)
* Front-End: Bootstrap4
* JavaScript: KnockoutJS
* Continuous Integration: Travis-CI
* Host : Heroku
* Test : Pytest


### Prerequisites

Existing Python 3.6 installation

### Installation

First clone the repository

```
git clone git@github.com:aitoehigie/britecore-flask.git
```

After that install the requirements via pip and pipenv

```
pipenv --python 3.6
pipenv shell
pipenv run pip install -r requirements.txt
```

If everything goes smooth all you have to do run below command in project root;

```
python app.py
```

You will see that some information project and host and port number (most probably like that  * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit))
When you open a browser and type 127.0.0.0.1:5000 you will see the project running.

## Running the tests

In this project I use the unittest for automated testing and you can see in tests folder. For the running; just run this command ;

```
python -m unittest discover
```
You can see the results whether test OK or FAIL.

## Deployment

## Author

Ehigie (Pystar) Aito

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details
