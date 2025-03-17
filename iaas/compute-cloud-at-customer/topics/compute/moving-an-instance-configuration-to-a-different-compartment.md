Updated 2024-11-07
# Moving an Instance Configuration to a Different Compartment
On Compute Cloud@Customer, you can move an instance configuration to a different compartment within the same tenancy. 
When you move an instance configuration to a different compartment, instances and instance pools created by using this instance configuration aren't moved. 
New instances and instance pools that are created using this instance configuration are created in the compartment specified in the instance configuration, not in the compartment to which the instance configuration has been moved.
Avoid entering confidential information in names and tags.
  * [Console](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/compute/moving-an-instance-configuration-to-a-different-compartment.htm)
  * [CLI](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/compute/moving-an-instance-configuration-to-a-different-compartment.htm)
  * [API](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/compute/moving-an-instance-configuration-to-a-different-compartment.htm)


  * This task isn't available in the Console. 
  * Use the [oci compute-management instance-configuration change-compartment](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/compute-management/instance-configuration/change-compartment.html) command and required parameters move an instance configuration to a different compartment.
Copy
```
oci compute-management instance-configuration change-compartment --compartment-id destination_compartment_OCID --instance-configuration-id instance_configuration_OCID
```

For a complete list of CLI commands, flags, and options, see the [Command Line Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/index.html).
  * This task is not available in the API.
For information about using the API and signing requests, see [REST APIs](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm#REST_APIs) and [Security Credentials](https://docs.oracle.com/iaas/Content/General/Concepts/credentials.htm). For information about SDKs, see [Software Development Kits and Command Line Interface](https://docs.oracle.com/iaas/Content/API/Concepts/sdks.htm#Software_Development_Kits_and_Command_Line_Interface).


Was this article helpful?
YesNo

