Updated 2025-02-21
# Bring Your Own IP
Oracle Cloud Infrastructure allows you to Bring Your Own IP (BYOIP) address space to use with resources in Oracle Cloud Infrastructure, in addition to using Oracle owned addresses.
BYOIP lets you manage your IPv4 CIDR blocks and IPv6 prefixes to align with your existing security, management, and deployment policies and achieve: 
  * **Solution continuity and hardcoded dependencies:** Your VCN is an extension of your public Internet presence, without needing to reinvent policies and management processes. If you have IP addresses hard-coded in devices or built architectural dependencies on specific IP addresses, using BYOIP you have a smooth migration to Oracle Cloud Infrastructure.
  * **IP pool management:** Some network administrators require the ability to summarize groups of IPv4 addresses into pools and to create resources for deployment such as load balancers, firewalls, or web servers. IP Pool management provides tools to manage reserved public IPv4 addresses. IPv6 does not use IP Pool management.
  * **IP reputation:** Some internet services rely on a contiguous IP address space (such as a full span of IP addresses from 1 through 255) and act as a trusted contact point between services such as major email service providers and mail delivery systems.


Oracle performs a validation process on imported IPv4 CIDR blocks or IPv6 prefixes, and after validation you are notified that they are available for advertisement. You can create one or many public IPv4 pools from this address space by specifying subranges from the BYOIP CIDR block and use IP pools to allocate specific resources. You can start or stop advertisement of the BYOIP routes when needed. IPv6 does not use IP pools, but you can similarly assign prefixes to VCNs and subnets.
## Requirements and Preparation 🔗 
  * You must have ownership of the public IPv4 CIDR block or IPv6 prefix you want to import into Oracle Cloud Infrastructure, and the ownership must be registered with a supported Regional Internet Registry (RIR). Oracle validates ownership of your addresses. Only the following registries are supported, and the addresses must have a specified type or status:
    * [American Registry for Internet Numbers](https://www.arin.net/) (ARIN) - "Direct Allocation" and "Direct Assignment" network types
    * [Réseaux IP Européens Network Coordination Centre](https://www.ripe.net/) (RIPE NCC) - "ALLOCATED PA," "LEGACY," "ASSIGNED PI," and "ALLOCATED-BY-RIR" allocation statuses
    * [Asia-Pacific Network Information Centre](https://www.apnic.net/) (APNIC) – "ALLOCATED PORTABLE" and "ASSIGNED PORTABLE" allocation statuses
  * The addresses in the IP address range must have a clean history. We might investigate the reputation of the IP address range and reserve the right to reject an IP address range that contains an IP address that is associated with malicious behavior.


## Limits and Quotas 🔗 
  * Your addresses can only be imported to a specific Oracle region. 
  * You can use BYOIP with an IPv4 CIDR block that is a minimum of /24 and a maximum of /8. 
  * An imported IPv6 prefix must be /48 or larger. 
  * You can't bring the same address range to more than one compartment at a time.
  * You can bring up to 20 IPv4 CIDR blocks or IPv6 prefixes (or combination) to your Oracle Cloud Infrastructure account.
  * You can assign up to five total IPv6 prefixes per VCN and up to three per subnet. You may assign IPv6 addresses from multiple prefixes to a VNIC if its subnet has multiple IPv6 prefixes assigned.
  * BYOIP is not available with Oracle Cloud Infrastructure Free Tier, and must be requested for Pay As You Go services. 


See [IP Management Limits](https://docs.oracle.com/iaas/Content/General/Concepts/servicelimits.htm#byoip_limits) and [Requesting a Service Limit Increase](https://docs.oracle.com/iaas/Content/General/Concepts/servicelimits.htm#Requesti) for other limits-related information.
## BYOIP Process Overview 🔗 
The steps needed for BYOIP in Oracle Cloud Infrastructure require significant time, so plan accordingly. The process is shown in the following diagram:
[![Swimlane diagram showing the BYOIP import process.](https://docs.oracle.com/en-us/iaas/Content/Network/Images/network_byoip_swimlane.svg)](https://docs.oracle.com/en-us/iaas/Content/Network/Images/network_byoip_swimlane.svg)
  1. Within a compartment in your tenancy, you request to import a public IPv4 CIDR block or IPv6 prefix you own. 
  2. Oracle issues a verification token. (API users have to modify their token. Console users get a completed token.)
  3. You add the verification token to the information about that public IPv4 CIDR block or IPv6 prefix kept by your RIR service. The details vary depending on the RIR. It can take up to one day for the update to take effect. If you move to the next step before that update takes effect, a day will be added to the total time to complete the process. See [To import a BYOIP IPv4 CIDR block or IPv6 prefix](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/BYOIP.htm#import_cidr) for details.
  4. Create a Route Origin Authorization (ROA) with your RIR. As part of the ROA, provide the Oracle BGP ASN. Oracle's BGP ASN for the commercial cloud is 31898, except the Serbia Central (Jovanovac) region which is 14544. The ROA allows Oracle to advertise the BYOIP CIDR block. 
  5. Request that Oracle finish the import request. This workflow takes up to 10 business days to complete, while Oracle communicates with the RIR and verifies that you own the IP addresses. 
  6. Oracle provisions the BYOIP addresses to your compartment within your tenancy.
  7. At this point, the BYOIP IPv4 CIDR block or IPv6 prefix is yours to manage in your compartment. You can [add IPv4 addresses to an IP pool](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/BYOIP.htm#divide_byoip), and then use them as reserved IP addresses. IPv6 prefixes do not use pools, and you can directly assign subdivisions to VCNs or the assign the entire IPv6 prefix to a VCN. You can also [advertise the BYOIP CIDR Block or BYOIPv6 Prefix](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/BYOIP.htm#advertise_byoip) to the internet.


## Required IAM Policy
To use Oracle Cloud Infrastructure, an administrator must be a member of a group granted security access in a **policy** by a tenancy administrator. This access is required whether you're using the Console or the REST API with an SDK, CLI, or other tool. If you get a message that you don't have permission or are unauthorized, verify with the tenancy administrator what type of access you have and which **compartment** your access works in.
For administrators: see [IAM Policies for Networking](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/accesscontrol.htm#Policies). 
## Limits on IAM Resources 🔗 
For a list of applicable limits and [instructions for requesting a limit increase](https://docs.oracle.com/iaas/Content/General/Concepts/servicelimits.htm#Requesti), see [Service Limits](https://docs.oracle.com/iaas/Content/General/Concepts/servicelimits.htm). To set compartment-specific limits on a resource or resource family, administrators can use [compartment quotas](https://docs.oracle.com/iaas/Content/Quotas/Concepts/resourcequotas.htm).
## Managing BYOIP
## Using the console 🔗 
[To import a BYOIP IPv4 CIDR block or IPv6 prefix](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/BYOIP.htm)
  1. Confirm you are viewing the region and compartment you're interested in. 
  2. Open the **navigation menu** and select **Networking**. Under **IP management** , select **BYOIP**.
  3. Click **Import BYOIP CIDR Block**. The **Import BYOIP CIDR Block** screen appears.
  4. In the **Import BYOIP CIDR Block** screen, enter a name for the BYOIP CIDR block, choose the compartment, and enter the IPv4 CIDR block or IPv6 prefix you intend to bring to your tenancy. Avoid entering confidential information.
  5. Click **Save Changes**. The details page for that BYOIP import request appears.
  6. In the **Next Steps** section, make a copy of the validation token. The token format depends on the IP version.
Format for an IPv4 CIDR block:
```
OCITOKEN::<cidrBlock>:<validationToken>
```

Format for an IPv6 prefix: 
```
OCITOKEN::<ipv6CidrBlock>:<validationToken>
```

While the console presents you with a token that is ready to submit, the API does not. API users need to manually modify the token as shown.
  7. Create a Route Origin Authorization (ROA) object that authorizes Oracle to advertise the BYOIP CIDR block. Oracle's BGP ASN for the commercial cloud is 31898, except the Serbia Central (Jovanovac) region which is 14544. For the US Government Cloud, see [Oracle's BGP ASN](https://docs.oracle.com/iaas/Content/General/Concepts/govinfo.htm#bgp_asn). Set an expiry date at least 6 months in the future. Follow the instructions appropriate for your RIR:
     * **ARIN:**[ROA Requests](https://www.arin.net/resources/manage/rpki/roa_request/)
     * **RIPE NCC:** [Managing ROAs](https://www.ripe.net/manage-ips-and-asns/resource-management/certification/resource-certification-roa-management)
     * **APNIC:** [Route/ROA management](https://www.apnic.net/wp-content/uploads/2017/01/route-roa-management-guide.pdf)
**Note** If you do not create an ROA, Oracle can't advertise the BYOIP IPv4 CIDR block or IPv6 prefix. Without being able to advertise the routes, there may be little point in importing them. 
  8. Now add the validation token to the RIR account information associated with your address range. Each RIR uses a slightly different method:
     * **ARIN:** Add the token string in the "Public Comments" section associated with your address range. 
     * **RIPE NCC:** Add the token string as a new "descr" field associated with your address range. 
     * **APNIC:** Add the token string to the "remarks" field for your address range by emailing it to helpdesk@apnic.net. The email must be sent from the APNIC authorized contact account for the IP address range.
**Note** The validation token must be associated with the address range information. Do not add it to the information for the organization that owns the address range.
  9. Wait until both the ROA and the token registration is complete (up to a day) before you click the **Finish Import** button. Otherwise, the process can be delayed up to one day.
  10. Return to the details page for the BYOIP request and click **Finish Import**. A confirmation screen appears.
  11. Click **Finish Import** , confirming that you would like to validate the BYOIP request. Allow up to 10 business days for Oracle to contact your RIR, validate the import, and provision the CIDR block. View the work requests to see the status.


[To view your BYOIP CIDR blocks and prefixes](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/BYOIP.htm)
  1. Confirm you are viewing the region and compartment you're interested in. 
  2. Open the **navigation menu** and select **Networking**. Under **IP management** , select **BYOIP**.


[To rename a BYOIP CIDR block or prefix](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/BYOIP.htm)
  1. Confirm you are viewing the region and compartment you're interested in. 
  2. Open the **navigation menu** and select **Networking**. Under **IP management** , select **BYOIP**.
  3. Click the name of the BYOIP CIDR block or prefix you're interested in. 
  4. Click **Rename**. A window appears.
  5. In the window, enter the new name. Avoid entering confidential information.
  6. Click **Save Changes**.


[To remove a BYOIP IPV4 CIDR block from a pool](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/BYOIP.htm)
**Note** To successfully remove a BYOIP CIDR block from a pool, there must be no reserved public IP addresses in that address range. You may have to terminate one or more reserved public IP addresses. IPv6 prefixes do not use IP pools.
  1. Confirm you are viewing the region and compartment you're interested in. 
  2. Open the **navigation menu** and select **Networking**. Under **IP management** , select **BYOIP**.
  3. Click the name of the BYOIP IPv4 CIDR block you're interested in. 
  4. Click the Action Icon corresponding to the subrange you want to remove from a public IP pool, and then click **Remove from Public IP Pool**. A confirmation window appears.
  5. If you are sure you want to delete the BYOIP CIDR block, click **Remove CIDR Block**. 


[To delete a BYOIP IPv4 CIDR block or IPv6 prefix](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/BYOIP.htm)
To successfully delete a BYOIP CIDR block, it must be in the CREATING, PROVISIONED, ACTIVE, or FAILED state, and it must not have any subranges added to public IP pools. BYOIPv6 prefixes must not have any prefixes or subranges allocated to VCNs. 
**Note** If you delete a BYOIP CIDR block, you need to repeat the import process to undo your action.
  1. Confirm you are viewing the region and compartment you're interested in. 
  2. Open the **navigation menu** and select **Networking**. Under **IP management** , select **BYOIP**.
  3. Click the name of the BYOIP CIDR block you're interested in. 
  4. Click **Delete**. A confirmation window appears.
  5. If you are sure you want to delete the BYOIP CIDR block, click **Delete BYOIP CIDR block**.


[To advertise a BYOIP CIDR block or prefix](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/BYOIP.htm)
A BYOIP IPv4 CIDR block or IPv6 prefix must be provisioned before it can be advertised. 
**Note** The BYOIP CIDR block or IPv6 prefix is advertised using an Oracle-owned BGP ASN. Oracle's BGP ASN for the commercial cloud is 31898, except the Serbia Central (Jovanovac) region which is 14544.
  1. Confirm you are viewing the region and compartment you're interested in. 
  2. Open the **navigation menu** and select **Networking**. Under **IP management** , select **BYOIP**.
  3. Click the name of the BYOIP IPv4 CIDR block or IPv6 prefix you're interested in. 
  4. Click **Advertise**. A confirmation window appears.
  5. In the confirmation window, click **Advertise**.


[To withdraw a BYOIP CIDR block](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/BYOIP.htm)
  1. Confirm you're viewing the region and compartment you're interested in. 
  2. Open the **navigation menu** and select **Networking**. Under **IP management** , select **BYOIP**.
  3. Click the name of the BYOIP IPv4 CIDR block or IPv6 prefix you're interested in. 
  4. Click **Withdraw**. A confirmation window appears.
  5. In the confirmation window, click **Withdraw**.
**Note** Withdrawing your prefix from advertisement by Oracle doesn't remove objects within Oracle systems services such as geolocation, RADB, and so on. To stop using a BYOIP prefix with an OCI tenancy, it's important to delete the BYOIP prefix along with the withdrawal of the prefix advertisement. If you don't delete the prefix, the geolocation changes associated with the prefix continue to exist in Oracle systems and services.


[To divide a BYOIP IPv4 CIDR block and assign subranges to a public IP pool](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/BYOIP.htm)
  1. Confirm you are viewing the region and compartment you're interested in. 
  2. Open the **navigation menu** and select **Networking**. Under **IP management** , select **BYOIP**.
  3. Click the name of the BYOIP CIDR block you're interested in. 
  4. Scroll down to the BYOIP CIDR Block Subranges section and click **Manage BYOIP CIDR Block**. The Manage BYOIP CIDR Blocks screen appears.
  5. Either by entering a number for the CIDR suffix or using the up/down arrows next to the suffix, change the suffix number (often a /24). New rows in the table appear, representing possible subranges within the entire CIDR block. 
  6. For each of the newly created subranges of the BYOIP CIDR block, check the box in the first column of the table and click **Add BYOIP CIDR Blocks to Public IP Pools**. 
    1. Choose whether to **Select an Existing Public IP Pool** or **Create New Public IP Pool**. 
       * **Select an Existing Public IP Pool:** Choose an existing IP pool using the selection list.
       * **Create New Public IP Pool:** Assign the new pool a name and choose a compartment. You can move the public IP pool to another compartment later. Avoid entering confidential information.
    2. Click **Add BYOIP CIDR Blocks to Public IP Pools**
  7. Repeat the previous step until all subranges of the BYOIP CIDR block are assigned to a public IP pool, then click **Submit**.


**Note** If a subrange of a BYOIP CIDR block is left unassigned to a pool, the table may look different after you click **Submit**.
[To manage BYOIPv6 prefixes](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/BYOIP.htm)
  1. Confirm you are viewing the region and compartment you're interested in. 
  2. Open the **navigation menu** and select **Networking**. Under **IP management** , select **BYOIP**.
  3. Click the name of the BYOIPv6 prefix you want to manage.
  4. On the details page for the resource, click **Manage BYOIPv6 prefixes**. 
  5. You can assign some or all of the IPv6 prefix to a VCN. If you want to assign the whole BYOIPv6 prefix to an existing VCN, select the VCN in the Virtual Cloud Network column. 
  6. If you want to assign some of the BYOIPv6 prefix to one VCN and some to a different VCN, change the prefix shown from the default /48. Groupings of address ranges appear on-screen and you can assign them to existing VCNs.
  7. Click **Save changes** when you are finished. Click **Cancel** if you haven't made any selections. 
**Note** Assign at least one portion of the BYOIPv6 prefix to a VCN or the **Save changes** action can't be completed.


## Using the API 🔗 
For information about using the API and signing requests, see [REST API documentation](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm) and [Security Credentials](https://docs.oracle.com/iaas/Content/General/Concepts/credentials.htm). For information about SDKs, see [SDKs and the CLI](https://docs.oracle.com/iaas/Content/API/Concepts/sdks.htm).
To manage the [ByoipRange](https://docs.oracle.com/iaas/api/#/en/iaas/latest/ByoipRange) object, use these operations:
  * [AdvertiseByoipRange](https://docs.oracle.com/iaas/api/#/en/iaas/latest/ByoipRange/AdvertiseByoipRange)
  * [ChangeByoipRangeCompartment](https://docs.oracle.com/iaas/api/#/en/iaas/latest/ByoipRange/ChangeByoipRangeCompartment)
  * [CreateByoipRange](https://docs.oracle.com/iaas/api/#/en/iaas/latest/ByoipRange/CreateByoipRange): see below for further details.
  * [DeleteByoipRange](https://docs.oracle.com/iaas/api/#/en/iaas/latest/ByoipRange/DeleteByoipRange)
  * [GetByoipRange](https://docs.oracle.com/iaas/api/#/en/iaas/latest/ByoipRange/GetByoipRange)
  * [ListByoipRanges](https://docs.oracle.com/iaas/api/#/en/iaas/latest/ByoipRange/ListByoipRanges)
  * [UpdateByoipRange](https://docs.oracle.com/iaas/api/#/en/iaas/latest/ByoipRange/UpdateByoipRange)
  * [ValidateByoipRange](https://docs.oracle.com/iaas/api/#/en/iaas/latest/ByoipRange/ValidateByoipRange)
  * [WithdrawByoipRange](https://docs.oracle.com/iaas/api/#/en/iaas/latest/ByoipRange/WithdrawByoipRange)


The following operations are specific to BYOIPv6: 
  * [AddIpv6VcnCidr](https://docs.oracle.com/iaas/api/#/en/iaas/latest/Vcn/AddIpv6VcnCidr)
  * [RemoveIpv6VcnCidr](https://docs.oracle.com/iaas/api/#/en/iaas/latest/Vcn/RemoveIpv6VcnCidr)


### After creating a ByoipRange object
After you have created a `ByoipRange` object, make a copy of its `validationToken` and either the `ipv6CidrBlock` or the `ipv6CidrBlock` of the ByoipRange. Using any text editor, create a token string in one of the following formats.
To import an IPv4 CIDR block:
```
OCITOKEN::<cidrBlock>:<validationToken>
```

To import an IPv6 prefix: 
```
OCITOKEN::<ipv6CidrBlock>:<validationToken>
```

Present this modified validation token to your Regional Internet Registry (RIR) before you request validation.
Was this article helpful?
YesNo

