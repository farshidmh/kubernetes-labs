<link rel='stylesheet' href='../assets/css/main.css'/>

# Lab - Resource Limits

## Overview

Let's experiment with resource limits

## Duration

15 minutes

## Step-1: Spec

Inspect  [resources.yaml](resources.yaml)

## Step-2: Create a pod

```bash
$   cd ~/kubernets-labs/resource-limits
$   kubectl apply -f resources.yaml
```

## Step-3: Setup Metrics

First we need to install metric server

```bash
$   kubectl apply -f https://github.com/kubernetes-sigs/metrics-server/releases/latest/download/components.yaml
```

Verify the metrics server is running

```bash
$   kubectl get pods --all-namespaces | grep metrics-server
```

## Step-4: Monitor Resource usage

Inspect the usage

```bash
$   kubectl  top node
```

You may see output like:

```console
NAME       CPU(cores)   CPU%   MEMORY(bytes)   MEMORY%   
minikube   782m         4%     1009Mi          3%       
```

```bash
$   kubectl  get pod
```

You will see output like

```console
AME       CPU(cores)   MEMORY(bytes)   
frontend   4m           12Mi            
```

## Step-5: Re-adjust the limits

Let's stop the  running pod

```bash
$   kubectl  delete pod  frontend
```

Edit file [resources.yaml](resources.yaml)

Change the memory request to something really high, like `64 Gi`

```yaml
    resources:
      requests:
        memory: "64Gi"
```

Try to create the Pod again

```bash
$   cd ~/kubernets-labs/resource-limits
$   kubectl apply -f resources.yaml
```

You might get an error like this:

```console
The Pod "frontend" is invalid: spec.containers[0].resources.requests: Invalid value: "64Gi": must be less than or equal to memory limit
```

So adjust the `memory limit` to something higher than `request` (say `65Gi`)

And re-create the Pod

```bash
$   cd ~/kubernets-labs/resource-limits
$   kubectl apply -f resources.yaml
```

## Step-6: Check status

```bash
$   kubectl get pods
```

```console
NAME       READY   STATUS    RESTARTS   AGE
frontend   0/1     Pending   0          32s
```
We see our Pod is not running.  Let's inspect the Pod

```bash
$   kubectl   describe   pod  frontend
```

Looks at the event section

```console
Events:
  Type     Reason            Age   From               Message
  ----     ------            ----  ----               -------
  Warning  FailedScheduling  113s  default-scheduler  0/1 nodes are available: 1 Insufficient memory.
  Warning  FailedScheduling  112s  default-scheduler  0/1 nodes are available: 1 Insufficient memory.
```

As you can see the Pod is not running, because we don't have enough memory