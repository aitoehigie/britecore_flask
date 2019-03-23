
# BriteCore FeatureRequests

This documentation details the process involved in solving the test for the Britecore Software Engineer (Implementation) role.

The sections are as below:
1.) About the project
2.) Setup Instructions
3.) Details of tech stack
    * Reasons behind the choice of items in the tech stack.
4.) Details of the HTTP endpoints, methods,  arguments passed in and results returned.
5.) Details of how the search function as implemented works.
    * HTTP method used
    ** Endpoint created for the search function
6.) TODOs
7.) License


### About The Project
This project contains software written in Python as a solution to the Britecore Software Engineer (Implementation) task by the candidate:
Name: Ehigie Pascal Aito
Email: <aitoehigie@gmail.com>
Date: 03/23/2019

Feature Request is a simple web application for making records of feature requests from IWS customers

## Tech Stack

* Server-Side: Python 3.7.2
* Microframework: Flask
* ORM: SqlAlchemy and SQLite3.
* Front-End: Bootstrap4
* JavaScript: KnockoutJS
* Host : Digitalocean with Docker and docker-compose
* Test : Pytest


### Prerequisites

* Python 3.7.2
* Docker
* docker-compose



### Setup & Installation Instruction

First clone the repository

```
git clone git@github.com:aitoehigie/britecore-flask.git
```

```sh
$ cd britecore-flask
$ docker-compose build
$ docker-compose up -d
```
The commands above will install all the dev dependencies in the "requirements.txt", configure the Python flask API and setup the sqlite database.
Navigate to <http://localhost:8000> to start interacting with the endpoints.


## Running the tests

In this project I use the unittest for automated testing and you can see in tests folder. For the running; just run this command ;

```
python -m unittest discover
```
You can see the results whether test OK or FAIL.

## Deployment
A sample of the project is presently running on a digitialocean droplet at: 

http://46.101.227.225:8000/index

Visit that URL to see it in action.

## Author

Ehigie (Pystar) Aito

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details
