<link rel='stylesheet' href='../../assets/css/main.css'/>

![](https://upload.wikimedia.org/wikipedia/commons/thumb/2/20/WordPress_logo.svg/1200px-WordPress_logo.svg.png)
![](https://kubernetes.io/images/kubernetes-horizontal-color.png)

# Lab - Deploy WordPress

## Overview

This is an **practice-labs** lab, snippets of the code will be given to you, and you have to complete them.

### What is WordPress?

WordPress is a free and open-source content management system written in PHP and paired with a MySQL or MariaDB database.

This lab will guide you to deploy a complete WordPress and MySQL database instances using k8.

### Notes

- You have to fill out the question mark in each file of the project.
- There could be unnecessary question marks in some files, They are there to test you.
- Check the indentations
- Use `alpine` or `nginx` images, if possible.
- Use your own knowledge to confirm the result of your actions.

## Duration

90 minutes

## Database

### Step-1: Secret

complete [mysql-secrets](mysql/secret.yaml) file

**Hint:**

- Use [this site](https://www.base64encode.org/) to create base64

### Step-2: PVC

complete [mysql-pvc](mysql/secret.yaml) file

**Hint:**

- Only one node should be able to read from and write to this volume

apply

```bash
$ cd ~/kubernets-labs/practice-labs/wordpress/mysql/
$ kubectl apply -f secret.yaml
```

### Step-3: Service

complete [mysql-service](mysql/service.yaml) file

**Hint:**

- Search the official documentation of mysql for port
- This should be a local service, do not expose this service

apply

```bash
$ cd ~/kubernets-labs/practice-labs/wordpress/mysql/
$ kubectl apply -f service.yaml
```

### Step-4: Deploy

complete [mysql-deployment](mysql/deployment.yaml) file

**Hint:**

- Use Mysql 5.6
- If updated, We want to `Recreate` the pods

apply

```bash
$ cd ~/kubernets-labs/practice-labs/wordpress/mysql/
$ kubectl apply -f deployment.yaml
```

### Step-5: Verify

Verify that your mysql pod is working properly, secret, service and pvc are created properly.

## WordPress

### Step-1: PVC

complete [mysql-pvc](wordpress/pvc.yaml) file

**Hint:**

- Only one node should be able to read from and write to this volume

### Step-2: Deploy

complete [wordpress-deployment](wordpress/deployment.yaml) file

**Hint:**

- Use Apache
- Use php 7.0
- Use wordpress 4.8
- If updated, We want to `Recreate` the pods

apply

```bash
$ cd ~/kubernets-labs/practice-labs/wordpress/wordpress/
$ kubectl apply -f deployment.yaml
```

### Step-3: Service

complete [mysql-service](mysql/service.yaml) file

**Hint:**

- Use this service to access your pod.
- Since we are using a Cloud Environment, type should be `LoadBalancer`

apply

```bash
$ cd ~/kubernets-labs/practice-labs/wordpress/wordpress/
$ kubectl apply -f service.yaml
```

Get the External IP from your wordpress service and try to access it.

**Note:** It could take up to 10 minutes to get the `External-IP` and be able to access it.

If every thing goes great, you should be able to access your wordpress instances.

**Extra:**

- Try to delete your database and wordpress pods and investigate what happens.

## Lab is Complete! 👏