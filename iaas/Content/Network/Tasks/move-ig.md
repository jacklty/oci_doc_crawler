Updated 2025-01-17
# Moving an Internet Gateway to a Different Compartment 
Move an internet gateway into a different compartment within the same tenancy.
You can move an internet gateway from one compartment to another. When you move an internet gateway to a new compartment, inherent policies apply immediately. 
For more information about using compartments and policies to control access to a cloud network, see [Access Control](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/accesscontrol.htm#Access_Control). For general information about compartments, see [Managing Compartments](https://docs.oracle.com/iaas/Content/Identity/Tasks/managingcompartments.htm). 
  * [Console](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/move-ig.htm)
  * [CLI](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/move-ig.htm)
  * [API](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/move-ig.htm)


  *     1. Open the **navigation menu** , select **Networking** , and then select **Virtual cloud networks**.
    2. Select the name of the VCN you're interested in.
    3. Under **Resources** , select **Internet Gateway**. 
    4. Select the the Actions menu (![Actions Menu](https://docs.oracle.com/en-us/iaas/Content/libraries/global-images/actions-menu.png)) for the internet gateway, and then select **Move Resource**.
    5. Select the destination compartment from the list. 
    6. Select **Move Resource**.
  * Use the [network internet-gateway change-compartment](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/network/internet-gateway/change-compartment.html) command and required parameters to move an internet gateway to a different compartment:
Command
CopyTry It
```
oci network internet-gateway change-compartment --ig-id ig-ocid --compartment-id target-compartment-ocid ... [OPTIONS]
```

For a complete list of parameters and values for CLI commands, see the [CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest).
  * Run the [ChangeInternetGatewayCompartment](https://docs.oracle.com/iaas/api/#/en/iaas/latest/InternetGateway/ChangeInternetGatewayCompartment) operation to move an internet gateway into a different compartment.
For information about using the API and signing requests, see [REST API documentation](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm) and [Security Credentials](https://docs.oracle.com/iaas/Content/General/Concepts/credentials.htm). For information about SDKs, see [SDKs and the CLI](https://docs.oracle.com/iaas/Content/API/Concepts/sdks.htm).


Was this article helpful?
YesNo

