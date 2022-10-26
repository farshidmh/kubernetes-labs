<link rel='stylesheet' href='../../assets/css/main.css'/>

![](https://upload.wikimedia.org/wikipedia/commons/thumb/3/3f/Redmine_logo.svg/1280px-Redmine_logo.svg.png)
![](https://kubernetes.io/images/kubernetes-horizontal-color.png)

# Lab - Deploy Redmine

## Overview

This is an **practice-labs** lab, snippets of the code will be given to you, and you have to complete them.

### What is Redmine?

Redmine is a free and open source, web-based project management and issue tracking tool. It allows users to manage multiple projects and associated subprojects. It features per project wikis and forums, time tracking, and flexible, role-based access control.

This lab will guide you to deploy a complete Redmine and MySQL database instances using k8.

### Notes

- You have to fill out the question mark in each file of the project.
- There could be unnecessary question marks in some files, They are there to test you.
- Check the indentations
- Use your own knowledge to confirm the result of your actions.

## Duration

90 minutes

## Database

This is a single file deployment.

complete [mysql-all](mysql-all.yaml) file based on your own knowledge

**Hint:**

- Use [this site](https://www.base64encode.org/) to create base64
- There are some sections missing in this file, find them and fill them out
- Use MySQL 5.6

apply

```bash
$ cd ~/kubernets-labs/practice-labs/redmine/
$ kubectl apply -f mysql-all.yaml
```


## Redmine

### Step-1: Deploy

complete [redmin-deployment](redmine-deployment.yaml) file

**Hint:**

- Use Bitnami image
- We want 2 pods for this deployment
- We only want to pull the image from DockerHuB if it's not on the master.

apply

```bash
$ cd ~/kubernets-labs/practice-labs/redmine/
$ kubectl apply -f redmine-deployment.yaml
```

### Step-3: Service

Design a service to expose redmine through a `loadbalancer`.

**Hint:**
- Default http port is 80
- Use this service to access your pod.

Get the External IP from your redmine service and try to access it.

**Note:** It could take up to 10 minutes to get the `External-IP` and be able to access it.

If every thing goes great, you should be able to access your redmine instances.

**Extra:**

- Try to create a health checker for pods.

## Lab is Complete! 👏