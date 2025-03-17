Updated 2025-01-17
# Deleting an Internet Gateway
Delete an internet gateway from a Virtual Cloud Network (VCN) in Networking.
**Prerequisite:** Before you delete an internet gateway, delete all route rules in the VCN that specify the gateway as the target. Deleting those rules stops the routing in the VCN to the gateway. If a route rule refers to the gateway, it can't be deleted until the reference is removed.
See [Listing VCN Route Tables](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/list-routetable.htm#list-routetable "List VCN route tables in a given VCN and compartment.") and [Updating a VCN Route Table's Rules](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/update-rules-routetable.htm#update-rules-routetable "Add, edit, or delete rules for a Virtual Cloud Network \(VCN\) route table.") for more about finding and updating route rules that refer to a gateway.
  * [Console](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/delete-ig.htm)
  * [CLI](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/delete-ig.htm)
  * [API](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/delete-ig.htm)


  *     1. Open the **navigation menu** , select **Networking** , and then select **Virtual cloud networks**.
    2. Select the name of the VCN that you're interested in.
    3. Under **Resources** , select **Internet Gateway**. 
    4. Select the Actions menu (![Actions Menu](https://docs.oracle.com/en-us/iaas/Content/libraries/global-images/actions-menu.png)) for the internet gateway, and then select **Terminate**.
    5. Confirm when prompted.
  * Use the [network internet-gateway delete](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/network/internet-gateway/delete.htm) command and required parameters to delete an internet gateway:
Command
CopyTry It
```
oci network internet-gateway create --ig-id ig-ocid ... [OPTIONS]
```

  * Run the [DeleteInternetGateway](https://docs.oracle.com/iaas/api/#/en/iaas/latest/InternetGateway/DeleteInternetGateway) operation to delete an internet gateway.
For information about using the API and signing requests, see [REST API documentation](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm) and [Security Credentials](https://docs.oracle.com/iaas/Content/General/Concepts/credentials.htm). For information about SDKs, see [SDKs and the CLI](https://docs.oracle.com/iaas/Content/API/Concepts/sdks.htm).


Was this article helpful?
YesNo

