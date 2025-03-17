Updated 2024-08-14
# Applying Tags to Clusters
_Find out how to apply tags to Kubernetes clusters you create using Kubernetes Engine (OKE)._
When you create a cluster, you can optionally apply tags to the cluster resource. These tags are referred to as **cluster tags**. You can specify both defined tags and free-form tags as cluster tags.
Tag defaults with default values that are specified for the compartment are automatically applied to the cluster resource as well. Note that Kubernetes Engine does not currently support tag defaults with user-applied values.
Note the following:
  * If you use the 'Quick Create' workflow to create a new cluster, the free-form tag `"OKEclusterName": <cluster-name>` is automatically added to the cluster. The tag is not added to a cluster if you use the 'Custom Create' workflow to create the cluster. Note that the value of this tag does not change if you subsequently change the name of the cluster.
  * Tags applied to a cluster resource are not applied to either the cluster's private IP address resource or to the optional public IP address resource.
  * To apply defined tags from a tag namespace belonging to one compartment to a cluster resource belonging to a different compartment, you must include a policy statement to allow the cluster to use the tag namespace. See [Additional IAM Policy when a Cluster and a Tag Namespace are in Different Compartments](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengtaggingclusterresources_iam-tag-namespace-policy.htm#contengtaggingclusterresources_iam-tag-namespace-policy "Find out about an additional IAM policy you have to create if you want to apply defined tags from a tag namespace belonging to one compartment to cluster-related resources belonging to a different compartment, when using Kubernetes Engine \(OKE\).").


## Using the Console to Specify Cluster Tags 🔗 
To add a cluster tag to a new cluster:
  1. Follow the instructions in [Using the Console to create a Cluster with Explicitly Defined Settings in the 'Custom Create' workflow](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengcreatingclusterusingoke_topic-Using_the_Console_to_create_a_Custom_Cluster_with_Explicitly_Defined_Settings.htm#create-custom-cluster "Find out how to use the 'Custom Create' workflow to create a Kubernetes cluster with explicitly defined settings and existing network resources using Kubernetes Engine \(OKE\).") to create a new cluster.
  2. Display the **Cluster tags** section of the **Create Cluster** page.
  3. To add a defined tag to the cluster: 
     * **Tag namespace:** Select the tag namespace to which the tag belongs.
     * **Tag key:** Select the name of the defined tag to apply to the cluster.
     * **Tag value:** Either select the value for the tag from a pre-defined list of values, or enter a new value, or leave blank (depending on how the defined tag has been set up).
  4. To add a free-form tag to the cluster: 
     * **Tag namespace:** Set to None (free-form tags do not belong to a tag namespace).
     * **Tag key:** Enter a name for the free-form tag to apply to the cluster.
     * **Tag value:** Enter a value for the tag to apply to the cluster.


To update cluster tags applied to an existing cluster:
  1. Follow the instructions in [Updating a Cluster](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/update-cluster.htm#update-cluster "Find out how to update a cluster using Kubernetes Engine \(OKE\).") to update an existing cluster.
  2. Display the **Cluster tags** tab of the **Cluster details** page.
  3. Click **Add tags** to add, remove, and change the value of defined tags and free-form tags applied to the cluster.


## Using the CLI to Specify Cluster Tags 🔗 
Command
CopyTry It
```
oci ce cluster create \
--compartment-id <compartment-ocid> \
--kubernetes-version <kubernetes-version> \
--name <cluster-name> --vcn-id <vcn-ocid> \
--defined-tags <json-name-value-pairs> \
--freeform-tags <json-name-value-pairs>
```

For example:
Command
CopyTry It
```
oci ce cluster create \
--compartment-id ocid1.compartment.oc1..aaaaaaaay______t6q \
--kubernetes-version v1.20.11 \
--name Finance-Cluster \
--vcn-id ocid1.vcn.oc1.iad.aaaaaae___yja \
--defined-tags {"Operations": {"CostCenter": "42"}} \
--freeform-tags {"Department": "Finance"}
```

## Using the API to Specify Cluster Tags 🔗 
Use the `freeformTags` and `definedTags` attributes of the `CreateClusterDetails` and `UpdateClusterDetails` objects used by the [CreateCluster](https://docs.oracle.com/iaas/api/#/en/containerengine/latest/Cluster/CreateCluster) and [Update Cluster](https://docs.oracle.com/iaas/api/#/en/containerengine/latest/Cluster/UpdateCluster) operations to add and update cluster tags.
Was this article helpful?
YesNo

