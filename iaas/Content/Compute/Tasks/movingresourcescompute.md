Updated 2025-02-13
# Moving Compute Resources to a Different Compartment
You can move Compute resources such as instances, instance pools, and custom images from one compartment to another.
When you move a Compute resource to a new compartment, associated resources such as boot volumes and VNICs are not moved.
After you move the resource to the new compartment, inherent policies apply immediately and affect access to the resource through the Console. For more information, see [Managing Compartments](https://docs.oracle.com/iaas/Content/Identity/Tasks/managingcompartments.htm).
## Required IAM Policy 🔗 
To use Oracle Cloud Infrastructure, an administrator must be a member of a group granted security access in a **policy** by a tenancy administrator. This access is required whether you're using the Console or the REST API with an SDK, CLI, or other tool. If you get a message that you don't have permission or are unauthorized, verify with the tenancy administrator what type of access you have and which **compartment** your access works in.
For administrators: The following policies allow users to move Compute resources to a different compartment:
Copy
```
Allow group ComputeCompartmentMovers to manage instance-family in tenancy
Allow group ComputeCompartmentMovers to manage compute-management-family in tenancy
Allow group ComputeCompartmentMovers to manage auto-scaling-configurations in tenancy
Allow group ComputeCompartmentMovers to manage dedicated-vm-hosts in tenancy
```

If you're new to policies, see [Managing Identity Domains](https://docs.oracle.com/iaas/Content/Identity/domains/overview.htm) and [Common Policies](https://docs.oracle.com/iaas/Content/Identity/Concepts/commonpolicies.htm).
## Security Zones 🔗 
[Security Zones](https://docs.oracle.com/iaas/security-zone/home.htm) ensure that your cloud resources comply with Oracle security principles. If any operation on a resource in a security zone compartment violates a [policy for that security zone](https://docs.oracle.com/iaas/security-zone/using/security-zone-policies.htm), then the operation is denied.
The following security zone policies affect your ability to move Compute resources from one compartment to another:
  * You can't move a compute instance from a security zone to a compartment that is not in the same security zone.
  * You can't move a compute instance to a security zone from a compartment that is not in the same security zone.


## Using the Console 🔗 
[To move an instance to a different compartment](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/movingresourcescompute.htm)
  1. Open the **navigation menu** and select **Compute**. Under **Compute** , select **Instances**.
  2. In the **List Scope** section, select a compartment.
  3. Click the instance that you're interested in.
  4. Click **More Actions** , and then click **Move Resource**.
  5. Choose the destination compartment from the list. 
  6. Click **Move Resource**.
To track the progress of the operation and [troubleshoot errors](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/instances-monitoring-work-requests.htm#work-requests "Work requests help you monitor long-running operations such as database backups or the provisioning of compute instances.") that occur during instance creation, use the associated [work request](https://docs.oracle.com/iaas/Content/General/Concepts/workrequestoverview.htm#viewingwr).
  7. If there are alarms monitoring the instance, update the alarms to reference the new compartment. See [Updating an Alarm After Moving a Resource](https://docs.oracle.com/iaas/Content/Monitoring/Tasks/update-alarm-after-resource-move.htm) for more information.
  8. Optionally, move the resources that are attached to the instance to the new compartment.


[To move an instance configuration to a different compartment](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/movingresourcescompute.htm)
**Note** Most of the properties for an existing instance configuration, including the compartment, cannot be modified after you create the instance configuration. Although you can move an instance configuration to a different compartment, you will not be able to use the instance configuration to manage instance pools in the new compartment. If you want to update an instance configuration to point to a different compartment, you should instead create a new instance configuration in the target compartment. For steps, see [Creating an Instance Configuration](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/creatinginstanceconfig.htm#Creating_an_Instance_Configuration).
  1. Open the navigation menu and click **Compute**. Under **Compute** , click **Instance Configurations**. 
  2. In the **List Scope** section, select a compartment.
  3. Click the instance configuration that you're interested in.
  4. Click **Move resource**.
  5. Choose the destination compartment from the list. 
  6. Click **Move Resource**.


[To move an instance pool to a different compartment](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/movingresourcescompute.htm)
  1. Open the **navigation menu** and select **Compute**. Under **Compute** , select **Instance Pools**.
  2. In the **List Scope** section, select a compartment.
  3. Click the instance pool that you're interested in.
  4. Click **More Actions** , and then click **Move resource**.
  5. Choose the destination compartment from the list. 
  6. Click **Move Resource**.
  7. Optionally, update the instance pool with an instance configuration that points to the new compartment. Do the following:
    1. Create a new instance configuration in the new compartment. You can do this using the Console or the API. For steps, see [Creating an Instance Configuration](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/creatinginstanceconfig.htm#Creating_an_Instance_Configuration).
    2. Update the instance pool with the new instance configuration. You can do this using the API. For steps, see [Updating Instance Pools](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/updatinginstancepool.htm#Updating_an_Instance_Pool "You can change the size of an instance pool, attach existing instances to a pool, attach load balancers and network load balancers, and update various other properties.").
  8. Optionally, move the instances and other resources that are associated with the instance pool to the new compartment.


[To move an autoscaling configuration to a different compartment](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/movingresourcescompute.htm)
  1. Open the **navigation menu** and select **Compute**. Under **Compute** , select **Autoscaling Configurations**.
  2. In the **List Scope** section, select a compartment.
  3. Click the autoscaling configuration that you're interested in.
  4. Click **Move resource**.
  5. Choose the destination compartment from the list. 
  6. Click **Move Resource**.


[To move a custom image to a different compartment](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/movingresourcescompute.htm)
  1. Open the **navigation menu** and select **Compute**. Under **Compute** , select **Custom Images**.
  2. In the **List Scope** section, select a compartment.
  3. Click the custom image that you're interested in.
  4. Click **Move Resource**.
  5. Choose the destination compartment from the list. 
  6. Click **Move Resource**.


[To move a cluster network to a different compartment](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/movingresourcescompute.htm)
  1. Open the navigation menu and click **Compute**. Under **Compute** , click **Cluster Networks**.
  2. In the **List Scope** section, select a compartment.
  3. Click the cluster network that you're interested in.
  4. Click **Move Resource**.
  5. Choose the destination compartment from the list. 
  6. Click **Move Resource**.
  7. Optionally, move the instances and other resources that are associated with the cluster network to the new compartment.


[To move a dedicated virtual machine host to a different compartment](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/movingresourcescompute.htm)
  1. Open the **navigation menu** and select **Compute**. Under **Compute** , select **Dedicated Virtual Machine Hosts**. 
  2. In the **List Scope** section, select a compartment.
  3. Click the dedicated virtual machine host that you're interested in.
  4. Click **Move Resource**.
  5. Choose the destination compartment from the list.
  6. Click **Move Resource**.
  7. Optionally, move the instances that are placed on the dedicated virtual machine host to the new compartment.


## Using the API 🔗 
For information about using the API and signing requests, see [REST API documentation](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm) and [Security Credentials](https://docs.oracle.com/iaas/Content/General/Concepts/credentials.htm). For information about SDKs, see [SDKs and the CLI](https://docs.oracle.com/iaas/Content/API/Concepts/sdks.htm).
Use these API operations to move Compute resources to different compartments:
  * [ChangeInstanceCompartment](https://docs.oracle.com/iaas/api/#/en/iaas/latest/Instance/ChangeInstanceCompartment)
  * [ChangeInstanceConfigurationCompartment](https://docs.oracle.com/iaas/api/#/en/iaas/latest/InstanceConfiguration/ChangeInstanceConfigurationCompartment)
  * [ChangeInstancePoolCompartment](https://docs.oracle.com/iaas/api/#/en/iaas/latest/InstancePool/ChangeInstancePoolCompartment)
  * [ChangeAutoScalingConfigurationCompartment](https://docs.oracle.com/iaas/api/#/en/autoscaling/latest/AutoScalingConfiguration/ChangeAutoScalingConfigurationCompartment)
  * [ChangeImageCompartment](https://docs.oracle.com/iaas/api/#/en/iaas/latest/Image/ChangeImageCompartment)
  * [ChangeClusterNetworkCompartment](https://docs.oracle.com/iaas/api/#/en/iaas/latest/ClusterNetwork/ChangeClusterNetworkCompartment)
  * [ChangeDedicatedVmHostCompartment](https://docs.oracle.com/iaas/api/#/en/iaas/latest/DedicatedVmHost/ChangeDedicatedVmHostCompartment)


Was this article helpful?
YesNo

