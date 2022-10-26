<link rel='stylesheet' href='../../assets/css/main.css'/>

# Lab - Deploying a Service

## Overview

In this lab you will how to create a service and access your cluster using that service.

## Duration

20 minutes

## Step 1 - Deploy

Project directory:

```bash
$   cd ~/kubernets-labs/service/nginx
```

[deployment-nginx.yaml](deployment-nginx.yaml)

Deploy

```bash
$   kubectl apply -f deployment-nginx.yaml
```

and verify

```bash
$   kubectl get deployments

$   kubectl get pods -o wide
```

## Step 2 - Service manifest file

Inspect  [service-nginx.yaml](service-nginx.yaml)

## Step 3 - Apply service file

Apply the config files using `kubectl apply` command

```bash
$   kubectl apply -f service-nginx.yaml
```

output will look like:
```console
service/nginx-service created
```

## Step 4 - get list of services

Run the following command to get list of services on your cluster

```bash
$ kubectl get services
```

output will look like:

```console
NAME            TYPE        CLUSTER-IP    EXTERNAL-IP   PORT(S)          AGE
kubernetes      ClusterIP   10.96.0.1     <none>        443/TCP          5d5h
nginx-service   NodePort    10.99.46.93   <none>        8080:30007/TCP   61s
```

## Step 4 - access cluster

First let's find out our worker nodes IP address

```bash
$   kubectl get nodes -o wide
```


```console
AME      STATUS   ROLES                  AGE   VERSION   INTERNAL-IP 
master    Ready    control-plane,master   22h   v1.22.1   172.16.0.15 
worker1   Ready    <none>                 21h   v1.22.1   172.16.0.78 
worker2   Ready    <none>                 21h   v1.22.1   172.16.0.111
```

From the output we can see 

- worker1 IP is 172.16.0.78
- worker2 IP is 172.16.0.111

**Note: Your nodes' IPs might be different, so adjust accordingly**

On terminal you can use curl:

```bash
# replace nodeIP with your node's IP address
$   curl  nodeIP:30007/

# in our case
#   curl 172.16.0.78:30007/
# or
#   curl 172.16.0.111:30007/
```

If you have access to an UI environment, open a browser and open any of the nodes in the cluster with port `30007`

`http://nodeIP:30007/`

output should look like:

![](pf.jpg)

## Step 5 - Delete services

Use the following command to delete your service;

```bash
kubectl  delete service nginx-service
```

output

```console
service "nginx-service" deleted
```


## Lab is done! 👏
