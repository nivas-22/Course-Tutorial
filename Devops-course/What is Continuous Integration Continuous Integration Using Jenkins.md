

Continuous Integration is a development practice where developers integrate code into a shared repository frequently where each integration is verified by an automated build and automated tests. It is the most important part of DevOps that is used to integrate various DevOps stages. In this blog, we will deal with the problems developers face while writing, testing and delivering software to end users and how they solve it using CI.

In this blog, we will focus on the below topics:

1. Traditional Integration
2. Problems with Traditional Integration
3. What is Continuous Integration?
4. Benefits of Continuous Integration
5. Requirements for CI System
6. What is Jenkins — The Ultimate CI Tool
7. Demo on Continuous Integration Using Jenkins

# Traditional Integration

In Traditional Integration or/software development cycle,

- Each developer gets a copy of the code from the central repository.
- All developers begin at the same starting point and work on it.
- Each developer makes progress by working on their own or in a team.
- They add or change classes, methods, and functions, shaping the code to meet their needs, and eventually, they complete the task they were assigned to do.
- Meanwhile, the other developers and teams continue working on their own tasks, changing the code or adding new code, solving the problems they have been assigned.
- If we take a step back and look at the big picture, i.e. the entire project, we can see that all developers working on a project are changing the context for the other developers as they are working on the source code.

The main factors that can make these problems escalate:

- The size of the team working on the project.
- The amount of time passed since the developer got the latest version of the code from the central repository.

