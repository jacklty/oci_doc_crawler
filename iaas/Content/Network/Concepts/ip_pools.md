Updated 2025-02-12
# Public IP Pools
A public IP pool is simply a set of IPv4 CIDR blocks allocated to a tenancy. These CIDR blocks can be all or part of a BYOIP CIDR block. Public IP CIDR blocks assigned to a pool are only available for your tenancy. Public IP pools are available as a source for IP allocation when launching a NAT gateway, load balancer, or compute instance. You can add more IP CIDR blocks to a public IP pool at any time. You can also: 
  * **Create a Reserved IP:** You can reserve individual IPs from your public IP pools. These reserved IP addresses can be attached to your resources.
  * **Direct launch from pool:** You can launch resources with an IP directly allocated from a public IP pool without previously creating a reserved IP for that resource.
  * **Delete CIDR blocks and pools:** You can delete the entire public IP pool or certain IP CIDR blocks within the pool, provided none of the IP addresses are currently attached or reserved.


**Note** IPv6 addresses do not use the IP Pools functionality described here. Instead, you can directly assign IPv6 prefixes to VCNs and subnets.
## Requirements and Preparation 🔗 
  * To use public IP pools with BYOIP addresses, you need to import your addresses.
  * To reserve Oracle-supplied public IP addresses, select "Oracle" as the public IP pool when creating the reserved public IP address.


## Limits and quotas 🔗 
  * You can create one or up to 10 public IP pools in a compartment.
  * A public IP pool can have zero or more IP CIDR ranges assigned to it, with a minimum size of /28 to a maximum size of /24.


