
**What is Service in Kubernetes ?.**

📌 A service in Kubernetes is an abstraction that defines a logical collection of Pods (groups of one or more container instances) and a policy for accessing them. Services enable you to separate application code from the network, ensuring that your application components communicate with one another in a dependable and scalable manner.

📌**Labels and Selectors**: Label selectors are used by services to identify which Pods to include. The labels on the Pods are defined by you, and the service selects the Pods based on these labels. This makes it simple to group and manage Pods that serve a specific purpose.

📌**Load Balancing:** Services provide load balancing for the Pods they target. When you create a service, Kubernetes assigns it a virtual IP address (ClusterIP) that is used to route traffic to one or more Pods associated with the service. This load balancing can be helpful for distributing incoming traffic and ensuring high availability.

**There are three types of service available**

1. **ClusterIP**: Makes the service available via an internal IP address that is only accessible from within the cluster. It’s good for intra-cluster communication.
2. **NodePort**: Makes the service available via a static port on each Node’s IP address. This makes the service externally available, but you may require an external load balancer to deliver traffic to the relevant Nodes.
3. **Load Balancer**: Provisions an external load balancer (if supported by your cloud provider) to distribute traffic to the service automatically. This is often used for services that require internet access.
4. **What is ClusterIP ?.**

▶ The ClusterIP service is the standard Kubernetes service.

▶ It provides a service within your cluster that other apps within your cluster can use.

▶ It restricts application access within the cluster and prevents external access.

▶When a front-end app has to communicate with a back-end system.

▶Within the cluster, each ClusterIP service is assigned a unique IP address.

**ClusterIP Diagram:-**

![](https://miro.medium.com/v2/resize:fit:1374/1*MPawztFvOInikofGsb0XnQ.png)

**Cluster IP Hands-on :-**

**How to Create ClusterIP and TAG the Cluster IP into the POD**

**vi clusterip.yaml**

---  
apiVersion: v1  
kind: Service  
metadata:  
  name: nginxclusterip  
spec:  
  type: ClusterIP  
  ports:  
  - name: httpd  
    port: 80  
    targetPort: 80  
    protocol: TCP  
  selector:  
    app: webapp  
---  
  
apiVersion: v1  
kind: Pod  
metadata:  
  name: webserver  
  labels:  
    app: webapp  
    tier: backend  
spec:  
  containers:  
  - name: nginx-web  
    image: nginx  
    ports:  
      - containerPort: 80  

![](https://miro.medium.com/v2/resize:fit:1400/1*aF0-9NibH4bCTweKND_aaA.png)

**Validation Steps:-**

I have logged into the container and trying to access the Cluster IP to ensure the webpage is accessible or not.

Now Webpage in Accessible

![](https://miro.medium.com/v2/resize:fit:1400/1*zHedWII_D7Ren9OZ4tt1Kw.png)

**2. What is Node Port ?.**

▶ NodePort opens a specified port on all cluster Nodes and redirects any traffic received on this port to internal services.

▶ When front end pods have to be exposed outside the cluster for consumers to access, this is useful.

▶ NodePort is built on top of the ClusterIP service by exposing it outside of the cluster.

▶ NodePort must be in the range 30000–32767.

▶ If this port is not specified, a random port will be provided. It is suggested that k8s assign this port automatically.

![](https://miro.medium.com/v2/resize:fit:1400/0*ZU-j92YiRTe13uH0.JPG)

**NodePort Hands-on :-**

vi node-service.yml

  
vi node-service.yml ---> open the file and add the below content into the file in order to create the NodePort   
  
---  
apiVersion: v1  
kind: Namespace  
metadata:  
  name: webapptier1  
  
---  
apiVersion: v1  
kind: Service  
metadata:  
  name: nodeportservice  
  namespace: webapptier1  
spec:  
  type: NodePort  
  ports:  
  - port: 80  
    targetPort: 80  
    nodePort: 30005  
    protocol: TCP  
  selector:  
    app: web-app  
---  
  
apiVersion: v1  
kind: Pod  
metadata:  
   name: webapp  
   namespace: webapptier1  
   labels:  
     app: web-app  
spec:  
 containers:  
 - name: webapp1  
   image: nginx  
   ports:  
    - containerPort: 80

Execute the below commands in Order to create nodeport service.

 kubectl create -f node-service.yml

![](https://miro.medium.com/v2/resize:fit:1400/1*NwY9aeF9BWGNRb7oKjBHzg.png)

**Validation Steps:-**

Let me check the IP address of the AKS Worker node.

 kubectl get nodes -o wide

![](https://miro.medium.com/v2/resize:fit:1400/1*iNeSDv34JCajVQGzKAQOuA.png)

**Validate and Ensure NodePort service is working:-**

**Validation 1**:- I am trying to access the webpage using AKS worker Node IP address with different port which not configured. — Not Accessible because we have configured port 30005 not 30006.

**Validation 2**:- I am trying to access the webpage using AKS worker Node IP address with 30005 — Accessible

curl http://10.10.0.5:30005  

![](https://miro.medium.com/v2/resize:fit:1400/1*bgeUyVGP8-FFd3c8x_LB9w.png)

**3. Load Balancer:-**

In most cases, you do not explicitly build a Load Balancer in an Azure Kubernetes Service (AKS) cluster. When you expose a Kubernetes Service of type LoadBalancer, AKS and Other Cloud provider controls the construction of a Load Balancer for you.

![](https://miro.medium.com/v2/resize:fit:1200/0*iHBPwMCvoXOdnr16.gif)

The following Yaml file will be used to create in Load Balancer in

root@vm-jumpbox:~# vi LB.yml (open the file and add the below content into the file in order to create the LoadBalancer)  
---  
apiVersion: v1  
kind: Namespace  
metadata:  
  name: facebook  
---  
apiVersion: v1  
kind: Pod  
metadata:  
  name: webserver  
  namespace: facebook  
  labels:  
    role: web-service  
spec:  
  containers:  
  - name: nginx  
    image: nginx  
    ports:  
    - containerPort: 80  
---  
apiVersion: v1  
kind: Service  
metadata:  
  name: web-service  
  namespace: facebook  
  labels:  
    role: web-service  
spec:  
  selector:  
    role: web-service  
  type: LoadBalancer  
  ports:  
  - port: 80  
root@vm-jumpbox:~#

root@vm-jumpbox:~# kubectl create -f LB.yml  
namespace/facebook created  
pod/webserver created  
service/web-service created  
  
root@vm-jumpbox:~# kubectl get svc --namespace facebook  
NAME          TYPE           CLUSTER-IP   EXTERNAL-IP      PORT(S)        AGE  
web-service   LoadBalancer   10.2.0.78    52.228.115.207   80:30235/TCP   32s  
  
root@vm-jumpbox:~# kubectl get pods  --namespace  facebook  
NAME        READY   STATUS    RESTARTS   AGE  
webserver   1/1     Running   0          59s  
root@vm-jumpbox:~#

![](https://miro.medium.com/v2/resize:fit:1400/1*srSM66QF1a6r8DuYDWOprg.png)

**Validation:-**

From Azure Console: —

We can the see the two IP address are configured in the Load balance. the one start 4.172.0.114 configured as default as part of AKS cluster setup.

The Second one which is configured after we executed the LB.yml file ( Which contains the creation of Load Balancer service and NameSpace and tag the Load Balancer into the POD.

![](https://miro.medium.com/v2/resize:fit:1400/1*MPNOri4hWzQUZTVTcgbo6A.png)

![](https://miro.medium.com/v2/resize:fit:1400/1*AkU4ev7vIVBFpk6sJ-35XA.png)