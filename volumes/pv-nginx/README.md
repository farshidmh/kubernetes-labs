<link rel='stylesheet' href='../../assets/css/main.css'/>

# Nginx with Persistent Volume

Reference : https://kubernetes.io/docs/tasks/configure-pod-container/configure-persistent-volume-storage/

## Step 1 - Create a volume storage dir

```bash
# create a volume dir
$   mkdir /tmp/nginx-volume

# create an index.html file
$   echo "Hello world -- v1" >> /tmp/nginx-volume/index.html

```

## Create PV

file : [1-pv.yaml](1-pv.yaml)

```bash
$    kubectl apply -f 1-pv.yaml

$    kubectl get pv -o wide

$    kubectl describe pv nginx-pv
```

## Create a Claim

file : [2-claim.yaml](2-claim.yaml)

```bash
$   kubectl apply -f 2-claim.yaml
$   kubectl get pvc
$   kubectl describe pvc nginx-pv-claim
$   kubectl get pv
```

you should see the claim is already bound the PV we created.

## Create a POD

spec : [3-pod.yaml](3-pod.yaml)

```bash
$   kubectl  apply -f 3-pod.yaml
$   kubectl  get pods -o wide
$   kubtctrl describe pod nginx
```

You should see under 'mounts' the pv is mounted

## Login to Nginx

```bash
$   kubectl exec -it nginx -- /bin/bash

## curl to see the page
$   curl  http://localhost/
# You should see "Hello world -- v1"
```

exit out

## Change the web content

From the host machine

```bash
$   echo "hello world -v2" | sudo tee  /tmp/nginx-volume/index.html
```

## Log back into Nginx and check

```bash
$   kubectl exec -it nginx -- /bin/bash

## curl to see the page
$   curl  http://localhost/
# You should see "Hello world -- v2"
```

exit out

## Bonus Lab:

Here we are updating the content from the host node. 

Try this:

- Add another container to act as a 'dev' machine.  
- share the same pv as /web
- update the content from this container