See [IP Management Limits](https://docs.oracle.com/iaas/Content/General/Concepts/servicelimits.htm#byoip_limits) for general information and [requesting a service limit increase](https://docs.oracle.com/iaas/Content/General/Concepts/servicelimits.htm#Requesti) when necessary.
## Required IAM Policy
To use Oracle Cloud Infrastructure, an administrator must be a member of a group granted security access in a **policy** by a tenancy administrator. This access is required whether you're using the Console or the REST API with an SDK, CLI, or other tool. If you get a message that you don't have permission or are unauthorized, verify with the tenancy administrator what type of access you have and which **compartment** your access works in.
For administrators: see [IAM Policies for Networking](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/accesscontrol.htm#Policies). 
## Limits on IAM Resources 🔗 
For a list of applicable limits and [instructions for requesting a limit increase](https://docs.oracle.com/iaas/Content/General/Concepts/servicelimits.htm#Requesti), see [Service Limits](https://docs.oracle.com/iaas/Content/General/Concepts/servicelimits.htm). To set compartment-specific limits on a resource or resource family, administrators can use [compartment quotas](https://docs.oracle.com/iaas/Content/Quotas/Concepts/resourcequotas.htm).
## Managing IP pools using the console 🔗 
[To view your public IP pools](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/ip_pools.htm)
  1. Confirm you're viewing the region and compartment you're interested in. 
  2. Open the **navigation menu** and select **Networking**. Under **IP management** , select **Public IP pools**.


[To create a public IP pool](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/ip_pools.htm)
  1. Confirm you're viewing the region and compartment you're interested in. 
  2. Open the **navigation menu** and select **Networking**. Under **IP management** , select **Public IP pools**.
  3. Click **Create Public IP Pool**. 
     * Give the pool a name. Avoid entering confidential information.
     * Assign the Public IP pool to a compartment.
  4. Click **Create Public IP Pool**.


[To delete a public IP pool](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/ip_pools.htm)
  1. Confirm you're viewing the region and compartment you're interested in. 
  2. Open the **navigation menu** and select **Networking**. Under **IP management** , select **Public IP pools**.
  3. Select a public IP pool from the list and click **Delete Public IP Pool**. 
  4. If there are no warnings or errors, click **Delete Public IP Pool**. If this public IP pool contains reserved public IP addresses currently in use, you can't delete the public IP pool.


[To rename a public IP pool ](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/ip_pools.htm)
  1. Confirm you're viewing the region and compartment you're interested in. 
  2. Open the **navigation menu** and select **Networking**. Under **IP management** , select **Public IP pools**.
  3. Click **Rename Public IP Pool**. 
     * Enter a new name for the public IP pool. Avoid entering confidential information.
  4. Click **Save Changes**.


[To add CIDR blocks to a public IP pool](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/ip_pools.htm)
  1. Confirm you're viewing the region and compartment you're interested in. 
  2. Open the **navigation menu** and select **Networking**. Under **IP management** , select **Public IP pools**.
  3. Click **Add CIDR Blocks**. 
  4. Choose a named BYOIP CIDR block.
  5. Click **Add CIDR Blocks**.


[To remove CIDR blocks from an IP pool](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/ip_pools.htm)
**Note** To successfully remove a BYOIP CIDR block from a public IP pool, there must be no reserved public IP addresses from that address range. You may have to terminate one or more reserved public IP addresses.
  1. Confirm you're viewing the region and compartment you're interested in. 
  2. Open the **navigation menu** and select **Networking**. Under **IP management** , select **BYOIP**.
  3. Click on the BYOIP CIDR block.
  4. Click the Action Icon corresponding to the subrange you want to remove from a public IP pool, and then click **Remove from Public IP Pool**. A confirmation window appears.
  5. If you are sure you want to delete the BYOIP CIDR block, click **Remove CIDR Block**. 


[To reserve a public IP](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/ip_pools.htm)
  1. Confirm you're viewing the region and compartment you're interested in. 
  2. Open the **navigation menu** and select **Networking**. Under **IP management** , select **Public IP pools**.
  3. Click the name of a public IP pool from the list.
  4. Click the **Create Reserved Public IP** button. 
  5. Enter a name and specify the compartment for the new reserved public IP address. Avoid entering confidential information.
  6. When finished, click **Create Reserved Public IP**.


[To move a public IP pool to another compartment](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/ip_pools.htm)
  1. Confirm you're viewing the region and compartment you're interested in. 
  2. Open the **navigation menu** and select **Networking**. Under **IP management** , select **Public IP pools**.
  3. Click the name of a public IP pool from the list.
  4. Click the **Move Public IP Pool** button. An input screen appears. 
  5. Choose a new compartment for the public IP pool.
  6. Click **Move Public IP Pool**.


## Using the API 🔗 
For information about using the API and signing requests, see [REST API documentation](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm) and [Security Credentials](https://docs.oracle.com/iaas/Content/General/Concepts/credentials.htm). For information about SDKs, see [SDKs and the CLI](https://docs.oracle.com/iaas/Content/API/Concepts/sdks.htm).
To manage the [Public IP Pool](https://docs.oracle.com/iaas/api/#/en/iaas/latest/PublicIpPool) object, use these operations:
  * [AddPublicIpPoolCapacity](https://docs.oracle.com/iaas/api/#/en/iaas/latest/PublicIpPool/AddPublicIpPoolCapacity)
  * [ChangePublicIpPoolCompartment](https://docs.oracle.com/iaas/api/#/en/iaas/latest/PublicIpPool/ChangePublicIpPoolCompartment)
  * [CreatePublicIpPool](https://docs.oracle.com/iaas/api/#/en/iaas/latest/PublicIpPool/CreatePublicIpPool)
  * [DeletePublicIpPool](https://docs.oracle.com/iaas/api/#/en/iaas/latest/PublicIpPool/DeletePublicIpPool)
  * [GetPublicIpPool](https://docs.oracle.com/iaas/api/#/en/iaas/latest/PublicIpPool/GetPublicIpPool)
  * [ListPublicIpPools](https://docs.oracle.com/iaas/api/#/en/iaas/latest/PublicIpPool/ListPublicIpPools)
  * [RemovePublicIpPoolCapacity](https://docs.oracle.com/iaas/api/#/en/iaas/latest/PublicIpPool/RemovePublicIpPoolCapacity)
  * [UpdatePublicIpPool](https://docs.oracle.com/iaas/api/#/en/iaas/latest/PublicIpPool/UpdatePublicIpPool)


Was this article helpful?
YesNo

