# DjangoRestBlog 


![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg)
![HTML and CSS](https://img.shields.io/badge/HTML%20and-CSS-1f425f.svg)
[![Open in Visual Studio Code](https://img.shields.io/static/v1?logo=visualstudiocode&label=&message=Open%20in%20Visual%20Studio%20Code&labelColor=2c2c32&color=007acc&logoColor=007acc)](https://github.dev/Nayemjaman/DjangoRestBlog)
</hr>

Dockerize a blog API Implementing Multiple User Type Registration using Django rest-auth.

## Key Features 
1. Docker.
2. Django rest fremwork</br>
3. PostgreSQL for database.</br>
3. Implement CRUD operations for blog posts by a particular user, </br>
4. Implement features for user interaction with blog posts, including upvoting posts and adding comments. </br>
5. Multiple User. </br>
6. Swagger UI.</br>



## Built With

```
Django==4.1.3
django-ckeditor==6.5.1
django-cors-headers==3.14.0
django-environ==0.10.0
django-js-asset==2.0.0
django-rest-knox==4.2.0
django-taggit==3.1.0
djangorestframework==3.14.0
djangorestframework-simplejwt==5.2.2
drf-spectacular==0.26.2
Pillow==9.4.0
psycopg2-binary==2.9.6
PyJWT==2.6.0

```
## Requirements

- Python
- Django 
- Django REST Framework 
- PostgreSQL 
- Docker 
- Git 
- .env 

Docker hub
      - https://hub.docker.com/r/nayemjaman/djangorestblog
      
Docker Pull Command
 ``` 
docker pull nayemjaman/djangorestblog
 ```

### Swagger UI
Swagger UI is a popular tool for documenting and testing APIs. It provides a user-friendly interface that allows developers to quickly explore and understand the functionality of an API. In a Django Rest Framework project, using Swagger UI can enhance the documentation and testing of the API, making it easier for developers to interact with the API and ensuring that the API meets the project requirements. Additionally, Swagger UI can simplify the integration of the API with other services, as the documentation provided by Swagger can help other developers understand how to consume the API.

![Screenshot (159)](https://user-images.githubusercontent.com/40755491/236793377-7ebd8cf1-996d-477b-8523-32a3bbba7810.png)

### Why Django Rest Framework?
For creating web APIs, Django Rest Framework (DRF) is a potent tool. 
It is constructed using the well-liked Django web framework. 
It enables programmers to quickly develop APIs that can be used by a variety of clients, 
including desktop, mobile, and web apps. DRF offers a wide range of tools for constructing and testing
APIs and makes it simple to create APIs with complicated functionality, such as authentication, authorization, and data validation. 
Using DRF, 
developers can concentrate on creating the logic for their applications rather than spending time on the specifics of an API's implementation. Because of this, it's a great option for creating scalable and reliable online APIs.

Users may test and use their APIs rapidly with DRF's browsable API interface, which it also offers. Debugging, troubleshooting, and providing documentation and examples to other developers who might be using the API can all be facilitated by doing this. Moreover, DRF provides a number of serialization options, enabling programmers to quickly return data in multiple formats like JSON or XML. Django Rest Framework is a useful tool for anyone trying to create solid and dependable web APIs in general.



### Several reasons why I  want to dockerize a Django Rest Framework blog API:

1. Portability: Dockerizing your API allows you to package it into a container that can be run on any machine that supports Docker, regardless of the underlying operating system or software installed. This makes it easier to deploy and run your API in different environments, such as development, staging, and production.

2. Consistency: Docker provides a consistent runtime environment for my API, ensuring that it runs the same way every time, regardless of where it's deployed. This can help avoid issues caused by differences in the underlying software stack, such as different versions of Python or database drivers.

3. Scalability: Docker makes it easy to scale your API horizontally by running multiple instances of the container on different machines or in a cluster. This can help to handle increased traffic or load without having to manually manage multiple instances of your API.

4. Security: Docker provides a layer of isolation between API and the host operating system, which can help improve security by reducing the attack surface and limiting the impact of any vulnerabilities that may be present in code.

Overall, dockerizing your Django Rest Framework blog API can make it easier to manage, deploy, and scale, while also improving consistency and security.



