# Full Stack Code Assessment Challenge
![python3.7](https://img.shields.io/badge/Python-FFD43B?style=for-the-badge&logo=python&logoColor=darkgreen)
![redis](https://img.shields.io/badge/redis-%23DD0031.svg?&style=for-the-badge&logo=redis&logoColor=white)
![AWS](https://img.shields.io/badge/Amazon_AWS-FF9900?style=for-the-badge&logo=amazonaws&logoColor=white)
![Docker](https://img.shields.io/badge/Docker-2CA5E0?style=for-the-badge&logo=docker&logoColor=white)
![Swagger](https://img.shields.io/badge/Swagger-85EA2D?style=for-the-badge&logo=Swagger&logoColor=white
)

Design and build a wrapper for the Open Weather API current weather data service that returns a city's temperature, with caching, also allowing for the temperature of the latest queried cities that are still validly cached to be retrieved.


## PROJECT STRUCTURE
The project structure is based on the official [Flask RESTPlus scaling your project](https://flask-restplus.readthedocs.io/en/stable/scaling.html#multiple-apis-with-reusable-namespaces)


```
.
├── main
│   ├── helpers
│   │   └── redis.py
│   ├── __init__.py
│   └── resources
│       ├── __init__.py
│       └── openweather
│           ├── __init__.py
│           ├── routes.py
│           ├── test_request_by_citY_name.py
│           └── test_request_temperature.py
├── main
│   ├── base.py
│   ├── test_config.py
│   ├── serializers.py
│   └── services.py
├── .dockerignore
├── .gitignore
├── app.py   
├── config.py
├── docker-compose.yml
├── Dockerfile
├── README.md
└── requirements.txt
```
##### Folders

* `main` - All the RESTful API implementation is here.
* `main/helpers` - Useful function for working with redis cache.
* `tests` - All the tests used on API.

##### Files
* `main/__init__.py` - Resource agroupment for all `v1` [Namespaces](https://flask-restplus.readthedocs.io/en/stable/scaling.html#multiple-namespaces).
* `main/resources/__init__.py` - The Flask Application factory (`create_app()`).  
* `config.py` - Config file for envs, global config vars and so on.
* `Dockerfile` - Dockerfile used to build a Docker image.
* `.dockerignore` - Lists files and directories which should be ignored while Docker build process.
* `.gitignore` - Lists files and directories which should not be added to git repository.
* `requirements.txt` - All project dependencies.
* `app.py` - The application entrypoint.

## RUNNING ON CLOUD
You can check this application live running on AWS cloud using Lambda functions: [My Cloud App](https://9rrecyhtw4.execute-api.us-east-1.amazonaws.com/dev/swagger)

## RUNNING ON DOCKER

##### Requirements
Make sure you have already installed both [Docker Engine](https://docs.docker.com/get-docker/) and [Docker Compose](https://docs.docker.com/compose/install/). You don’t need to install Python or Redis, as both are provided by Docker images.

##### Clone the repository 

```
$ git clone https://github.com/duanribeiro/DevGrid_exercise.git
$ cd DevGrid_exercise
```

##### Add Environment Variables

A file called `docker-compose.yml` contains all environment variables.
Variables declared in file have the following format: `ENVIRONMENT_VARIABLE=value`.

In order for Flask to run, there must be set `OPENWEATHER_ENDPOINT, OPENWEATHER_APIKEY, CACHE_TTL_SECONDS, DEFAULT_MAX_NUMBER` variables declared.


| Variable                 | Default                                           | Discussion  |
| ---------------          |-------------                                      | -----|
| `OPENWEATHER_ENDPOINT`   | `https://api.openweathermap.org/data/2.5/weather` | Endpoint used to fetch data from Open Weather API. |
| `OPENWEATHER_APIKEY`     | `your_secret_api_password`                        | The API key is a unique identifier that authenticates requests associated with your project for usage and billing purposes. |
| `CACHE_TTL_SECONDS`      | `300`                                             | Time to live (TTL) is an integer value that specifies the number of seconds until the cached key expires. |
| `DEFAULT_MAX_NUMBER`     | `5`                                               | Default value from max number of queried cities that are still valid. |
| `REDIS_ENDPOINT`         | `redis`  `localhost`                           | Redis host address. |
| `REDIS_PORT`             | `6379`                                            | Redis host port. |


##### Create and run the images:

```
$ docker-compose up
```


It will deploy 2 docker containers:

- wrapper_api: Flask app running on [http://localhost:5000/swagger](http://localhost:5000/swagger) with self-documented interactive API.
- redis: Redis container for app cache

## TESTING
Unittest supports simple test discovery. In order to be compatible with test discovery, all of the test files must be importable from the top-level directory of the project.
```
$ python -m unittest discover .\tests\
```
