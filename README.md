# Random Story Generator

Projet aiming to return to the user a random short story comprised of a beginning and an end, where the sotries are put together with the use of microservices.

## Index

1. [Brief](#brief)
2. [Trello Board](#trello)
3. [Risk Assessment](#riskassessment)

4. [Architecture](#architecture)
   + [Entity Relationship Diagrams(ERDs)](#ERD)
   
5. [Testing](#testing)

6. [Deployment](#deployment)

7. [Front End Design](#design)

8. [Future Improvements](#improvements)


<a name="brief"></a>
## 1. The Brief 
   The project intends to fulfill the brief provided in week six of training.
   The requirements include: 
+ A Kanban board;
+ Application to be fully integrated using the Feature-Branch model;
+ Project must follow Micro Services architecture;
+ Project must be deployed using containerisation and an orchestration tool;
+ Must create an Ansible Playbook to provision the environment that the application needs to run.


<a name="trello"></a> 
## 2. Trello Board

As shown in  the figure below, Trello has been used to keep track of the progress across its duration.

The project started by defining the user stories, which have been added as a reminder of the project scope and its deliverables, hence serving the role of product backlog as well. 

The project  itself has been split in 4 major sprints(lasting a week each). In order to make tracking of progress easier and to monitor the time left until the deadline, the sprints have been assigned different colours starting with green, which represents the first sprint and ending with red, which represents the last sprint. The image below represents the Trello board at the beginning of the project, right after the sprints have been divided into individual tasks. 

 <a name="riskassessment"></a>
 ## 3. Risk Assessment
 
| Risk ID       | Risk Description   | Mitigation     | Likelyhood of occurrence |  Possible Impact  | Impact at occurrence| 
|:-------------:|:------------------:|:--------------:|:------------------------:|:-----------------:|:-------------------:|
| 1    | Unstable internet connection | Work on small, individual parts of the project, to avoid being dependent on the internet connection. When unavailable, work on the project management part. | 4 | Not being able to deliver the project in time, pushing back some of the tasks that require internet.| 3|
| 2    | Data compromised on the workstation | Make frequent back ups of the project, set up an account password, and ensure computer is locked when leaving the station.  | 2 | Having to start the project/parts of the project from scratch, missing out on possible crucial information previously included| 4|
| 3    | Security breach of the databases | Ensure a strong password is selected, encrypt the data, and hash the passwords. | 3 | Depending on what stage of the process it occurs at, its impact varies. If it happens in the first half of the project, may consist in small delays, if it's happening in the second half of the project, it might push back the other steps.| 5|
| 4    | Exhausting the free trial offered by GCP | Keep track of all the instances used, making sure to delete/terminate the ones that are not useful for the project, and stopping the instances when not in use. | 1 | Having to start the project/parts of the project from scratch, missing out on possible crucial information previously included| 5 |
| 5    | Difficulty understanding the material  | Pay attention to the material taught in class. Follow up on the supplemental materials provided, and practice when given the opportunity. Always ask for help if needed. | 3 | Delivering a poor project due to the lack of not understanding the brief/ not knowing how to execute the project| 4|
| 6    | Not being able to complete the project in time | Keeping track of the project management timeline using the Trello board, making sure to complete/start at least a task daily.  | 2 | Falling behind with the weekly tasks, randomly working on different other parts of the project, not boxing off particular sections of it | 5|
