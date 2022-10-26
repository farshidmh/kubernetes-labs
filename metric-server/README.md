<link rel='stylesheet' href='../assets/css/main.css'/>

# Lab - Metrics Server

## Overview

Metrics Server is a scalable, efficient source of container resource metrics for Kubernetes built-in autoscaling pipelines.

## Duration

5 minutes

## Step 1 - Install

Execute the following command to install metrics server

```bash
$ kubectl apply -f https://github.com/kubernetes-sigs/metrics-server/releases/latest/download/components.yaml
```

output

```console
serviceaccount/metrics-server created
clusterrole.rbac.authorization.k8s.io/system:aggregated-metrics-reader created
clusterrole.rbac.authorization.k8s.io/system:metrics-server created
rolebinding.rbac.authorization.k8s.io/metrics-server-auth-reader created
clusterrolebinding.rbac.authorization.k8s.io/metrics-server:system:auth-delegator created
clusterrolebinding.rbac.authorization.k8s.io/system:metrics-server created
service/metrics-server created
deployment.apps/metrics-server created
apiservice.apiregistration.k8s.io/v1beta1.metrics.k8s.io created
```

## Step 2 - Query pods and nodes status

Wait for a few minutes for the server to startup.

to get `pods` usage

```bash
$   kubectl top pods
```

output will look like:

```console
NAME            CPU(cores)   MEMORY(bytes)
<YOUR-POD>      1m           13Mi
```

to get `nodes` usage

```bash
$   kubectl top nodes
```

output will look like:

```console
NAME                                          CPU(cores)   CPU%   MEMORY(bytes)   MEMORY%
ip-172-31-21-129.us-east-2.compute.internal   43m          2%     447Mi           80%
ip-172-31-39-81.us-east-2.compute.internal    50m          2%     497Mi           89%
ip-172-31-7-11.us-east-2.compute.internal     55m          2%     456Mi           82%
```

# Resource units in Kubernetes

### Meaning of CPU

Limits and requests for CPU resources are measured in cpu units. One cpu, in Kubernetes, is equivalent to 1 vCPU/Core for cloud providers and 1 hyperthread on bare-metal Intel processors.

Fractional requests are allowed. A Container with spec.containers[].resources.requests.cpu of 0.5 is guaranteed half as much CPU as one that asks for 1 CPU. The expression 0.1 is equivalent to the
expression 100m, which can be read as "one hundred millicpu". Some people say "one hundred millicores", and this is understood to mean the same thing. A request with a decimal point, like 0.1, is
converted to 100m by the API, and precision finer than 1m is not allowed. For this reason, the form 100m might be preferred.

CPU is always requested as an absolute quantity, never as a relative quantity; 0.1 is the same amount of CPU on a single-core, dual-core, or 48-core machine

### Meaning of memory

Limits and requests for memory are measured in bytes. You can express memory as a plain integer or as a fixed-point number using one of these suffixes: E, P, T, G, M, k. You can also use the
power-of-two equivalents: Ei, Pi, Ti, Gi, Mi, Ki. For example, the following represent roughly the same value:

```console
128974848, 129e6, 129M, 123Mi
```

## Well done! 👏