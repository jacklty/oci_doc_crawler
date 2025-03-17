Updated 2025-01-17
# Listing Internet Gateways
List the internet gateway.
A VCN only needs one internet gateway.
  * [Console](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/list-ig.htm)
  * [CLI](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/list-ig.htm)
  * [API](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/list-ig.htm)


  *     1. Open the **navigation menu** , select **Networking** , and then select **Virtual cloud networks**.
    2. Select the name of the VCN you're interested in.
    3. Under **Resources** , select **Internet Gateway**. 
The internet gateway (if one exists) in the chosen VCN displays in the list shown. 
  * Use the [network internet-gateway list](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/network/internet-gateway/list.html) command and required parameters to list the internet gateways in a specified compartment:
Command
CopyTry It
```
oci network internet-gateway list --compartment-id compartment-ocid ... [OPTIONS]
```

For a complete list of parameters and values for CLI commands, see the [CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest).
  * Run the [ListInternetGateways](https://docs.oracle.com/iaas/api/#/en/iaas/latest/InternetGateway/ListInternetGateways) operation to list the internet gateways.
For information about using the API and signing requests, see [REST API documentation](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm) and [Security Credentials](https://docs.oracle.com/iaas/Content/General/Concepts/credentials.htm). For information about SDKs, see [SDKs and the CLI](https://docs.oracle.com/iaas/Content/API/Concepts/sdks.htm).


Was this article helpful?
YesNo

