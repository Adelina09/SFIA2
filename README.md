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
   
   4.4. [Technologies Used](#technologies)

   
5. [Testing](#testing)

6. [Front End Design](#design)

7. [Retrospective](#retrospective)

   7.1. [What Went Well?](#good)
   
   7.2. [What Went Wrong?](#bad)
   
   7.3. [Future Improvements](#improvements)

8. [Installation guide](#installation)


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


Further tracking of the project progress and its results has been performed separately, on paper(for convinience). Due to the limitations of this file, if evidence is needed, please request it personally. 

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

  The application has initially been constructed on the master node, where the testing of the application has also been performed. After having a simple model of the application, docker has been installed on the local machine, and images of the services have been created and deployed on Docker Hub. The Docker compose file has been created, services deployed, followed by the creation of a docker stack. This has connected the master node to a worker node, and thus the services have been deployed between the two nodes to ensure redundancy. This has all then been automated using Jenkins on the manager node. To ensure that all the nodes have the necessary dependencies installed, Ansible has also been added to the manager node. Thus Jenkins deploys Ansible across the other two nodes and starts the application. 
  The process is shown in the diagram below. 
   
 INSERT DIAGRAM HERE
 
 
   <a name="technologies"></a>
  ## 4.4. Technologies Used
  
  * GitHub: Version Control System
  * Jenkins: Continuous Intergration Server
  * Google Cloud Services: Live Environment + SQL Database Host
  * Visual Studio Code: IDE for frontend and backend development
  * Trello: Kanban board and Project tracking
  * Docker: Containerisation
  * Docker Swarm + Stack: Orchestration
  * Dockerhub: Version Control for Docker Images and Containers
  * Ansible: Configuration Management

   
     <a name="testing"></a>
 ## 5.Testing
   The application has been tested using pytest. The unit testing conducted includes URL as well as database testing. The latter consists of testing the select, insert and delete function by inserting a test sample and manipulating it to test the functions. 
   The image below represents the final test coverage of the application. It can be observed that the coverage stops at only 38%. It is believed that this is due to a combination of a high number of libraries tested and a limited amount of test functions implemented. 
   
   ![alt text][tests]
 
[tests]:        https://i.imgur.com/Wa3S5Ju.png "Successful tests"

   
   ![alt text][coverage]
 
[coverage]:     https://i.imgur.com/qV8poZl.png "Coverage report"
   
   
   Due to various complications that arose throughout the duration of the project, the testing phase is not implemented within Jenkins. It has been conducted on the local machine only, this being one of the future improvements feature. 
   
   
   <a name="design"></a>
 ## 6. Front end design 
 
 The front end design of this project is simplistic, as seen in the image below. 
 
   ![alt text][frontend]
 
[frontend]:    https://i.imgur.com/jaCEkqi.png "Front end design"

The button on the right hand side of the page gives the user the ability to generate a new short story idea. Every time the button is pressed, the entry is recorded in a database and saved as a reminder of all previous ideas. 
As a future update on the front end, it is desired that the content saved in the database to be deplayed to the user, as a reminder of the previous stories they might have started to write. A thematic background is also desired to be implemented, along with a user option to add their name to the story, hence to receive a personalised story. 
   

   
 <a name="retrospective"></a>
 ## 7. Retrospective 
  <a name="good"></a>
 ## 7.1. What Went Well
 
   * Project complete in time 
   * Implemented Jenkins
   * Deployed Docker Swarm with little to no issues
   * Deployed the application on three different VMs, having Jenkins and Ansible separate from the rest of the application
   
   
     <a name="bad"></a>
 ## 7.2. What Went Wrong
   
   * Major issues when trying to SSH into the other VMs using Jenkins
   * Bank Holiday Weekend made it hard to ask for help with the said issue 
   * Deleting and re-creating the entire project, two days before the deadline
   * Issues setting up the Manager node on VirtualBox, hence having to resort to using another VM on GCP
   
      <a name="improvements"></a>
 ## 7.3. Future Improvements 
 
  * Further development of the front end of the application
  * Integrating testing within Jenkins script
  * More test cases implemented, testing the fuctionality of the randomising button amongst them 
  * Increasing coverage report
  * NGINX implementation
  * CRUD implementation 
  * Selenium testing 
 

    <a name="installation"></a>
 ## 8. Installation guide 
### Before Installation

  * Google Cloud Platform account 
  * Git Hub account

### Creating the virtual machines
Navigate to GCP's Compute Engine menu, followed by VM Instances menu. From here, you will be creating one virtual machine with a distinct name, e.g. manager and the operating system set to UBUNTU 18.04. Make sure to tick the "allow http traffic" box in the firewall section before you create the machine. Now SSH into the newly created machine, and create a set of ssh keys using the "ssh-keygen" command. Copy the content of the public key file(id_rsa.pub) and keep it in a safe place for further use.

Whilst you are still inside the virtual machine, install Jenkins using this [link](https://linuxize.com/post/how-to-install-jenkins-on-ubuntu-18-04/). When done, access the public ip address in a browser, folowed by ":8080". Now you have just accessed the Jenkins user interface. From here, follow the instructions on screen and set up Jenkins using your credentials. 

The final thing to be installed on this virtual machine is Ansible. Follow this [link](https://www.howtoforge.com/how-to-install-and-configure-ansible-on-ubuntu-1804/), and then you are done. 

Now go back to GCP and create another virtual machine, with the same UBUNTU 18.04 operating sysyem, but this time name it master. After its creation, navigate to the VPC Network menu on GCP, followed by Firewall Rules menu. Here we are setting up the firewall rules needed for the application to work. 

Create a new firewall rule named jenkins, and navigate to the part where it allows you to set specified protocols and ports. Here you tick the first option, and you set it to 8080 to allow jenkins to function on your other machines. Create one more firewall rule named flaskapp and for this one allow a range of ip addressess, from 5000 to 5004. 

Now navigate back to your master VM, press edit, and make sure to add your firewall rules to the network tags section. Before you press save, bring back the public key saved from before, and add it in the SSH keys section. Now save the VM. Before you go back to the main VM list, in the top right corner you can press "create similar" and now you have a third VM, this one having the same set up as the previous one. Call this one worker. Before any further steps, ensure you have openjdk-8 installed on all your VMs using this command "sudo apt install openjdk-8-jdk -y".

Once all your VMs are set up, go into your master node, and clone down the repository found at this [address](https://github.com/Adelina09/SFIA2.git). Similarly, go into the manager node and clone down this other [repository](https://github.com/Adelina09/SFIA2-Ansible.git). Ensure you change your IP addresses and the location of your own private keys in the inventory.cfg file before running any commands. 

After setting up your IP addresses, run the ansible playbook. This will install all the dependencies needded for your application to function. Now you can run the docker compose file from the master VM and now you will have the application running. 

If you want to set up the Jenkins pipeline, follow [these steps](https://dzone.com/articles/jenkins-03-configure-master-and-slave) to set your nodes, and then follow the usual steps to create the pipeline. Don't forget to set the agents to none in the Jenkinsfile and to mention on which VM you want the stage to take place. 

