Updated 2024-04-02
# Attaching VCNs to a Dynamic Routing Gateway
On Compute Cloud@Customer, you can connect many VCNs to a DRG, but each VCN can have only one DRG attached. Ensure that the route tables and security lists allow communication.
  * [Console](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/network/attaching-vcns-to-a-dynamic-routing-gateway.htm)
  * [CLI](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/network/attaching-vcns-to-a-dynamic-routing-gateway.htm)
  * [API](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/network/attaching-vcns-to-a-dynamic-routing-gateway.htm)


  *     1. In the [Compute Cloud@Customer Console](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/overview/compute-cloud-customer-console.htm#accessing-the-console "Use the Compute Cloud@Customer Console to create and manage compute, storage and other resources on a Compute Cloud@Customer infrastructure.") navigation menu, under **Networking** , click **Dynamic Routing Gateway** s (DRGs).
    2. At the top of the page, select the compartment that contains the DRG.
    3. Click the name of the DRG that you plan to attach to a VCN.
    4. Click **Attach to Virtual Cloud Network**.
    5. From the list of VCNs in the drop-down list, click the VCN.
    6. Click the VCN to attach the DRG to from the list of VCNs in the drop down list. 
    7. Select the correct compartment. 
    8. Click **Attach to DRG**.
The DRG is attached to the selected VCN. 
    9. Repeat the process to attach the other VCNs to the DRG.
  * Use the [oci network drg-attachment create](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/network/drg-attachment/create.html) command and required parameters to attach the specified VCN to a DRG.
Copy
```
oci network drg-attachment create [OPTIONS]
```

For a complete list of CLI commands, flags, and options, see the [Command Line Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/index.html).
  * Use the [CreateDrgAttachment](https://docs.oracle.com/iaas/api/#/en/iaas/latest/DrgAttachment/CreateDrgAttachment) operation to attach the specified VCN to a DRG.
For information about using the API and signing requests, see [REST APIs](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm#REST_APIs) and [Security Credentials](https://docs.oracle.com/iaas/Content/General/Concepts/credentials.htm). For information about SDKs, see [Software Development Kits and Command Line Interface](https://docs.oracle.com/iaas/Content/API/Concepts/sdks.htm#Software_Development_Kits_and_Command_Line_Interface).


Was this article helpful?
YesNo

