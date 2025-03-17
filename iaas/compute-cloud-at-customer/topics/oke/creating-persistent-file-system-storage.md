Updated 2024-12-16
# Creating Persistent File System Storage Using an Existing File System
On Compute Cloud@Customer, you can provision a PVC on an existing file system.
This procedure creates a mount target, file system, and file system export. Then uses the `kubectl` command to create the storage class, persistent volume, and persistent volume claim.
  1. Create a mount target.
For instructions, see [Creating a Mount Target](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/file/creating-a-mount-target.htm#creating-a-mount-target "On Compute Cloud@Customer, A mount target is an NFS endpoint assigned to a subnet of your choice. The mount target provides the IP address or DNS name that's used in the mount command when connecting NFS clients to a file system.").
**Important**
To ensure that the mount target can be reached from worker nodes, create the mount target on the subnet that has the worker subnet described in [Creating an OKE Worker Subnet](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/oke/creating-a-worker-subnet.htm#creating-a-worker-subnet "On Compute Cloud@Customer, part of configuring OKE requires external and internal access security lists and a worker subnet."). Ensure that TCP port 2049 to the NFS server is open on that subnet.
Note the export set OCID and mount target OCID. The export set OCID is required to create the file system export, and the mount target OCID is required to create the storage class in later steps.
You can have only one mount target per VCN.
  2. Create a file system.
For instructions, see [Creating a File System](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/file/creating-a-file-system.htm#creating-a-file-system "On Compute Cloud@Customer, you can create a shared file system using the File Storage service.").
You can create only one file system per VCN. You can have multiple storage classes, persistent volumes, and persistent volume claims per cluster, and they all share one NFS.
  3. Create a file system export to associate the mount target with the file system.
For instructions, see [Creating an Export for a File System](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/file/creating-an-export-for-a-file-system.htm#creating-an-export-for-a-file-system "On Compute Cloud@Customer, exports control how NFS clients access file systems when they connect to a mount target. A file system must have at least one export in one mount target for instances to mount the file system.").
     * Specify the export set OCID from the output from creating the mount target.
     * Specify the longest CIDR (smallest network) in the CIDR range that you specified when you created the "worker" subnet as described in [Creating an OKE Worker Subnet](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/oke/creating-a-worker-subnet.htm#creating-a-worker-subnet "On Compute Cloud@Customer, part of configuring OKE requires external and internal access security lists and a worker subnet.").
Note the export path and the mount target IP address.
  4. Create a storage class, specifying the mount target OCID from the output of the create mount target step.
Copy
```
$ kubectl create -f sc.yaml
```

The following is the content of the `sc.yaml` file:
Copy
```
kind: StorageClass
apiVersion: storage.k8s.io/v1
metadata:
 name: pca-fss
provisioner: fss.csi.oraclecloud.com
parameters:
 mntTargetId: ocid1.mounttarget. _unique_ID_
      
```

The values of the `apiVersion` and `provisioner` properties are standard. The value of the storage class name in the metadata section is user-specified. You can create more than one storage class per mount target, and the storage class name is used in the following steps to create a persistent volume and persistent volume claim.
Use the `get sc` subcommand to view information about the new storage class:
Copy
```
$ kubectl get sc
```

  5. Create a persistent volume, specifying the storage class name, the export path, and the mount target IP address.
The storage class name is in the metadata in the `sc.yaml` file in the preceding step. The export path and the mount target IP address are output from the create file system export step. See Step 3 above.
Copy
```
$ kubectl create -f pv.yaml
```

The following is the content of the `pv.yaml` file:
```
apiVersion: v1
kind: PersistentVolume
metadata:
 name: fss-pv
spec:
 storageClassName: pca-fss
 capacity:
  storage: 200Gi
 accessModes:
  - ReadWriteMany
 mountOptions:
  - nosuid
 nfs:
  server: mount_target_IP_address
  path: "/export/_unique_ID_"
  readOnly: false
```

The persistent volume name in the `metadata` section is user-specified. You can have more than one persistent volume in a storage class.
In the `nfs` section, the `server` value is the mount target IP address, and the `path` value is the export path.
Use the `get pv` subcommand to view information about the new persistent volume:
Copy
```
$ kubectl get pv
NAME  CAPACITY ACCESS MODES RECLAIM POLICY STATUS CLAIM      STORAGECLASS REASON AGE
fss-pv 200Gi   RWX      Retain     Bound  default/fss-pvc pca-fss        20h
```

  6. Create a persistent volume claim, specifying the persistent volume name and the storage class name.
The persistent volume name and storage class name are in the output of the `get pv` command.
Wait for the PVC status to be Bound before using this storage.
Copy
```
kubectl create -f pvc.yaml
```

The following is the content of the `pvc.yaml` file:
Copy
```
apiVersion: v1
kind: PersistentVolumeClaim
metadata:
 name: fss-pvc
spec:
 storageClassName: pca-fss
 accessModes:
  - ReadWriteMany
 resources:
  requests:
   storage: 200Gi
 volumeName: fss-pv
```

The persistent volume claim name in the `metadata` section is user-specified. You can have more than one persistent volume claim on a persistent volume.
The value of the `accessModes` property must be `ReadWriteMany`.
The value of the `storage` property must be at least 50 gigabytes.
Run the following command to view information about the new persistent volume claim:
Copy
```
$ kubectl get pvc
NAME   STATUS  VOLUME  CAPACITY  ACCESSMODES  STORAGECLASS  AGE
fss-pvc  Bound  fss-pv  200Gi   RWX      pca-fss    2h
```

  7. Use the PVC when creating other objects, such as pods.
For example, you could create a new pod from the following pod definition, which instructs the system to use the `fss-pvc` PVC as the `nginx` volume, which is mounted by the pod at `/persistent-storage`:
Copy
```
apiVersion: v1
kind: Pod
metadata:
 name: fss-dynamic-app
spec:
 containers:
  - name: nginx
   image: nginx:latest
   ports:
    - name: http
     containerPort: 80
   volumeMounts:
    - name: persistent-storage
     mountPath: /usr/share/nginx/html
 volumes:
 - name: persistent-storage
  persistentVolumeClaim:
   claimName: fss-pvc
```

Run the following command to verify that the pod is using the new PVC:
Copy
```
$ kubectl describe pod fss-dynamic-app
```



Was this article helpful?
YesNo

