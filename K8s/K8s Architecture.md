
ontainers have become the definitive way to develop applications because they provide packages that contain everything you need to run your applications. In this blog, we will discuss Kubernetes architecture, the moving parts of Kubernetes and also what are the key elements, what are the roles and responsibilities of them in Kubernetes architecture.

# Kubernetes: An Overview

**Kubernetes** is an open-source Container Management tool that automates container deployment, container (de)scaling & container load balancing.

- Written on Golang, it has a huge community because it was first developed by Google & later donated to **CNCF**
- Can group ’n’ no of containers into one logical unit for managing & deploying them easily

**_Note_**_: Kubernetes is not a containerization platform. It is a multi-container management solution._

# Features Of Kubernetes

For a detailed explanation, check this [blog](https://medium.com/edureka/what-is-kubernetes-container-orchestration-tool-d972741550f6).

![](https://miro.medium.com/v2/resize:fit:1400/1*QFwMu3jkjWR8GBLd52O72Q.png)

Features of Kubernetes - Kubernetes Architecture

# Kubernetes Architecture/Kubernetes Components

![](https://miro.medium.com/v2/resize:fit:1400/1*P4cnZnT-XoXI-dATTSYIuw.png)

Components of Kubernetes Architecture - Kubernetes Architecture

Kubernetes Architecture has the following main components:

- Master nodes
- Worker/Slave nodes
- Distributed key-value store(etcd)

# Master Node

![](https://miro.medium.com/v2/resize:fit:480/1*oXozt5ISp6zc0p7SF4SqNQ.png)

Master Node of Kubernetes - Kubernetes Architecture

It is the entry point for all administrative tasks which is responsible for managing the Kubernetes cluster. There can be more than one master node in the cluster to check for fault tolerance. More than one master node puts the system in a High Availability mode, in which one of them will be the main node which we perform all the tasks.

For managing the cluster state, it uses **etcd** in which all the master nodes connect to it.

Let us discuss the components of a master node. As you can see in the diagram above it consists of 4 components:

**API server:**

- Performs all the administrative tasks through the API server within the master node.
- In this REST commands are sent to the API server which validates and processes the requests.
- After requesting, the resulting state of the cluster is stored in the distributed key-value store.

**Scheduler:**

- The scheduler schedules the tasks to slave nodes. It stores the resource usage information for each slave node.
- It schedules the work in the form of Pods and Services.
- Before scheduling the task, the scheduler also takes into account the quality of the service requirements, data locality, affinity, anti-affinity, etc.

**Controller manager:**

- Also known as **controllers**.
- It is a daemon which regulates the Kubernetes cluster which manages the different non-terminating control loops.
- It also performs lifecycle functions such as namespace creation and lifecycle, event garbage collection, terminated-pod garbage collection, cascading-deletion garbage collection, node garbage collection, etc.
- Basically, a controller watches the desired state of the objects it manages and watches their current state through the API server. If the current state of the objects it manages does not meet the desired state, then the control loop takes corrective steps to make sure that the current state is the same as the desired state.

**What is the ETCD?**

- etcd is a distributed key-value store which stores the cluster state.
- It can be part of the Kubernetes Master, or, it can be configured externally.
- etcd is written in the Go programming language. In Kubernetes, besides storing the cluster state (based on the **Raft Consensus Algorithm**) it is also used to store configuration details such as subnets, ConfigMaps, Secrets, etc.
- A raft is a consensus algorithm designed as an alternative to Paxos. The Consensus problem involves multiple servers agreeing on values; a common problem that arises in the context of replicated state machines. Raft defines three different roles (Leader, Follower, and Candidate) and achieves consensus via an elected leader

Now you have understood the functioning of the Master node. Let’s see what is the Worker/Minions node and its components.

# Worker Node (formerly minions)

![](https://miro.medium.com/v2/resize:fit:748/1*HPCVEBc9DyYeY-ddgESPSQ.png)

Worker Node of Kubernetes - Kubernetes Architecture

It is a physical server or you can say a VM which runs the applications using Pods (**a pod scheduling unit**) which is controlled by the master node. On a physical server (worker/slave node), pods are scheduled. For accessing the applications from the external world, we connect to nodes.

Let’s see what are the following components:

**Container runtime:**

- To run and manage a container’s lifecycle, we need a **container runtime** on the worker node.
- Sometimes, Docker is also referred to as a container runtime, but to be precise, Docker is a platform which uses **containers** as a container runtime.

**Kubelet:**

- It is an agent which communicates with the Master node and executes on nodes or the worker nodes. It gets the Pod specifications through the API server and executes the containers associated with the Pod and ensures that the containers described in those Pod are running and healthy.

**Kube-proxy:**

- Kube-proxy runs on each node to deal with individual host sub-netting and ensure that the services are available to external parties.
- It serves as a network proxy and a load balancer for a service on a single worker node and manages the network routing for TCP and UDP packets.
- It is the network proxy which runs on each worker node and listens to the API server for each Service endpoint creation/deletion.
- For each Service endpoint, kube-proxy sets up the routes so that it can reach to it.

# Pods

A pod is one or more containers that logically go together. Pods run on nodes. Pods run together as a logical unit. So they have the same shared content. They all share the same IP address but can reach other Pods via localhost, as well as shared storage. Pods don’t need to all run on the same machine as containers can span more than one machine. One node can run multiple pods.

# Use Case: How Luminis Technologies used Kubernetes in production

**Problem:** Luminis is a software technology company which used [AWS](https://www.edureka.co/blog/amazon-aws-tutorial/?utm_source=medium&utm_medium=content-link&utm_campaign=kubernetes-architecture) for deployment for their applications. For deploying the applications, it required custom scripts and tools to automate which was not easy for teams other than operations. Also, the small teams didn’t have the resources to learn all of the details about the scripts and tools.

**Main Issue:** There was no **unit-of-deployment** which created a gap between the development and the operations teams.

**Solution:**

**How did they Deploy in Kubernetes:**

![](https://miro.medium.com/v2/resize:fit:1400/1*XUe2JqXjQ1J-nmvol4h7aA.png)

Use Case of Deploying in Kubernetes - Kubernetes Architecture

They used a blue-green deployment mechanism to reduce the complexity of handling multiple concurrent versions. (As there’s always only one version of the application running in the background)

In this, a component called “**Deployer**” that orchestrated the deployment was created by their team by open sourcing their implementation under the Apache License as part of the Amdatu umbrella project. This mechanism performed the health checking on the pods before re-configuring the load balancer because they wanted each component that was deployed to provide a health check.

**How did they Automate Deployments?**

![](https://miro.medium.com/v2/resize:fit:878/1*WghBebTmo0vm9rJMkDijJA.png)

Automate Deployments - Kubernetes Architecture

With the **Deployer** in place, they were able to engage up deployments to a build pipeline. After a successful build, their build server pushed a new Docker image to a registry on Docker Hub. Then the build server invoked the **Deployer** to automatically deploy the new version to a test environment. That same image was promoted to production by triggering the **Deployer** on the production environment.