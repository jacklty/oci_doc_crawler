Updated 2024-08-14
# Applying Tags to Block Volumes
_Find out how to apply tags to block volume resources, and how to override initial block volume tags, when using Kubernetes Engine (OKE)._
When you create a cluster, you can optionally define tags to apply to block volumes created when persistent volume claims (PVCs) are defined. These tags are referred to as **initial block volume tags**. You can specify both defined tags and free-form tags as initial block volume tags.
You can override the initial block volume tags by defining a new Kubernetes storage class that includes tag parameters, and then using this storage class to create PVCs (see [Overriding Initial Block Volume Tags](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengtaggingclusterresources_tagging-oke-resources_block-volume-tags.htm#contengtaggingclusterresources_tagging_oke_resources_block_volume_tags__block-volume-tag-override-parameters)). If you use a storage class that includes tag parameters, none of the initial block volume tags specified in the cluster definition are applied to block volumes. Instead, the tags set in the storage class are applied to the block volume resources.
Tag defaults with default values that are specified for the compartment are automatically applied to the block volume resources as well. Note that Kubernetes Engine does not currently support tag defaults with user-applied values.
Note the following:
  * Tags are only applied to block volumes when the block volumes are first created. If you update the initial block volume tags applied to block volume resources, the changes only apply to new block volumes (assuming the tags are not overridden by parameters in the storage class definition). Tags applied to existing block volumes are unaffected.
  * If you apply a cost-tracking defined tag to block volumes, you can include block volume usage in budgets (see [Using Cost-Tracking Tags](https://docs.oracle.com/iaas/Content/Tagging/Tasks/usingcosttrackingtags.htm)).
  * To apply defined tags from a tag namespace belonging to one compartment to a block volume resource belonging to a different compartment, you must include a policy statement to allow the cluster to use the tag namespace. See [Additional IAM Policy when a Cluster and a Tag Namespace are in Different Compartments](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengtaggingclusterresources_iam-tag-namespace-policy.htm#contengtaggingclusterresources_iam-tag-namespace-policy "Find out about an additional IAM policy you have to create if you want to apply defined tags from a tag namespace belonging to one compartment to cluster-related resources belonging to a different compartment, when using Kubernetes Engine \(OKE\).").


## Using the Console to Specify Initial Block Volume Tags
To specify an initial block volume tag to apply to block volume resources created for a new cluster:
  1. Follow the instructions in [Using the Console to create a Cluster with Explicitly Defined Settings in the 'Custom Create' workflow](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengcreatingclusterusingoke_topic-Using_the_Console_to_create_a_Custom_Cluster_with_Explicitly_Defined_Settings.htm#create-custom-cluster "Find out how to use the 'Custom Create' workflow to create a Kubernetes cluster with explicitly defined settings and existing network resources using Kubernetes Engine \(OKE\).") to create a new cluster.
  2. Display the **Initial block volume tags** section of the **Create Cluster** page.
  3. To add a defined tag to block volume resources: 
     * **Tag Namespace:** Select the tag namespace to which the tag belongs.
     * **Tag Key:** Select the name of the defined tag to apply to block volume resources.
     * **Tag Value:** Either select the value for the tag from a pre-defined list of values, or enter a new value, or leave blank (depending on how the defined tag has been set up).
  4. To add a free-form tag to block volume resources: 
     * **Tag Namespace:** Set to None (free-form tags do not belong to a tag namespace).
     * **Tag Key:** Enter a name for the free-form tag to apply to block volume resources.
     * **Tag Value:** Enter a value for the tag to apply to block volume resources.


To update initial block volume tags to apply to new block volume resources created for a cluster::
  1. Follow the instructions in [Updating a Cluster](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/update-cluster.htm#update-cluster "Find out how to update a cluster using Kubernetes Engine \(OKE\).") to update an existing cluster.
  2. Display the **Initial Block Volume Tags** tab of the **Cluster Details** page.
  3. Click **Add Tags** to add, remove, and change the value of defined tags and free-form tags applied to new block volume resources.
Note that tags are only applied to block volume resources when the block volume resources are first created. So if you update initial block volume tags, the changes only apply to new block volume resources. Tags already applied to existing block volume resources are unaffected.


## Using the CLI to Specify Initial Block Volume Tags 🔗 
Command
CopyTry It
```
oci ce node-pool create \
--cluster-id <cluster-ocid> \
--compartment-id <compartment-ocid> \
--kubernetes-version <kubernetes-version> \
--name <node-pool-name> \
--node-shape <node-shape> \
--persistent-volume-defined-tags <json-name-value-pairs> \
--persistent-volume-freeform-tags <json-name-value-pairs>
```

For example:
Command
CopyTry It
```
oci ce node-pool create \
--cluster-id ocid1.cluster.oc1.iad.aaaaaaaaaf______jrd \
--compartment-id ocid1.compartment.oc1..aaaaaaaay______t6q \
--kubernetes-version v1.20.11 \
--name Finance-Node-Pool \
--node-shape VM.Standard2.1 \
--persistent-volume-defined-tags {"Operations": {"CostCenter": "42"}} \
--persistent-volume-freeform-tags {"Department": "Finance"}
```

## Using the API to Specify Initial Block Volume Tags
Use the `freeformTags` and `definedTags` attributes of the `PersistentVolumeConfigDetails` object used by the [CreateCluster](https://docs.oracle.com/iaas/api/#/en/containerengine/latest/Cluster/CreateCluster) and [Update Cluster](https://docs.oracle.com/iaas/api/#/en/containerengine/latest/Cluster/UpdateCluster) operations to add and update initial block volume tags.
## Overriding Initial Block Volume Tags 🔗 
You can override initial block volume tags applied to a block volume resource using parameters in a storage class manifest file as follows:
  * To override defined initial block volume tags, include the following parameter in the parameters section of the StorageClass definition:
Copy
```
oci.oraclecloud.com/initial-defined-tags-override: '{"<tag-namespace>": {"<tag-key>": "<tag-value>"}}'
```

  * To override free-form initial block volume tags, include the following parameter in the parameters section of the StorageClass definition:
Copy
```
oci.oraclecloud.com/initial-freeform-tags-override: '{"<tag-key>": "<tag-value>"}'
```



For example:
Copy
```
apiVersion: storage.k8s.io/v1
kind: StorageClass
metadata:
 name: oci-bv-specifictags
provisioner: blockvolume.csi.oraclecloud.com
parameters:
 attachment-type: "paravirtualized"
 oci.oraclecloud.com/initial-freeform-tags-override: '{"Department": "Finance"}'
 oci.oraclecloud.com/initial-defined-tags-override: '{"Operations": {"CostCenter": "42"}}'
reclaimPolicy: Delete
volumeBindingMode: WaitForFirstConsumer
```

Note the following:
  * If you specify the above parameters, none of the initial block volume tags set for the cluster are applied to the block volume resource. Only the tags specified by the parameters, along with tag defaults, are applied to the block volume resource.
  * Having applied a manifest file containing a StorageClass definition to create the storage class, you cannot subsequently change the tag parameter values by updating the definition and reapplying the manifest file. Once a storage class has been created, it is immutable. To specify different tag parameter values to the ones you previously specified, you have to create a new StorageClass definition that includes the new values for the tag parameters. Then specify the new storage class in the PVC definition.


## Which Tags Are Applied to Block Volumes? 🔗 
[![This image shows a flowchart that provides a graphical representation of how Kubernetes Engine applies tags to block volume resources. The same information is provided in the surrounding text.](https://docs.oracle.com/en-us/iaas/Content/ContEng/images/conteng-tagging-flowchart-blockvolumes.png)](https://docs.oracle.com/en-us/iaas/Content/ContEng/images/conteng-tagging-flowchart-blockvolumes.png)
Was this article helpful?
YesNo

