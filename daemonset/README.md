<link rel='stylesheet' href='../assets/css/main.css'/>

# Lab - Service manifest


## Overview
On this lab you will lean how to create a configmap and pass its values to your pod


## Duration
30 minutes

## Step 1 - daemonset file

Inspect  [daemonset file](daemonset.yaml)

## Step 3 - Apply service file

Apply the configmap files using `kubectl apply` command

```bash
$   cd ~/kubernets-labs/daemonset
$   kubectl apply -f daemonset.yaml
```

output will look like:
```console
daemonset.apps/nginx-daemonset created
```

## Step 4 - get list of daemonset

run the following command to get list of configmaps on your cluster

```bash
$ kubectl get daemonset
```

output will look like:

```console
NAME              DESIRED   CURRENT   READY   UP-TO-DATE   AVAILABLE   NODE SELECTOR   AGE
nginx-daemonset   2         2         2       2            2           <none>          9s
```

## Step 4 - Verify configmap
To get manifest of your configmap, run the following

```bash
$   kubectl describe daemonset nginx-daemonset
```

output will look like:

```console
Name:           nginx-daemonset
Selector:       name=nginx-match
Node-Selector:  <none>
Labels:         <none>
Annotations:    deprecated.daemonset.template.generation: 1
Desired Number of Nodes Scheduled: 2
Current Number of Nodes Scheduled: 2
Number of Nodes Scheduled with Up-to-date Pods: 2
Number of Nodes Scheduled with Available Pods: 2
Number of Nodes Misscheduled: 0
Pods Status:  2 Running / 0 Waiting / 0 Succeeded / 0 Failed
Pod Template:
  Labels:  name=nginx-match
  Containers:
   nginx:
    Image:        nginx
    Port:         <none>
    Host Port:    <none>
    Environment:  <none>
    Mounts:       <none>
  Volumes:        <none>
Events:
  Type    Reason            Age   From                  Message
  ----    ------            ----  ----                  -------
  Normal  SuccessfulCreate  9m2s  daemonset-controller  Created pod: nginx-daemonset-2n7n5
  Normal  SuccessfulCreate  9m2s  daemonset-controller  Created pod: nginx-daemonset-xnj4l
```

## Step 5 - verify pods

To get list of pods and where they are created use the following command

```bash
$ kubectl get pods -o wide
```
output

```console
NAME                    READY   STATUS    RESTARTS   AGE   IP                NODE        NOMINATED NODE   READINESS GATES
nginx-daemonset-2n7n5   1/1     Running   0          10m   192.168.130.160   k-worker1   <none>           <none>
nginx-daemonset-xnj4l   1/1     Running   0          10m   192.168.82.144    k-worker2   <none>           <none>
```

**Note:** `IP` and `Name` might be different for you but status must be `Running` and you should have one pod on each `node`.

## Step 6 - remove daemonset

to delete the daemonset and its pods use the following command:

```bash
$ kubectl delete daemonset nginx-daemonset
```

output:

```console
daemonset.apps "nginx-daemonset" deleted
```

## Well done! 👏