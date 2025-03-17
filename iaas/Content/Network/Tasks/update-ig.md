Updated 2025-01-17
# Updating an Internet Gateway
Update an internet gateway (IGW) in a Virtual Cloud Network (VCN) in Networking. 
You can't change the display name or disable or enable an internet gateway by using the Console, but you can do both using the CLI or API. If the gateway is disabled, that means no traffic flows to or from the internet even when a route rule allows that traffic.
You can associate a route table with the internet gateway, and also [change its tags](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/tags-ig.htm#tags-ig "Add metadata to an internet gateway, which lets you define keys and values and associate them with resources."). After a route table is associated with a gateway, the gateway must always have a route table associated with it.
  * [Console](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/update-ig.htm)
  * [CLI](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/update-ig.htm)
  * [API](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/update-ig.htm)


  *     1. Open the **navigation menu** , select **Networking** , and then select **Virtual cloud networks**.
    2. Select the name of the VCN that you're interested in.
    3. Under **Resources** , select **Internet Gateway**. 
    4. Select the the Actions menu (![Actions Menu](https://docs.oracle.com/en-us/iaas/Content/libraries/global-images/actions-menu.png)) for the internet gateway, and then select **Associate Route Table**.
    5. Select a route table, changing the compartment as needed to find the one that you want. Then, select **Associate Route Table**.
  * Use the [network internet-gateway update](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/network/internet-gateway/update.html) command and required parameters to change the display name of the specified internet gateway:
Command
CopyTry It
```
oci network internet-gateway update --ig-id ig-ocid --display-name new-name ... [OPTIONS]
```

Use the [network internet-gateway update](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/network/internet-gateway/update.html) command and required parameters to enable or disable the specified internet gateway:
Command
CopyTry It
```
oci network internet-gateway update --ig-id ig-ocid --is-enabled [true | false] ... [OPTIONS]
```

Use the [network internet-gateway update](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/network/internet-gateway/update.html) command and required parameters to associate a route table to the specified internet gateway:
Command
CopyTry It
```
oci network internet-gateway update --ig-id ig-ocid --route-table-id route-table-ocid ... [OPTIONS]
```

For a complete list of parameters and values for CLI commands, see the [CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest).
  * Run the [UpdateInternetGateway](https://docs.oracle.com/iaas/api/#/en/iaas/latest/InternetGateway/UpdateInternetGateway) operation to update the specified internet gateway.
For information about using the API and signing requests, see [REST API documentation](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm) and [Security Credentials](https://docs.oracle.com/iaas/Content/General/Concepts/credentials.htm). For information about SDKs, see [SDKs and the CLI](https://docs.oracle.com/iaas/Content/API/Concepts/sdks.htm).


Was this article helpful?
YesNo

