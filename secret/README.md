<link rel='stylesheet' href='../assets/css/main.css'/>

# Lab - Service manifest


## Overview
On this lab you will lean how to create a configmap and pass its values to your pod


## Duration
30 minutes

## Step 1 - configmap file

Inspect  [secret file](secret.yaml)

**Note:** As you can see, `username` and `password` fields are encrypted

## Step 3 - Apply secret file

Apply the secret files using `kubectl apply` command

```bash
$   cd ~/kubernets-labs/secret
$   kubectl apply -f secret.yaml
```

output will look like:
```console
secret/sample-secret created
```

## Step 4 - get list of secrets

run the following command to get list of configmaps on your cluster

```bash
$ kubectl get configmap
```

output will look like:

```console
NAME                  TYPE                                  DATA   AGE
default-token-cxbx8   kubernetes.io/service-account-token   3      3d5h
sample-secret         Opaque                                2      25s
```

## Step 4 - Verify secret
To get manifest of your configmap, run the following

```bash
$   kubectl describe secret sample-secret
```

output will look like:

```console
Name:         sample-secret
Namespace:    default
Labels:       <none>
Annotations:  <none>

Type:  Opaque

Data
====
```

On the next steps, we are going to pass `app_username` and `app_password` to a pod.

## Step 5 - pod file

Inspect  [pod file](secret-pod.yaml)

## Step 6 - Deploy the pod

```bash
# to start the pod in background
$ kubectl apply -f secret-pod.yaml
```

Output will look like

```console
pod/secret-pod created
```

## Step 6 - Connect to the pod

To run commands on the pod, use following command to connect to the pod

```bash
$ kubectl exec --stdin --tty secret-pod  -- /bin/bash
```

output will look like:

```console
root@secret-pod:/#
```

## Step 7 - get all the environment variable 

to get the variables in the pods, execute the following command:

```bash
$ printenv
```

output will look like:

```console
app_env_username=username
KUBERNETES_SERVICE_PORT_HTTPS=443
KUBERNETES_SERVICE_PORT=443
HOSTNAME=secret-pod
PWD=/
PKG_RELEASE=1~buster
HOME=/root
KUBERNETES_PORT_443_TCP=tcp://10.96.0.1:443
NJS_VERSION=0.6.2
app_env_passowrd=password
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

you can see `app_env_username` and `app_env_passowrd` passed to the pod from your secret and they are decrypted

use the following command to exit from the pod 

```bash
$ exit
```


## Step 8 - clean up

to delete the pod

```bash
#To delete pod
$ kubectl delete pod secret-pod
```
output

```console
pod "secret-pod" deleted
```

to delete the configmap 

```bash
#to delete configmap
$ kubectl delete secret sample-secret
```

output

```console
secret "sample-secret" deleted
```


## Well done! 👏