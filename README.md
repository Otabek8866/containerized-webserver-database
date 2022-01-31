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
