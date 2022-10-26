<link rel='stylesheet' href='../assets/css/main.css'/>

# Lab - Config Maps

## Overview

On this lab you will lean how to create a configmap and pass its values to your pod

## Duration

30 minutes

## Step 1 - configmap file

Inspect  [configmap file](config-map.yaml)

## Step 3 - Apply service file

Apply the configmap files using `kubectl apply` command

```bash
$   cd ~/kubernets-labs/config-map
$   kubectl apply -f config-map.yaml
```

output will look like:

```console
configmap/sample-config created
```

## Step 4 - get list of configmaps

Run the following command to get list of configmaps on your cluster

```bash
$ kubectl get configmap
```

output will look like:

```console
NAME               DATA   AGE
kube-root-ca.crt   1      3d1h
sample-config      2      77s
```

## Step 4 - Verify configmap

To get manifest of your configmap, run the following

```bash
$   kubectl describe configmap sample-config
```

output will look like:

```console
Name:         sample-config
Namespace:    default
Labels:       <none>
Annotations:  <none>

Data
====
app_password:
----
doe
app_username:
----
jone

BinaryData
====

Events:  <none>
```

On the next steps, we are going to pass `app_username` and `app_password` to a pod.

## Step 5 - pod file

Inspect  [pod file](config-pod.yaml)

## Step 6 - Deploy the pod

```bash
# to start the pod in background
$ kubectl apply -f config-pod.yaml
```

Output will look like

```console
pod/configmap-pod created
```

## Step 6 - Connect to the pod

To run commands on the pod, use following command to connect to the pod

```bash
$ kubectl exec --stdin --tty configmap-pod  -- /bin/bash
```

output will look like:

```console
root@configmap-pod:/#
```

## Step 7 - get all the environment variable 

to get the variables in the pods, execute the following command:

```bash
$ printenv
```

output will look like:

```console
app_env_username=jane
KUBERNETES_SERVICE_PORT_HTTPS=443
KUBERNETES_SERVICE_PORT=443
HOSTNAME=configmap-pod
PWD=/
PKG_RELEASE=1~buster
HOME=/root
KUBERNETES_PORT_443_TCP=tcp://10.96.0.1:443
NJS_VERSION=0.6.2
app_env_passowrd=doe
TERM=xterm
SHLVL=1
KUBERNETES_PORT_443_TCP_PROTO=tcp
KUBERNETES_PORT_443_TCP_ADDR=10.96.0.1
KUBERNETES_SERVICE_HOST=10.96.0.1
KUBERNETES_PORT=tcp://10.96.0.1:443
KUBERNETES_PORT_443_TCP_PORT=443
PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin
NGINX_VERSION=1.21.3
_=/usr/bin/printenv
```

you can see `app_env_username` and `app_env_passowrd` passed to the pod from your configmap

use the following command to exit from the pod 

```bash
$ exit
```


## Step 8 - clean up

to delete the pod

```bash
#To delete pod
$ kubectl delete pod configmap-pod
```

output

```console
pod "configmap-pod" deleted
```

to delete the configmap 

```bash
#to delete configmap
$ kubectl delete configmap sample-config 
```

output

```console
configmap "sample-config" deleted
```

## Lab is done! 👏