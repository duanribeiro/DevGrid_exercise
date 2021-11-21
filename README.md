# Full Stack Code Assessment Challenge
![python3.7](https://img.shields.io/badge/python-3.7-brightgreen.svg)  ![redis.x](https://img.shields.io/badge/redis-6.2.6-red.svg)

Design and build a wrapper for the Open Weather API current weather data service that returns a city's temperature, with caching, also allowing for the temperature of the latest queried cities that are still validly cached to be retrieved.


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
| `OPENWEATHER_ENDPOINT`   | `https://api.openweathermap.org/data/2.5/weather` | Endpoint used to fetch data from Open Weather API |
| `OPENWEATHER_APIKEY`     | `your_secret_api_password`                        | The API key is a unique identifier that authenticates requests associated with your project for usage and billing purposes. |
| `CACHE_TTL_SECONDS`      | `300`                                             | Time to live (TTL) is an integer value that specifies the number of seconds until the cached key expires. |
| `DEFAULT_MAX_NUMBER`     | `5`                                               | Default value from max number of queried cities that are still valid |
| `REDIS_ENDPOINT`         | `redis`  `192.168.0.10`                           | Redis host address |
| `REDIS_PORT`             | `6379`                                            | Redis host port |


##### Create and run the images:

```
$ docker-compose up
```


It will deploy 2 docker containers:

- wrapper_api: Flask app running in [http://localhost:5000/swagger](http://localhost:5000/swagger).
- redis: Redis container for app cache

## TESTING

```
$ python -m unittest discover .\tests\
```
