<link rel='stylesheet' href='../../assets/css/main.css'/>
# Sharing a Persistent Volume

- create PV: [1-pv.yaml](1-pv.yaml)
- Claim PV : [2-claim.yaml](2-claim.yaml)
- Use PV : [3-pod.yaml](3-pod.yaml)

```bash
$   kubectl  apply -f 1-pv.yaml

# check
$   kubectl  get pv
# should see pv-1

# now create a claim
$   kubectl  apply -f 2-claim.yaml

# check
$   kubectl  get pv
$   kubectl  get pvc
# should see claim bound to pv-1

# start pods
$   kubectl apply -f 3-pod.yaml 
$   kubectl get pods -o wide

## login to a pod and check
$   kubectl exec -it shared-volume-example-2 -c c1 -- bash
    # now from C1
    $  echo "hi from c1" >> /tmp/data/a
    $  cat /tmp/data/a

## now from another terminal login to C2
$   kubectl exec -it shared-volume-example-2 -c c2 -- bash
    # now from C2
    $  cat /tmp/data/a
    $  echo "hi from c2" >> /tmp/data/a
    $  cat /tmp/data/a

## now from c1 terminal
    $  cat /tmp/data/a

## disconnect from both pods

## destroy the pods
$   kubectl  delete pod shared-volume-example-2
$   kubectl get pods -o wide

## recreate the pods
$   kubectl apply -f 3-pod.yaml 
$   kubectl get pods -o wide

## login to a pod and check
$   kubectl exec -it shared-volume-example-2 -c c1 -- bash
    # now from C1
    $  ls -l /tmp/data
    $  cat /tmp/data/a
    ## you should see data persisted

## delete the pods
$   kubectl  delete pod shared-volume-example-2

## delete PV
$   kubectl delete pvc myclaim-1
$   kubectl delete pv pv-1
```