Updated 2024-12-16
# Creating Persistent Block Volume Storage
The Compute Cloud@Customer Block Volume service provides persistent, durable, and high-performance block storage that you can use to store data outside of containers.
This procedure automatically creates the requested `oci-bv` storage class; you don't need to create it. This procedure starts with using the `kubectl` command to create the persistent volume claim.
  1. Create a persistent volume claim, specifying the storage class name `oci-bv`.
Copy
```
$ kubectl create -f csi-bvs-pvc.yaml
```

The following is the content of the `csi-bvs-pvc.yaml` file:
Copy
```
apiVersion: v1
kind: PersistentVolumeClaim
metadata:
 name: mynginxclaim
spec:
 storageClassName: "oci-bv"
 accessModes:
  - ReadWriteOnce
 resources:
  requests:
   storage: 50Gi
```

The persistent volume claim name in the `metadata` section is user-specified. You can have more than one persistent volume claim on a persistent volume.
For the value of `accessModes`, specify `ReadWriteOnce`; don't use `ReadWriteMany`.
The value of the `storage` property must be at least 50 gigabytes.
  2. Run the following command to verify that the PVC has been created:
Copy
```
$ kubectl get pvc
NAME      STATUS  VOLUME  CAPACITY  ACCESSMODES  STORAGECLASS  AGE
mynginxclaim  Pending                  oci-bv     4m
```

The PVC has a status of `Pending` because the `oci-bv` storage class definition includes the following:
Copy
```
volumeBindingMode: WaitForFirstConsumer
```

  3. Use the PVC when creating other objects, such as pods.
For example, you could create a new pod from the following pod definition, which instructs the system to use the `mynginxclaim` PVC as the `nginx` volume, which is mounted by the pod at `/data`:
Copy
```
apiVersion: v1
kind: Pod
metadata:
 name: nginx
spec:
 containers:
  - name: nginx
   image: nginx:latest
   ports:
    - name: http
     containerPort: 80
   volumeMounts:
    - name: data
     mountPath: /usr/share/nginx/html
 volumes:
  - name: data
   persistentVolumeClaim:
    claimName: mynginxclaim
```

Run the following command to verify that the PVC has been bound to a new PV:
Copy
```
$ kubectl get pvc
NAME      STATUS  VOLUME     CAPACITY  ACCESSMODES  STORAGECLASS  AGE
mynginxclaim  Bound  csi- _unique_ID_  50Gi    RWO      oci-bv
```

Run the following command to verify that the pod is using the new PVC:
Copy
```
$ kubectl describe pod nginx
```



Was this article helpful?
YesNo

