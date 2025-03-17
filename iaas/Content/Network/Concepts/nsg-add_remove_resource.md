Updated 2024-11-06
# Adding or Removing a Resource from an NSG
Describes how to add or remove a resource from a network security group (NSG).
In general, you manage the resource membership of an NSG _at the[parent resource](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/securityrules.htm#comparison)_, and not at the NSG itself. In other words, to add a parent resource to an NSG, you execute the action on the _parent resource_ (by specifying which NSGs the parent resource should be added to). You do not execute the action on the NSG (by specifying which VNICs or parent resources should be added to the NSG). Similarly, to remove a VNIC from an NSG, you execute that action by updating the parent resource, not the NSG. For a list of the parent resources that support the use of NSG, see [Support for Network Security Groups](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/networksecuritygroups.htm#support).
[Example: Compute Instances](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/nsg-add_remove_resource.htm)
  * **When creating an instance:** In the **Networking** section, under the advanced options, select **Use network security groups to control traffic**. Then, specify one or more NSGs. The instance's **primary VNIC** is added to the NSGs. See the procedure in [Creating an Instance](https://docs.oracle.com/iaas/Content/Compute/Tasks/launchinginstance.htm).
  * **For an existing instance:** Adding an existing instance to an NSG means adding its _primary VNIC_ to the NSG. You can also add a **secondary VNIC** to an NSG. See [Adding or Removing a VNIC from a Network Security Group](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/managingvnics_tasks-nsg.htm#managingvnics_tasks_nsg "Learn to add or remove a VNIC from a network security group."). 


[Example: Exadata Cloud VM Cluster](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/nsg-add_remove_resource.htm)
  * **When creating an Exadata cloud VM cluster:** In the **Network Information** section, you set up the client network and backup network. For each network, select **Use network security groups to control traffic** , and then specify one or more NSGs for the specific network. See [To create a cloud VM cluster resource](https://docs.oracle.com/iaas/exadatacloud/exacs/ecs-create-instance.html#GUID-11C092BB-2B85-4342-B143-8FC5FC80ECA3). Also see [Network Setup for Exadata Cloud Service Instances](https://docs.oracle.com/iaas/exadatacloud/exacs/ecs-network-setup.html).
  * **For an existing Exadata Cloud Service instance:** An Exadata cloud VM cluster's details include a list of the NSGs that the client network belongs to (if any), and a list of the NSGs that the backup network belongs to (if any). Next to the relevant **Network Security Groups** , click **Edit** to change that list.


Was this article helpful?
YesNo

