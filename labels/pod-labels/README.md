<link rel='stylesheet' href='../../assets/css/main.css'/>

# Lab - Labels

## Overview

On this lab you will lean how to assign labels for pods and query by labels

## Duration

30 minutes

## Step 1 - Manifest files

Inspect  [pod1 file](label-pod-dev-canary.yaml)

Inspect  [pod2 file](label-pod-dev-stable.yaml)

Inspect  [pod3 file](label-pod-pro-canary.yaml)

Inspect  [pod4 file](label-pod-pro-stable.yaml)

## Step 2 - Apply service file

create the pods

```bash
$   cd ~/kubernetes-labs/labels/pod-labels

$   kubectl apply -f label-pod-dev-canary.yaml -f label-pod-dev-stable.yaml  -f label-pod-pro-canary.yaml  -f label-pod-pro-stable.yaml
```

**Note:** This is the first time that we are applying multiple files with a single command;

output will look like:

```console
pod/pod-labels-dev-canary created
pod/pod-labels-dev-stable created
pod/pod-labels-pro-canary created
pod/pod-labels-pro-stable created
```

## Step 3 - get list of Pods

run the following command to get list of pods on your cluster

```bash
$ kubectl get pods -o wide

# get labels
$ kubectl get pods --show-labels
```

output will look like:

```console
NAME                                READY   STATUS    RESTARTS      AGE     LABELS
pod-labels-dev-canary               1/1     Running   0             2m17s   app=nginx,environment=dev,release=canary
pod-labels-dev-stable               1/1     Running   0             2m17s   app=nginx,environment=dev,release=stable
pod-labels-pro-canary               1/1     Running   0             2m17s   app=nginx,environment=production,release=canary
pod-labels-pro-stable               1/1     Running   0             2m17s   app=nginx,environment=production,release=stable

```

## Step 4 - search for pods

Search for a pod with dev `environment` and stable `release`

```bash
$   kubectl get pods -l release=stable,environment=dev
```

output will look like:

```console
NAME                    READY   STATUS    RESTARTS   AGE
pod-labels-dev-stable   1/1     Running   0          5m26s
```

---

Search for a pods with stable `release`

```bash
$   kubectl get pods -l release=stable
```

output will look like:

```console
NAME                    READY   STATUS    RESTARTS   AGE
pod-labels-dev-stable   1/1     Running   0          6m41s
pod-labels-pro-stable   1/1     Running   0          6m41s
```

---

Search for a pods with `dev` or `production`

```bash
$   kubectl get pods -l 'environment in (dev,production)'
```

**Note:**  ' (single quotation mark) is necessary;

output will look like:

```console
NAME                    READY   STATUS    RESTARTS   AGE
NAME                    READY   STATUS    RESTARTS   AGE
pod-labels-dev-canary   1/1     Running   0          8m23s
pod-labels-dev-stable   1/1     Running   0          8m23s
pod-labels-pro-canary   1/1     Running   0          8m23s
pod-labels-pro-stable   1/1     Running   0          8m23s
```

Let's try some NOT commands

```bash
$   kubectl get pods -l environment=production,release!=dev
```

```console
NAME                    READY   STATUS    RESTARTS   AGE
pod-labels-pro-canary   1/1     Running   0          4m20s
pod-labels-pro-stable   1/1     Running   0          4m20s
```

```bash
$   kubectl get pods -l 'environment in (production,dev),release notin (canary,test)'
```

```console
NAME                    READY   STATUS    RESTARTS   AGE
pod-labels-dev-stable   1/1     Running   0          7m42s
pod-labels-pro-stable   1/1     Running   0          7m42s
```


---

## Step 5 - clean up

Delete all the pods with `dev` or `production`

```bash
$ kubectl delete pods -l 'environment in (dev,production)'
```

output will look like:

```console
pod "pod-labels-dev-canary" deleted
pod "pod-labels-dev-stable" deleted
pod "pod-labels-pro-canary" deleted
pod "pod-labels-pro-stable" deleted
```

to verify that all pods are deleted:

```bash
$ kubectl get pods -o wide
```

output will look like:

```console
No resources found in default namespace.
```

## Lab is done! 👏