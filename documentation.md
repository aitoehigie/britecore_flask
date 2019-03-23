# HelloFresh Senior Backend Developer Test Solution




This documentation details the process involved in solving the HelloFresh Senior Backend Developer test. The sections are as below:
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
This project contains software written in Python as a solution to the Hellofresh Senior Backend Developer test by the candidate:
Name: Ehigie Pascal Aito
Email: <aitoehigie@gmail.com>
Date: 03/11/2019

### Setup & Installation Instruction

```sh
$ cd aitoehigie-api-test
$ docker-compose build
$ docker-compose up -d
```
The commands above will install all the dev dependencies in the "requirements.txt", configure the Python flask API and setup the Redis database.
Navigate to <http://localhost:5000/recipes> to start interacting with the API endpoints.

## Tech stack details


#### Web stack: I created a microframework in Python with the following: 
- The standard WSGI Python library .
- WebOb library (Requests and Response objects): I used this library to wrap around HTTP requests and response objects in the API framework.
- Gunicorn (a battle test WSGI server that runs the API [api.py]): this is a production ready WSGI server and is better than anything I could have written myself.
- Ratelimiting library to prevent abuse from consummers of the API. This limits requests to 5 requests/15 minutes.
- WSGI CORS Middleware library: I incorporated this into my REST API framework to enable Cross Site Origin Requests. As CORS is the standard way to do cross domain AJAX calls (for browsers that support it).

This microframework which I call "hellofresh.py" can be found in the web directory of my project folder was used to create a HTTP REST API which I put in api.py. It responds to HTTP requests and returns JSON responses.

#### Data storage
- Redis database: I chose this because of its ease of use and also because it can be used as a queue and cache.
- Redis python library: makes it easy to interact with the Redis database from Python code.
- Serialized Redis Interface (this makes it a serialization to and from the redis database extremely easy).
- A dbtools library in the utils directory. I implemented this to handle the Redis db connections and teardowns.


#### Caching
- lru_cache decorator from the functools standard Python library. I used this to decorate all the HTTP endpoints so subsequent HTTP requests receive a faster response because the initial response has been cached. The reason for choosing it is for speedups.

#### Testing
- I used py.test to create test cases, fixtures and clients to test the HTTP endpoints.

#### Authentication
- The authentication scheme supported by the API is Basic HTTP Authentication where the user sends a token and is authenticated against details stored in the Redis database for protected routes.
- 
#### REST API HTTP ENDPOINTS
| Name   | Method     | URL Protected     |
| :------------- | :----------: | -----------: |
|  List | GET /recipes    | No    |
| Create  | POST /recipes | Yes |
| Get | GET /recipes/{id} | No |
| Update | PUT/PATCH /recipes/{id}|Yes |
| Delete| DELETE /recipes/{id}|Yes|
| Rate | POST /recipes/{id}/rating|No|
| Search | Search /recipes/{id}| No|

These endpoints return valid JSON objects as returns from the callbacks. Any method not supported by each endpoint will return an error if called.
Supported REST methods are:
* GET
* POST
* PUT/PATCH
* DELETE





### Todos

 - Write MORE Tests
 - Add async support
 - Pagination

License
----

MIT


**Free Software, Hell Yeah!**
