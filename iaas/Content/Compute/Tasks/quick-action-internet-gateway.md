Updated 2025-01-13
# Quick Action: Connecting a Public Subnet to the Internet
When you create a compute instance, additional steps are necessary to enable it to contact a host on the internet or accept a connection from a user on the internet. You can use a quick action to connect a public subnet to the internet.
**Before you begin:**
Quick actions provide an easy way to set up resources. To use this quick action, you must have [created at least one compute instance](https://docs.oracle.com/iaas/Content/Compute/Tasks/launchinginstance.htm) with at least one public IP address.
**About this task:**
This quick action performs the steps to enable an instance to contact a host on the internet or accept a connection from a user on the internet. The quick action also creates the following resources:
  * An [internet gateway](https://docs.oracle.com/iaas/Content/Network/Tasks/managingIGs.htm)
  * A route rule in a [route table](https://docs.oracle.com/iaas/Content/Network/Tasks/managingroutetables.htm)
  * A [security rule](https://docs.oracle.com/iaas/Content/Network/Concepts/networksecuritygroups.htm#rules) in a [security list](https://docs.oracle.com/iaas/Content/Network/Concepts/securitylists.htm) or [network security group](https://docs.oracle.com/iaas/Content/Network/Concepts/networksecuritygroups.htm).


  1. Open the **navigation menu** and select **Compute**. Under **Compute** , select **Instances**.
  2. Select the instance that you're interested in. It needs to have at least one public IP address.
  3. Select **Connect public subnet to internet**.
  4. Enter the following values:
     * **Resource name prefix** : This prefix is applied to any resource created by the quick action, such as a route table, gateway, or network security group.
     * **Internet gateway** : If the instance's IP address is in a private subnet of a VCN that already has an internet gateway, the quick action detects that fact and uses the gateway in the configuration changes. 
     * **Network security group** : If your instance's VNIC has already reached its [limit](https://docs.oracle.com/iaas/Content/General/Concepts/servicelimits.htm#nsg_limits) of five NSGs or the VCN is at its NSG limit, select an existing NSG. Otherwise, the quick action creates a new NSG for this instance's VNIC. 
     * **Route table** : If the instance's IP address is in a subnet that already has a route table, then route rule changes are made to that route table. Otherwise, a new route table is created for that subnet, with a rule pointing to the internet gateway.
  5. Select **Create**.
Wait briefly while new resources are created or existing resources are modified.
  6. Select **Close**.


The compute instance is now able to connect to other hosts on the internet, and accept connections from internet clients. The required gateway, security settings, and route rules are configured.
Was this article helpful?
YesNo

