Updated 2024-12-16
# Creating Persistent High Performance Block Volume Storage
This procedure creates a high performance block volume as persistent storage on Compute Cloud@Customer.
If you don't need a high performance block volume, use the instructions in [Creating Persistent Block Volume Storage](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/oke/creating-persistent-block-volume-storage.htm#creating-persistent-block-volume-storage "The Compute Cloud@Customer Block Volume service provides persistent, durable, and high-performance block storage that you can use to store data outside of containers.").
  1. Create a high performance block volume using the CSI plugin specified by the `oci-bv-high` storage class definition (`provisioner: blockvolume.csi.oraclecloud.com`).
Copy
```
$ kubectl create -f csi-bvs-high.yaml
```

The following is the content of the `csi-bvs-high.yaml` file:
Copy
```
apiVersion: storage.k8s.io/v1
kind: StorageClass
metadata:
 name: oci-bv-high
provisioner: blockvolume.csi.oraclecloud.com
parameters:
 vpusPerGB: "20"
 attachment-type: "paravirtualized"
volumeBindingMode: WaitForFirstConsumer
allowVolumeExpansion: true
reclaimPolicy: Delete
```

  2. Create a persistent volume claim, specifying the storage class name `oci-bv-high`.
Copy
```
$ kubectl create -f csi-bvs-high-pvc.yaml
```

The following is the content of the `csi-bvs-high-pvc.yaml` file:
Copy
```
apiVersion: v1
kind: PersistentVolumeClaim
metadata:
 name: mynginxclaim-high
spec:
 storageClassName: "oci-bv-high"
 accessModes:
  - ReadWriteOnce
 resources:
  requests:
   storage: 50Gi
```

The persistent volume claim name in the `metadata` section is user-specified. You can have more than one persistent volume claim on a persistent volume.
For the value of `accessModes`, specify `ReadWriteOnce`; do not use `ReadWriteMany`.
The value of the `storage` property must be at least 50 gigabytes.
  3. Run the following command to verify that the PVC has been created:
Copy
```
$ kubectl get pvc
NAME        STATUS  VOLUME  CAPACITY  ACCESSMODES  STORAGECLASS  AGE
mynginxclaim-high  Pending                  oci-bv     4m
```

The PVC has a status of Pending because the `oci-bv-high` storage class definition includes the following:
Copy
```
volumeBindingMode: WaitForFirstConsumer
```

  4. Use the PVC when creating other objects, such as pods.
For example, you could create a new pod from the following pod definition, which instructs the system to use the `mynginxclaim-high` PVC as the `nginx` volume, which is mounted by the pod at `/data`:
Copy
```
apiVersion: v1
kind: Pod
metadata:
 name: nginx-high
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
    claimName: mynginxclaim-high
```

Run the following command to verify that the PVC has been bound to a new PV:
Copy
```
$ kubectl get pvc
NAME        STATUS  VOLUME     CAPACITY  ACCESSMODES  STORAGECLASS  AGE
mynginxclaim-high  Bound  csi-** _unique_ID_**  50Gi    RWO      oci-bv-high
```

Run the following command to verify that the pod is using the new PVC:
Copy
```
$ kubectl describe pod nginx-high
```



Was this article helpful?
YesNo

