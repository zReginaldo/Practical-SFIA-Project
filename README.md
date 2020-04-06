# Practical-SFIA-Project

## Contents 
* [Project Breif](#ProjectBreif)
* [Introduction](#Introduction) 
* [Planning](#Planning)
* [Use Cases](#UserCases)
* [Risk Analysis](#RiskAssesment) 
* [Front End Design](#Design) 
* [Testing](#Testing)
* [CI Pipeline & Deployment](#Deployment) 
* [Project Conclusion](#Conclusion) 
* [Future Work](#FutureWork) 

<a name="Introduction"></a>
# Introduction 
## Project Breif
* The general outline of this project was to use concepts from previous training modules such as, **Software Development with Python**, **Continuous Intergration** and **Cloud Fundamentals** to create a micro-service orientated Flask application. 

* This application had to be composed of at least 4 services that work together, two services that would generate a **random** object, the following service will create another object based on the results of the two services using logic, and lastly the final service will be responsible for communicating with the other 3 services, adn also persisting some data in an SQL database. The project required us to deploy this application using Docker and Jenkins. 

### My Solution 
My final solution for the project at hand was to create an application based on the popular TV show COUNTDOWN, where the **Top two** services would produce random numbers and letters, The **Main** service would then take the results, apply logic and post the results to a HTML web page, having the **Final** service take the information posted on to the HTML page and store this into a database.  

<a name="Planning"></a>
## Planning
The best couse of action for initiating this project was to set out a plan that would clearly state the duringation of time i would have to compleate the project, along with the tasks that need to be done so that i stay on track. I decided that using MS Project as my projecet planning technology was the best course of action. The Gantt chart below neatly displays the project deliverables and timeframe on when to compleat each task. 


![Gantt Chart](https://github.com/zReginaldo/PracticalSFIAProject/blob/master/Documentation/Main_Plan.PNG)

<a name="Risk"></a>
## Risk Analysis





![](https://github.com/zReginaldo/PracticalSFIAProject/blob/master/Documentation/Risk%20Assesment.PNG)





