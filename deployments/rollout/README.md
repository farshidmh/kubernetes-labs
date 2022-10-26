<link rel='stylesheet' href='../../assets/css/main.css'/>

# Lab - Rollout Deployment

## Overview

On this lab, we are going to create a deployment with 4 pods, the image of this deployment is called `nginx-v1` after creating the original deployment, we will `rollout` to update the image
to `nginx-v2`

Notice the difference that when we are updating the image instead of using `apply`, we will use `replace`

## Duration

20 minutes

## Step-1: Deployment file

Project dir

```bash
$   cd ~/kubernetes-labs/deployments/rollout
```

Inspect  [deployment-nginx-v1.yaml](deployment-nginx-v1.yaml)

## Step-3: Apply Deployment file

Apply the config files using `kubectl -apply` command

```bash
$   kubectl apply -f deployment-nginx-v1.yaml
```

output will look like:

```console
deployment.apps/nginx-deployment created
```

## Step-2: Expose

- expose the deployment

```bash
$ kubectl expose deployment nginx-deployment --port=80 --type=NodePort
```

output

```console
service/nginx-deployment exposed
```

- get nodeport

```bash
$  kubectl get service
```

output

```console
NAME               TYPE        CLUSTER-IP      EXTERNAL-IP   PORT(S)        AGE
kubernetes         ClusterIP   10.96.0.1       <none>        443/TCP        6m12s
nginx-deployment   NodePort    10.107.20.175   <none>        80:32073/TCP   54s
```

Find the worker1's IP address and access it.  
So if the worker's IP is 1.2.3.4  and NodPort is 32073

```bash
# substitute 1.2.3.4 with your worker node IP
# substitute 32073 with your service NodePort port
$   curl   1.2.3.4:32073/
```

output will look like:

```console
Welcome to Webapp - v1
```

## Step-4: rollout an update

**Note:** Read the entire section before starting the rollout process.

**Note:** monitor the results as soon as possible. it will be fast.

Inspect v2  : [deployment-nginx-v2.yaml](deployment-nginx-v2.yaml)

use the `v2` to update nginx from v1 to v2

```bash
$   kubectl replace  -f deployment-nginx-v2.yaml
```

Notice that instead of `apply` we are using `replace`.

Monitor the status of rollout using the following command:

```bash
$  kubectl rollout status deployment nginx-deployment
```

Note the events section at the end of output.  It will look like:

<img src="../../assets/images/rollout-1a.png" style="width:90%;"/>

**Note the following**

- Look at how new Pods are being created in new replica-set,  while pods are being removed from old-replica-set
- Also look at how much time has elapsed since the rollout began (104  - 99 = 5 seconds)

## Step-5: verify

Verify if the new rolled out service

```bash
# substitute 1.2.3.4 with your worker node IP
# substitute 32073 with your service NodePort port
$   curl   1.2.3.4:32073/
```

```console
Welcome to Webapp - v2
```

## Lab is Complete! 👏
