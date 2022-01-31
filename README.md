# Contact Details Application

WebServer and Database run in different docker containers on AWS instance. 

# Implementation
We separated a simple contact details application into two micro services, the database and the web server. The micro services will be containerized using docker and deployed on EC2 instance in Amazon Web Services.

Flask, a micro web framework written in Python is used in this lab for creating the micro services and RESTful API. This API in url format, pointing towards the database IP address or DNS (Domain Name Service) which in this case is the EC2 instance where the database container deployed with port 5000 exposed.

## Application Architecture
![arch_main](https://user-images.githubusercontent.com/55482580/151801802-5a90eec4-6209-44c5-aacf-52c63c883b67.png)
                         
                         Fig. Main architecture of "Contact Recording Application"
                         
The figure above depicts the architecture of the application. Two docker containers were deployed on an AWS EC2 instance. Each container represents a microservice. The database server is responsible for retrieving, entering and changing data from/to/in the database. It has three APIs to communicate with the other microservice which is the web-server.


The web-server container is designed to host the web application. It interacts with users. All the user requests go through the web-server, which makes it a proxy server in a sense. In the web-server, other functionalities can be implemented since it is separated from the database. Any change in the web-server has no effect on the database microservice, which makes the application scalable. The webserver is the entry point to access the application.

## Webserver
The web server has multiple API endpoints that point to the database in a separate machine/container. We exposed port 80 to be used like a web-server.
Several API routes were created as follows:
1. base API route, ’/’ is pointing to "index.html" to display the front-end.
2. contacts API route, ’/contacts’ is to retrieve all the data to be displayed on the table
3. add entry API route, ’/add_entry’ is to submit a new data using POST method with json payload towards the back-end database.
4. delete API route, ’/delete’ is to delete a data by sending json payload using POST method towards the back-end database.

## Database
The back-end or database micro service was implemented in the same way as the web server using flask to provide several API to be accessed.

# Deployment
The deployment of these micro services was done on Amazon EC2 instance with docker image. The first step is to create a docker image using the Dockerfile and then run the container on with required configuration.
![image](https://user-images.githubusercontent.com/55482580/151803041-655e4739-0e64-4bf4-985b-afe67ad535f6.png)

                          Main interface of the aplication
                          
![image](https://user-images.githubusercontent.com/55482580/151803153-76814fd2-f617-403d-8fa7-065b6457e767.png)

                          Accessing Database APIs

# Experiment
We were experimenting by separating the application into 3 microservices (front-end, back-end, and database) instead of 2 (web-server and database). It was resulting a slower response from the application as it has more APIs communication overhead.
