# Kubernetes Volumes

## Raw Block Devices

Typically volumes show up as file systems, `/mnt/data`.  But we can also mount volumes as raw block devices `/dev/xda`

This is great for databases, who want to manage the whole device for very fast IO, rather than going through a file system layer.

https://kubernetes.io/blog/2019/03/07/raw-block-volume-support-to-beta/



