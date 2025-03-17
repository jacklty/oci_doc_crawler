Updated 2024-01-18
# Deleting a Public IP Address
On Compute Cloud@Customer, in certain circumstances, you can delete public IP addresses.
An ephemeral public IP address object can't be unassigned and can't be directly deleted. An ephemeral public IP address object is deleted in the following cases:
  * Its private IP address object is deleted.
  * Its VNIC is detached or deleted.
  * Its instance is deleted.


A reserved public IP address object is unassigned but remains available for reassignment when its private IP address object is deleted, its VNIC is detached or deleted, or its instance is deleted.
Use the procedures in this section to delete a reserved public IP address object.
  * [Console](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/network/deleting-a-public-ip-address.htm)
  * [CLI](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/network/deleting-a-public-ip-address.htm)
  * [API](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/network/deleting-a-public-ip-address.htm)


  * This task isn't available in the Console.
  * Use the [oci network private-ip delete](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/network/private-ip/delete.html) command and required parameters to unassign and delete the specified public IP.
Copy
```
oci network public-ip delete [OPTIONS]
```

For a complete list of CLI commands, flags, and options, see the [Command Line Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/index.html).
  * Use the [DeletePublicIp](https://docs.oracle.com/iaas/api/#/en/iaas/latest/PublicIp/DeletePublicIp) operation to unassign and delete the specified public IP.
For information about using the API and signing requests, see [REST APIs](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm#REST_APIs) and [Security Credentials](https://docs.oracle.com/iaas/Content/General/Concepts/credentials.htm). For information about SDKs, see [Software Development Kits and Command Line Interface](https://docs.oracle.com/iaas/Content/API/Concepts/sdks.htm#Software_Development_Kits_and_Command_Line_Interface).


Was this article helpful?
YesNo

