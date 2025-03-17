Updated 2024-12-16
# Using a Persistent Volume
On Compute Cloud@Customer, to use this persistent storage, create a Kubernetes deployment and assign a persistent volume claim as shown in the following sections.
  * [Using Block Volume Storage](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/oke/using-a-persistent-volume.htm#using-a-persistent-volume__block-volume-peristent-storage)
  * [Using File System Storage](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/oke/using-a-persistent-volume.htm#using-a-persistent-volume__file-system-peristent-storage)
  * [Verify the New Storage Asset](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/oke/using-a-persistent-volume.htm#using-a-persistent-volume__verify-asset)


## Using Block Volume Storage 🔗 
The following example uses block volume storage:
Copy
```
$ kubectl create -f nginx-deploy.yaml
```

The following output is the content of the `nginx-deploy.yaml` file.
Copy
```
apiVersion: apps/v1
kind: Deployment
metadata:
 name: nginx-bv-deployment
spec:
 replicas: 3
 selector:
  matchLabels:
   app: nginx-bv
 template:
  metadata:
   labels:
    app: nginx-bv
  spec:
   containers:
   - name: nginx
    image: available_internal_registry/nginx:latest
    volumeMounts:
    - mountPath: /usr/share/nginx/
     name: data
    ports:
    - containerPort: 80
     name: http
     protocol: TCP
   volumes:
   - name: data
    persistentVolumeClaim:
     claimName: mynginxclaim
```

## Using File System Storage 🔗 
The following example uses file system storage:
Copy
```
$ kubectl create -f nginx-deploy.yaml
```

The following output is the content of the `nginx-deploy.yaml` file.
Copy
```
apiVersion: apps/v1
kind: Deployment
metadata:
 name: nginx-fss-deployment
spec:
 replicas: 3
 selector:
  matchLabels:
   app: nginx-fss
 template:
  metadata:
   labels:
    app: nginx-fss
  spec:
   containers:
   - name: nginx
    image: nginx:latest
    volumeMounts:
    - mountPath: /usr/share/nginx/
     name: data
    ports:
    - containerPort: 80
     name: http
     protocol: TCP
   volumes:
   - name: data
    persistentVolumeClaim:
     claimName: fss-pvc
```

## Verify the New Storage Asset 🔗 
Use the `get pod` subcommand to show the names of the replicas in the pod:
```
$ kubectl get pod
nginx-deployment-55ff88b668-2k8rt 1/1 Running 0 4m54s
nginx-deployment-55ff88b668-79c2t 1/1 Running 0 4m54s
nginx-deployment-55ff88b668-qpdfd 1/1 Running 0 4m54s
```

Log in to the pod and use the Linux `df` command to show that the application replicas are using the `persistentVolumeClaim` storage. The `Filesystem` column in the `df` output shows the mount target IP address and the file system export path.
Copy
```
$ kubectl exec -it nginx-deployment-55ff88b668-2k8rt -- df -h /usr/share/nginx/html
Filesystem                                     Size Used Avail Use% Mounted on
xxx.xx.xxx.xxx:/export/4fsderwh09ufyf84ei1lh3q2x8ou86pq5vcbx3aeeo060xxxxxxxxxxxxxxx 67T 0  67T  0%  /usr/share/nginx/html
```

Was this article helpful?
YesNo