![](https://miro.medium.com/v2/resize:fit:1050/1*Adozcnj29DrsfioQe5XUlA.png)

# Problems With Traditional Integration

![](https://miro.medium.com/v2/resize:fit:1050/1*eVYU40ErK70deEW3rIf3Ew.png)

# What’s the Solution for Problems faced in Traditional Integration?

So, below are the **steps** to solve the above problems:

![](https://miro.medium.com/v2/resize:fit:1050/1*um0JZSj02TwQG0XLys0XdA.png)

So, let us see what exactly is Continuous Integration?

# What is Continuous Integration?

**We will Start with the Martin Fowler’s Definition:**

> Continuous Integration is a software development practice where members of a team integrate their work frequently, usually, each person integrates at least daily leading to multiple integrations per day. Each integration is verified by an automated build (including test) to detect integration errors as quickly as possible. Many teams find that this approach leads to significantly reduced integration problems and allows a team to develop cohesive software more rapidly.
> 
> **– Martin Fowler**

![](https://miro.medium.com/v2/resize:fit:729/1*VnLbmBU7OIbWV1VrBtIfrg.png)

Automating your build, test and deploy processes can increase the problems commonly happening on projects. So we should have a reliable method of integrating that will ensure that the errors can be found sooner than later.

Let’s move on and see what are the benefits of Continuous Integration.

# Benefits of Continuous Integration

![](https://miro.medium.com/v2/resize:fit:1050/1*z8ZLwRy2YtTBLS-aIlrxIw.png)

1. **Reduced Integration Risk:** Often, working on projects means multiple people are working on the separate tasks or parts of the code which makes it risky to integrate. Debugging and solving the issue can be really painful and can potentially mean a lot of changes to the code. Integrating more frequently can help reduce these kinds of problems to a minimum.
2. **Higher Code Quality:** Focusing more on the functionality of the code results in a higher quality product.
3. **The Code in Version Control works:** If you commit something that breaks the build, you and your team get the notice immediately and the problem is fixed before anyone else pulls the “broken” code.
4. **Reduced friction between team members:** Having the impartial system in place reduces the frequency of quarrels among team members.
5. **Easy for QA Team:** Having different versions and builds of the code can help isolate and trace bugs efficiently, and it makes life easier for the QA team.
6. **Less time deploying:** Deploying projects can be very tedious and time-consuming, and automating that process makes perfect sense.

# Requirements for CI System

![](https://miro.medium.com/v2/resize:fit:1050/1*BGaFsnSSyMAFfXuF7rkJ3w.png)

But you might be wondering what are the requirements for the installing of the CI system for your needs. If you want to install CI server in your own environment, you’ll need a few things first.

- **Version control system (VCS)**. It provides a reliable method to centralize and preserve changes made to your project over time.
- **Virtual Machine:** For onsite solutions, you should have a spare server or at least a virtual machine. for a clean machine to build your system on is of the essential importance.
- **Hosted CI Tool solutions:** To avoid servers or virtual machines, you can go for hosted CI tool solutions that help in the maintenance of the whole process and offers easier scalability.
- **Tools:** If you opt-in for the self-hosted variant, you will need to install one of the many available continuous integration tools like Jenkins, TeamCity, Bamboo etc.

# What is Jenkins — The Ultimate CI Tool

Jenkins is an open source automation tool written in Java with plugins built for Continuous Integration purpose. Jenkins is used to build and test your software projects continuously making it easier for developers to integrate changes to the project, and making it easier for users to obtain a fresh build. It also allows you to continuously deliver your software by integrating with a large number of testing and deployment technologies.

With Jenkins, organizations can accelerate the software development process through automation. Jenkins integrates development life-cycle processes of all kinds, including build, document, test, package, stage, deploy, static analysis and much more.

Jenkins achieves Continuous Integration with the help of plugins. Plugins allow the integration of Various DevOps stages. If you want to integrate a particular tool, you need to install the plugins for that tool. **For example** Git, Maven 2 project, Amazon EC2, HTML publisher etc.

The image below depicts that Jenkins is integrating various DevOps stages:

![](https://miro.medium.com/v2/resize:fit:1050/1*nQgPUMBV-pAD-rv28ze47w.jpeg)

# Demo on Continuous Integration Using Jenkins

A company named Sanders & Fresco Private Ltd. got the project from a client which consisted of 4 modules. The Project manager divided these modules between two developers. Now to maintain the consistency in the flow of the project, they built a _Continuous Delivery Pipeline_ where they executed all the modules in terms of jobs (a single job will have two modules). After building those jobs, they synced it in a pipeline. They also checked the build at regular intervals of time while they were developing their project. So, the path of the project which was in git hub repository was provided through Jenkins. Using the concept of CI, they built their project after a fixed interval of time which can be defined by build trigger option in Jenkins.

So, let us see how we can do this using Jenkins.

**Step 1:** Open the Jenkins on your designated port number in your VM.

![](https://miro.medium.com/v2/resize:fit:1050/1*R178oBH6pXwV5hbqaZ572g.png)

**Step 2:** Click on New Item to create a new Job.

![](https://miro.medium.com/v2/resize:fit:1050/1*XAuW79UGxmhaClPamlqEeg.png)

**Step 3:** Give the name of Freestyle Project. Here I have given Job1.

![](https://miro.medium.com/v2/resize:fit:1050/1*9r7P2ECW2CofyE5YAdxuXg.png)

**Step 4:** Now go to **Source Code Management-> Git**. Fill the project path to pull the project from Git and Click on Apply.

![](https://miro.medium.com/v2/resize:fit:1050/1*3qH4FZZI9u58OzyHW5dkfQ.png)

**Step 5:** Click on Build Now.

![](https://miro.medium.com/v2/resize:fit:1050/1*f3e7jAF93aNHaQH0AN33dg.png)

**Step 6:** The Job1 will start building it.

![](https://miro.medium.com/v2/resize:fit:1050/1*fRHSlJR3OqNfauDQ23oe8g.png)

**Now we will create a project/Job2 which will build after a fixed interval of time (i.e. after every minute) which we can define by using Poll SCM.**

**Step 7:** Click on New Item to create a new Job.

![](https://miro.medium.com/v2/resize:fit:1050/1*A-6AgaijKiQRePXB9e1vxA.png)

**Step 8:** Give the name of Freestyle Project. Here I have given Job2.

![](https://miro.medium.com/v2/resize:fit:1050/1*M-NuY5iIzbLZEodW9h-UKA.png)

**Step 9:** Now go to **Source Code Management-> Git**. Fill the project path to pull the project from Git and Click on Apply.

![](https://miro.medium.com/v2/resize:fit:1050/1*uYIHBERZR1Dv2KH_B2vjiw.png)

**Step 10:** Then go to **Build Trigger -> Poll SCM**. Enter ” * * * * * ” to build the Job2 after every minute and click on Apply.

![](https://miro.medium.com/v2/resize:fit:1050/1*s52s2uwrVWHiYrFhAiYLlA.png)

After clicking on Apply, a message will be displayed. Click on **Save** button.

![](https://miro.medium.com/v2/resize:fit:1050/1*h4nWq9JIEe52AtDOwNewIw.png)

**Step 11:** Click on Build Now.

![](https://miro.medium.com/v2/resize:fit:1050/1*UNTzCcAzOGwcGyWwr5KkbQ.png)

**Step 12:** The Job2 will start building after every minute.

> **Note:** To check for build status, Click on **Git Polling Log.** This will show details of Job2 i.e. the time at which it got built.

![](https://miro.medium.com/v2/resize:fit:1050/1*W0u2uv3VsxxkDv01d2lO3Q.png)

**Now, we will be building a Jenkins Pipeline to show Continuous Delivery.**

**Step 13:** Now go to Jenkins homepage by clicking on Jenkins.

![](https://miro.medium.com/v2/resize:fit:1050/1*Unr6m3md9_l7XvU4qkfxIA.png)

**Step 14:** Click on “+” to create a pipeline view.

![](https://miro.medium.com/v2/resize:fit:1050/1*xIyPvbCYhks6vqTapm4G6w.png)

**Step 15:** Name the view and check mark **“Build Pipeline View”** and Click on OK.

![](https://miro.medium.com/v2/resize:fit:1050/1*QelPZuOUVCxjwCPTDXGEMQ.png)

**Step 16:** Go to **Pipeline Flow** and add **Job1** in **Select Initial Job.** Click on OK.

![](https://miro.medium.com/v2/resize:fit:1050/1*jcWDrBLLOjzkBEtVVG2qXQ.png)

**Step 17:** Now Click on Job1.

![](https://miro.medium.com/v2/resize:fit:1050/1*vTGS92pJylkQJ8JeSK7VPA.png)

**Step 18:** Then Click on **Configure**.

![](https://miro.medium.com/v2/resize:fit:1050/1*44UWQ21dxQVoIXNfCiU5Fg.png)

**Step 19:** Go to **Post-build Actions** and select **Build other projects.** Add Job2 in Projects to build and checkmark the “**Trigger only if the build is stable**“. Click on **Save**.

![](https://miro.medium.com/v2/resize:fit:1050/1*oxeK9pbwOOreTjcWtikH4w.png)

**Step 20:** Now Click on Job2 and click on **Configure**.

![](https://miro.medium.com/v2/resize:fit:1050/1*WV-E_KbnJGs-9xf7fVJ_sg.png)

**Step 21:** Go to **Build Triggers ->** Select **Build after other projects are built.** Add Job1 in Projects to watch label.

![](https://miro.medium.com/v2/resize:fit:1050/1*7ZgrdDuWO_OXeQd145PgGw.png)

**Step 22:** Click on the **pipeline1** view you created.

![](https://miro.medium.com/v2/resize:fit:1050/1*0z1_skdHSfGtUhZBJupaQw.png)

**Step 23:** Click on **Run.** Job1 will start building.

![](https://miro.medium.com/v2/resize:fit:1050/1*VajfWitz7e6BZt_OUnrtug.png)

After building Job1, Job2 will automatically build itself.

![](https://miro.medium.com/v2/resize:fit:1050/1*-T5YkLkl0KKfKKSf2KDQ2Q.png)

So, this was all about the What Is Continuous Integration and its implementation using Jenkins.