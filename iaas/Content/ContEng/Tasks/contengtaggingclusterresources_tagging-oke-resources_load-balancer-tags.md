Updated 2024-08-14
# Applying Tags to Load Balancers
_Find out how to apply tags to load balancer resources, and how to override initial load balancer tags, when using Kubernetes Engine (OKE)._
**Note** References to load balancer in this section apply to both OCI load balancer resources and OCI network load balancer resources, unless explicitly stated otherwise.
When you create a cluster, you can optionally define tags to apply to load balancer resources created when Kubernetes services of type LoadBalancer are defined. These tags are referred to as **initial load balancer** tags. You can specify both defined tags and free-form tags as initial load balancer tags.
You can override initial load balancer tags using annotations on the Kubernetes service (see [Overriding Initial Load Balancer Tags](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengtaggingclusterresources_tagging-oke-resources_load-balancer-tags.htm#contengtaggingclusterresources_tagging_oke_resources_load_balancer_tags__load-balancer-tag-override-annotations)). If you specify the annotations when defining the Kubernetes service, none of the initial load balancer tags specified in the cluster definition are applied to the load balancer resource. Instead, the tags specified by the annotations are applied to the load balancer resource.
Tag defaults with default values that are specified for the compartment are automatically applied to the load balancer resource as well. Note that Kubernetes Engine does not currently support tag defaults with user-applied values.
Note the following:
  * Tags are only applied to load balancers when the load balancers are first created. If you update the initial load balancer tags, the changes only apply to new load balancers (assuming the tags are not overridden by annotations on the Kubernetes service). Tags applied to existing load balancers are unaffected.
  * If you apply a cost-tracking defined tag to a load balancer resource, you can include load balancer usage in budgets (see [Using Cost-Tracking Tags](https://docs.oracle.com/iaas/Content/Tagging/Tasks/usingcosttrackingtags.htm)).
  * To apply defined tags from a tag namespace belonging to one compartment to a load balancer resource belonging to a different compartment, you must include a policy statement to allow the cluster to use the tag namespace. See [Additional IAM Policy when a Cluster and a Tag Namespace are in Different Compartments](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengtaggingclusterresources_iam-tag-namespace-policy.htm#contengtaggingclusterresources_iam-tag-namespace-policy "Find out about an additional IAM policy you have to create if you want to apply defined tags from a tag namespace belonging to one compartment to cluster-related resources belonging to a different compartment, when using Kubernetes Engine \(OKE\).").


## Using the Console to Specify Initial Load Balancer Tags
To specify an initial load balancer tag to apply to load balancer resources created for a new cluster:
  1. Follow the instructions in [Using the Console to create a Cluster with Explicitly Defined Settings in the 'Custom Create' workflow](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengcreatingclusterusingoke_topic-Using_the_Console_to_create_a_Custom_Cluster_with_Explicitly_Defined_Settings.htm#create-custom-cluster "Find out how to use the 'Custom Create' workflow to create a Kubernetes cluster with explicitly defined settings and existing network resources using Kubernetes Engine \(OKE\).") to create a new cluster.
  2. Display the **Initial load balancer tags** section of the **Create Cluster** page.
  3. To add a defined tag to load balancer resources: 
     * **Tag Namespace:** Select the tag namespace to which the tag belongs.
     * **Tag Key:** Select the name of the defined tag to apply to load balancer resources.
     * **Tag Value:** Either select the value for the tag from a pre-defined list of values, or enter a new value, or leave blank (depending on how the defined tag has been set up).
  4. To add a free-form tag to load balancer resources: 
     * **Tag Namespace:** Set to None (free-form tags do not belong to a tag namespace).
     * **Tag Key:** Enter a name for the free-form tag to apply to load balancer resources.
     * **Tag Value:** Enter a value for the tag to apply to load balancer resources.


To update initial load balancer tags to apply to new load balancer resources created for a cluster:
  1. Follow the instructions in [Updating a Cluster](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/update-cluster.htm#update-cluster "Find out how to update a cluster using Kubernetes Engine \(OKE\).") to update an existing cluster.
  2. Display the **Initial Load Balancer Tags** tab of the **Cluster Details** page.
  3. Click **Add Tags** to add, remove, and change the value of defined tags and free-form tags applied to new load balancer resources.
Note that tags are only applied to load balancers when the load balancers are first created. So if you update initial load balancer tags, the changes only apply to new load balancer resources. Tags already applied to existing load balancer resources are unaffected.


## Using the CLI to Specify Initial Load Balancer Tags 🔗 
Command
CopyTry It
```
oci ce node-pool create \
--cluster-id <cluster-ocid> \
--compartment-id <compartment-ocid> \
--kubernetes-version <kubernetes-version> \
--name <node-pool-name> \
--node-shape <node-shape> \
--service-lb-defined-tags <json-name-value-pairs> \
--service-lb-freeform-tags <json-name-value-pairs>
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
--service-lb-defined-tags {"Operations": {"CostCenter": "42"}} \
--service-lb-freeform-tags {"Department": "Finance"}
```

## Using the API to Specify Initial Load Balancer Tags
Use the `freeformTags` and `definedTags` attributes of the `ServiceLbConfigDetails` object used by the [CreateCluster](https://docs.oracle.com/iaas/api/#/en/containerengine/latest/Cluster/CreateCluster) and [Update Cluster](https://docs.oracle.com/iaas/api/#/en/containerengine/latest/Cluster/UpdateCluster) operations to add and update initial load balancer tags.
## Overriding Initial Load Balancer Tags 🔗 
You can override initial load balancer tags specified for a cluster using annotations in the definition of a Kubernetes service of type LoadBalancer, as follows:
  * For load balancer resources:
    * To override defined initial load balancer tags for load balancer resources, add the following annotation in the metadata section of the manifest file:
Copy
```
oci.oraclecloud.com/initial-defined-tags-override: '{"<tag-namespace>": {"<tag-key>": "<tag-value>"}}'
```

    * To override free-form initial load balancer tags for load balancer resources, add the following annotation in the metadata section of the manifest file:
Copy
```
oci.oraclecloud.com/initial-freeform-tags-override: '{"<tag-key>": "<tag-value>"}'
```

  * For network load balancer resources:
    * To override defined initial load balancer tags for network load balancer resources, add the following annotation in the metadata section of the manifest file:
Copy
```
oci-network-load-balancer.oraclecloud.com/initial-defined-tags-override: '{"<tag-namespace>": {"<tag-key>": "<tag-value>"}}'
```

    * To override free-form initial load balancer tags for network load balancer resources, add the following annotation in the metadata section of the manifest file:
Copy
```
oci-network-load-balancer.oraclecloud.com/initial-freeform-tags-override: '{"<tag-key>": "<tag-value>"}'
```



For example:
Copy
```

apiVersion: v1
kind: Service
metadata:
 name: my-nginx-svc
 labels:
  app: nginx
 annotations:
  oci.oraclecloud.com/initial-defined-tags-override: '{"Operations": {"CostCenter": "42"}}'
  oci.oraclecloud.com/initial-freeform-tags-override: '{"Department": "Finance"}'
spec:
 type: LoadBalancer
 ports:
 - port: 80
 selector:
  app: nginx
```

Note the following:
  * If you specify the above annotations, none of the initial load balancer tags set for the cluster are applied to the load balancer resource. Only the tags specified by the annotations, along with tag defaults, are applied to the load balancer resource.
  * If you change the annotations in the manifest file, the changes only apply to new load balancer resources. Tags already applied to existing load balancer resources are unaffected. You cannot change the tags applied to an existing load balancer resource by changing the annotations. Instead, you have to create a new Kubernetes service of type LoadBalancer with the annotations for the tags you require.


## Which Tags Are Applied to Load Balancers? 🔗 
[![This image shows a flowchart that provides a graphical representation of how Kubernetes Engine applies tags to load balancer resources created for Kubernetes services of type LoadBalancer. The same information is provided in the surrounding text.](https://docs.oracle.com/en-us/iaas/Content/ContEng/images/conteng-tagging-flowchart-loadbalancers.png)](https://docs.oracle.com/en-us/iaas/Content/ContEng/images/conteng-tagging-flowchart-loadbalancers.png)
Was this article helpful?
YesNo

