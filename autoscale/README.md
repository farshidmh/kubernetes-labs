<link rel='stylesheet' href='../assets/css/main.css'/>

# Lab - Horizontal Scale Up

## Overview

On this lab you will learn an automated approach to increase or decrease the compute, memory or networking resources they have allocated.

**Note:**

- This lab may need to be run on a cloud based kubernetes cluster, so we can use load balancer

## Duration

30 minutes

## Step-1: Enable Metrics

Change to working directory

```bash
$ cd ~/kubernets-labs/autoscale
```

Enable metrics:

```bash
$   kubectl apply -f https://github.com/kubernetes-sigs/metrics-server/releases/latest/download/components.yaml
```

## Step-2: Deployment

inspect  [1-deployment.yaml](1-deployment.yaml)

we are creating a `php-apache` deployment from Google's repository.

**Note:**

- This is a special image, when you open a page, an intense calculation will be executed to generate cpu load.

look at this part:

```yaml
resources:
    requests:
        cpu: 500m # 0.5 of a core
         memory: 100M
```

In this scenario, we are limiting the pods to use only half of a single core to achieve high load on cpu core easier.

apply the file

```bash
$   kubectl apply -f 1-deployment.yaml
```

Verify deployment

```bash
$ kubectl get deployment
```

output

```console
NAME                   READY   UP-TO-DATE   AVAILABLE   AGE
php-apache-deployment  1/1     1            1           28s
```

verify pods

```bash
$ kubectl get pods -o wide
```

output

```console
NAME                          READY   STATUS    RESTARTS   AGE
php-apache-7bc7b7f897-bhr5d   1/1     Running   0          59s
```

## Step-3: Service

Service definition: [2-service.yaml](2-service.yaml)

Expose the deployment using `LoadBalancer`

```bash
$   kubectl apply -f 2-service.yaml
```

Verify

```bash
$   kubectl get svc
```

Output

```console
NAME                 TYPE           CLUSTER-IP       EXTERNAL-IP          PORT(S)        AGE
kubernetes           ClusterIP      10.100.0.1       <none>               443/TCP        43m
php-apache-service   LoadBalancer   10.100.186.232   <YOUR-ACCESS-LINK>   80:31799/TCP   23s
```

Keep an eye on the  `EXTERNAL-IP` attribute.

**Note:It could take upto 10 minutes to get `EXTERNAL-IP`  address**

Test the service

```bash
$   curl EXTERNAL_IP_ADDRESS
```

You should get `ok` as output

## Step-4: Pod usage

execute the following command to get list of pods and their cpu/ram usage

```bash
$ kubectl top pods
```

output

```console
NAME                          CPU(cores)   MEMORY(bytes)
php-apache-7bc7b7f897-bhr5d   1m           10Mi
```

This means your pod is almost idle.

---
<span style="color:red">**IMPORTANT**</span> 

if you are getting the following error, it means that you skipped the `metric-server` lab

```console
error: Metrics API not available
```
---



## Step-5: Generate Load

**IMPORTANT:**  OPEN A NEW TERMINAL SESSION FOR THIS STEP

Now, we are going to create a pod with busybox image, connect to it, and try to stress the deployment.

```bash
$ kubectl run -i --tty load-generator --image=busybox /bin/sh

#Hit enter for command prompt

$ while true; do wget -q -O- <YOUR-SERVICE-URL>; done
```

Output will give you lots of `OK!`

**KEEP THIS TERMINAL OPEN**

Switch to your main terminal and try to get the load of your pods

```bash
$ kubectl top pods
```

output

```console
NAME                          CPU(cores)   MEMORY(bytes)
load-generator                9m           0Mi
php-apache-7bc7b7f897-bhr5d   883m         13Mi
```

Also try

```bash
$   kubectl get all
```

as you can see, the load on our deployment pods is very high, time to scale up the deployment automatically.

## Step-6: Scale Up

Autoscale definition:   [3-autoscale.yaml](3-autoscale.yaml)

note the following lines:

```console
  minReplicas: 1
  maxReplicas: 10
  targetCPUUtilizationPercentage: 50
```

using these settings we are telling k8 to to spawn a pod once current pods hit 50% cpu usage.  
maximum of 10 pods will be created and if a pod's usage is below 50%, k8 will de-spawn that pod, but it will keep 1 pod active

```bash
$   kubectl apply -f 3-autoscale.yaml
```

output

```console
horizontalpodautoscaler.autoscaling/php-apache created
```

verify hpa

```bash
$ kubectl get hpa
```

output

```console
NAME         REFERENCE               TARGETS   MINPODS   MAXPODS   REPLICAS   AGE
php-apache   Deployment/php-apache   198%/50%   1         10        4          69s
```

as you can see, cpu load is very high, k8 will try to lower the load on the cluster by spawning more pods

Also try

```bash
$   kubectl get all
```

**Note: it could take a while to see the new pods.**

```bash
$ kubectl get pods
```

output

```console
NAME                          READY   STATUS    RESTARTS   AGE
load-generator                1/1     Running   0          12m
php-apache-7bc7b7f897-4wczk   1/1     Running   0          2m13s
php-apache-7bc7b7f897-72kfc   1/1     Running   0          2m13s
php-apache-7bc7b7f897-bhr5d   1/1     Running   0          32m
php-apache-7bc7b7f897-c2hsl   1/1     Running   0          2m13s
```

## Step-7: Scale Down

Let's do the opposite of what we just did, lower the load to scale down.

Kill the `load-generator` pod.

```bash 
$ kubectl delete pods load-generator
```

output

```console
pod "load-generator" deleted
```

_wait for a few minutes_

check hpa

```bash
$ kubectl get hpa
```

output

```console
NAME         REFERENCE               TARGETS   MINPODS   MAXPODS   REPLICAS   AGE
php-apache   Deployment/php-apache   29%/50%   1         10        4          18m
```

Also try

```bash
$   kubectl get all
```

Load is going down, k8 will start to de-spawn pods slowly.

**Wait for a few minutes**

This waiting time is called `cooldown delay` to prevent excessive scale up/down.

check your pods configuration

```bash
$ kubectl get pods
```

output

```console
NAME                          READY   STATUS    RESTARTS   AGE
php-apache-7bc7b7f897-bhr5d   1/1     Running   0          55m
```

Since load is very low, only one pod is working.

## Lab is done! 👏