<link rel='stylesheet' href='../../assets/css/main.css'/>

# Lab - Deploy Nginx

## Important

This lab requires you to edit `host` file on your own machine.

**BE CAREFUL**

## Overview

In this lab you will learn how to create an ingress service and use ingress to open two different pods using a URL

## Duration

60 minutes

## Requirements - Install Ingress controller

before start working with `Ingress` you have to install and ingress controller, since we are using EKS, we'll use `NLB`

```bash
$ kubectl apply -f https://raw.githubusercontent.com/kubernetes/ingress-nginx/controller-v1.0.0/deploy/static/provider/aws/deploy.yaml
```

verify:

```bash
$ kubectl get pods -n ingress-nginx -l app.kubernetes.io/name=ingress-nginx --watch
```

**Note:** It could take up to 5 minutes for the controller to be installed correctly.

To verify that you have the controller installed correctly:

```bash
$ kubect get pods -n ingress-nginx
```

output will look like:

```console
NAME                                       READY   STATUS      RESTARTS   AGE
ingress-nginx-admission-create-dc4rr       0/1     Completed   0          119s
ingress-nginx-admission-patch-ck5b6        0/1     Completed   0          118s
ingress-nginx-controller-fd7bb8d66-nj4l6   1/1     Running     0          2m1s
```

`ingress-nginx-admission-create` and `ingress-nginx-admission-patch` should be `stopped` (0/1) and `Completed` 



## Check ingress version:

run the following command to get the installed version:

```bash
$ kubectl exec -it <ingress-nginx-controller-xxx> -n ingress-nginx -- /nginx-ingress-controller --version
```

**Note:** 
- Find `ingress-nginx-controller-xxx` from previous command,  
- It is called `ingress-nginx-controller-fd7bb8d66-nj4l6` in this case

output:

```console
-------------------------------------------------------------------------------
NGINX Ingress controller
  Release:       v1.0.0
  Build:         041eb167c7bfccb1d1653f194924b0c5fd885e10
  Repository:    https://github.com/kubernetes/ingress-nginx
  nginx version: nginx/1.20.1

-------------------------------------------------------------------------------
```

## Step-1: create two deployments

create two different deployments using commands lines and `gcr.io/google-samples/hello-app:1.0` and `gcr.io/google-samples/hello-app:2.0` images

```bash
#Web V1
$   kubectl create deployment web --image=sujee/nginx:1

#Web V2
$ kubectl create deployment web2 --image=sujee/nginx:2
```

output:

```console
#Web V1
deployment.apps/web created

#Web V2
deployment.apps/web2 created
```

## Step-2: Expose deployments

Expose the deployments you have created to port 8080

```bash

#Web V1
$ kubectl expose deployment web --type=NodePort --port=8080

#Web V2
$ kubectl expose deployment web2 --port=8080 --type=NodePort
```

output:

```console
#Web V1
service/web exposed

#Web V2
service/web2 exposed
```

## Step-3: Verify services

verify that services are created for the deployments

```console
$ kubectl get service
```

output:

```console
NAME         TYPE        CLUSTER-IP       EXTERNAL-IP   PORT(S)          AGE
kubernetes   ClusterIP   10.96.0.1        <none>        443/TCP          6d4h
web          NodePort    10.102.100.134   <none>        8080:32073/TCP   11s
web2         NodePort    10.97.111.76     <none>        8080:30616/TCP   8s
```

**Note:** `CLUSTER-IP` and `PORT(S)` might be different for you.

## Step-5: verify access to deployments

Open a browser and try to access your master ip and node port for example:

- Web 1

```bash
http://<MASTER-IP>:32073
```

output

```console
Hello, world!
Version: 1.0.0
Hostname: web-XXX
```

- Web 2

```bash
http://<MASTER-IP>:30616
```

output

```console
Hello, world!
Version: 2.0.0
Hostname: web2-XXX
```

## Step-6:  Deploy Ingress

inspect  [ingress file](ingress-nginx-1.yaml)

- apply:

```bash
$   cd ~/kubernets-labs/ingress/1-nginx
$   kubectl  apply -f ingress-nginx-1.yaml
```

output:

```console
ingress.networking.k8s.io/example-ingress created
```

verify:

```bash
$ kubectl get ingress
```

output:

```console
NAME              CLASS    HOSTS              ADDRESS   PORTS   AGE
example-ingress   <none>   hello-world.info             80      105s
```

checkout what is happening

```bash
$ kubectl describe ingress example-ingress
```

## Lab is Complete! 👏