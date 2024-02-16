//README.md
# RestAPI

### Introduction 
This api is to test interaction between the user and browser with the use of specific endpoints and designated port

### Instalation (2-ways)

#### 1st-way (using IDE)

- Clone this repository https://github.com/kk3397/restapi/
- Create a new project with your favored IDE and run the .py file and interact locally

#### 2nd-way (with Dockerhub and terminal)
- Install Docker (install dockerhub from offical site)
- Pull docker image with docker pull kk3397/my_rest_api:v2
- Run the image with docker run -p 3000:3000 kk3397/my_rest_api:v2
*if this doesn't work check your defauilt host port using netstat

### Usage
- Install bottle with pip install focker
- Install python3 in the same fasion
- The port should run through 3000

### Endpoints

| HTTP Verbs | Endpoints | Action |
| --- | --- | --- |
| POST | / | A simple welcome screen is displayed
| POST | /area/rec | Gets the area of a rectangle with parameters width and length |
| POST | /area/tri | Gets the area of a triangle with parameters width and length |
| POST | /perm/rec | Gets the perimeter of a rectangle with parameters width and length |
### Used Technologies

Docker https://www.docker.com/
Docker Hub https://hub.docker.com/

### Author
Kengo Kobayashi https://github.com/kk3397

