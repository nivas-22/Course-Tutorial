
Docker is an open source platform that enables developers to build, deploy, run, update and manage containerized applications.

Docker Images is a read-only template containing a set of instructions for creating a container that can run on the Docker platform.

Docker container encapsulate the application, its dependencies, and the runtime environment in a self-sufficient package.

Docker Hub is a cloud-based registry service that allows you to store and share Docker images. It hosts a vast collection of images that can be used as base images for building custom images.

**Prerequisites:**

a. one Linux EC2 instance with docker installed.

— yum install docker -y

— sudo systemctl start docker

— sudo systemctl status docker

b. Create a inbound rule with port 8080 on EC2 Security Group.

**1.** **Steps to pull image from Docker hub:**

i. First check if any images are present.

docker images

![](https://miro.medium.com/v2/resize:fit:874/1*FRE6H515aChqrZm8g9p2bg.png)

ii. Now execute below command to pull latest nginx image from dockerhub.

docker pull nginx

![](https://miro.medium.com/v2/resize:fit:875/1*lUiS_viYVEVpKgrLWpHxcw.png)

![](https://miro.medium.com/v2/resize:fit:875/1*EaLfKl_EZwGYAqH30XEBaA.png)

**2.** **Customise the image:**

i. Create a new folder and a create new dockerfile inside that folder.

![](https://miro.medium.com/v2/resize:fit:845/1*kEo9jWANUwVzXvsBnc5Cpw.png)

mkdir website  
cd website  
vi Dockerfile (copy below lines inside the file)  
FROM nginx  
COPY index.html /usr/share/nginx/html  
COPY title.png /usr/share/nginx/html  
EXPOSE 8080  
CMD ["nginx", "-g", "daemon off;"]  

ii. Add index.html and title.png files inside website folder.

Sample files are available in below github page:

https://github.com/Vaishu-psv/Vaishu-psv.github.io.git

![](https://miro.medium.com/v2/resize:fit:538/1*gilGH8gJvJa8AaRFqeLYsA.png)

docker build -t custom-nginx .

![](https://miro.medium.com/v2/resize:fit:875/1*CfZKGfjpBw1Z6wu1zYbchg.png)

iv. Now we can see new image created.

![](https://miro.medium.com/v2/resize:fit:875/1*b5CEHh2O2v5pUcj68voADw.png)

**3.** **Build a container out of new image:**

i. Create a container out of new image generated in previous step.

docker run -d --name <name-container> -p 8080:80 <new_image_name>

![](https://miro.medium.com/v2/resize:fit:875/1*hd3QubGYaDvKWPtLsGYLaw.png)

ii. To verify if container is running or not, use below command:

Docker ps

![](https://miro.medium.com/v2/resize:fit:875/1*If1SCQhjk1HPxEj-Jmv6Uw.png)

iii. Check if website is working or not in ec2 using below command:

curl -v localhost:8080

![](https://miro.medium.com/v2/resize:fit:875/1*j0m4KY75e6z84jA-PAtSDA.png)

iv. We can also view website through browser using below command:

http://public_ip_dns:8080

![](https://miro.medium.com/v2/resize:fit:875/1*Ecpet3h587fwz8p7V2gEFQ.png)

**4.** **Push the customized image to DockerHub:**

i. Log into DockerHub.

![](https://miro.medium.com/v2/resize:fit:875/1*7cFZtvVxuhrKDRnZkNOSOA.png)

ii. Create a new Repository inside DockerHub.

![](https://miro.medium.com/v2/resize:fit:875/1*L781Y-NSZxccVNhXQPgWzQ.png)

iii. Now login to Docker hub in ec2.

docker login -u <docker username>

![](https://miro.medium.com/v2/resize:fit:875/1*780uuqmn8ASCQ-rrUFbS-w.png)

iv. To commit a container’s file changes or settings into a new image, execute below command:

docker commit <container id> <dockerhub username/docker hub repo name:tag name

![](https://miro.medium.com/v2/resize:fit:875/1*WSpkyMA8JwbuSqssQVL1Ew.png)

v. Now push the new image into Dockerhub using below command:

docker push dockerhub_username/docker_repo:tag_name

![](https://miro.medium.com/v2/resize:fit:875/1*PxdrzK3VQIOAtWjxy5UFcw.png)

vi. Navigate back to the Docker Hub home page and click on the Repository and we should see that image .

![](https://miro.medium.com/v2/resize:fit:875/1*aqkZw2h8PAMxedbxXFPjNw.png)

[](https://medium.com/m/signin?actionUrl=https%3A%2F%2Fmedium.com%2F_%2Fbookmark%2Fp%2F73ccdc1016fd&operation=register&redirect=https%3A%2F%2Fmedium.com%2F%40vaishnavipolichetti%2Fcustomise-docker-image-and-push-into-dockerhub-73ccdc1016fd&source=--------------------------bookmark_footer-----------)