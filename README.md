# Data_Eng_project_2

## Group members : BERNADINE Léna 20190781 and BOUMRICHE Lydia 201901000

This GitHub repository contains the code of our Toxicity Application
We have 6 branches : main, Frontend, backend-app, Website, test_app, web-connection-app 

### Command to run the app :
- run the docker image

or

- Enter in a terminal : python website/toxic_app.py


### Task management 

We used trello to manage the project : https://trello.com/invite/b/bF3wnCwu/794628f72df0ec18d60fd075d0c5708b/data-engineering-project-2

## Source code management 

We used GitHub repository with different branches according to the task.
The repository contains dockerfile, docker-compose.yml and requirement.txt to dockerise the application. 

## Testing
the tests forlder contains files to test the app. 
The test_app.py file is used for unit test of necessary methods for our application. 
The test_integration .py app is used to test the proper functioning of the application via the interface.
We had problems to test a user requests example on the app. 

## Automation 
We use a Jenkinsfile to generate the script. However, we could make calls like run the application, but for testing, it doesn't find the path to import the create_app() methods.

![image](https://user-images.githubusercontent.com/71543467/156934833-bbc0b7ec-d3b9-46ef-845d-1a602046da50.png)

However, we could test our app on a terminal, with the command "pytest".


## Containarization

## Monitoring

We tried to use prometheus on our app. 
But we failed to display metrics.
