# Short Story Idea Generator

Projet aiming to return to the user a random short story idea, with the aid of microservices. 

## Index

1. [Brief](#brief)
2. [Trello Board](#trello)
3. [Risk Assessment](#riskassessment)

   3.1. [Initial Risk Assessment](#initialrisk)
   
   3.2. [Final Risk Assessment](#finalrisk)
   
   3.3. [Risk Assessment Matrix](#riskmatrix)

4. [Architecture](#architecture)

   4.1. [Feature Branch Model](#featurebranchmodel)
   
   4.2. [Service Architecture Diagram](#servicediagram)
   
   4.3. [Deployment](#deployment)

   
5. [Testing](#testing)

6. [Front End Design](#design)

7. [Retrospective](#retrospective)

   7.1. [What Went Well?](#good)
   7.2. [What Went Wrong?](#bad)
   7.3. [Future Improvements](#improvements)


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

As shown below, Trello has been used to keep track of the progress across its duration. The MoSCow Prioritisation Method has been used in order to identify key areas of development, thus allowing for a functional product to be presented as early as possible, increasing the complexity of the project once the minimum viable product is met. 

The project started by defining the user stories, which have been added as a reminder of the project scope and its deliverables, hence serving the role of product backlog as well. 

The project itself has been split in just one sprint, as it was only meant to be a three week long process. The image below represents the Trello board at the beginning of the project. It can be observed in the right side of the board that there are no bugs present in the project at this stage.

![alt text][trello1]
 
[trello1]:  https://i.imgur.com/5n2onCw.png " Initial Trello Board"

As the project has advanced, the tasks started moving across the board from left to right, until they eventually all reached the 'Done' column. Bugs column has also been slowly populated by the various issues that arose during the duration of the project. This final state of the board can be observed in the figure below. 

![alt text][trello2]
 
[trello2]:  https://i.imgur.com/cAu3URT.png " Initial Trello Board"


 <a name="riskassessment"></a>
 ## 3. Risk Assessment
  <a name="initialrisk"></a>
 ## 3.1. Initial Risk Assessment
The project started by creating an initial risk assessment as shown below. As the project went on, new risks started appearing as well as current risks changing their likelyhood of occurrence at it got closer to the end of the project.
 
| Risk ID       | Risk Description   | Mitigation     | Likelyhood of occurrence |  Possible Impact  | Impact at occurrence| 
|:-------------:|:------------------:|:--------------:|:------------------------:|:-----------------:|:-------------------:|
| 1    | Unstable internet connection | Work on small, individual parts of the project, to avoid being dependent on the internet connection. When unavailable, work on the project management part, or documentation. | 4 | Not being able to deliver the project in time, pushing back some of the tasks that require internet.| 3|
| 2    | Data compromised on the workstation | Make frequent back ups of the project and ensure computer is locked when leaving the station unattended. Ensure version controlling any changes at the end of each day.  | 2 | Having to start the project/parts of the project from scratch, missing out on possible crucial information previously included. | 4|
| 3    | Security breach of the database | Ensure a strong password is selected, encrypt the data and set up strong firewall rules. | 3 | Not much impact, as just the results of the randomiser application are stored in the database. | 1|
| 4    | Exhausting the free trial offered by GCP | Keep track of all the instances used, making sure to delete/terminate the ones that are not useful for the project, and stopping the instances when not in use. | 3 | Not being able to deliver parts or the full project, due to the lack of access to the free trial. | 5 |
| 5    | Difficulty understanding the material  | Pay attention to the material taught on a daily basis. Follow up on the supplemental materials provided, and practice when given the opportunity. Keep on top of the work by using the video tutorials and the courseware. | 3 | Delivering a poor project due to not understanding the brief/ not knowing how to execute the project. | 4|
| 6    | Not being able to complete the project in time | Keeping track of the project management timeline using the Trello board, making sure to complete/start at least a task daily.  | 2 | Falling behind with the weekly tasks, randomly working on different other parts of the project, not boxing off particular sections of it, hence not meeting the agile principles. | 5|


  <a name="finalrisk"></a>
 ## 3.2. Final Risk Assessment
 
| Risk ID       | Risk Description   | Mitigation     | Likelyhood of occurrence |  Possible Impact  | Impact at occurrence| 
|:-------------:|:------------------:|:--------------:|:------------------------:|:-----------------:|:-------------------:|
| 1    |Unstable internet connection | Work on small, individual parts of the project, to avoid being dependent on the internet connection. When unavailable, work on the project management part, or documentation. | 4 | Not being able to deliver the project in time, pushing back some of the tasks that require internet. | 3 |
| 2    | Data compromised on the workstation | Make frequent back ups of the project and ensure computer is locked when leaving the station unattended. Ensure version controlling any changes at the end of each day.  | 2 | Having to start the project/parts of the project from scratch, missing out on possible crucial information previously included. | 4|
| 3    | Security breach of the database | Ensure a strong password is selected, encrypt the data and set up strong firewall rules.  | 3 | Not much impact, as just the results of the randomiser application are stored in the database. | 1|
| 4    | Exhausting the free trial offered by GCP | Keep track of all the instances used, making sure to delete/terminate the ones that are not useful for the project, and stopping the instances when not in use.  | 5 | Not being able to deliver parts or the full project, due to the lack of access to the free trial. | 5|
| 5    | Difficulty understanding the material | Pay attention to the material taught on a daily basis. Follow up on the supplemental materials provided, and practice when given the opportunity. Keep on top of the work by using the video tutorials and the courseware.  | 3 | Delivering a poor project due to not understanding the brief/ not knowing how to execute the project. | 4|
| 6    | Not being able to complete the project in time | Keeping track of the project management timeline using the Trello board, making sure to complete/start at least a task daily.  | 3 | Falling behind with the weekly tasks, randomly working on different other parts of the project, not boxing off particular sections of it, hence not meeting the agile principles. | 5|
| 7    | Falling ill | Work from home, do not leave the house unless necessary. Wash hands immediately after entering the house, disinfect the groceries if necessary.  | 4 | Not being able to work, lacking focus, potentially getting admitted into hospital, and therefore not being able to deliver a project. | 5|
| 8    | GCP connection issues | Work on the database/virtual machines part of the project in the morning, at hours that it is less likely that traffic is high. Focus on documentation during the day, and resume the work in the afternoon.   | 4 | Not being able to work on the main parts of the project, not being able to get help from the trainer regarding the more complicated parts of it. Delivering only the documentation part, hence not being able to pass the project. | 4|
 
 
  <a name="riskmatrix"></a>
 ## 3.3. Risk Assessment Matrix
 
A risk matrix is a matrix that is used during the risk assessment process to define the level of risk by considering the category of probability or likelihood against the category of consequence severity. This is a simple mechanism to increase visibility of risks and assist management decision making.
 
![alt text][riskmatrix]
 
[riskmatrix]:  https://i.imgur.com/hKCCSIJ.png " Risk Assessment Matrix"


  <a name="architecture"></a>
 ## 4. Architecture
 
   <a name="featurebranchmodel"></a>
 ## 4.1. Feature Branch Model
 The project consists of 2 branches, to ensure code quality across the duration of the project. These branches can be observed in the figure below, the main one being the master branch, and the one on which the new features were added before the final delivery of the project, the developer branch. 
 
 ![alt text][featurebranch]
 
[featurebranch]:   https://i.imgur.com/DGnFz6i.png " Feature Branch Model"

 The project starts at point A, with a basic architecture of the four services on the master branch as a clean starting point. The developer branch is then created at point B, and all the features are then created on this branch, up until point C, where it is merged back into the master branch. Point D finally represents the final stage of the process. As the project consists of three virtual machines, the same process has been followed for the Jenkins node, up until the final commit, when it has been merged onto this repository, to have a full overview of the project in one place. 
 
   <a name="servicediagram"></a>
 ## 4.2. Service Architecture Diagram
 
   The application consists of four services as shown in the image below. The first service is responsible of hosting the front end of the application, as well as of ensuring there is an active connection with a MySql database to ensure data persistency. 
   The second and third services are simply generating two random parts of a story, chosen from a set list, which are then merged together into one string in the fourth service. This is then recalled by the first service, added to the database and displayed then to the user. 
 
 
![alt text][servicediagram]
 
[servicediagram]:  https://i.imgur.com/e5s7yRS.png " Risk Assessment Matrix"

   <a name="deployment"></a>
 ## 4.3. Deployment
   The deployment of the application uses the toolsets covered in training, focusing on the application's ability to scale the resources needed, as well as its portability. The application rests on three virtal machines: a manager one, a master node and a worker node. This approach has been chosen due to its modularity and ease of maintenance. The master node comprises of Jenkins and Ansible and aims to deploy the necessary dependencies onto the master node. A jenkins pipeline has been implemented, this consisting of installing the set dependencies and deploying the Docker Stack onto the manager and worker node. The architecture of the VMs can be observed in the figure below. 
   
![alt text][VMs]
 
[VMs]:  https://i.imgur.com/tqVx3GB.png "VM architecture"

  
   
    
   
   
   
   
