Updated 2024-12-11
# Migrating from the FlexVolume Volume Plugin to the CSI Volume Plugin
_Find out how to migrate a Kubernetes workload (managed by a StatefulSet) from the FlexVolume volume plugin to the CSI volume plugin._
You can use either the CSI volume plugin or the FlexVolume volume plugin to connect clusters to block volumes from the Block Volume service. However, Oracle recommends using the CSI volume plugin because:
  * The upstream Kubernetes project deprecates the FlexVolume volume plugin in Kubernetes version 1.23.
  * New functionality is only being added to the CSI volume plugin, not to the FlexVolume volume plugin.
  * The CSI volume plugin does not require access to underlying operating system and root file system dependencies.


In Kubernetes, one way to manage stateful applications that require persistent storage is to use StatefulSet objects. For more information about StatefulSet objects, see [StatefulSets](https://kubernetes.io/docs/concepts/workloads/controllers/statefulset/) in the Kubernetes documentation.
If you have a stateful application that requires persistent storage, and the StatefulSet that manages the application is currently using the FlexVolume volume plugin to provision a persistent volume, we recommend that you migrate the workload to use the CSI volume plugin instead. 
This section provides generic steps to migrate a workload (managed by a StatefulSet) from the FlexVolume volume plugin to the CSI volume plugin, as follows:
  * [Step 1: Change the reclaim policy of existing FlexVolume PV objects to "Retain"](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengcreatingpersistentvolumeclaim_topic-Provisioning_PVCs_on_BV-PV_Migrating-from-FlexVolume.htm#contengcreatingpersistentvolumeclaim_topic_Provisioning_PVCs_on_BV_PV_Migrating_from_FlexVolume__change-reclaim-policy-to-retain)
  * [Step 2: Create new CSI PV objects and bind them to block volumes](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengcreatingpersistentvolumeclaim_topic-Provisioning_PVCs_on_BV-PV_Migrating-from-FlexVolume.htm#contengcreatingpersistentvolumeclaim_topic_Provisioning_PVCs_on_BV_PV_Migrating_from_FlexVolume__create-new-pv)
  * [Step 3: Create new CSI PVC objects and bind them to the CSI PV objects](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengcreatingpersistentvolumeclaim_topic-Provisioning_PVCs_on_BV-PV_Migrating-from-FlexVolume.htm#contengcreatingpersistentvolumeclaim_topic_Provisioning_PVCs_on_BV_PV_Migrating_from_FlexVolume__create-new-pvc)
  * [Step 4: Recreate the StatefulSet object to use the new CSI PVC objects](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengcreatingpersistentvolumeclaim_topic-Provisioning_PVCs_on_BV-PV_Migrating-from-FlexVolume.htm#contengcreatingpersistentvolumeclaim_topic_Provisioning_PVCs_on_BV_PV_Migrating_from_FlexVolume__recreate-statefulset)
  * [Step 5: Delete the original FlexVolume PVC and PV objects](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengcreatingpersistentvolumeclaim_topic-Provisioning_PVCs_on_BV-PV_Migrating-from-FlexVolume.htm#contengcreatingpersistentvolumeclaim_topic_Provisioning_PVCs_on_BV_PV_Migrating_from_FlexVolume__delete-old-pvc-pv)


This section also includes a fully worked example, so you can see the steps in practice. See [Example of migrating a workload from the FlexVolume volume plugin to the CSI volume plugin](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengcreatingpersistentvolumeclaim_topic-Provisioning_PVCs_on_BV-PV_Migrating-from-FlexVolume.htm#contengcreatingpersistentvolumeclaim_topic_Provisioning_PVCs_on_BV_PV_Migrating_from_FlexVolume_Example).
Note that in this section:
  * Persistent volumes and persistent volume claims created by the FlexVolume volume plugin are referred to as FlexVolume PVs and FlexVolume PVCs respectively.
  * Persistent volumes and persistent volume claims created by the CSI volume plugin are referred to as CSI PVs and CSI PVCs respectively.


## Step 1: Change the reclaim policy of existing FlexVolume PV objects to "Retain" 🔗 
  1. Find out the names of the FlexVolume PVs that are bound to the FlexVolume PVCs in the StatefulSet by entering:
Copy
```
kubectl get pvc
```

  2. Change the reclaim policy of the existing FlexVolume PV objects to `Retain` to prevent the block volumes backing the PVs from being deleted during the migration, by entering:
Copy
```
kubectl patch pv <volume-name> -p '{"spec":{"persistentVolumeReclaimPolicy":"Retain"}}'
```

  3. Confirm that each FlexVolume PV has been updated, by entering:
Copy
```
kubectl get pv <volume-name>
```

  4. Verify that the output shows that the reclaim policy has been set to Retain for each FlexVolume PV.
**Important** Double-check that the reclaim policy has been set to Retain for each FlexVolume PV. If the reclaim policy is not set to Retain, the block volume backing the FlexVolume PV will be deleted during the migration.


## Step 2: Create new CSI PV objects and bind them to block volumes 🔗 
  1. Create a new PV manifest file.
  2. For each existing FlexVolume PV object, copy the following template PV definition into the file to define a corresponding new CSI PV object:
Copy
```
kind: PersistentVolume
apiVersion: v1
metadata:
 name: <new-pv-name>
 annotations:
  pv.kubernetes.io/provisioned-by: blockvolume.csi.oraclecloud.com
spec:
 storageClassName: oci-bv
 persistentVolumeReclaimPolicy: Retain
 capacity:
  storage: <original-pv-storage>
 accessModes:
  - ReadWriteOnce
 csi:
  driver: blockvolume.csi.oraclecloud.com
  fsType: <original-pv-fs-type>
  volumeHandle: <original-pv-volume-ocid>
 nodeAffinity:
  required:
   nodeSelectorTerms:
   - matchExpressions:
    - key: topology.kubernetes.io/zone
     operator: In
     values:
     - <original-pv-ad-location>
```

  3. For each new CSI PV object definition, provide values as follows:
     * Set `metadata.name` to a string of your choice for the name of the new CSI PV object. 
     * Set `spec.capacity.storage` to the existing FlexVolume PV's capacity. For example, `50Gi`
     * Set `spec.csi.fstype` to the type of file system backing the existing FlexVolume PV. For example, `ext4` . 
**Tip:** If you are not sure of the type of file system backing the existing FlexVolume PV, see details of the FlexVolume PV by entering:
Copy
```
kubectl get pv <original-pv-name> -o yaml
```

     * Set `spec.csi.volumeHandle` to the OCID of the original block volume backing the existing FlexVolume PV. The OCID was also used as the name of the FlexVolume PV. For example, `ocid1.volume.oc1.phx.aaaaaa______xbd`
     * Set `spec.nodeAffinity.required.nodeSelectorTerms.matchExpressions.key: topology.kubernetes.io/zone.values` to the availability domain for the CSI PV, based on the value of the Flex PV's `failure-domain.beta.kubernetes.io/zone` . For example, `PHX-AD-1`. 
**Tip:** If you are not sure of the value of the existing Flex PV's `failure-domain.beta.kubernetes.io/zone`, see details of the FlexVolume PV by entering:
Copy
```
kubectl get pv <original-pv-name> -o yaml
```

Notice that in the template, `spec.storageClassName` is already set to the storage class used by the CSI volume plugin (`oci-bv`).
For example:
```
kind: PersistentVolume
apiVersion: v1
metadata:
 name: csi-pv-web-app-0
 annotations:
  pv.kubernetes.io/provisioned-by: blockvolume.csi.oraclecloud.com
spec:
 storageClassName: oci-bv
 persistentVolumeReclaimPolicy: Retain
 capacity:
  storage: 50Gi
 accessModes:
  - ReadWriteOnce
 csi:
  driver: blockvolume.csi.oraclecloud.com
  fsType: ext4
  volumeHandle: ocid1.volume.oc1.phx.aaaaaa______xbd
 nodeAffinity:
  required:
   nodeSelectorTerms:
   - matchExpressions:
    - key: topology.kubernetes.io/zone
     operator: In
     values:
     - PHX-AD-1
```

  4. Create the new CSI PV objects by entering:
Copy
```
kubectl apply -f <pv-manifest-filename>.yaml
```

  5. Confirm that the new CSI PV objects have been created by entering:
Copy
```
kubectl get pv
```

  6. Verify that the output shows:
     * A new CSI PV object for each FlexVolume PV object.
     * All of the new CSI PV objects have a status of `Available`.


## Step 3: Create new CSI PVC objects and bind them to the CSI PV objects 🔗 
You now define a new CSI PVC object for each CSI PV object you created in the previous step:
  1. Create a new PVC manifest file.
  2. For each existing FlexVolume PVC object, copy the following template PVC definition into the new file to define a new CSI PVC object:
Copy
```
apiVersion: v1
kind: PersistentVolumeClaim
metadata:
 name: <new-pvc-name>
spec:
 accessModes:
  - ReadWriteOnce
 resources:
  requests:
   storage: <original-pvc-size>
 volumeName: <new-pv-name>
 storageClassName: oci-bv
```

  3. For each new CSI PVC object definition, provide values as follows:
     * Set `metadata.name` to specify the name for the new CSI PVC in the following format:```
<new-volumeClaimTemplates.metadata.name>-<statefulset-name>-<index>
```

where:
       * `<new-volumeClaimTemplates.metadata.name>` is a string of your choice to be the first part of the name for the new CSI PVC. The string you specify here must be different to the original `volumeClaimTemplates.metadata.name` value in the StatefulSet manifest. In [Step 4: Recreate the StatefulSet object to use the new CSI PVC objects](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengcreatingpersistentvolumeclaim_topic-Provisioning_PVCs_on_BV-PV_Migrating-from-FlexVolume.htm#contengcreatingpersistentvolumeclaim_topic_Provisioning_PVCs_on_BV_PV_Migrating_from_FlexVolume__recreate-statefulset), you update the StatefulSet manifest and specify this string as the value of `volumeClaimTemplates.metadata.name`.
       * `<statefulset-name>` is the name of the StatefulSet that manages the application.
       * `<index>` is an ordinal number, starting at 0, and incremented by 1 for the number of replicas specified in the StatefulSet.
     * Set `spec.resources.requests.storage` to the same value as specified for the FlexVolume PVC. For example, `50Gi`
     * Set `spec.volumeName` to the name that you specified as the name of the new CSI PV object in [Step 2: Create new CSI PV objects and bind them to block volumes](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengcreatingpersistentvolumeclaim_topic-Provisioning_PVCs_on_BV-PV_Migrating-from-FlexVolume.htm#contengcreatingpersistentvolumeclaim_topic_Provisioning_PVCs_on_BV_PV_Migrating_from_FlexVolume__create-new-pv).
Notice that in the template, `spec.storageClassName` is already set to the storage class used by the CSI volume plugin (`oci-bv`).
For example:
```
apiVersion: v1
kind: PersistentVolumeClaim
metadata:
 name: storage-csi-web-app-0
spec:
 accessModes:
  - ReadWriteOnce
 resources:
  requests:
   storage: 50Gi
 volumeName: csi-pv-web-app-0
 storageClassName: oci-bv
```

  4. Create the new CSI PVC objects by entering:
Copy
```
kubectl apply -f <pvc-manifest-filename>.yaml
```

  5. Confirm that the new CSI PVC objects have been created and bound to the CSI PV objects by entering:
Copy
```
kubectl get pvc
```

  6. Verify that the output shows:
     * A CSI PVC object has been created for each FlexVolume PVC object.
     * All of the CSI PVC objects have a status of `Bound`.
     * Each CSI PVC object is bound to the CSI PV object specified in the manifest.


## Step 4: Recreate the StatefulSet object to use the new CSI PVC objects 🔗 
  1. Create a new StatefulSet manifest by copying the file containing the manifest of the existing StatefulSet, and save the new manifest file with a new name.
  2. Update the new manifest, so that the StatefulSet uses the new CSI PVCs you created in [Step 3: Create new CSI PVC objects and bind them to the CSI PV objects](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengcreatingpersistentvolumeclaim_topic-Provisioning_PVCs_on_BV-PV_Migrating-from-FlexVolume.htm#contengcreatingpersistentvolumeclaim_topic_Provisioning_PVCs_on_BV_PV_Migrating_from_FlexVolume__create-new-pvc), as follows:
     * Change `spec.template.spec.containers.volumeMounts.name` to the string you chose as the first part of the new CSI PVC names.
     * Change `spec.volumeClaimTemplates.metadata.name` to the string you chose as the first part of the new CSI PVC names.
     * Change `spec.volumeClaimTemplates.spec.storageClassName` to `oci-bv` (the storage class used by the CSI volume plugin).
  3. Delete the existing StatefulSet object by entering:
Copy
```
kubectl delete statefulsets <statefulset-name>
```

  4. Create a new StatefulSet object from the new manifest by entering:
Copy
```
kubectl apply -f <statefulset-manifest-filename>
```



## Step 5: Delete the original FlexVolume PVC and PV objects 🔗 
Having changed the FlexVolume PV's persistentVolumeReclaimPolicy to Retain in [Step 1: Change the reclaim policy of existing FlexVolume PV objects to "Retain"](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengcreatingpersistentvolumeclaim_topic-Provisioning_PVCs_on_BV-PV_Migrating-from-FlexVolume.htm#contengcreatingpersistentvolumeclaim_topic_Provisioning_PVCs_on_BV_PV_Migrating_from_FlexVolume__change-reclaim-policy-to-retain), and completed the other steps in this section, you can now delete the original FlexVolume PV and PVC objects.
  1. For each FlexVolume PV object, delete the PV object by entering:
Copy
```
kubectl delete pv <flexvolume-pv-name>
```

  2. For each FlexVolume PVC object, delete the PVC object by entering:
Copy
```
kubectl delete pvc <flexvolume-pvc-name>
```



## Example of migrating a workload from the FlexVolume volume plugin to the CSI volume plugin 🔗 
This example shows how to migrate a sample workload from the FlexVolume volume plugin to the CSI volume plugin. The instructions in this example assume a workload that is managed by a StatefulSet object named `web-app`.
### Example StatefulSet Workload
Initially, the StatefulSet uses the FlexVolume volume plugin to provision storage. The original StatefulSet is defined in flex-statefulset.yaml as follows:
```
apiVersion: apps/v1
kind: StatefulSet
metadata:
 name: web-app
spec:
 serviceName: "nginx"
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
     image: nginx:latest
     ports:
      - containerPort: 80
       name: web
     volumeMounts:
      - name: storage-flex
       mountPath: /usr/share/nginx/html
 volumeClaimTemplates:
 - apiVersion: v1
  kind: PersistentVolumeClaim
  metadata:
   creationTimestamp: null
   name: storage-flex
  spec:
   accessModes:
   - ReadWriteOnce
   resources:
    requests:
     storage: 50Gi
   storageClassName: oci
   volumeMode: Filesystem
```

The original StatefulSet manifest defines:
  * The name of the StatefulSet as `web-app` (the value of `metadata.name`).
  * The name of a volumeClaimTemplate as `storage-flex` (the value of `volumeClaimTemplates.metadata.name`).
  * Three replicas (the value of `spec.replicas`).


When creating PVCs for a StatefulSet, Kubernetes uses the following convention to name the PVCs:
```
<volumeClaimTemplate-name>-<StatefulSet-name>-<index>
```

where:
  * `<volumeClaimTemplate-name>` is the name of the volumeClaimTemplate specified by the value of `volumeClaimTemplates.metadata.name` in the StatefulSet manifest. In this example, `storage-flex`.
  * `<StatefulSet-name>` is the name of the StatefulSet specified by the value of `metadata.name` in the StatefulSet manifest. In this example, `web-app`.
  * `<index>` is an ordinal number, starting at 0, and incremented by 1 for the number of replicas specified in the StatefulSet. In this example, three replicas are specified.


So when Kubernetes created the original FlexVolume PVCs for the `web-app` StatefulSet, it created three PVCs with the following names:
  * `storage-flex-web-app-0`
  * `storage-flex-web-app-1`
  * `storage-flex-web-app-2`


### Example Step 1: Change the reclaim policy of existing FlexVolume PV objects to "Retain" 🔗 
  1. You find out the names of the three FlexVolume PVs that are bound to the three FlexVolume PVCs in the StatefulSet by entering:
```
kubectl get pvc
NAME           STATUS  VOLUME                 CAPACITY  ACCESS MODES  STORAGECLASS  VOLUMEATTRIBUTESCLASS  AGE
storage-flex-web-app-0  Bound  ocid1.volume.oc1.phx.aaaaaa______xbd  50Gi    RWO      oci      <unset>         9m28s       
storage-flex-web-app-1  Bound  ocid1.volume.oc1.phx.aaaaaa______xbe  50Gi    RWO      oci      <unset>         2m59s       
storage-flex-web-app-2  Bound  ocid1.volume.oc1.phx.aaaaaa______xbf  50Gi    RWO      oci      <unset>         2m3s       
```

  2. You change the reclaim policy of the existing three FlexVolume PV objects to `Retain` to prevent the block volumes backing the PVs from being deleted during the migration, by entering:
```
kubectl patch pv <volume-name> -p '{"spec":{"persistentVolumeReclaimPolicy":"Retain"}}'
```

In this example:
```
kubectl patch pv ocid1.volume.oc1.phx.aaaaaa______xbd -p '{"spec":{"persistentVolumeReclaimPolicy":"Retain"}}'
persistentvolume/ocid1.volume.oc1.phx.aaaaaa______xbd patched
```
```
kubectl patch pv ocid1.volume.oc1.phx.aaaaaa______xbe -p '{"spec":{"persistentVolumeReclaimPolicy":"Retain"}}'
persistentvolume/ocid1.volume.oc1.phx.aaaaaa______xbe patched
```
```
kubectl patch pv ocid1.volume.oc1.phx.aaaaaa______xbf -p '{"spec":{"persistentVolumeReclaimPolicy":"Retain"}}'
persistentvolume/ocid1.volume.oc1.phx.aaaaaa______xbf patched
```

  3. Confirm that each FlexVolume PV has been updated, by entering:
```
kubectl get pv
NAME                  CAPACITY  ACCESS MODES  RECLAIM POLICY  STATUS    CLAIM              STORAGECLASS  VOLUMEATTRIBUTESCLASS  REASON  AGE
ocid1.volume.oc1.phx.aaaaaa______xbd  50Gi    RWO      Retain      Bound     default/storage-flex-web-app-0  oci      <unset>             13m
ocid1.volume.oc1.phx.aaaaaa______xbe  50Gi    RWO      Retain      Bound     default/storage-flex-web-app-2  oci      <unset>             6m8s
ocid1.volume.oc1.phx.aaaaaa______xbf  50Gi    RWO      Retain      Bound     default/storage-flex-web-app-1  oci      <unset>             7m8s
```

  4. Verify that the output shows that reclaim policy has been set to Retain for each FlexVolume PV.
**Important** Double-check that the reclaim policy has been set to Retain for each FlexVolume PV. If the reclaim policy is not set to Retain, the block volume backing the FlexVolume PV will be deleted during the migration.


### Example Step 2: Create new CSI PV objects and bind them to block volumes 🔗 
  1. You create a new PV manifest file and save it as migrated-csi-pv.yaml. 
  2. For each of the three existing FlexVolume PV objects, you copy the following template PV definition into the migrated-csi-pv.yaml file to define a corresponding new CSI PV object. 
Copy
```
kind: PersistentVolume
apiVersion: v1
metadata:
 name: <new-pv-name>
 annotations:
  pv.kubernetes.io/provisioned-by: blockvolume.csi.oraclecloud.com
spec:
 storageClassName: oci-bv
 persistentVolumeReclaimPolicy: Retain
 capacity:
  storage: <original-pv-storage>
 accessModes:
  - ReadWriteOnce
 csi:
  driver: blockvolume.csi.oraclecloud.com
  fsType: <original-pv-fs-type>
  volumeHandle: <original-pv-volume-ocid>
 nodeAffinity:
  required:
   nodeSelectorTerms:
   - matchExpressions:
    - key: topology.kubernetes.io/zone
     operator: In
     values:
     - <original-pv-ad-location>
```

  3. For each new CSI PV object definition, you provide values as follows:
     * Set `metadata.name` to a string of your choice for the name of the new CSI PV object. In this example, you name the new CSI PV objects `csi-pv-web-app-0`, `csi-pv-web-app-1`, and `csi-pv-web-app-2`. 
     * Set `spec.capacity.storage` to the existing FlexVolume PV's capacity. In this example, you specify `50Gi` for all three new CSI PV objects.
     * Set `spec.csi.fstype` to the type of file system backing the existing FlexVolume PV. In this example, you specify `ext4` for all three new CSI PV objects. 
     * Set `spec.csi.volumeHandle` to the OCID of the original block volume backing the existing FlexVolume PV. The OCID was also used as the name of the FlexVolume PV object. In this example, you specify the following OCIDs for the three new CSI PV objects:
       * `ocid1.volume.oc1.phx.aaaaaa______xbd`
       * `ocid1.volume.oc1.phx.aaaaaa______xbe`
       * `ocid1.volume.oc1.phx.aaaaaa______xbf`
     * Set `spec.nodeAffinity.required.nodeSelectorTerms.matchExpressions.key: topology.kubernetes.io/zone` to the availability domain for the CSI PV, based on the value of the Flex PV's `failure-domain.beta.kubernetes.io/zone` . In this example, you specify the following availability domains for the three new CSI PV objects:
       * `PHX-AD-1`
       * `PHX-AD-2`
       * `PHX-AD-3`
Having entered the information, the migrated-csi-pv.yaml file contains the following three CSI PV definitions:
```
kind: PersistentVolume
apiVersion: v1
metadata:
 name: csi-pv-web-app-0
 annotations:
  pv.kubernetes.io/provisioned-by: blockvolume.csi.oraclecloud.com
spec:
 storageClassName: oci-bv
 persistentVolumeReclaimPolicy: Retain
 capacity:
  storage: 50Gi
 accessModes:
  - ReadWriteOnce
 csi:
  driver: blockvolume.csi.oraclecloud.com
  fsType: ext4
  volumeHandle: ocid1.volume.oc1.phx.aaaaaa______xbd
 nodeAffinity:
  required:
   nodeSelectorTerms:
   - matchExpressions:
    - key: topology.kubernetes.io/zone
     operator: In
     values:
     - PHX-AD-3
---
kind: PersistentVolume
apiVersion: v1
metadata:
 name: csi-pv-web-app-1
 annotations:
  pv.kubernetes.io/provisioned-by: blockvolume.csi.oraclecloud.com
spec:
 storageClassName: oci-bv
 persistentVolumeReclaimPolicy: Retain
 capacity:
  storage: 50Gi
 accessModes:
  - ReadWriteOnce
 csi:
  driver: blockvolume.csi.oraclecloud.com
  fsType: ext4
  volumeHandle: ocid1.volume.oc1.phx.aaaaaa______xbe
 nodeAffinity:
  required:
   nodeSelectorTerms:
   - matchExpressions:
    - key: topology.kubernetes.io/zone
     operator: In
     values:
     - PHX-AD-2
---
kind: PersistentVolume
apiVersion: v1
metadata:
 name: csi-pv-web-app-2
 annotations:
  pv.kubernetes.io/provisioned-by: blockvolume.csi.oraclecloud.com
spec:
 storageClassName: oci-bv
 persistentVolumeReclaimPolicy: Retain
 capacity:
  storage: 50Gi
 accessModes:
  - ReadWriteOnce
 csi:
  driver: blockvolume.csi.oraclecloud.com
  fsType: ext4
  volumeHandle: ocid1.volume.oc1.phx.aaaaaa______xbf
 nodeAffinity:
  required:
   nodeSelectorTerms:
   - matchExpressions:
    - key: topology.kubernetes.io/zone
     operator: In
     values:
     - PHX-AD-1
```

  4. You create the three new CSI PV objects by entering:
```
kubectl apply -f migrated-csi-pv.yaml
persistentvolume/csi-pv-web-app-0 created
persistentvolume/csi-pv-web-app-1 created
persistentvolume/csi-pv-web-app-2 created
```

  5. You confirm that the three new CSI PV objects have been created by entering:
```
kubectl get pv
NAME                  CAPACITY  ACCESS MODES  RECLAIM POLICY  STATUS    CLAIM              STORAGECLASS  VOLUMEATTRIBUTESCLASS  REASON  AGE
csi-pv-web-app-0            50Gi    RWO      Retain      Available                   oci-bv     <unset>             11s
csi-pv-web-app-1            50Gi    RWO      Retain      Available                   oci-bv     <unset>             11s
csi-pv-web-app-2            50Gi    RWO      Retain      Available                   oci-bv     <unset>             10s
ocid1.volume.oc1.phx.aaaaaa______xbd  50Gi    RWO      Retain      Bound     default/storage-flex-web-app-0  oci      <unset>             23m
ocid1.volume.oc1.phx.aaaaaa______xbe  50Gi    RWO      Retain      Bound     default/storage-flex-web-app-2  oci      <unset>             16m
ocid1.volume.oc1.phx.aaaaaa______xbf  50Gi    RWO      Retain      Bound     default/storage-flex-web-app-1  oci      <unset>             17m
```

  6. You verify that the output shows:
     * A new CSI PV object for each of the original FlexVolume PV objects.
     * All three of the new CSI PV objects have a status of `Available`.


### Example Step 3: Create new CSI PVC objects and bind them to the CSI PV objects 🔗 
You now define a new CSI PVC object for each CSI PV object you created in the previous step:
  1. You create a new PVC manifest file and save it as migrated-csi-pvc.yaml. 
  2. For each of the three existing FlexVolume PVC objects, you copy the following template PVC definition into the migrated-csi-pvc.yaml file to define a new CSI PVC object. 
Copy
```
apiVersion: v1
kind: PersistentVolumeClaim
metadata:
 name: <new-pvc-name>
spec:
 accessModes:
  - ReadWriteOnce
 resources:
  requests:
   storage: <original-pvc-size>
 volumeName: <new-pv-name>
 storageClassName: oci-bv
```

  3. For each new CSI PVC object definition, you provide values as follows:
     * You set `metadata.name` to specify the name for the new CSI PVC in the following format:
```
<new-volumeClaimTemplates.metadata.name>-<statefulset-name>-<index>
```

where:
       * `<new-volumeClaimTemplates.metadata.name>` is a string of your choice to be the first part of the name for the new CSI PVC. The string you specify here must be different to the original `volumeClaimTemplates.metadata.name` value in the StatefulSet manifest. In [Example Step 4: Recreate the StatefulSet object to use the new CSI PVC objects](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengcreatingpersistentvolumeclaim_topic-Provisioning_PVCs_on_BV-PV_Migrating-from-FlexVolume.htm#contengcreatingpersistentvolumeclaim_topic_Provisioning_PVCs_on_BV_PV_Migrating_from_FlexVolume_Example__example-recreate-statefulset), you update the StatefulSet manifest and specify this string as the new value of `volumeClaimTemplates.metadata.name`. In this example, you specify `storage-csi`.
       * `<statefulset-name>` is `web-app` (the name of the StatefulSet that manages the example application).
       * `<index>` is an ordinal number, starting at 0, and incremented by 1 for the number of replicas specified in the StatefulSet. In this example, the `web-app` StatefulSet specifies three replicas.
     * You set `spec.resources.requests.storage` to the same value as specified for the FlexVolume PVC. In this example, you specify `50Gi`
     * You set `spec.volumeName` to one of the names (`csi-pv-web-app-0`, `csi-pv-web-app-1`, or `csi-pv-web-app-2`) that you specified for the new CSI PV objects in [Example Step 2: Create new CSI PV objects and bind them to block volumes](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengcreatingpersistentvolumeclaim_topic-Provisioning_PVCs_on_BV-PV_Migrating-from-FlexVolume.htm#contengcreatingpersistentvolumeclaim_topic_Provisioning_PVCs_on_BV_PV_Migrating_from_FlexVolume_Example__example-create-new-pv).
Having entered the information, the migrated-csi-pvc.yaml file contains the following three CSI PVC definitions:
```
apiVersion: v1
kind: PersistentVolumeClaim
metadata:
 name: storage-csi-web-app-0
spec:
 accessModes:
  - ReadWriteOnce
 resources:
  requests:
   storage: 50Gi
 volumeName: csi-pv-web-app-0
 storageClassName: oci-bv
---
apiVersion: v1
kind: PersistentVolumeClaim
metadata:
 name: storage-csi-web-app-1
spec:
 accessModes:
  - ReadWriteOnce
 resources:
  requests:
   storage: 50Gi
 volumeName: csi-pv-web-app-1
 storageClassName: oci-bv
---
apiVersion: v1
kind: PersistentVolumeClaim
metadata:
 name: storage-csi-web-app-2
spec:
 accessModes:
  - ReadWriteOnce
 resources:
  requests:
   storage: 50Gi
 volumeName: csi-pv-web-app-2
 storageClassName: oci-bv
```

  4. You create the new CSI PVC objects by entering:
```
kubectl apply -f migrated-csi-pvc.yaml
persistentvolumeclaim/storage-csi-web-app-0 created
persistentvolumeclaim/storage-csi-web-app-1 created
persistentvolumeclaim/storage-csi-web-app-2 created
```

  5. You confirm that the new CSI PVC objects have been created and bound to the CSI PV objects by entering:
```
kubectl get pvc
NAME           STATUS  VOLUME                 CAPACITY  ACCESS MODES  STORAGECLASS  VOLUMEATTRIBUTESCLASS  AGE
storage-csi-web-app-0  Bound  csi-pv-web-app-0            50Gi    RWO      oci-bv     <unset>         2m32s
storage-csi-web-app-1  Bound  csi-pv-web-app-1            50Gi    RWO      oci-bv     <unset>         2m31s
storage-csi-web-app-2  Bound  csi-pv-web-app-2            50Gi    RWO      oci-bv     <unset>         2m31s
storage-flex-web-app-0  Bound  ocid1.volume.oc1.phx.aaaaaa______xbd  50Gi    RWO      oci      <unset>         38m
storage-flex-web-app-1  Bound  ocid1.volume.oc1.phx.aaaaaa______xbe  50Gi    RWO      oci      <unset>         31m
storage-flex-web-app-2  Bound  ocid1.volume.oc1.phx.aaaaaa______xbf  50Gi    RWO      oci      <unset>         30m
```

  6. You verify that the output shows:
     * A CSI PVC object has been created for each FlexVolume PVC object.
     * All three of the CSI PVC objects have a status of `Bound`.
     * Each CSI PVC object is bound to the CSI PV object specified in the manifest.


### Example Step 4: Recreate the StatefulSet object to use the new CSI PVC objects 🔗 
  1. You create a new StatefulSet manifest by copying the file containing the manifest of the existing StatefulSet (flex-statefulset.yaml), and saving the new manifest file as csi.statefulset.yaml.
  2. You update the new manifest in csi.statefulset.yaml, so that the StatefulSet uses the new CSI PVCs you created in [Example Step 3: Create new CSI PVC objects and bind them to the CSI PV objects](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengcreatingpersistentvolumeclaim_topic-Provisioning_PVCs_on_BV-PV_Migrating-from-FlexVolume.htm#contengcreatingpersistentvolumeclaim_topic_Provisioning_PVCs_on_BV_PV_Migrating_from_FlexVolume_Example__example-create-new-pvc), as follows:
     * You change `spec.template.spec.containers.volumeMounts.name` to `storage-csi` (the string you chose as the first part of the new CSI PVC names).
     * You change `spec.volumeClaimTemplates.metadata.name` to `storage-csi` (the string you chose as the first part of the new CSI PVC names).
     * You change `spec.volumeClaimTemplates.spec.storageClassName` to `oci-bv` (the storage class used by the CSI volume plugin).
The new StatefulSet manifest in csi.statefulset.yaml now looks as follows: 
```
apiVersion: apps/v1
kind: StatefulSet
metadata:
 name: web-app
spec:
 serviceName: "nginx"
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
     image: nginx:latest
     ports:
      - containerPort: 80
       name: web
     volumeMounts:
      - name: storage-csi
       mountPath: /usr/share/nginx/html
 volumeClaimTemplates:
 - apiVersion: v1
  kind: PersistentVolumeClaim
  metadata:
   creationTimestamp: null
   name: storage-csi
  spec:
   accessModes:
   - ReadWriteOnce
   resources:
    requests:
     storage: 50Gi
   storageClassName: oci-bv
   volumeMode: Filesystem
```

  3. Delete the existing `web-app` StatefulSet object by entering:
```
kubectl delete statefulsets web-app
statefulset.apps "web-app" deleted
```

  4. Create a new `web-app` StatefulSet object from the new manifest by entering:
```
kubectl apply -f csi.statefulset.yaml
```



### Example Step 5: Delete the original FlexVolume PVC and PV objects 🔗 
Having changed the FlexVolume PV's persistentVolumeReclaimPolicy to Retain in [Example Step 1: Change the reclaim policy of existing FlexVolume PV objects to "Retain"](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengcreatingpersistentvolumeclaim_topic-Provisioning_PVCs_on_BV-PV_Migrating-from-FlexVolume.htm#contengcreatingpersistentvolumeclaim_topic_Provisioning_PVCs_on_BV_PV_Migrating_from_FlexVolume_Example__example-change-reclaim-policy-to-retain), and completed the other steps in this section, you can now delete the original FlexVolume PV and PVC objects.
  1. For each FlexVolume PV object, you delete the PV object by entering:
```
kubectl delete pv <flexvolume-pv-name>
```

In this example:
```
kubectl delete pv ocid1.volume.oc1.phx.aaaaaa______xbd
persistentvolume ocid1.volume.oc1.phx.aaaaaa______xbd deleted
```
```
kubectl delete pv ocid1.volume.oc1.phx.aaaaaa______xbe
persistentvolume ocid1.volume.oc1.phx.aaaaaa______xbe deleted
```
```
kubectl delete pv ocid1.volume.oc1.phx.aaaaaa______xbf
persistentvolume ocid1.volume.oc1.phx.aaaaaa______xbf deleted
```

  2. For each FlexVolume PVC object, you delete the PVC object by entering:
```
kubectl delete pvc <flexvolume-pv-name>
```

In this example:
```
kubectl delete pvc storage-flex-web-app-0
persistentvolumeclaim storage-flex-web-app-0 deleted
```
```
kubectl delete pvc storage-flex-web-app-1
persistentvolumeclaim storage-flex-web-app-1 deleted
```
```
kubectl delete pvc storage-flex-web-app-2
persistentvolumeclaim storage-flex-web-app-2 deleted
```



Was this article helpful?
YesNo

