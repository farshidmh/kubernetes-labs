<link rel='stylesheet' href='../../assets/css/main.css'/>

# Lab - Blue/Green Deployment

## Overview

We will see how to seamlessly do blue/green deployment

## Duration 

30 mins

## Step-1 - Deploy 'Blue'

Be sure be to in the project dir

```bash
$   cd ~/kubernetes-labs/deployments/blue-green
```

Inspect [1-blue-deployment.yaml](1-blue-deployment.yaml)

Note the following section

```yaml
kind: Deployment
metadata:
  name: nginx-v1
spec:
  selector:
    matchLabels:
      app: nginx
      version: "v1"
    ...
    spec:
      containers:
      - name: nginx
        image: sujee/nginx:1
```

Verify

```bash
$   kubectl get deployments

$   kubectl describe deployemnt  nginx-v1
```

## Step-2: Deploy Service

Inspect [2-service-blue.yaml](2-service-blue.yaml)

Again observe the following  labels 

```yaml
  selector:
    app: nginx
    version: "v1"
```

Verify

```bash
$   kubectl get svc

$   kubectl  describe svc nginx-service
```


## Step-3: Access Blue Service

Now our blue deployemnt is running, let's verify it

```bash
$   curl worker_node_ip:30100/
```

You should `v1` deployment message

```console
<html>
    <head><title>V1</title></head>

    <body>
        <h1>Welcome to Webapp - v1</h1>
    </body>
</html>
```

## Step-4: Deploy GREEN Service

Inspect [3-green-deployment.yaml](3-green-deploymenmt.yaml)

Observe the following

```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: nginx-v2
spec:
  ...
  selector:
    matchLabels:
      app: nginx
      version: "v2"
      containers:
      - name: nginx
        image: sujee/nginx:2
```

Deploy

```bash
$   kubectl deploy -f 3-green-deployment.yaml

$   kubectl  get deployments

$   kubectl  describe deployment nginx-v2
```

## Step-5: Access our Service

Verify still **BLUE** is the active service

```bash
$   curl worker_node_ip:30100/
```


## Step-5: Make Green Service Live

Inspect [4-green-service.yaml](4-green-service.yaml)

Note the following, we are switching to `version: v2`

```yaml
apiVersion: v1
kind: Service
metadata:
  name: nginx-service
spec:
  ...
  selector:
    app: nginx
    version: "v2"
```

```bash
$   kubectl apply -f 4-green-service.yaml

$   kubectl get svc

$   kubectl  describe svc nginx-service

```

## Step-6: Access our Service

```bash
$   curl worker_node_ip:30100/
```

You should `v2` deployment message

```console
<html>
    <head><title>V2</title></head>

    <body>
        <h1>Welcome to Webapp - v2</h1>
    </body>
</html>
```

Whoohoo.. our **GREEN** is live now!

## Lab is done! 👏