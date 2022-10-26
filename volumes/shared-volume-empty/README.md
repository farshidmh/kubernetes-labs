<link rel='stylesheet' href='../../assets/css/main.css'/>

# Sharing data between two containers - Empty Dir

From: https://newrelic.com/blog/how-to-relic/how-to-use-kubernetes-volumes

yaml file : [shared-volume-1.yaml](shared-volume-1.yaml)

```bash

$   kubectl apply -f shared-volume-1.yaml

$   kubectl get pods
# 2 containers must be running

# login to one container
$   kubectl exec -it shared-volume-example-1 -c c1 -- bash
    # now you should be in c1
    $ df -kh
    # should see /tmp/data mounted

    # create a file
    $  echo "hi from c1" > /tmp/data/a
    $  cat /tmp/data/a

# open another terminal and login to another container
$   kubectl exec -it shared-volume-example-1 -c c2 -- bash
    # now you should be in c2

    $ df -kh
    # should see /tmp/data mounted

    # check the file content
    $  ls -l /tmp/data/
    $  cat /tmp/data/a

    # update the file
    $  echo "hi from c2" >> /tmp/data/a

# from c1 terminal
    $  cat /tmp/data/a

# logout from both containers

## cleanup
$   kubectl delete pod  shared-volume-example-1
$   kubectl get pods

```
