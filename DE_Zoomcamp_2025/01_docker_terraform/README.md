## Module 1: Containerization and Infrastructure as Code

* Course overview
* Introduction to GCP
* Docker and docker-compose
* Running Postgres locally with Docker
* Setting up infrastructure on GCP with Terraform
* Preparing the environment for the course
* Homework


### Docker & SQL

The data set we will use is the Taxi Rides NY dataset.

#### Introduction to Docker

Docker is a platform designed to help developers build, share, and run container applications. It can be useful to run a data pipeline in a container so this pipeline is isolated from the rest of things. A data pipeline is described as a process or service that takes input data, processes it (e.g., cleaning, transformation), and produces output data. It can be a pytom scipt that takes in some csv file and produces some data stored in Postgres databases. Many data pipelines also forms one data pipeline. Containers allow us to run many different data pipelines at the same time, each in its container, without interference, or even data bases so they communicate together like Postgres and pgAdmin. In fact, Docker allows for isolated and independent execution of different services, preventing conflicts and simplifying the management of dependencies. 
Why caring about Docker, as a data engineer:
- Reproducibility: Docker images act as snapshots of a container's environment, ensuring that the same code and dependencies will run identically across different machines. This is crucial for ensuring consistent results and avoiding environment-specific issues.
- Local Experiments and Testing: Docker allows data engineers to set up and run local experiments and integration tests (CI/CD or Continuous Integration/Continuous Delivery) without needing to install software directly on their host machines. This simplifies the development process and makes it easier to test data pipelines in a controlled environment.
- Cloud Deployment: Docker images can be easily deployed to cloud environments like Google Cloud Kubernetes jobs or AWS Batch or with Spark and Serverless (AWS Lambda, Google functions), ensuring that the same code and dependencies run consistently in production. This simplifies the deployment process and reduces the risk of environment-specific errors.
Let's create a directory: `mkdir 2_docker_sql`. Inside we will creae a `Dockerfile`. To get introduce with docker: `docker run hello-world`,
`docker run -it ubuntu bash`:
`run` to run the image
`-it` to get in interactive mode
`ubuntu` the environment we want to run
`bash` the command we want to execute in that image. As everything comming after the container name, it is like a parameter. Note that even if we delete everything in that docker container: `rm -rf / --no-preserve-root`, when we run the ccommand to launch it we get back all the files inside. Containers are not affected by anything done previously (isolation).
In `docker run -it python:3.9`, `3.9` is the tag specifying the exact version to run. To get into bash we need to overwrite the entrypoint:
`docker run -it --entrypoint-bash python:3.9` The problem is that each change made will be discarded at the next launch. That is why we need Dockerfile to build containers on top of others by specifying all the supplementary instructions or things to run. Here is an exemple of [Dockerfile](./2_docker_sql/Dockerfile):

```docker
FROM python:3.9.1 # the base image

RUN pip install pandas # istall pandas library

ENTRYPOINT [ "bash" ] # overwrite the entrypoint
```
To build it: `docker build -t test:pandas .`
`test:pandas`: the image name is test and the version is pandas.
`.` to create the image from the Dockerfile of the current directory. We can then run this image: `docker run -it test:pandas`




















