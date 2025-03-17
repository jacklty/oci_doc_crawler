Updated 2025-01-31
# Provisioning PVCs on the Block Volume Service
_Find out how to provision persistent volume claims for clusters you've created using Kubernetes Engine (OKE) by attaching volumes from the Block Volume service._
The Oracle Cloud Infrastructure Block Volume service (the Block Volume service) provides persistent, durable, and high-performance block storage for your data. You can use the CSI volume plugin or the FlexVolume volume plugin to connect clusters to volumes from the Block Volume service. Oracle recommends using the CSI volume plugin because:
  * New functionality is only being added to the CSI volume plugin, not to the FlexVolume volume plugin (although Kubernetes developers will continue to maintain the FlexVolume volume plugin).
  * The CSI volume plugin does not require access to underlying operating system and root file system dependencies.


**Note** The upstream Kubernetes project is deprecating the FlexVolume volume plugin in Kubernetes version 1.23. Removal of the feature will adhere to guidelines in the [Kubernetes Deprecation Policy](https://kubernetes.io/docs/reference/using-api/deprecation-policy/).
We recommend that you migrate existing workloads from the FlexVolume volume plugin to the CSI volume plugin. For migration instructions, see [Migrating from the FlexVolume Volume Plugin to the CSI Volume Plugin](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengcreatingpersistentvolumeclaim_topic-Provisioning_PVCs_on_BV-PV_Migrating-from-FlexVolume.htm#contengcreatingpersistentvolumeclaim_topic_Provisioning_PVCs_on_BV_PV_Migrating_from_FlexVolume "Find out how to migrate a Kubernetes workload \(managed by a StatefulSet\) from the FlexVolume volume plugin to the CSI volume plugin.").
The StorageClass specified for a PVC controls which volume plugin to use to connect to Block Volume service volumes. Two storage classes are defined by default, `oci-bv` for the CSI volume plugin and `oci` for the FlexVolume plugin. If you don't explicitly specify a value for `storageClassName` in the yaml file that defines the PVC, the cluster's default storage class is used. The cluster's default storage class is initially set according to the Kubernetes version that was specified when the cluster was created, as follows:
  * In clusters created by Kubernetes Engine to run Kubernetes version 1.24 (or later), the `oci-bv` storage class is initially set as the default. The `oci-bv` storage class is used by the CSI volume plugin.
  * In clusters created by Kubernetes Engine to run Kubernetes version 1.23 (or earlier), the `oci` storage class is initially set as the default. The `oci` storage class is used by the FlexVolume volume plugin.


**Note**
In clusters originally created by Kubernetes Engine to run Kubernetes version 1.23 (or earlier), and subsequently upgraded to Kubernetes version 1.24 (or later), the default storage class is not changed during the upgrade process. So if the default storage class was `oci` before the upgrade, the default storage class continues to be `oci` after the upgrade.
If you want `oci-bv` instead of `oci` to be the default storage class of a cluster that you've upgraded from Kubernetes version 1.23 (or earlier) to Kubernetes version 1.24 (or later), change the default storage class as follows:
  1. Specify that `oci` is not the default storage class by entering:
Copy
```
kubectl patch storageclass oci -p '{"metadata": {"annotations": {"storageclass.beta.kubernetes.io/is-default-class":"false"}}}'
```

  2. Specify that `oci-bv` is the default storage class by entering:
Copy
```
kubectl patch storageclass oci-bv -p '{"metadata": {"annotations": {"storageclass.kubernetes.io/is-default-class":"true"}}}'
```



In the case of the CSI volume plugin, the CSI topology feature ensures that worker nodes and volumes are located in the same availability domain. In the case of the FlexVolume volume plugin, you can use the `matchLabels` element to select the availability domain in which a persistent volume claim is provisioned. Note that you do not use the `matchLabels` element with the CSI volume plugin.
Regardless of the volume plugin you choose to use, if a cluster is in a different compartment to its worker nodes, you must create an additional policy to enable access to Block Volume service volumes. This situation arises when the subnet specified for a node pool belongs to a different compartment to the cluster. To enable the worker nodes to access Block Volume service volumes, create the additional policy with both the following policy statements:
  * `ALLOW any-user to manage volumes in TENANCY where request.principal.type =      'cluster'`
  * `ALLOW any-user to manage volume-attachments in TENANCY where      request.principal.type = 'cluster'`


To explicitly specify the volume plugin to use to connect to the Block Volume service when provisioning a persistent volume claim, specify a value for `storageClassName` in the yaml file that defines the PVC:
  * to use the CSI volume plugin, specify `storageClassName: "oci-bv"`
  * to use the FlexVolume volume plugin, specify `storageClassName: "oci"`


Note the following:
  * The minimum amount of persistent storage that a PVC can request is 50 gigabytes. If the request is for less than 50 gigabytes, the request is rounded up to 50 gigabytes.
  * If you want to be able to increase the amount of persistent storage that a PVC can request, set `allowVolumeExpansion: true` in the definition of the storage class specified for the PVC. See [Expanding a Block Volume](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengcreatingpersistentvolumeclaim_topic-Provisioning_PVCs_on_BV.htm#contengcreatingpersistentvolumeclaim_topic_Provisioning_PVCs_on_BV_PV_Volume_expansion).
  * When you create a cluster, you can optionally define tags to apply to block volumes created when persistent volume claims (PVCs) are defined. Tagging enables you to group disparate resources across compartments, and also enables you to annotate resources with your own metadata. See [Applying Tags to Block Volumes](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengtaggingclusterresources_tagging-oke-resources_block-volume-tags.htm#contengtaggingclusterresources_tagging_oke_resources_block_volume_tags "Find out how to apply tags to block volume resources, and how to override initial block volume tags, when using Kubernetes Engine \(OKE\).").
  * Having created a PVC on a new block volume using the CSI volume plugin, you can view capacity statistics for the block volume using a metrics aggregation tool (such as Prometheus), including:
    * `kubelet_volume_stats_available_bytes`
    * `kubelet_volume_stats_capacity_bytes`
    * `kubelet_volume_stats_inodes`
    * `kubelet_volume_stats_inodes_free`
    * `kubelet_volume_stats_inodes_used`
    * `kubelet_volume_stats_used_bytes`


## Creating a PVC on a Block Volume Using the CSI Volume Plugin 🔗 
You can dynamically provision a block volume using the CSI plugin specified by the `oci-bv` storage class's definition (`provisioner: blockvolume.csi.oraclecloud.com`). For example, if the cluster administrator has not created any suitable PVs that match the PVC request.
You define a PVC in a file called csi-bvs-pvc.yaml. For example:
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

Enter the following command to create the PVC from the csi-bvs-pvc.yaml file:
Command
CopyTry It
```
kubectl create -f csi-bvs-pvc.yaml
```

The output from the above command confirms the creation of the PVC:
```
persistentvolumeclaim "mynginxclaim" created
```

Verify that the PVC has been created by running `kubectl get pvc`:
Command
CopyTry It
```
kubectl get pvc
```

The output from the above command shows the current status of the PVC:
Copy
```
		
NAME        STATUS  VOLUME  CAPACITY  ACCESSMODES  STORAGECLASS  AGE
mynginxclaim    Pending                  oci-bv     4m
```

The PVC has a status of `Pending` because the `oci-bv` storage class's definition includes `volumeBindingMode: WaitForFirstConsumer`.
You can use this PVC when creating other objects, such as pods. For example, you could create a new pod from the following pod definition, which instructs the system to use the mynginxclaim PVC as the nginx volume, which is mounted by the pod at /data.
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

Having created the new pod, you can verify that the PVC has been bound to a new persistent volume by entering:
Command
CopyTry It
```
kubectl get pvc
```

The output from the above command confirms that the PVC has been bound:
Copy
```
			
NAME        STATUS  VOLUME                CAPACITY  ACCESSMODES  STORAGECLASS  AGE
mynginxclaim    Bound   ocid1.volume.oc1.iad.<unique_ID>   50Gi    RWO      oci-bv     4m
```

You can verify that the pod is using the new persistent volume claim by entering:
Command
CopyTry It
```
kubectl describe pod nginx
```

You can view capacity statistics for the new persistent volume using a metrics aggregation tool such as Prometheus.
## Creating a Volume Snapshot from a Block Volume Backup Using the CSI Volume Plugin 🔗 
A Kubernetes volume snapshot is a snapshot of a persistent volume on a storage system. You can use a volume snapshot to provision a new persistent volume. For more information, about Kubernetes volume snapshots, see [Volume Snapshots](https://kubernetes.io/docs/concepts/storage/volume-snapshots/) in the Kubernetes documentation.
When using the CSI volume plugin to connect clusters to block volumes in the Block Volume service, you can use block volume backups to provision Kubernetes volume snapshots. You can use a volume snapshot to create a new block volume and pre-populate it with data from the block volume backup. For more information about block volume backups in the Block Volume service, see [Overview of Block Volume Backups](https://docs.oracle.com/iaas/Content/Block/Concepts/blockvolumebackups.htm).
You can use the CSI volume plugin to provision a volume snapshot in one of two ways:
  * **Dynamically:** You can request the creation of a backup of the block volume provisioning a persistent volume. You specify the persistent volume claim using the `VolumeSnapshot` object, and you specify the parameters to use to create the block volume backup using the `VolumeSnapshotClass` object. Dynamically provisioned volume snapshots are also referred to as dynamic volume snapshots. See [Creating Dynamically Provisioned Volume Snapshots](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengcreatingpersistentvolumeclaim_topic-Provisioning_PVCs_on_BV.htm#contengcreatingpersistentvolumeclaim_topic-Provisioning_PVCs_on_BV-PV_From_Snapshot_CSI__section_dynamic-volume-snapshots).
  * **Statically:** You can provide details of an existing block volume backup using the `VolumeSnapshotContent` object. Statically provisioned volume snapshots are also referred to as static volume snapshots, and as pre-provisioned volume snapshots. [Creating Statically Provisioned Volume Snapshots](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengcreatingpersistentvolumeclaim_topic-Provisioning_PVCs_on_BV.htm#contengcreatingpersistentvolumeclaim_topic-Provisioning_PVCs_on_BV-PV_From_Snapshot_CSI__section_static-volume-snapshots)


When you create a dynamically provisioned volume snapshot, the same freeform tags and defined tags that were applied to the source block volume are applied to the block volume backup. However, you can use parameters to apply additional tags to the block volume backup (see [Tagging Block Volume Backups](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengcreatingpersistentvolumeclaim_topic-Provisioning_PVCs_on_BV.htm#contengcreatingpersistentvolumeclaim_topic-Provisioning_PVCs_on_BV-PV_From_Snapshot_CSI__section_tagging-block-volume-backups)).
There are a number of prerequisites to meet before creating volume snapshots for use with clusters created by Kubernetes Engine. See [Prerequisites for Creating Volume Snapshots](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengcreatingpersistentvolumeclaim_topic-Provisioning_PVCs_on_BV.htm#contengcreatingpersistentvolumeclaim_topic-Provisioning_PVCs_on_BV-PV_From_Snapshot_CSI__section_volume-snapshot-prerequisites).
Note the following when creating and using volume snapshots:
  * You can only create volume snapshots when using the CSI volume plugin (that is, you cannot create volume snapshots when using the FlexVolume volume plugin).
  * In the case of dynamic volume backups, the CSI volume plugin creates a new block volume backup to provision a dynamic volume snapshot in the same compartment as the cluster. In the case of static volume snapshots, the block volume backup provisioning a static volume snapshot can be in a different compartment to the cluster, provided appropriate policy statements exist to enable the cluster to access that other compartment (see [Prerequisites for Creating Volume Snapshots](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengcreatingpersistentvolumeclaim_topic-Provisioning_PVCs_on_BV.htm#contengcreatingpersistentvolumeclaim_topic-Provisioning_PVCs_on_BV-PV_From_Snapshot_CSI__section_volume-snapshot-prerequisites)).
  * You cannot use the CSI volume plugin to re-populate an existing volume with data. In other words, you cannot restore (revert) data in an existing persistent volume to an earlier state by changing the volume snapshot specified in the persistent volume claim's manifest. You can only use the CSI volume plugin to populate a new volume with data.
  * When you create a block volume backup (for example, when creating a dynamic volume snapshot), the encryption key that was used when creating the block volume is also used to create the block volume backup. You cannot specify a new encryption key when creating a block volume backup. So the block volume backup uses the same encryption as the block volume it backs up.
  * The size specified for a persistent volume provisioned by a volume snapshot must not be smaller than the size of the original volume from which the snapshot was created. 
  * When the CSI volume plugin creates a new block volume to back a persistent volume provisioned by a volume snapshot, the placement of the block volume depends on the topology requirements of the volume creation request. For example, if the CSI volume plugin creates a block volume for a pod that uses a persistent volume claim, the block volume is created in the same availability domain as the worker node on which the pod is running. 
  * Cross-namespace snapshots are not supported.
  * As the number of `VolumeSnapshot` and `VolumeSnapshotContent` objects in a cluster increases, they can consume significant space in etcd, which might lead to unexpected cluster behavior. To keep the cluster healthy, we recommend that you implement a purging mechanism to regularly clean up `VolumeSnapshot` and `VolumeSnapshotContent` objects that are no longer required.


### Prerequisites for Creating Volume Snapshots 🔗 
To create volume snapshots for use with clusters created by Kubernetes Engine:
  * the cluster's control plane nodes must be running Kubernetes version 1.24 or later
  * the cluster's worker nodes must be using x86-based or Arm-based processor compute shapes
  * the cluster's worker nodes must be running Oracle Linux 7 or Oracle Linux 8, or Ubuntu 


The `VolumeSnapshot`, `VolumeSnapshotContent`, and `VolumeSnapshotClass` objects are not part of the core Kubernetes API. Therefore, before you can create volume snapshots using the CSI volume plugin, you have to install the necessary CRD (Custom Resource Definition) files on the cluster, by running the following commands: 
```
kubectl apply -f https://raw.githubusercontent.com/kubernetes-csi/external-snapshotter/master/client/config/crd/snapshot.storage.k8s.io_volumesnapshotclasses.yaml
```
```
kubectl apply -f https://raw.githubusercontent.com/kubernetes-csi/external-snapshotter/master/client/config/crd/snapshot.storage.k8s.io_volumesnapshotcontents.yaml
```
```
kubectl apply -f https://raw.githubusercontent.com/kubernetes-csi/external-snapshotter/master/client/config/crd/snapshot.storage.k8s.io_volumesnapshots.yaml
```

If you want to use a statically provisioned volume snapshot to provision a new persistent volume, and the underlying block volume backup is in a different compartment to the cluster, appropriate policy statements must exist to enable the cluster to access the block volume backups in that other compartment. For example:
```
ALLOW any-user to manage volume-backups in compartment <compartment-name> where request.principal.type = 'cluster'
ALLOW any-user to use volumes in compartment <compartment-name> where request.principal.type = 'cluster'
```

### Creating Dynamically Provisioned Volume Snapshots 🔗 
To dynamically provision a volume snapshot by creating a backup of the block volume provisioning a persistent volume claim, you first define a `VolumeSnapshotClass` object that specifies the type of block volume backup to create. Having created the `VolumeSnapshotClass` object, you then define a `VolumeSnapshot` object that uses the `VolumeSnapshotClass`. You use the `VolumeSnapshot` object to specify the persistent volume claim provisioned by the block volume that you want to back up.
**Note** When you create a dynamically provisioned volume snapshot, Kubernetes Engine creates a `VolumeSnapshotContent` object. Do not modify the `VolumeSnapshotContent` objects that Kubernetes Engine creates, nor create your own `VolumeSnapshotContent` objects, when creating dynamically provisioned volume snapshots.
For example, you define a persistent volume claim named sample-pvc in a file called csi-mypvctobackup.yaml, provisioned by a block volume: 
```
apiVersion: v1
kind: PersistentVolumeClaim
metadata:
 name: sample-pvc
spec:
 accessModes:
  - ReadWriteOnce
 storageClassName: "oci-bv"
 resources:
  requests:
   storage: 50Gi
```

Create the persistent volume claim:
```
kubectl create -f csi-mypvctobackup.yaml
```

You can use the persistent volume claim when defining other objects, such as pods. For example, the following pod definition instructs the system to use the sample-pvc persistent volume claim as the nginx volume, which is mounted by the pod at /sample-volume.
```
apiVersion: v1
kind: Pod
metadata:
 name: sample-pod
spec:
 containers:
  - name: sample-nginx
   image: nginx
   ports:
    - containerPort: 80
     name: "http-server"
   volumeMounts:
    - mountPath: "/usr/share/nginx/html"
     name: sample-volume
 volumes:
 - name: sample-volume
  persistentVolumeClaim:
   claimName: sample-pvc
```

Having created the new pod, the persistent volume claim is bound to a new persistent volume provisioned by a block volume.
In readiness for creating a backup of the block volume provisioning the persistent volume claim, you set parameters for the block volume backup by defining a `VolumeSnapshotClass` object named my-snapclass in a file called csi-mysnapshotclass.yaml:
```
apiVersion: snapshot.storage.k8s.io/v1
kind: VolumeSnapshotClass
metadata:
 name: my-snapclass
driver: blockvolume.csi.oraclecloud.com
parameters:
 backupType: full
deletionPolicy: Delete
```

where:
  * `driver: blockvolume.csi.oraclecloud.com` specifies the CSI volume plugin to provision `VolumeSnapshot` objects.
  * `parameters.backupType: full` specifies a block volume backup is to include all changes since the block volume was created. Specify `incremental` to create a backup with only the changes since the last backup. Note that for data recovery purposes, there is no functional difference between an incremental backup and a full backup. See [Volume Backup Types](https://docs.oracle.com/iaas/Content/Block/Concepts/blockvolumebackups.htm#backuptype).
  * `deletionPolicy: Delete` specifies what happens to a block volume backup if the associated `VolumeSnapshot` object is deleted. Specify `Retain` to keep a block volume backup if the associated `VolumeSnapshot` object is deleted.


By default, the same freeform tags and defined tags that were applied to the source block volume are applied to the block volume backup. However, you can use parameters to apply additional tags to the block volume backup (see [Tagging Block Volume Backups](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengcreatingpersistentvolumeclaim_topic-Provisioning_PVCs_on_BV.htm#contengcreatingpersistentvolumeclaim_topic-Provisioning_PVCs_on_BV-PV_From_Snapshot_CSI__section_tagging-block-volume-backups)).
Create the `VolumeSnapshotClass` object:
```
kubectl create -f csi-mysnapshotclass.yaml
```

To create a backup of the block volume provisioning the persistent volume claim, you then define a `VolumeSnapshot` object as my-snapshot in a file called csi-mysnapshot.yaml:
```
apiVersion: snapshot.storage.k8s.io/v1
kind: VolumeSnapshot
metadata:
 name: my-snapshot
 namespace: default
spec:
 volumeSnapshotClassName: my-snapclass
 source:
  persistentVolumeClaimName: sample-pvc
```

where:
  * `volumeSnapshotClassName: my-snapclass` specifies `my-snapclass` as the `VolumeSnapshotClass` object from which to obtain parameters to use when creating the block volume backup. Note that you cannot change `volumeSnapshotClassName` after you have created the `VolumeSnapshot` object (you have to create a new `VolumeSnapshot` object).
  * `persistentVolumeClaimName: sample-pvc` specifies `sample-pvc` as the persistent volume claim based on the block volume for which you want to create a block volume backup. Note that you cannot change the source after you have created the `VolumeSnapshot` object (you have to create a new `VolumeSnapshot` object).


Create the `VolumeSnapshot` object:
```
kubectl create -f csi-mysnapshot.yaml
```

The `VolumeSnapshot` object is created and provisioned by a new block volume backup. You can use the volume snapshot to provision a new persistent volume (see [Using a Volume Snapshot to Provision a New Volume](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengcreatingpersistentvolumeclaim_topic-Provisioning_PVCs_on_BV.htm#contengcreatingpersistentvolumeclaim_topic-Provisioning_PVCs_on_BV-PV_From_Snapshot_CSI__section_using-volume-snapshot-to-provision-restore)).
### Creating Statically Provisioned Volume Snapshots 🔗 
To statically provision a volume snapshot from an existing block volume backup, you first create the block volume backup (see [Creating a Manual Backup for a Block Volume](https://docs.oracle.com/iaas/Content/Block/Tasks/backingupavolume.htm) ).
Having created the block volume backup, define a `VolumeSnapshotContent` object and specify details (including the OCID) of the existing block volume backup. You can then define a `VolumeSnapshot` object and specify the `VolumeSnapshotContent` object that provides details of the existing block volume backup. 
For example, you define the `VolumeSnapshotContent` object as my-static-snapshot-content in a file called csi-mystaticsnapshotcontent.yaml:
```
apiVersion: snapshot.storage.k8s.io/v1
kind: VolumeSnapshotContent
metadata:
 name: my-static-snapshot-content
spec:
 deletionPolicy: Retain
 driver: blockvolume.csi.oraclecloud.com
 source:
  snapshotHandle: ocid1.volumebackup.oc1.iad.aaaaaa______xbd
 volumeSnapshotRef:
  name: my-static-snapshot
  namespace: default
```

where:
  * `deletionPolicy: Retain` specifies what happens to a block volume backup if the associated `VolumeSnapshot` object is deleted. Specify `Delete` to delete a block volume backup if the associated `VolumeSnapshot` object is deleted.
  * `driver: blockvolume.csi.oraclecloud.com` specifies to use the CSI volume plugin to provision `VolumeSnapshot` objects.
  * `snapshotHandle: ocid1.volumebackup.oc1.iad.aaaaaa______xbd` specifies the OCID of the existing block volume backup.
  * `volumeSnapshotRef.name: my-static-snapshot` specifies the name of the corresponding `VolumeSnapshot` object to be provisioned from the existing block volume backup. This field is required. Note that the `VolumeSnapshot` object need not exist when you create the `VolumeSnapshotContent` object.
  * `namespace: default` specifies the namespace containing the corresponding `VolumeSnapshot` object to be provisioned from the existing block volume backup. This field is required.


Create the `VolumeSnapshotContent` object:
```
kubectl create -f csi-mystaticsnapshotcontent.yaml
```

You define the statically provisioned `VolumeSnapshot` object as my-static-snapshot in a file called csi-mystaticsnapshot.yaml:
```
apiVersion: snapshot.storage.k8s.io/v1
kind: VolumeSnapshot
metadata:
 name: my-static-snapshot
spec:
 source:
  volumeSnapshotContentName: my-static-snapshot-content
```

where `VolumeSnapshotContentName: my-static-snapshot-content` specifies the name of the `VolumeSnapshotContent` object you created previously. Note that you cannot change the source after you have created the `VolumeSnapshot` object (you have to create a new `VolumeSnapshot` object).
Create the `VolumeSnapshot` object:
```
kubectl create -f csi-mystaticsnapshot.yaml
```

The `VolumeSnapshot` object is created and provisioned by the block volume backup specified in the `VolumeSnapshotContent` object. You can use the volume snapshot to provision a new persistent volume (see [Using a Volume Snapshot to Provision a New Volume](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengcreatingpersistentvolumeclaim_topic-Provisioning_PVCs_on_BV.htm#contengcreatingpersistentvolumeclaim_topic-Provisioning_PVCs_on_BV-PV_From_Snapshot_CSI__section_using-volume-snapshot-to-provision-restore)).
### Using a Volume Snapshot to Provision a New Volume 🔗 
Having created a dynamically provisioned or statically provisioned volume snapshot, you can specify the volume snapshot as the datasource for a persistent volume claim to provision a new persistent volume.
For example, you define a persistent volume claim named pvc-fromsnapshot in a file called csi-mypvcfromsnapshot.yaml, provisioned by a volume snapshot named test-snapshot: 
```
apiVersion: v1
kind: PersistentVolumeClaim
metadata:
 name: pvc-fromsnapshot
 namespace: default
spec:
 storageClassName: oci-bv
 dataSource:
  name: test-snapshot
  kind: VolumeSnapshot
  apiGroup: snapshot.storage.k8s.io
 accessModes:
  - ReadWriteOnce
 resources:
  requests:
   storage: 50Gi
```

where:
  * `datasource.name: test-snapshot` specifies test-snapshot as the name of the `VolumeSnapshot` object to use as the data source for the persistent volume.
  * `datasource.apiGroup: snapshot.storage.k8s.io` specifies the version of the Kubernetes snapshot storage API to use.


Create the persistent volume claim:
```
kubectl create -f csi-mypvcfromsnapshot.yaml
```

When the persistent volume claim is used to provision another object (such as a pod), a persistent volume is created and the `VolumeSnapshot` object you specified is used to populate the underlying block volume. For example, you could create a new pod from the following pod definition that instructs the system to use the pvc-fromsnapshot PVC as the nginx volume, which is mounted by the pod at /data.
```
apiVersion: v1
kind: Pod
metadata:
 name: sample-pod-restore
spec:
 containers:
  - name: nginx
   image: nginx:latest
   ports:
    - name: http
     containerPort: 80
   volumeMounts:
    - name: data
     mountPath: /data
 volumes:
  - name: data
   persistentVolumeClaim:
    claimName: pvc-fromsnapshot
```

Having created the new pod, the persistent volume claim is bound to a new persistent volume provisioned by a new block volume populated by the `VolumeSnapshot` object.
### Tagging Block Volume Backups  🔗 
When you use the CSI volume plugin to create a dynamically provisioned volume snapshot, the same freeform tags and defined tags that were applied to the source block volume are also applied to the block volume backup.
To apply additional freeform tags to the new block volume backup, include the following parameter in the parameters section of the VolumeSnapshotClass manifest file: 
```
oci.oraclecloud.com/freeform-tags: '{"<first-tag-key>":","<first-tag-value>","<second-tag-key>":"<second-tag-value>"...}'
```

To apply additional defined tags to the new block volume backup, include the following parameter in the parameters section of the VolumeSnapshotClass manifest file: 
```
oci.oraclecloud.com/defined-tags: '{"<tag-namespace>": {"<first-tag-key>":","<first-tag-value>","<second-tag-key>":"<second-tag-value>"...}}'
```

For example:
```
apiVersion: snapshot.storage.k8s.io/v1
kind: VolumeSnapshotClass
metadata:
 name: my-snapclass
driver: blockvolume.csi.oraclecloud.com
parameters:
 backupType: full
 oci.oraclecloud.com/freeform-tags: '{"<first-tag-key>":","<first-tag-value>","<second-tag-key>":"<second-tag-value>"...}'
deletionPolicy: Delete
```

## Creating a PVC by Cloning an Existing Block Volume Using the CSI Volume Plugin 🔗 
A Kubernetes clone is an exact duplicate of an existing persistent volume on a storage system. You can clone an existing persistent volume to provision a new persistent volume claim. The new persistent volume contains a copy of the data from the source persistent volume, but is independent of the source persistent volume. You can use volume clones to test configuration changes quickly, without impacting a production environment. For more information about Kubernetes clones, see [CSI Volume Cloning](https://kubernetes.io/docs/concepts/storage/volume-pvc-datasource/) in the Kubernetes documentation..
In the Block Volume service, you can clone a block volume to create a new block volume pre-populated with data from the source block volume. For more information about cloning block volumes in the Block Volume service, see [Cloning a Block Volume](https://docs.oracle.com/iaas/Content/Block/Tasks/cloningavolume.htm).
When using the CSI volume plugin to connect clusters to block volumes in the Block Volume service, you can provision a new PVC with a new block volume that has been cloned from an existing block volume provisioning another existing PVC. To indicate that you want the CSI volume plugin to clone the existing block volume for the new PVC, you specify the existing PVC as the datasource for the new PVC.
The new PVC can be used in the same way as any other PVC, and is entirely separate to the existing PVC specified as the datasource. Similarly, the new block volume and the existing block volume from which it is cloned are entirely separate resources, and can be updated, cloned, snapshot, and deleted independently of each other. 
As soon as the source block volume has been cloned and a new block volume created (usually within a few seconds), the new block volume has a state of Available. All data present in the source block volume at that moment is copied to the new block volume (no subsequent changes are copied). However, the data is copied in the background, which can take up to thirty minutes depending on the size of the block volume (for example, it can take up to fifteen minutes to copy a 1 TB block volume). Therefore, to avoid the possibility of errors or data corruption, the new PVC has a state of Pending until all the data has been copied. When all the data has been copied, the new PVC is bound to the PV provisioned by the new block volume, and the new PVC has a state of Available.
There are a number of prerequisites to meet before provisioning a new persistent volume claim by cloning the block volume that is already provisioning an existing persistent volume claim. See [Prerequisites for Cloning an Existing Block Volume to Provision a New PVC](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengcreatingpersistentvolumeclaim_topic-Provisioning_PVCs_on_BV.htm#contengcreatingpersistentvolumeclaim_topic-Provisioning_PVCs_on_BV-PV_From_Clone_CSI__section_volume-clone-prerequisites).
Note the following when cloning a block volume to provision a new PVC:
  * The CSI volume plugin creates the new block volume in the same availability domain, region, and tenancy as the source block volume. 
  * The new block volume created by the CSI volume plugin can itself be cloned as soon at it has a state of Available.
  * Any topology requirements in a volume creation request are ignored. For example, if the CSI volume plugin clones a block volume for a pod that uses a persistent volume claim, the new block volume is created in the same availability domain as the worker node on which the pod is running.
  * You cannot use the CSI volume plugin to clone block volumes created by the FlexVolume volume plugin.
  * You cannot delete the source PVC while cloning is in progress. Similarly, you cannot delete a source block volume while data is being copied to a block volume that has been cloned from it.
  * Cross-namespace cloning is not supported. The new PVC and the source PVC must both be in the same namespace.
  * You do not have to explicitly specify a storage class for the new PVC. If you do explicitly specify a storage class for the new PVC, the storage class you specify can be different to the storage class specified for the source PVC. If you do not specify a storage class for the new PVC, the default storage class is used. 


### Prerequisites for Cloning an Existing Block Volume to Provision a New PVC 🔗 
To provision a new persistent volume claim by cloning the block volume that is already provisioning an existing persistent volume claim:
  * The cluster's control plane nodes must be running Kubernetes version 1.25 or later.
  * The cluster's worker nodes must be using x86-based or Arm-based processor compute shapes.
  * The cluster's worker nodes must be running Oracle Linux 7 or Oracle Linux 8, or Ubuntu. 
  * The existing PVC that you specify as the datasource for the new PVC must:
    * Already be bound to a PV provisioned by a block volume.
    * Have a state of Available.
  * The new block volume must be the same size as, or larger than, the source block volume from which it is cloned. If you specify a storage value for the new PVC that is larger than the source block volume, the new block volume is sized accordingly. You cannot specify a storage value for the new PVC that is smaller than the block volume you want to clone, or smaller than the storage value of the source PVC.
  * The file system type specified for the new block volume must be the same as the file system type of the source block volume from which it is cloned (see [Specifying File System Types for Block Volumes](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengcreatingpersistentvolumeclaim_topic-Provisioning_PVCs_on_BV.htm#contengcreatingpersistentvolumeclaim_topic-Provisioning_PVCs_on_BV-PV_File-storage-types)).


### Cloning an Existing Block Volume to Provision a New PVC
To provision a new persistent volume claim by cloning the block volume that is already provisioning an existing persistent volume claim, you specify the existing persistent volume claim as the `dataSource` of the new persistent volume claim.
For example, you define a persistent volume claim named my-clone-pvc in a file called csi-myclonepvc.yaml. The my-clone-pvc persistent volume claim is provisioned by a block volume created by cloning the block volume that provisions the my-source-pvc persistent volume claim: 
```
apiVersion: v1
kind: PersistentVolumeClaim
metadata:
 name: my-clone-pvc
spec:
 accessModes:
  - ReadWriteOnce
 storageClassName: custom-clone-storage-class
 resources:
  requests:
   storage: 50Gi
 dataSource:
  kind: PersistentVolumeClaim
  name: my-source-pvc
```

Create the persistent volume claim:
```
kubectl create -f csi-myclonepvc.yaml
```

You can use the persistent volume claim when defining other objects, such as pods. For example, the following pod definition instructs the system to use the my-clone-pvc persistent volume claim as the nginx volume, which is mounted by the pod at /sample-volume.
```
apiVersion: v1
kind: Pod
metadata:
 name: sample-pod
spec:
 containers:
  - name: sample-nginx
   image: nginx
   ports:
    - containerPort: 80
     name: "http-server"
   volumeMounts:
    - mountPath: "/usr/share/nginx/html"
     name: sample-volume
 volumes:
 - name: sample-volume
  persistentVolumeClaim:
   claimName: my-clone-pvc
```

Having created the new pod, the my-clone-pvc persistent volume claim is bound to a new persistent volume provisioned by a block volume that has been cloned from the block volume provisioning the my-source-pvc persistent volume claim.
### Tagging Cloned Block Volumes
When you use the CSI volume plugin to provision a persistent volume by cloning a block volume provisioning another persistent volume claim, the same freeform tags and defined tags that were applied to the source block volume are also applied to the new block volume. The CSI volume plugin doesn't apply any additional tags to the new block volume. 
## Creating a PVC From an Existing Block Volume or Backup Using the FlexVolume Volume Plugin 🔗 
You can create a PVC from an existing block volume or a block volume backup for use by the FlexVolume volume plugin. For example, if the cluster administrator has created a block volume backup for you to use when provisioning a new persistent volume claim. Such a block volume backup might come with data ready for use by other objects such as pods. 
You define a PVC in a file called flex-pvcfrombackup.yaml. You use the `volume.beta.kubernetes.io/oci-volume-source` annotation element to specify the source of the block volume to use when provisioning a new persistent volume claim using the FlexVolume volume plugin. You can specify the OCID of either a block volume or a block volume backup as the value of the annotation. In this example, you specify the OCID of the block volume backup created by the cluster administrator. For example:
Copy
```
kind: PersistentVolumeClaim
apiVersion: v1
metadata:
 name: myvolume
 annotations:
  volume.beta.kubernetes.io/oci-volume-source: ocid1.volumebackup.oc1.iad.abuw...
spec:
 selector:
  matchLabels:
   topology.kubernetes.io/zone: US-ASHBURN-AD-1
 accessModes:
  - ReadWriteOnce
 resources:
  requests:
   storage: 50Gi
```

Note that the flex-pvcfrombackup.yaml file includes the `matchLabels` element, which is only applicable in the case of the FlexVolume volume plugin. 
Enter the following command to create the PVC from the flex-pvcfrombackup.yaml file:
Command
CopyTry It
```
kubectl create -f flex-pvcfrombackup.yaml
```

The output from the above command confirms the creation of the PVC:
```
persistentvolumeclaim "myvolume" created
```

Verify that the PVC has been created and bound to a new persistent volume created from the volume backup by entering:
Command
CopyTry It
```
kubectl get pvc
```

The output from the above command shows the current status of the PVC:
Copy
```
			
NAME      STATUS  VOLUME                CAPACITY  ACCESSMODES  STORAGECLASS  AGE
myvolume    Bound   ocid1.volume.oc1.iad.<unique_ID>   50Gi    RWO      oci      4m
```

You can use the new persistent volume created from the volume backup when defining other objects, such as pods. For example, the following pod definition instructs the system to use the myvolume PVC as the nginx volume, which is mounted by the pod at /data.
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
    claimName: myvolume
```

Having created the new pod, you can verify that it is running and using the new persistent volume claim by entering:
Command
CopyTry It
```
kubectl describe pod nginx
```

**Note**
In the FlexVolume example in this topic, the PVC requests storage in an availability domain in the Ashburn region using the `topology.kubernetes.io/zone` label. For more information about using this label (and the shortened versions of availability domain names to specify), see [topology.kubernetes.io/zone](https://docs.oracle.com/en-us/iaas/Content/ContEng/Reference/contengsupportedlabelsusecases.htm#failure-domain).
## Encrypting Data At Rest and Data In Transit with the Block Volume Service 🔗 
The Oracle Cloud Infrastructure Block Volume service always encrypts all block volumes and volume backups at rest by using the Advanced Encryption Standard (AES) algorithm with 256-bit encryption. By default all volumes and their backups are encrypted using the Oracle-provided encryption keys. Each time a volume is cloned or restored from a backup the volume is assigned a new unique encryption key.
You have the option to encrypt all of your volumes and their backups using the keys that you own and manage using the Vault service, for more information see [Key Management](https://docs.oracle.com/iaas/Content/KeyManagement/Concepts/keyoverview.htm). If you do not configure a volume to use the Vault service or you later unassign a key from the volume, the Block Volume service uses the Oracle-provided encryption key instead. This applies to both encryption at-rest and paravirtualized in-transit encryption.
All the data moving between the instance and the block volume is transferred over an internal and highly secure network. If you have specific compliance requirements related to the encryption of the data while it is moving between the instance and the block volume, the Block Volume service provides the option to enable in-transit encryption for paravirtualized volume attachments on virtual machine (VM) instances. Some bare metal shapes support in-transit encryption for the instance's iSCSI-attached block volumes. 
For more information about block volume encryption, and in-transit encryption support, see [Block Volume Encryption](https://docs.oracle.com/iaas/Content/Block/Concepts/overview.htm#BlockVolumeEncryption).
When Kubernetes PVCs are backed by the Block Volume service, you choose how block volumes are encrypted by specifying:
  * The master encryption key to use, by setting the `kms-key-id` property in the Kubernetes storage class's definition. You can specify the OCID of a master encryption key in the Vault service.
  * How the block volume is attached to the compute instance, by setting the `attachment-type` property in the Kubernetes storage class's definition to either `iscsi` or `paravirtualized`.
  * Whether in transit encryption is enabled for each node pool in a cluster, by setting the node pool's `isPvEncryptionInTransitEnabled` property (using the CLI, the API, or the node pool's **Use in transit encryption:** option in the Console).


The interaction of the settings you specify determines how block volumes are encrypted, as shown in the table:
Node pool `isPvEncryptionInTransitEnabled` property set to: | Storage `class kms-key-id` property set to: | Storage class `attachment-type` property set to | Is data encrypted at rest? | Is data encrypted in transit? | Notes  
---|---|---|---|---|---  
`true` | OCID of a key in Vault  | `paravirtualized` | Yes (user-managed key) | Yes (user-managed key)  
`true` | OCID of a key in Vault  | `iscsi` | Error | Error | The PV cannot be provisioned because the `attachment-type` property must be set to `paravirtualized` when `isPvEncryptionInTransitEnabled` is set to `True`.  
`true` | not set | `paravirtualized` | Yes (Oracle-managed key) | Yes (Oracle-managed key)  
`true` | not set | `iscsi` | Error | Error | The PV cannot be provisioned because the `attachment-type` property must be set to `paravirtualized` when `isPvEncryptionInTransitEnabled` is set to `True`.  
`false` | OCID of a key in Vault  | `paravirtualized` | Yes (user-managed key) | No  
`false` | OCID of a key in Vault  | `iscsi` | Yes (user-managed key) | No  
`false` | not set | `paravirtualized` | Yes (Oracle-managed key) | No  
`false` | not set | `iscsi` | Yes (Oracle-managed key) | No  
Before you can create a cluster for which you want to manage the master encryption key yourself, you have to:
  * Create a suitable master encryption key in Vault (or obtain the OCID of such a key). See [Managing Keys](https://docs.oracle.com/iaas/Content/KeyManagement/Tasks/managingkeys.htm).
  * Create a policy granting access to the master encryption key. See [Create Policy to Access User-Managed Encryption Keys for Encrypting Boot Volumes, Block Volumes, and/or File Systems](https://docs.oracle.com/en-us/iaas/Content/ContEng/Concepts/contengpolicyconfig.htm#contengpolicyconfig_topic_Create_Policies_for_User_Managed_Encryption).


For more information about key rotation in the Vault service, see [Rotating a Vault Key](https://docs.oracle.com/iaas/Content/KeyManagement/Tasks/managingkeys_topic-To_rotate_a_master_encryption_key.htm).
### Example: Configuring a storage class to enable at-rest and in-transit encryption using the default Oracle-managed key 🔗 
To provision a PVC on a block volume, using a master encryption key managed by Oracle to encrypt data at rest (and optionally in transit), define a storage class and set:
  * `provisioner: ` to `blockvolume.csi.oraclecloud.com`
  * `attachment-type` to `paravirtualized`


For example:
```
apiVersion: storage.k8s.io/v1
kind: StorageClass
metadata:
 name: bv-encrypted-storage-class
provisioner: blockvolume.csi.oraclecloud.com
parameters:
 attachment-type: "paravirtualized"
reclaimPolicy: Delete
volumeBindingMode: WaitForFirstConsumer
```

You can then create a PVC that is provisioned by the storage class you have created.
Having defined the storage class and created the PVC, set each node pool's `isPvEncryptionInTransitEnabled` property to `true` (using the CLI, the API, or the node pool's **Use in transit encryption:** option in the Console). Note that encryption of in transit data is only supported in some situations (see [Encrypting Data At Rest and Data In Transit with the Block Volume Service](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengcreatingpersistentvolumeclaim_topic-Provisioning_PVCs_on_BV.htm#contengcreatingpersistentvolumeclaim_topic_Provisioning_PVCs_on_BV_Encrypting_data)).
### Example: Configuring a storage class to enable at-rest and in-transit encryption using a key that you manage 🔗 
To provision a PVC on a block volume, using a master encryption key managed by you to encrypt data at rest (and optionally in transit), you have to:
  * Create a suitable master encryption key in Vault (or obtain the OCID of such a key). See [Managing Keys](https://docs.oracle.com/iaas/Content/KeyManagement/Tasks/managingkeys.htm).
  * Create a policy granting access to the master encryption key. See [Create Policy to Access User-Managed Encryption Keys for Encrypting Boot Volumes, Block Volumes, and/or File Systems](https://docs.oracle.com/en-us/iaas/Content/ContEng/Concepts/contengpolicyconfig.htm#contengpolicyconfig_topic_Create_Policies_for_User_Managed_Encryption).


Having created a suitable master encryption key and policy, define a storage class and set:
  * `provisioner: ` to `blockvolume.csi.oraclecloud.com`
  * `attachment-type` to `paravirtualized`
  * `kms-key-id` to the OCID of the master encryption key in the Vault service that you want to use to encrypt data


For example:
```
apiVersion: storage.k8s.io/v1
kind: StorageClass
metadata:
 name: bv-user-encrypted-storage-class
provisioner: blockvolume.csi.oraclecloud.com
parameters:
 attachment-type: "paravirtualized"
 kms-key-id: "ocid1.key.oc1.iad.anntl______usjh"
reclaimPolicy: Delete
volumeBindingMode: WaitForFirstConsumer
```

You can then create a PVC that is provisioned by the storage class you have created.
Having defined the storage class and created the PVC, set each node pool's `isPvEncryptionInTransitEnabled` property to `true` (using the CLI, the API, or the node pool's **Use in transit encryption:** option in the Console). Note that encryption of in transit data is only supported in some situations (see [Encrypting Data At Rest and Data In Transit with the Block Volume Service](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengcreatingpersistentvolumeclaim_topic-Provisioning_PVCs_on_BV.htm#contengcreatingpersistentvolumeclaim_topic_Provisioning_PVCs_on_BV_Encrypting_data)).
## Expanding a Block Volume 🔗 
When a PVC is created using the CSI volume plugin (`provisioner: blockvolume.csi.oraclecloud.com`), you can expand the volume size online. By doing so, you make it possible to initially deploy applications with a certain amount of storage, and then subsequently increase the available storage without any downtime.
If you want to support storage request increases, set `allowVolumeExpansion: true` in the definition of the storage class that you specify for the PVC. For example:
```
apiVersion: storage.k8s.io/v1
kind: StorageClass
metadata:
 name: my-bv
provisioner: blockvolume.csi.oraclecloud.com
parameters:
 attachment-type: "paravirtualized"
reclaimPolicy: Delete
volumeBindingMode: WaitForFirstConsumer
allowVolumeExpansion: true
```

The default `oci-bv` storage class for the CSI volume plugin has `allowVolumeExpansion: true` by default.
To expand the size of a volume, edit the PVC manifest and update the volume size, and then apply the manifest. When the disk is next rescanned to enable the operating system to identify the expanded volume size (which can take a few minutes), the increased storage automatically becomes available to pods using the PVC. The pods do not have to be restarted.
Enter the following command to confirm the PVC has been bound to a newly-enlarged block volume:
Command
CopyTry It
```
kubectl get pvc <pvc_name> -o yaml
```

Note the following:
  * Volume expansion is supported in clusters running Kubernetes 1.19 or later. 
  * The default `oci-bv` storage class for the CSI volume plugin is configured with `allowVolumeExpansion: true` in clusters running Kubernetes 1.19 or later. Definitions of `oci-bv` storage classes in existing clusters running Kubernetes 1.19 or later are automatically edited to set `allowVolumeExpansion: true`.
  * You cannot reduce the size of a block volume. You can only specify a larger value than the block volume’s current size. If you update a PVC manifest to request less storage than previously requested, the storage request fails.
  * For more information about increasing block volume sizes in the Block Volume service, see [Resizing a Volume](https://docs.oracle.com/iaas/Content/Block/Tasks/resizingavolume.htm). In particular, note the recommendation to create a backup before resizing a block volume.


### Example: Configuring a storage class to enable block volume expansion 🔗 
Edit the manifest of a PVC provisioned by the `oci-bv` storage class and include a request for storage. For example, you might initially set `storage: 100Gi` to request 100 GB of storage for the PVC, in a file called csi-bvs-pvc-exp.yaml:
```
apiVersion: v1
kind: PersistentVolumeClaim
metadata:
 name: my-pvc
spec:
 storageClassName: oci-bv
 resources:
 requests:
  storage: 100Gi
 volumeName: pvc-bv1
```

Enter the following command to create the PVC from the csi-bvs-pvc-exp.yaml file:
```
kubectl apply -f csi-bvs-pvc-exp.yaml
```

Subsequently, you might find you need to increase the amount of storage available to the PVC. For example, you might change the manifest and set `storage: 200Gi`:
```
apiVersion: v1
kind: PersistentVolumeClaim
metadata:
 name: my-pvc
spec:
 storageClassName: oci-bv
 resources:
 requests:
  storage: 200Gi
 volumeName: pvc-bv1
```

After you apply the manifest, the PV that provisions the PVC is increased to 200 GB. The manifest update triggers the Block Volume service to increase the size of the existing block volume to 200 GB. When the disk is next rescanned (which can take a few minutes), the increased storage automatically becomes available to pods using the PVC. 
## Specifying Block Volume Performance 🔗 
Block volumes in the Block Volume service can be configured for different levels of performance, according to expected workload I/O requirements. Block volume performance is expressed in volume performance units (VPUs). A number of performance levels are available, including:
  * **Lower Cost** (0 VPUs)
  * **Balanced** (10 VPUs)
  * **Higher Performance** (20 VPUs)
  * **Ultra High Performance** (between 30 VPUs and 120 VPUs)


By default, block volumes are configured for the **Balanced** performance level (10 VPUs). For more information about the different block volume performance levels, see [Block Volume Performance Levels](https://docs.oracle.com/iaas/Content/Block/Concepts/blockvolumeperformance.htm#perf_levels).
When you define a PVC using the CSI volume plugin (`provisioner: blockvolume.csi.oraclecloud.com`), you can specify a different block volume performance level in the storage class definition that is appropriate for the expected workload.
Note that you cannot subsequently change the performance level of a block volume backing a PVC. Instead, you have to define a new storage class, set the performance level as required, and create a new PVC provisioned by that new storage class.
### Creating PVCs with Lower Cost (0 VPUs), Balanced (10 VPUs), and Higher Performance (20 VPUs) performance levels 🔗 
To create a PVC backed by a block volume with a **Lower Cost** , **Balanced** , or **Higher Performance** performance level, set `vpusPerGB` in the storage class definition as follows:
  * for a **Lower Cost** performance level, set `vpusPerGB: "0"`
  * for a **Balanced** performance level, set `vpusPerGB: "10"`
  * for a **Higher Performance** performance level, set `vpusPerGB: "20"`


For example:
```
apiVersion: storage.k8s.io/v1
kind: StorageClass
metadata:
 name: oci-high
provisioner: blockvolume.csi.oraclecloud.com
parameters:
 vpusPerGB: "20"
reclaimPolicy: Delete
volumeBindingMode: WaitForFirstConsumer
allowVolumeExpansion: true
```

The value of `vpusPerGB` must be "0", "10", or "20". Other values are not supported.
Create a manifest for a PVC provisioned by the `oci-high` storage class and include a request for storage. For example, in a file called csi-bvs-pvc-perf.yaml:
```
apiVersion: v1
kind: PersistentVolumeClaim
metadata:
 name: oci-pvc-high
spec:
 storageClassName: oci-high
 accessModes:
  - ReadWriteOnce
 resources:
  requests:
   storage: 5Gi
```

Enter the following command to create the PVC from the csi-bvs-pvc-perf.yaml file:
```
kubectl apply -f csi-bvs-pvc-perf.yaml
```

Having created the PVC, you can use it when creating other objects, such as pods. For example, you could create a new pod from the following pod definition, which instructs the system to use the `oci-pvc-high` PVC:
```
apiVersion: v1
kind: Pod
metadata:
 name: pod-high
spec:
 containers:
  - name: app
   image: busybox:latest
   command: ["/bin/sh"]
   args: ["-c", "while true; do echo $(date -u) >> /data/out.txt; sleep 5; done"]
   volumeMounts:
    - name: persistent-storage
     mountPath: /data
 volumes:
  - name: persistent-storage
   persistentVolumeClaim:
    claimName: oci-pvc-high
```

When you create the pod, a new block volume is created in the Block Volume service to back the PVC. The new block volume has the performance level you specified in the `oci-high` storage class definition.
### Creating PVCs with Ultra-High Performance (30 to 120 VPUs) levels 🔗 
To create a PVC backed by a block volume with an **Ultra High Performance** level, you have to complete a number of steps. The steps are described in detail in this section, but in summary, you have to:
  * Create a node pool with worker nodes of a supported shape.
  * If attaching a block volume to compute instances as an iSCSI attachment, install and enable the Block Volume Management plugin on the instances hosting the worker nodes.
  * Create a storage class definition, and set `vpusPerGB` in the storage class definition to a value between 30 and 120.
  * Create a PVC provisioned by the storage class, and include a request for storage.


Having created a suitable PVC, you can define a pod that uses an **Ultra High Performance** block volume, and schedule the pod onto a node that supports **Ultra High Performance** block volumes.
To offer **Ultra High Performance** characteristics, **Ultra High Performance** block volumes must be attached to compute instances hosting worker nodes using a multipath-enabled attachment. However, only the first **Ultra High Performance** block volume that is attached to an instance is attached with a multipath-enabled attachment. As a result, only the first **Ultra High Performance** block volume that is attached to an instance has **Ultra High Performance** characteristics.
If you intend to use more than one **Ultra High Performance** block volume in a cluster, create the same number of nodes that support **Ultra High Performance** block volumes as there are **Ultra High Performance** block volumes.
To create a PVC backed by a block volume with an **Ultra High Performance** level:
  1. Follow the instructions to create a node pool (see [Creating a Managed Node Pool](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/create-node-pool.htm#create-node-pool "Find out how to create a managed node pool using Kubernetes Engine \(OKE\).")), and specify the following:
    1. Specify a Bare Metal (BM) or Virtual Machine (VM) shape that is both supported by Kubernetes Engine and that also supports the **Ultra High Performance** level. 
Note that **Ultra High Performance** block volumes require shapes that support multipath-enabled attachments. Note also that if you want to attach the block volume to the compute instances hosting worker nodes in the node pool as a paravirtualized attachment, the VM.Standard.E4.Flex shape is the only supported shape.
See:
       * [Supported Shapes for Managed Nodes and Virtual Nodes](https://docs.oracle.com/en-us/iaas/Content/ContEng/Reference/contengimagesshapes.htm#shapes) for the shapes supported by Kubernetes Engine
       * [Performance Details for Instance Shapes](https://docs.oracle.com/iaas/Content/Block/Concepts/blockvolumeperformance.htm#shapes_block_details) for the shapes that support the **Ultra High Performance** level.
    2. Specify a label to add to all worker nodes in the node pool to indicate that the worker nodes support the **Ultra High Performance** level. For example, `uhp: supported`
  2. If you want to attach an **Ultra High Performance** block volume to the compute instances hosting worker nodes in the node pool as an iSCSI attachment, install and enable the Block Volume Management plugin on the instances. 
There are different ways to install and enable the Block Volume Management plugin, such as using the Console, or the CLI. Alternatively, you can install and enable the Block Volume Management plugin by specifying a custom cloud-init script similar to the following:
```
#!/bin/bash
curl --fail -H "Authorization: Bearer Oracle" -L0 http://169.254.169.254/opc/v2/instance/metadata/oke_init_script | base64 --decode >/var/run/oke-init.sh
bash /var/run/oke-init.sh
echo "Installing oci cli package"
sudo yum install -y python36-oci-cli
echo "Completed oci cli package"
instance_id=$(curl -H "Authorization: Bearer Oracle" -L http://169.254.169.254/opc/v2/instance/id)
echo "Instance Id : $instance_id"
echo "Updating compute instance agent config."
oci compute instance update --instance-id $instance_id --force --agent-config '{
  "is-agent-disabled": false,
  "plugins-config": [
    {"name": "Block Volume Management", "desiredState": "ENABLED" }
  ]
}' --auth instance_principal
echo "Update completed for instance agent config."

```

Note the following when installing and enabling the Block Volume Management plugin:
     * The Block Volume Management plugin must be able to connect to Oracle services, either because the compute instance has a public IP address, or because the VCN has a service gateway.
     * Permissions must be configured to allow the Block Volume Management plugin to report the iSCSI setup results for multipath-enabled iSCSI attachments.
For more information: 
     * About the Block Volume Management plugin, see [Enabling the Block Volume Management Plugin](https://docs.oracle.com/iaas/Content/Block/Tasks/enablingblockvolumemanagementplugin.htm).
     * About writing custom cloud-init scripts, see [Using Custom Cloud-init Initialization Scripts to Set Up Managed Nodes](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengusingcustomcloudinitscripts.htm#contengwritingcustomcloudinitscripts "Find out how to write custom cloud-init scripts to run on worker nodes in clusters you've created using Kubernetes Engine \(OKE\).").
  3. Create a storage class definition for block volumes with an **Ultra High Performance** performance level, and set `vpusPerGB` in the storage class definition to a value between 30 and 120.
For example:
```
apiVersion: storage.k8s.io/v1
kind: StorageClass
metadata:
 name: oci-uhp-sc
provisioner: blockvolume.csi.oraclecloud.com
parameters:
 vpusPerGB: "30"
 attachment-type: "iscsi"
reclaimPolicy: Delete
volumeBindingMode: WaitForFirstConsumer
allowVolumeExpansion: true
```

  4. Create a PVC provisioned by the storage class you just created, and include a request for storage, as follows: 
    1. Create a manifest for the PVC. 
For example, in a file called csi-bvs-pvc-uhp.yaml:
```
apiVersion: v1
kind: PersistentVolumeClaim
metadata:
 name: uhp-claim
spec:
 storageClassName: "oci-uhp-sc"
 accessModes:
  - ReadWriteOnce
 resources:
  requests:
   storage: 50Gi
```

    2. Create the PVC from the manifest file.
For example, by entering:
```
kubectl apply -f csi-bvs-pvc-uhp.yaml
```



Having created the PVC, you can use it when creating other objects, such as pods. For example, you could create a new pod from the following pod definition:
```
apiVersion: v1
kind: Pod
metadata:
 name: pod-uhp
 labels:
  uhp-pod: "true"
spec:
 affinity:
  podAntiAffinity:
   requiredDuringSchedulingIgnoredDuringExecution:
   - labelSelector:
     matchExpressions:
     - key: uhp-pod
      operator: In
      values:
      - "true"
    topologyKey: kubernetes.io/hostname
 containers:
  - name: app
   image: iad.ocir.io/odx-oke/oke-public/busybox:latest
   command: ["/bin/sh"]
   args: ["-c", "while true; do echo $(date -u) >> /data/out.txt; sleep 5; done"]
   volumeMounts:
    - name: persistent-storage
     mountPath: /data
 volumes:
  - name: persistent-storage
   persistentVolumeClaim:
    claimName: uhp-claim
 nodeSelector:
  uhp: supported
```

In this example, you have specified:
  * A label for the pod to indicate that it uses an **Ultra High Performance** block volume. In this example, `uhp-pod: "true"`
  * An anti-affinity rule that uses the pod label to ensure only one pod using the **Ultra High Performance** block volume runs on any one worker node.
  * A node selector, so that the pod only runs on worker nodes with a particular label (derived from the node pool label). In this example, `uhp: supported`
  * A PVC backed by an **Ultra High Performance** block volume. In this example, `claimName: uhp-claim`


When you create a pod based on the definition, the pod runs on a worker node hosted on an instance that has a shape suitable for the **Ultra High Performance** performance level. A new block volume is created in the Block Volume service to back the PVC. The new block volume has the **Ultra High Performance** performance level you specified in the storage class definition. 
## Specifying File System Types for Block Volumes 🔗 
Block volumes in the Block Volume service can be configured for different types of file system. The most appropriate file system to use depends on (among other things) the expected file size, and the number of files to be processed. A number of file system types are available, including:
  * **ext3:** The ext3 file system type includes journaling capabilities to improve reliability and availability. Consistency checks after a power failure or an uncontrolled system shutdown are unnecessary.
  * **ext4:** In addition to ext3 features, the ext4 file system type supports extents (contiguous physical blocks), pre-allocation, delayed allocation, faster file system checking, more robust journaling, and other enhancements.
  * **XFS:** The XFS file system is a high-performance journaling file system type, which provides high scalability for I/O threads, file system bandwidth, file and file system size, even when the file system spans many storage devices.


The ext3 and ext4 file systems are generally considered better-suited for applications that use a single read/write thread and small files. Whereas, the XFS file system is generally considered better-suited for applications that have multiple read/write threads and larger files.
When a PVC is created using the CSI volume plugin (`provisioner: blockvolume.csi.oraclecloud.com`), you can specify a file system type for the block volume that is appropriate for the expected workload.
**Note** Block volumes are configured with an ext4 file system by default. If an ext4 file system is appropriate for the expected workload, you do not have to explicitly specify the file system type in the storage class definition as described in the rest of this topic.
By default, block volumes are configured with an ext4 file system. If the ext4 file system is not the most appropriate file system for the expected workload, you can specify an alternative file system type in the storage class definition.
To create a PVC backed by a block volume with an ext3 or XFS file system, set the `fstype` parameter in the custom storage class definition as follows:
  * for **ext3** , set `csi.storage.k8s.io/fstype: ext3`
  * for **XFS** , set `csi.storage.k8s.io/fstype: xfs`


For example, to create a PVC backed by a block volume with an ext3 file system:
```
apiVersion: storage.k8s.io/v1
kind: StorageClass
metadata:
 name: oci-bv-ext3
provisioner: blockvolume.csi.oraclecloud.com
parameters:
 csi.storage.k8s.io/fstype: ext3
reclaimPolicy: Retain
allowVolumeExpansion: true
volumeBindingMode: WaitForConsumer
```

Create a manifest for a PVC provisioned by the `oci-bv-ext3` storage class and include a request for storage. For example, in a file called csi-bvs-pvc-fstype.yaml:
```
apiVersion: v1
kind: PersistentVolumeClaim
metadata:
 name: oci-bv-claim-ext3
spec:
 storageClassName: oci-bv-ext3
 accessModes:
  - ReadWriteOnce
 resources:
  requests:
   storage: 50Gi
```

Enter the following command to create the PVC from the csi-bvs-pvc-fstype.yaml file:
```
kubectl apply -f csi-bvs-pvc-fstype.yaml
```

Having created the PVC, you can use it when creating other objects, such as pods. For example, you could create a new pod from the following pod definition, which instructs the system to use the oci-bv-claim-ext3 PVC as the nginx volume, which is mounted by the pod at /data.
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
    claimName: oci-bv-claim-ext3
```

Having created the new pod, you can verify that the PVC has been bound to a new persistent volume by entering:
Command
CopyTry It
```
kubectl get pvc
```

The output from the above command confirms that the PVC has been bound:
Copy
```
			
NAME          STATUS  VOLUME                CAPACITY  ACCESSMODES  STORAGECLASS    AGE
oci-bv-claim-ext3    Bound   ocid1.volume.oc1.iad.<unique_ID>   50Gi    RWO      oci-bv-ext3     4m
```

You can verify that the pod is using the new persistent volume claim by entering:
Command
CopyTry It
```
kubectl describe pod nginx
```

Note that you cannot subsequently change the file system of a block volume backing a PVC. Instead, you have to define a new storage class, set the file system as required, and create a new PVC provisioned by that new storage class.
## Specifying Raw Block Volumes 🔗 
When using the CSI volume plugin ( `provisioner: blockvolume.csi.oraclecloud.com` ) to connect clusters to block volumes in the Block Volume service, you can bind a PVC to a PV that is provisioned by a block volume configured as a raw block volume. When a block volume has been configured as a raw block volume, rather than as a mounted file system, a PV provisioned by that block volume appears as a block device to the containers running on a cluster. As a result, applications running inside the container can access the attached block volume as a block device, without the performance overhead caused by accessing the device through a file system. That overhead can be particularly significant for performance-sensitive applications (such as databases) that benefit from direct block device access. 
To configure the block volume backing a PVC as a raw block volume, specify ` volumeMode: Block` in the PVC manifest. Note that if not specified, `volumeMode: Filesystem` is assumed, and block volumes are configured with an ext4 file system by default. 
For example, create a manifest for a PVC provisioned by the `oci-bv` storage class, include a request for storage, and specify ` volumeMode: Block` in the manifest. For example, in a file called csi-bvs-pvc-raw.yaml:
Copy
```
apiVersion: v1
kind: PersistentVolumeClaim
metadata:
 name: pvc-raw-block-volume
spec:
 accessModes:
  - ReadWriteOnce
 resources:
  requests:
   storage: 50Gi
 storageClassName: oci-bv
 volumeMode: Block
```

Enter the following command to create the PVC from the csi-bvs-pvc-raw.yaml file:
```
kubectl apply -f csi-bvs-pvc-raw.yaml
```

Having created the PVC, you can use it when creating other objects, such as pods. For example, you could create a new pod from the following pod definition, which instructs the system to use the pvc-raw-block-volume PVC as the storage volume for the raw-volume-test container, which the container can access at /dev/block:
Copy
```
apiVersion: v1
kind: Pod
metadata:
 name: raw-volume-test-pod
spec:
 containers:
 - name: raw-volume-test
  image: centos
  command: ["/bin/sh"]
  volumeDevices:
  - name: raw-volume
   devicePath: /dev/block
 volumes:
 - name: raw-volume
  persistentVolumeClaim:
   claimName: pvc-raw-block-volume

```

Having created the new pod, you can verify that the PVC has been bound to a new persistent volume by entering:
Command
CopyTry It
```
kubectl get pvc
```

The output from the above command confirms that the PVC has been bound:
Copy
```
			
NAME          STATUS  VOLUME                CAPACITY  ACCESSMODES  STORAGECLASS    AGE
pvc-raw-block-volume  Bound   ocid1.volume.oc1.iad.<unique_ID>   50Gi    RWO      oci-bv       4m
```

You can verify that the pod is using the new persistent volume claim by entering:
Command
CopyTry It
```
kubectl describe pod raw-volume-test-pod
```

Note that you cannot subsequently change whether the block volume backing a PVC is configured as a raw block volume, or as a mounted file system. Instead, you have to create a new PVC and set `volumeMode:` appropriately in the PVC manifest.
Note also that raw block volumes are not supported for Ultra High Performance block volumes.
Was this article helpful?
YesNo

