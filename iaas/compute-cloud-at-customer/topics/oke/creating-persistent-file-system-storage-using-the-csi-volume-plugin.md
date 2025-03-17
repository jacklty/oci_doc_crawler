Updated 2024-12-16
# Creating Persistent File System Storage Using the CSI Volume Plugin
On Compute Cloud@Customer, you can provision a PVC on a new file system using the CSI volume plugin. Use the `kubectl` command to create the storage class and persistent volume claim. The CSI volume plugin provisions the PVC on a new file system.
You can have only one mount target and one file system per VCN. You can have multiple storage classes, persistent volumes, and persistent volume claims per cluster. All storage classes, persistent volumes, and persistent volume claims in a cluster share one NFS.
  1. Create a new storage class that uses the `fss.csi.oraclecloud.com` provisioner.
```
$ kubectl create -f sc.yaml
```

The following is the content of the `sc.yaml` manifest file:
Copy
```
kind: StorageClass
apiVersion: storage.k8s.io/v1
metadata:
 name: fss-dyn-storage
provisioner: fss.csi.oraclecloud.com
parameters:
 availabilityDomain: AD-1
 compartmentOcid: ocid1.compartment.** _unique_ID_**
 mountTargetSubnetOcid: ocid1.subnet.**_unique_ID_**
 exportPath: AUTOSELECT
 exportOptions: "[{\"source\":\"0.0.0.0/0\",\"requirePrivilegedSourcePort\":false,\"access\":\"READ_WRITE\",\"identitySquash\":\"NONE\"}]"
 encryptInTransit: "false"
```

     * The name for the new storage class is `fss-dyn-storage`.
     * Either `mountTargetSubnetOcid` or `mountTargetOcid` is required. The value of `mountTargetSubnetOcid` is the OCID of the subnet where you want the CSI plugin to create a mount target. The value of `mountTargetOcid` is the OCID of an existing mount target. If you specify both `mountTargetSubnetOcid` and `mountTargetOcid`, `mountTargetOcid` is used and `mountTargetSubnetOcid` is ignored.
To ensure that the mount target can be reached from worker nodes, specify the subnet that has configuration like the "worker" subnet described in [Creating an OKE Worker Subnet](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/oke/creating-a-worker-subnet.htm#creating-a-worker-subnet "On Compute Cloud@Customer, part of configuring OKE requires external and internal access security lists and a worker subnet.") or create the mount target on the subnet that has configuration like the worker subnet. Ensure that TCP port 2049 to the NFS server is open on that subnet.
     * The `compartmentOcid` is optional. This value is the OCID of the compartment where the new file system (and the new mount target, if `mountTargetSubnetOcid` is specified) will be created. The default value is the same compartment as the cluster.
     * You must specify `AUTOSELECT` as the value for `exportPath`.
     * The `exportOptions` value is the NFS export options entry within the file system export that defines the access granted to NFS clients when they connect to a mount target. The `source` can be a single IP address or CIDR block range. This value is a set of parameters in JSON format.
     * The value of `encryptInTransit` specifies whether to encrypt data in transit.
  2. Create a PVC to be provisioned by the new file system in the File Storage service.
```
$ kubectl create -f fss-dyn-claim.yaml
```

The following is the content of the `fss-dyn-claim.yaml` manifest file:
Copy
```
apiVersion: v1
kind: PersistentVolumeClaim
metadata:
 name: fss-dynamic-claim
spec:
 accessModes:
 - ReadWriteMany
 storageClassName: "fss-dyn-storage"
 resources:
  requests:
   storage: 50Gi
```

  3. Verify that the PVC has been bound to the new persistent volume.
Copy
```
$ kubectl get pvc
NAME       STATUS VOLUME                    CAPACITY ACCESS MODES STORAGECLASS  AGE
fss-dynamic-claim Bound csi-fss-f6823a66-8b6f-4c42-9d1f-d25723e69257 50Gi   RWX     fss-dyn-storage 6m47s
```

  4. Use the new PVC when you create objects such as pods.
The following is an example object creation:
Copy
```
$ kubectl create nginx.yaml
```

The following is the content of the `nginx.yaml` file. See the `claimName` on the last line:
Copy
```
apiVersion: apps/v1
kind: Deployment
metadata:
 name: nginx-deployment
spec:
 replicas: 3
 selector:
  matchLabels:
   app: nginx
 template:
  metadata:
   labels:
    app: nginx
  spec:
   containers:
   - name: nginx
    image: nginx_image_url
    ports:
    - name: http
     containerPort: 80
    volumeMounts:
    - name: persistent-storage
     mountPath: /usr/share/nginx/html
   volumes:
   - name: persistent-storage
    persistentVolumeClaim:
     claimName: fss-dynamic-claim
```

Verify that the object is created and deployed:
Copy
```
$ kubectl get deploy
NAME       READY UP-TO-DATE AVAILABLE AGE
nginx-deployment 3/3  3     0     104s
```



Was this article helpful?
YesNo

