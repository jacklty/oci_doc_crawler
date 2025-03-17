Updated 2024-05-14
# Viewing CIDR or Prefix Utilization of a Subnet
View the percentage of IP addresses used from an IPv4 CIDR block or IPv6 prefix assigned to a subnet. 
  * [Console](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/ip_inventory_viewing_cidr_utilization.htm)
  * [CLI](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/ip_inventory_viewing_cidr_utilization.htm)
  * [API](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/ip_inventory_viewing_cidr_utilization.htm)


  *     1. Open the navigation menu and click **Networking**. Under **IP management** , click **IP Address Insights**.
    2. Under **Filters** , use each option to refine search. You can combine filters to narrow down the search results. Based on the selected filters, the Console displays IP address insights of resources.
    3. Expand the name of the VCN that contains the subnet.
    4. Click the name of the subnet to access the **Subnet Details** page.
    5. Under **Resources** , click **CIDR/Prefix utilization**. 
    6. Under **CIDR/Prefix utilization** , view the list of IPv4 CIDR blocks and IPv6 prefixes the subnet uses along with the percentage of IPs used from the CIDR block or prefix assigned to the subnet.
  * Use the `network ipam get-subnet-cidr-utilization` command and required parameters to view the percentage of IP addresses used from an IPv4 CIDR block or IPv6 prefix assigned to a subnet:
Command
CopyTry It
```
oci network ipam get-subnet-cidr-utilization --subnet-id subnet_ID_OCID
```

For a complete list of parameters and values for CLI commands, see the [CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest).
  * For information about using the API and signing requests, see [REST API documentation](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm) and [Security Credentials](https://docs.oracle.com/iaas/Content/General/Concepts/credentials.htm). For information about SDKs, see [SDKs and the CLI](https://docs.oracle.com/iaas/Content/API/Concepts/sdks.htm).
Run the `GetSubnetCidrUtilization` operation to view the percentage of IP addresses used from an IPv4 CIDR block or IPv6 prefix assigned to a subnet.


Was this article helpful?
YesNo

