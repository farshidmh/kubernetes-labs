<link rel='stylesheet' href='../../assets/css/main.css'/>

# Lab - Pod Placement Using Labels

## Overview

In this lab, we will place Pods on specific Nodes, by using labels

## Duration

20 minutes

## Step-1: Label Nodes

First let's label our nodes with `disk` label.

```bash
$   kubectl  label nodes worker1  disk=ssd
$   kubectl  label nodes worker2  disk=regular
```

Verify

```bash
$    kubectl get nodes --show-labels

$   kubectl get nodes -l disk=ssd
```

**TODO: Can you list only nodes with `disk` label defined.  It can be set to any value**

## Step-2: Inspect pod.yaml

File : [pod.yaml](pod.yaml)

**TODO: Fix the yaml to reflect the `disk: ssd`  as shown here**

```yaml
apiVersion: v1
kind: Pod
metadata:
  name: redis1
spec:
  containers:
  - name: redis
    image: redis
    imagePullPolicy: IfNotPresent
  nodeSelector:
    disk: ssd
```

Create two pods

```bash
$   kubectl apply -f pod.yaml
```

**TODO: Edit pod.yaml, and change the name of the pod to `redis2`**

```bash
$   kubectl apply -f pod.yaml
```

See where pods are running:

```bash
$   kubectl  get pods -o wide
```

The pods shoudl be bound to `worker1` as it is the only one labeled as `disk=ssd`

## Step-3: Schedule Another Pod on Worker2

**TODO: Make a copy of the pod.yaml and modify it to say**

- disk: regular
- image: alpine
- name: alpine1

Launch a few of these pods, and watch if they are binding to only `worker2`

## Step-4: Cleanup

```bash
$   kubectl delete pods  YOUR_POD_NAMEs
```

## Lab is done!  👏