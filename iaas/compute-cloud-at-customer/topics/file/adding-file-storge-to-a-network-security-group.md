Updated 2023-08-15
# Adding File Storage to a Network Security Group
On Compute Cloud@Customer, adding File Storage to a network security group is accomplished by performing several procedures. This section lists the procedures.
**Task Flow**
No. | Description | Links to Procedures  
---|---|---  
1. |  Create an NSG with the required security rules.  (Alternatively, you can add them to a previously existing NSG.) |  [Controlling Traffic with Network Security Groups](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/network/controlling-traffic-with-network-security-groups.htm#controlling-traffic-with-network-security-groups "On Compute Cloud@Customer, both network security groups \(NSGs\) and security lists are types of virtual firewalls for your compute instances. Both NSGs and security lists define network security rules that decide which types of traffic are allowed in and out of instances \(VNICs\).")  
2. |  Add the mount target (or more specifically, the mount target's VNIC) to the NSG.  You can do this task when you create the mount target, or you can update the mount target and add it to one or more NSGs that contain the required security rules. |  [Adding a Mount Target to a Network Security Group](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/file/adding-a-mount-target-to-a-network-security-group.htm#adding-a-mount-target-to-a-network-security-group "On Compute Cloud@Customer, you can add the mount target to one or more Network Security Groups \(NSGs\). File storage requires specific rules to be configured for NSGs that are associated with mount targets.")  
3. |  If you're setting up a mount target and instance in different subnets, add the instance (or more specifically, the instance's primary VNIC) to the NSG that contains the required security rules. You can do this task when you create the instance, or you can directly update the instance's primary VNIC. |  [Updating a VNIC](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/network/updating-a-vnic.htm#updating-a-vnic "On Compute Cloud@Customer, you can update the VNIC name, the host name, and whether to disable source/destination checks. You can add the VNIC to an NSG and remove the VNIC from an NSG.")  
Was this article helpful?
YesNo

