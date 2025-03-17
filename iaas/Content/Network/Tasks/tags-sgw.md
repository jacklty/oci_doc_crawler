Updated 2025-01-15
# Tagging a Service Gateway
Add tags to a service gateway.
Using tags enables you to define keys and values and associate them with resources. You can apply tags to a service gateway to help you organize resources according to your business needs. Apply tags at the time you create a service gateway, or update the service gateway with tags later. For more information, see [Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). 
**Note** If you are not sure whether to apply tags, ask your administrator for guidance.
  * [Console](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/tags-sgw.htm)
  * [CLI](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/tags-sgw.htm)
  * [API](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/tags-sgw.htm)


  * This task can't be performed using the Console.
    1. In the Console, confirm you're viewing the compartment that contains the VCN with the SGW you're interested in. For information about compartments and access control, see [Access Control](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/accesscontrol.htm#Access_Control). 
    2. Open the **navigation menu** , select **Networking** , and then select **Virtual cloud networks**.
    3. Click the name of the VCN that has the SGW you're interested in.
    4. On the left side of the page, click **Service Gateways**.
    5. For the service gateway you're interested in, click the Actions menu (![Actions Menu](https://docs.oracle.com/en-us/iaas/Content/libraries/global-images/actions-menu.png)), and then click**View Tags**. From there you can view the existing tags, edit them, and apply new ones.
  * Use the [network service-gateway create](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/network/service-gateway/create.html) command and parameters shown to add tags when you create a service gateway:
Command
CopyTry It
```
oci network service-gateway create --compartment-id compartment_id [. . .] [--defined-tags | --freeform-tags] tags [OPTIONS]
```

Use the [network service-gateway update](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/network/service-gateway/update.html) command and parameters shown to add tags to an existing service gateway:
Command
CopyTry It
```
oci network service-gateway update --service-gateway-id sgw-ocid [. . .] [--defined-tags | --freeform-tags] tags [OPTIONS] 
```

For a complete list of parameters and values for CLI commands, see the [CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest).
  * Run the [CreateServiceGateway](https://docs.oracle.com/iaas/api/#/en/iaas/latest/ServiceGateway/CreateServiceGateway) operation to add tags when you create a service gateway, and use the definedTags attribute.
Run the [UpdateServiceGateway](https://docs.oracle.com/iaas/api/#/en/iaas/latest/ServiceGateway/UpdateServiceGateway) operation to add tags when you update a service gateway, and use the definedTags or freeformTags attributes.


Was this article helpful?
YesNo

