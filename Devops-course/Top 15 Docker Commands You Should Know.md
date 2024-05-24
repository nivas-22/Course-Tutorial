
The trend of Docker container has been growing uncontrollably with organizations actively looking for professionals who have a sound knowledge of Docker commands. So, in this article, I will discuss the Top 15 Docker Commands.

Following are the commands which are being covered:

- docker –version
- docker pull
- docker run
- docker ps
- docker ps -a
- docker exec
- docker stop
- docker kill
- docker commit
- docker login
- docker push
- docker images
- docker rm
- docker rmi
- docker build

# 1. **docker –version**

## Usage: docker — — version

This command is used to get the currently installed version of docker

![](https://miro.medium.com/v2/resize:fit:1050/1*iNv31Tw86lXDfAuEDH1Dcg.png)

# 2. **docker pull**

## **Usage: docker pull <image name>**

This command is used to pull images from the **docker repository**(hub.docker.com)

![](https://miro.medium.com/v2/resize:fit:1050/1*VF0NPJsXA5OiruFgd4un3A.png)

# 3. **docker run**

## **Usage: docker run -it -d <image name>**

This command is used to create a container from an image

![](https://miro.medium.com/v2/resize:fit:1050/1*JKbbkxPXjBypDALDq11Fxg.png)

# 4. **docker ps**

## Usage: docker ps

This command is used to list the running containers

![](https://miro.medium.com/v2/resize:fit:1050/1*P_lQYir1WiF4Vv6QRJX6KQ.png)

# 5. **docker ps -a**

## Usage: docker ps -a

This command is used to show all the running and exited containers

![](https://miro.medium.com/v2/resize:fit:1050/1*3KOEfJSCqlvUDHhGQ0MGog.png)

# 6. **docker exec**

## **Usage: docker exec -it <container id> bash**

This command is used to access the running container

![](https://miro.medium.com/v2/resize:fit:1050/1*6PKZY9n9F7TBDRzi8AcxpA.png)

# 7. **docker stop**

## **Usage: docker stop <container id>**

This command stops a running container

![](https://miro.medium.com/v2/resize:fit:1050/1*uDwmhDhs0lmCEgNRZHzb3w.png)

# 8. **docker kill**

## **Usage: docker kill <container id>**

This command kills the container by stopping its execution immediately. The difference between ‘docker kill’ and ‘docker stop’ is that ‘docker stop’ gives the container time to shutdown gracefully, in situations when it is taking too much time for getting the container to stop, one can opt to kill it.

![](https://miro.medium.com/v2/resize:fit:1050/1*EXcTXK68nfcgJwR2UMq46g.png)

# 9. **docker commit**

## **Usage: docker commit <conatainer id> <username/imagename>**

This command creates a new image of an edited container on the local system

![](https://miro.medium.com/v2/resize:fit:1050/1*IdUi9OdTM-_IFFd11rdt6Q.png)

# 10. **docker login**

## Usage: docker login

This command is used to login to the docker hub repository

![](https://miro.medium.com/v2/resize:fit:1050/1*Ow3npJLdEW1J4296AI85LA.png)

# 11. **docker push**

## **Usage: docker push <username/image name>**

This command is used to push an image to the docker hub repository

![](https://miro.medium.com/v2/resize:fit:1050/1*JqJEb6pfxPiLOZ5m96eJlw.png)

# 12. **docker images**

## Usage: docker images

This command lists all the locally stored docker images.

![](https://miro.medium.com/v2/resize:fit:1050/1*3CFOcIyAo4toKZrPW_Y9YQ.png)

# 13. **docker rm**

## **Usage: docker rm <container id>**

This command is used to delete a stopped container.

![](https://miro.medium.com/v2/resize:fit:1050/1*0gCtWpDRcjDqteb5E7-VXA.png)

# 14. **docker rmi**

## **Usage: docker rmi <image-id>**

This command is used to delete an image from local storage.

![](https://miro.medium.com/v2/resize:fit:1050/1*RCpPgLdzxRDGM2ViD1rMbw.png)

# 15. **docker build**

## **Usage: docker build <path to docker file>**

This command is used to build an image from a specified docker file.

![](https://miro.medium.com/v2/resize:fit:1050/1*SJEMmyIFnuJzCdWmJb8e7Q.png)

This brings us to the end of the article.