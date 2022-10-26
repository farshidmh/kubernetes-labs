<link rel='stylesheet' href='../../assets/css/main.css'/>

# Jokes Server

## Overview

This is a little Python Flask app that serves jokes.

We use `pyjokes` package

## Building the Docker Image

**TODO: Fix up Dockerfile**

```bash
$   docker build . -t jokes-server
```

## Testing with Docker Image

```bash
$   docker run -it -v $(pwd):/app -p5000:5000 jokes-server /bin/bash
```

This will drop you into /app directory in container

```bash
$   python3  jokes-test.py
```

To run the server manually

```bash
$   python3 /app/app.py
```

From another terminal, access the page

```bash
$   curl localhost:5000
```

You will see a joke

## Running the Docker Image in 'Production'

```bash
$   docker run -it  -p5000:5000 jokes-server 
```

This will run flask app 

```bash
$   curl localhost:5000/
```

You will see a joke

## Pushing to DockerHub

Tag the image accordingly.

```bash
# replace 'my_user_name' with your docker_hub_user_name
# and replace :1 with appropriate version
$   docker tag jokes-server  my_user_name/jokes_server:1

$   docker login
# enter your user/password

$   docker push  my_user_name/jokes_server:1
```

## Deploying in Kubernetes

Deploy

```bash
$   kubectl  apply  -f deployment.yaml

$   kubectl  apply  -f service.yaml
```

Verify

```bash
$   kubectl get deployments
$   kubectl get svc
$   kubectl get nodes -o wide
```

Access 

```bash
# replace worker_ip 
$   curl worker_ip:30001/
```

## TODO: Update the Jokes App in Kubernetes

- Edit `app.py`
- Change the category to `chuck`
- Build a new docker image
- Increment the version
- Push it to Dockerhub
- Create another deployment file with new version number of image (i.e   XXX/jokes:2)
- deploy the new version
- Do a canary deploymnet between v1 and v2
- Access the service
- Decommision old version and route all traffic to new version