Updated 2024-03-22
# Public IP Addresses
Describes how to manage public IPv4 addresses on instances in a virtual cloud network (VCN).
A public IP address is an IPv4 address that is reachable from the internet. If a resource in your tenancy needs to be directly reachable from the internet, it must have a public IP address. Depending on the type of resource, there might be other requirements.
Certain types of resources in your tenancy are designed to be directly reachable from the internet and therefore automatically come with a public IP address. For example: a NAT gateway or a public load balancer. Other types of resources are directly reachable only if you configure them to be. For example: instances in your VCN.
There are two types of public IPs:
  * **Ephemeral:** Think of it as temporary and existing for the lifetime of the instance.
  * **Reserved:** Think of it as persistent and existing beyond the lifetime of the instance it's assigned to. You can unassign it and then reassign it to another instance whenever you like. Exception: reserved public IPs on public load balancers. 


You can perform the public IP address management tasks:
  * [Creating a Reserved Public IP Address](https://docs.oracle.com/en-us/iaas/Content/Rover/Network/VCN/create-public-ip.htm#top "Describes how to create a reserved public IP address for your Roving Edge Infrastructure device.")
  * [Listing Reserved Public IP Addresses](https://docs.oracle.com/en-us/iaas/Content/Rover/Network/VCN/list-public-ip.htm#top "Describes how to list the reserved public IP addresses for your Roving Edge Infrastructure device.")
  * [Getting a Reserved Public IP Address' Details](https://docs.oracle.com/en-us/iaas/Content/Rover/Network/VCN/get-public-ip.htm#top "Describes how to get the details of a reserved public IP address for your Roving Edge Infrastructure device.")
  * [Editing a Reserved Public IP Address](https://docs.oracle.com/en-us/iaas/Content/Rover/Network/VCN/update-public-ip.htm#top "Describes how to edit a reserved public IP address for your Roving Edge Infrastructure device.")
  * [Deleting a Reserved Public IP Address](https://docs.oracle.com/en-us/iaas/Content/Rover/Network/VCN/delete-public-ip.htm#top "Describes how to delete a reserved public IP address from your Roving Edge Infrastructure device.")


See [Public IP Addresses](https://docs.oracle.com/iaas/Content/Network/Tasks/managingpublicIPs.htm) in the Oracle Cloud Infrastructure documentation for more information on this topic.
## Ephemeral Public IP Addresses 🔗 
The following sections address using ephemeral IP addresses:
### Assigning an Ephemeral Public IP when Launching an Instance 🔗 
When you launch an instance into a public subnet, there is an **Assign a Public IPv4 Address** check box on the **Create Compute Instance** dialog box. By default, the check box is selected, which means the instance gets an ephemeral public IP. If you do not want an ephemeral public IP assigned, perform one of the following: 
  * Deselect **Assign a Public IPv4 Address**.
  * Delete the ephemeral public IP after instance launch.


### Assigning an Ephemeral Public IP when Creating a Secondary VNIC 🔗 
When you add a secondary VNIC to an instance, you choose whether the primary private IP on the new VNIC gets an ephemeral public IP. This choice is available only if the secondary VNIC is in a public subnet.
In the **Create VNIC** dialog box, there is an **Assign a public IPv4 address** check box. By default, the check box is not selected, which means the secondary VNIC does not get an ephemeral public IP. You must select the check box.
### Assigning an Ephemeral Public IP to an Existing Private IP 🔗 
The primary private IP must not have a reserved or ephemeral public IP already assigned to it. If it does, first delete the ephemeral public IP, or unassign the reserved public IP.
  1. Open the navigation menu and click **Compute**. Click **Instances** under **Compute**. The instances are listed in tabular form.
  2. Click the instance with the attached VNIC you need. The instance's **Details** page appears.
  3. Click **Attached VNICs** under **Resources**. The primary VNIC and any secondary VNICs attached to the instance are listed in tabular form.
  4. Click the VNIC with the IP address that you need. The VNIC's **Details** page appears.
  5. Click **IP Addresses** under **Resources**. The VNIC's primary private IP and any secondary private IPs are listed in tabular form.
  6. Click the Actions menu (![Actions Menu](https://docs.oracle.com/en-us/iaas/Content/libs-rover/libraries/global-images/actions-menu.png)) for the VNIC's primary private IP, then select **Edit**. The **Edit Private IP Address** dialog box appears.
  7. Select the **Ephemeral Public IP** option under **Public IP Type**. The **Ephemeral Public IP Address** box appears.
  8. (optional) Enter an name for the public IP.
  9. Click **Update**.


### Deleting an Ephemeral Public IP from an Instance 🔗 
  1. Open the navigation menu and click **Compute**. Click **Instances** under **Compute**. The instances are listed in tabular form.
  2. Click the instance with the attached VNIC you need. The instance's **Details** page appears.
  3. Click **Attached VNICs** under **Resources**. The primary VNIC and any secondary VNICs attached to the instance are listed in tabular form.
  4. Click the VNIC with the IP address that you need. The VNIC's **Details** page appears.
  5. Click **IP Addresses** under **Resources**. The VNIC's primary private IP and any secondary private IPs are listed in tabular form.
  6. Click the Actions menu (![Actions Menu](https://docs.oracle.com/en-us/iaas/Content/libs-rover/libraries/global-images/actions-menu.png)) for the VNIC's primary private IP, then select **Edit**. The **Edit Private IP Address** dialog box appears.
  7. Select the **No Public IP** option under **Public IP Type**.
  8. Click **Update**.


### Renaming an Ephemeral Public IP 🔗 
  1. Open the navigation menu and click **Compute**. Click **Instances** under **Compute**. The instances are listed in tabular form.
  2. Click the instance with the attached VNIC you need. The instance's **Details** page appears.
  3. Click **Attached VNICs** under **Resources**. The primary VNIC and any secondary VNICs attached to the instance are listed in tabular form.
  4. Click the VNIC with the IP address that you need. The VNIC's **Details** page appears.
  5. Click **IP Addresses** under **Resources**. The VNIC's primary private IP and any secondary private IPs are listed in tabular form.
  6. Click the Actions menu (![Actions Menu](https://docs.oracle.com/en-us/iaas/Content/libs-rover/libraries/global-images/actions-menu.png)) for the VNIC's primary private IP, then select **Edit**. The **Edit Private IP Address** dialog box appears.
  7. Update the ephemeral public IP's name in the **Ephemeral Public IP Address** box.
  8. Click **Update**.


Was this article helpful?
YesNo

