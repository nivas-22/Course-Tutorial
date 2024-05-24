
This Docker Tutorial blog will give you the conceptual & practical exposure to Docker - A new age containerization technology.

In this blog, we will focus on the below topics:

- What is Virtualization?
- What is Containerization
- Advantages of Containerization over Virtualization
- Introduction to Docker
- Benefits of Docker
- Virtualization vs Containerization

Docker is gaining popularity and its usage is spreading like wildfire. The reason for Docker’s growing popularity is the extent to which it can be used in an IT organization. Very few tools out there have the functionality to find itself useful to both developers and as well as system administrators. ==Docker is one such tool that truly lives up to its promise of== ==**Build**====,== ==**Ship**== ==and== ==**Run**====.==

In simple words, Docker is a software containerization platform, meaning you can build your application, package them along with their dependencies into a container and then these containers can be easily shipped to run on other machines.

_For example:_ Lets consider a linux based application which has been written both in Ruby and Python. This application requires a specific version of linux, Ruby and Python. In order to avoid any version conflicts on user’s end, a linux docker container can be created with the required versions of Ruby and Python installed along with the application. Now the end users can use the application easily by running this container without worrying about the dependencies or any version conflicts.

These containers uses Containerization which can be considered as an evolved version of Virtualization. The same task can also be achieved using Virtual Machines, however it is not very efficient.

I generally receive a question at this point, i.e. what is the difference between Virtualization and Containerization? These two terms are very similar to each other. So, let me first tell you What is Virtualization?

# What is Virtualization?

Virtualization is the technique of importing a Guest operating system on top of a Host operating system. This technique was a revelation at the beginning because it allowed developers to run multiple operating systems in different virtual machines all running on the same host. This eliminated the need for extra hardware resource. The advantages of Virtual Machines or Virtualization are:

- Multiple operating systems can run on the same machine
- Maintenance and Recovery were easy in case of failure conditions
- Total cost of ownership was also less due to the reduced need for infrastructure

![](https://miro.medium.com/v2/resize:fit:450/1*yvxERq0ax76gK6nK4RYr9A.png)

In the diagram on the left, you can see there is a host operating system on which there are 3 guest operating systems running which is nothing but the virtual machines.

As you know nothing is perfect, Virtualization also has some shortcomings. Running multiple Virtual Machines in the same host operating system leads to performance degradation. This is because of the guest OS running on top of the host OS, which will have its own kernel and set of libraries and dependencies. This takes up a large chunk of system resources, i.e. hard disk, processor and especially RAM.

Another problem with Virtual Machines which uses virtualization is that it takes almost a minute to boot-up. This is very critical in case of real-time applications.

**_Following are the disadvantages of Virtualization:_**

- Running multiple Virtual Machines leads to unstable performance
- Hypervisors are not as efficient as the host operating system
- Boot up process is long and takes time

These drawbacks led to the emergence of a new technique called Containerization. Now let me tell you about Containerization.

# What is Containerization?

Containerization is the technique of bringing virtualization to the operating system level. While Virtualization brings abstraction to the hardware, Containerization brings abstraction to the operating system. Do note that Containerization is also a type of Virtualization. Containerization is however more efficient because there is no guest OS here and utilizes a host’s operating system, share relevant libraries & resources as and when needed unlike virtual machines. Application specific binaries and libraries of containers run on the host kernel, which makes processing and execution very fast. Even booting-up a container takes only a fraction of a second. Because all the containers share, host operating system and holds only the application related binaries & libraries. They are lightweight and faster than Virtual Machines.

**Advantages of Containerization over Virtualization:**

- Containers on the same OS kernel are lighter and smaller
- Better resource utilization compared to VMs
- Boot-up process is short and takes few seconds

![](https://miro.medium.com/v2/resize:fit:765/1*cWUOGCEYmqBg12JVz2SvOA.png)

In the diagram on the left, you can see that there is a host operating system which is shared by all the containers. Containers only contain application specific libraries which are separate for each container and they are faster and do not waste any resources.

All these containers are handled by the containerization layer which is not native to the host operating system. Hence a software is needed, which can enable you to create & run containers on your host operating system.

Now, let me take you through the introduction to Docker.

# Introduction To Docker

Docker is a containerization platform that packages your application and all its dependencies together in the form of _Containers_ to ensure that your application works seamlessly in any environment.

![](https://miro.medium.com/v2/resize:fit:396/1*rVKaAVx02qU2CBK-ilcr9w.png)

As you can see in the diagram on the left, each application will run on a separate container and will have its own set of libraries and dependencies. This also ensures that there is process level isolation, meaning each application is independent of other applications, giving developers surety that they can build applications that will not interfere with one another.

As a developer, I can build a container which has different applications installed on it and give it to my QA team who will only need to run the container to replicate the developer environment.

# Benefits of Docker

Now, the QA team need not install all the dependent software and applications to test the code and this helps them save lots of time and energy. This also ensures that the working environment is consistent across all the individuals involved in the process, starting from development to deployment. The number of systems can be scaled up easily and the code can be deployed on them effortlessly.

# Virtualization vs Containerization

Virtualization and Containerization both let you run multiple operating systems inside a host machine.

Virtualization deals with creating many operating systems in a single host machine. Containerization, on the other hand, will create multiple containers for every type of application as required.

![](https://miro.medium.com/v2/resize:fit:792/1*tXpDazN2IkoaAJcqnKIKdA.png)

Virtualization vs Containerization - Docker Tutorial

As we can see from the image, the major difference is that there are multiple Guest Operating Systems in Virtualization which are absent in Containerization. The best part of Containerization is that it is very lightweight as compared to the heavy virtualization.