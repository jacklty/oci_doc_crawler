Updated 2025-01-17
# Getting Details for an Internet Gateway
Get detailed information for the specified internet gateway.
  * [Console](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/get-ig.htm)
  * [CLI](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/get-ig.htm)
  * [API](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/get-ig.htm)


  *     1. Open the **navigation menu** , select **Networking** , and then select **Virtual cloud networks**.
    2. Select the name of the VCN you're interested in.
    3. Under **Resources** , select **Internet Gateway**. 
  * Use the [network internet-gateway get](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/network/internet-gateway/get.html) command and required parameters to get detailed information for the specified internet gateway:
Command
CopyTry It
```
oci network internet-gateway get --ig-id ig-ocid ... [OPTIONS]
```

For a complete list of parameters and values for CLI commands, see the [CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest).
  * Run the [GetInternetGateway](https://docs.oracle.com/iaas/api/#/en/iaas/latest/InternetGateway/GetInternetGateway) operation to get detailed information for the specified internet gateway.
For information about using the API and signing requests, see [REST API documentation](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm) and [Security Credentials](https://docs.oracle.com/iaas/Content/General/Concepts/credentials.htm). For information about SDKs, see [SDKs and the CLI](https://docs.oracle.com/iaas/Content/API/Concepts/sdks.htm).


Was this article helpful?
YesNo

