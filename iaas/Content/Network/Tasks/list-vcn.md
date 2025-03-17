Updated 2025-02-12
# Listing VCNs
List the VCNs available in a given compartment.
  * [Console](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/list-vcn.htm)
  * [CLI](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/list-vcn.htm)
  * [API](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/list-vcn.htm)


  *     1. Open the **navigation menu** , select **Networking** , and then select **Virtual cloud networks**.
    2. Under **List Scope** , select a compartment that you have permission to work in.The page updates to display only the resources in that compartment. If you're not sure which compartment to use, contact an administrator. For more information, see [Access Control](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/accesscontrol.htm#Access_Control).
**Note** To create any new resource the service limit for that resource must not already have been reached. After the service limit for a resource type has been reached, you can either remove unused resources of that type or [request a service limit increase](https://docs.oracle.com/iaas/Content/General/Concepts/servicelimits.htm#Requesti).
The console displays a list of VCNs in that compartment. The table is empty if there are no VCNs in that compartment. 
  * Use the [network vcn list](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/network/vcn/list.html) command and required parameters to list the VCNs in a compartment:
Command
CopyTry It
```
oci network vcn list --compartment-id compartment_id [OPTIONS]
```

For a complete list of parameters and values for CLI commands, see the [CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest).
  * Run the [ListVcns](https://docs.oracle.com/iaas/api/#/en/iaas/latest/Vcn/ListVcns) operation to list the VCNs in the currently selected compartment.


Was this article helpful?
YesNo

