
# BriteCore FeatureRequests

This document details the process involved in implementing a solution to task given for the Britecore Software Engineer (Implementation) role.

The sections of the document are as below:
1.) About the project.
2.) Details of the tech stack.
3.) Setup and installation instructions.
4.) Deployment
5.) Author
6.) License


### About The Project
This project contains software written in Python as a solution to the Britecore Software Engineer (Implementation) task by the candidate:
Name: Ehigie Pascal Aito
Email: <aitoehigie@gmail.com>
Date: 03/23/2019

Feature Request is a simple web application for keeping records of feature requests from IWS customers.

## Tech Stack

* Server-Side: Python 3.7.2
* Microframework: Flask
* ORM: SqlAlchemy and SQLite3.
* Front-End: Bootstrap4
* JavaScript: KnockoutJS
* Host : Digitalocean with Docker and docker-compose
* Test : Pytest


### Setup & Installation Instructions

#####  Prerequisites

* Python 3.7.2
* Docker
* docker-compose

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


## Deployment
A sample of the project is presently running on a digitialocean droplet at: 

http://46.101.227.225:8000/index

Visit that URL to see it in action.

## Author

Ehigie (Pystar) Aito

## License

This project is licensed under the MIT License

