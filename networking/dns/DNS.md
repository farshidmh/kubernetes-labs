<link rel='stylesheet' href='../../assets/css/main.css'/>

# Lab: Understand DNS

## Overview

We will experiment with DNS settings in Pods

References:

- [DNS for Services and Pods](https://kubernetes.io/docs/concepts/services-networking/dns-pod-service/)

## Duration 10 mins

## Step-1: Inspect `dns1.yaml`

file : [dns1.yaml](dns1.yaml)

## Step-2: Create a Pod

```bash
$   kubectl apply -f dns1.yaml
```

Inspect the created Pod

```bash
$   kubectl describe pod busybox1
```

## Step-3: Inspect DNS Settings in `busybox1`

Let's execute some commands on `busybox1`

```bash
$    k exec -it  busybox1 -- cat /etc/resolv.conf
```

Your output may look like:

```console
nameserver 10.96.0.10
search default.svc.cluster.local svc.cluster.local cluster.local ec2.internal
options ndots:5
```

We see it is using **nameserver 10.96.0.1**

Let's find out about our **KubeDNS** service

```bash
$   kubectl  get svc -A
```

Your output may look like this.  So **10.96.0.1** is indeed our KubeDNS service IP

```console
NAMESPACE              NAME                        TYPE        CLUSTER-IP       EXTERNAL-IP   PORT(S)                  AGE
default                kubernetes                  ClusterIP   10.96.0.1        <none>        443/TCP                  8h
default                nginx-service               NodePort    10.105.187.250   <none>        8080:30100/TCP           84m
kube-system            kube-dns                    ClusterIP   10.96.0.10       <none>        53/UDP,53/TCP,9153/TCP   8h
kubernetes-dashboard   dashboard-metrics-scraper   ClusterIP   10.108.190.8     <none>        8000/TCP                 7h33m
kubernetes-dashboard   kubernetes-dashboard        ClusterIP   10.109.186.244   <none>        443/TCP                  7h33m

```

Let's do a NSLOOKUP

```bash
$   kubectl exec -it  busybox1 -- nslookup  www.google.com
```

This most likely will fail

## Step-4 : Custom DNS Settings

file : [dns2.yaml](dns2.yaml)

```bash
$   kubectl apply -f dns2.yaml

$   kubectl get pods -o wide
```

**ACTION:Check DNS Settings**

```bash
$   kubectl exec -it  custom-dns -- cat /etc/resolv.conf
```

output may look like

```console
nameserver 8.8.8.8
search ns1.svc.cluster-domain.example my.dns.search.suffix
options ndots:2 edns0
```

**ACTION: Do a DNS lookup**

```bash
$   kubectl exec -it  custom-dns -- nslookup google.com
```

you may see output like

```console
Server:		8.8.8.8
Address:	8.8.8.8:53

Non-authoritative answer:
Name:	google.com
Address: 2607:f8b0:4004:800::200e
```

DNS lookup worked!


## Step-5: Cleanup the Pods

```bash
$   kubectl delete pods busybox1  custom-dns
```

