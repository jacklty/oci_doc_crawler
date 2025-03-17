Updated 2025-01-17
# Tagging an Internet Gateway
Add metadata to an internet gateway, which lets you define keys and values and associate them with resources.
You can apply tags to an internet gateway to help you organize resources according to business needs. Apply tags at the time you create an internet gateway, or update the internet gateway with tags later. For more information, see [Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). 
**Note** If you're not sure whether to apply tags, ask an administrator for guidance.
  * [Console](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/tags-ig.htm)
  * [CLI](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/tags-ig.htm)
  * [API](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/tags-ig.htm)


  *     1. Open the **navigation menu** , select **Networking** , and then select **Virtual cloud networks**.
    2. Select the name of the VCN you're interested in.
    3. Under **Resources** , select **Internet Gateway**. 
    4. Select the Actions menu (![Actions Menu](https://docs.oracle.com/en-us/iaas/Content/libraries/global-images/actions-menu.png)) for the internet gateway, and then select **View Tags**. From there you can view the existing tags, edit them, and apply new ones.
  * Use the [network internet-gateway update](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/network/internet-gateway/update.html) command and required parameters to manage tags for the specified internet gateway:
Command
CopyTry It
```
oci network internet-gateway update --ig-id ig-ocid [--defined-tags | --freeform-tags] tags ... [OPTIONS]
```

For a complete list of parameters and values for CLI commands, see the [CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest).
  * Run the [UpdateInternetGateway](https://docs.oracle.com/iaas/api/#/en/iaas/latest/InternetGateway/UpdateInternetGateway) operation to manage tags for the specified internet gateway.
For information about using the API and signing requests, see [REST API documentation](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm) and [Security Credentials](https://docs.oracle.com/iaas/Content/General/Concepts/credentials.htm). For information about SDKs, see [SDKs and the CLI](https://docs.oracle.com/iaas/Content/API/Concepts/sdks.htm).


Was this article helpful?
YesNo

