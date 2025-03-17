Updated 2024-01-18
# Moving a Steering Policy to a Different Compartment
On Compute Cloud@Customer, you can move a steering policy to a different compartment.
  * [Console](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/network/moving-a-steering-policy-to-a-new-compartment.htm)
  * [CLI](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/network/moving-a-steering-policy-to-a-new-compartment.htm)
  * [API](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/network/moving-a-steering-policy-to-a-new-compartment.htm)


  * This task isn't available in the Console.
  * Use the [oci dns steering-policy change-compartment](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/dns/steering-policy/change-compartment.html) command and required parameters to move a steering policy to a different compartment.
Copy
```
oci dns steering-policy change-compartment -c ** _<destination_compartment_OCID>_** \
--steering-policy-id **_<steering_policy_OCID>_**
```

For a complete list of CLI commands, flags, and options, see the [Command Line Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/index.html).
  * This task is not available in the API. 
For information about using the API and signing requests, see [REST APIs](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm#REST_APIs) and [Security Credentials](https://docs.oracle.com/iaas/Content/General/Concepts/credentials.htm). For information about SDKs, see [Software Development Kits and Command Line Interface](https://docs.oracle.com/iaas/Content/API/Concepts/sdks.htm#Software_Development_Kits_and_Command_Line_Interface).


Was this article helpful?
YesNo

