Updated 2024-05-14
# Viewing IP Address Insights
Access IP Address Insights to view the IP addresses used across a tenancy in a compartment and get a hierarchical visibility into VCNs, respective subnets, and network resources. 
  * [Console](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/ip_inventory_viewing.htm)
  * [CLI](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/ip_inventory_viewing.htm)
  * [API](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/ip_inventory_viewing.htm)


  *     1. Open the navigation menu and click **Networking**. Under **IP management** , click **IP Address Insights**.
    2. Under **Filters** , use each option to refine search: 
       * To display the IP Address Insights of a certain region, select a region from the **Region** menu at the top of the Console.
       * To display the IP address insights along with VCNs, respective subnets, and network resources from a specific compartment or many compartments, 
         1. Click inside **Resource Compartments** box.
         2. In the **Resource compartment** page, select the entire **Group** or selective compartments under **Individual compartment**.
         3. Click **Continue**.
       * To search resources in IP Address Insights,
         1. Go to the search box and enter a search text to retrieve all resources matching the search text in the IP Address Insights. 
         2. Click **Search** or press enter. The results matching the search text are listed. For example, if you use the search text **10.0.0.0** , the results include all the resource names and IP addresses matching the search text. 
       * To display the IP utilization of a particular utilization threshold, select a value from the **Utilization greater than or equal to** list.
       * To display the VCN IPs that overlap, under **Overlaps** , enable **Only show VCN IP overlaps**.
       * To display the IP address insights of all resources according to their IP address type, under **Address type** , select the preferred IP address types.
You can combine filters to narrow down the search results. Based on the selected filters, the Console displays IP address insights of resources with the following information:
       * **Resource** : Displays the resource names in a hierarchical order. For example, VCNs, respective subnets, and network resources from a specific compartment or many compartments in a hierarchy. To access the resource details page, click the name of the resource.
       * **CIDR/prefix/IP** : Displays the CIDR block, prefix, or the IP address assigned to the resource.
       * **Utilization** : Displays the IP utilization of the CIDR/prefix associated with a VCN or subnet.
       * **Overlaps** : Displays when the same CIDR/prefix/IP addresses are used by other resources indicating an overap.
       * **DNS hostnames** : Displays the DNS hostname of the resource. Click **Show** to view the complete DNS hostname. Click **Copy** to copy the hostname.
       * **Region** : Displays the region of the resource.
       * **Compartment** : Displays the compartments where the resources reside. For example, if a VCN is in one compartmnet and its subnets are from another compartment, all the compartments are listed here.
  * Use the `network ipam list-ip-inventory` command and required parameters to view the IP addresses used across a tenancy in a compartment:
Command
CopyTry It
```
oci network ipam list-ip-inventory
```

Use the `network ipam get-vcn-overlap` command to view the CIDR overlap information of the specified VCN in selected compartments:
Command
CopyTry It
```
oci network ipam get-vcn-overlap
```

For a complete list of parameters and values for CLI commands, see the [CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest).
  * For information about using the API and signing requests, see [REST API documentation](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm) and [Security Credentials](https://docs.oracle.com/iaas/Content/General/Concepts/credentials.htm). For information about SDKs, see [SDKs and the CLI](https://docs.oracle.com/iaas/Content/API/Concepts/sdks.htm).
Run the `ListIpInventory` operation to view the IP addresses used across a tenancy in a compartment.
Run the `GetVcnOverlap` operation to view the CIDR overlap information of the specified VCN in selected compartments.


Was this article helpful?
YesNo

