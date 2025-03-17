Updated 2024-10-08
# Listing Resource Discovery Services
List services that are supported for resource discovery in Resource Manager.
When you create a stack from a compartment, the stack represents all [supported resources](https://registry.terraform.io/providers/oracle/oci/latest/docs/guides/resource_discovery#supported-resources) in the entire compartment, at the appropriate scope. If you select the root compartment for your tenancy, then the scope is the tenancy level, such as users and groups. If you select a non-root compartment, then the scope is compartment level, such as Compute instances.
For more information about resource discovery, see [Resource Discovery](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Concepts/resource-discovery.htm#top "Discover already deployed Oracle Cloud Infrastructure resources using Resource Manager.").
  * [Console](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/list-discovery-services.htm)
  * [CLI](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/list-discovery-services.htm)
  * [API](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/list-discovery-services.htm)


  * Begin the stack creation process for an existing compartment to view the list of [resource discovery](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Concepts/resource-discovery.htm#top "Discover already deployed Oracle Cloud Infrastructure resources using Resource Manager.") services.
    1. On the **Stacks** list page, select **Create stack**. If you need help finding the list page or the stack, see [Listing Stacks](https://docs.oracle.com/iaas/Content/ResourceManager/Tasks/list-stacks.htm).
    2. On the **Create stack** page, under **Choose the origin of the Terraform configuration** , select **Existing compartment**.
    3. (Optional) To filter for specific [services supported for resource discovery](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Reference/services-reference.htm#supported-services), select **Selected** and then select the services you want.
**Note** This setting can't be changed when editing the stack later.
    4. (Optional) To finish creating a stack from a compartment, provide values for other fields and select **Create**.
For information about the fields, see [Creating a Stack from an Existing Compartment](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/create-stack-compartment.htm#top "Using resource discovery, create a stack in Resource Manager based on an existing compartment to generate a Terraform configuration that describes the compartment's resources.").
  * Use the `oci resource-manager stack list-resource-discovery-services[](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/resource-manager/stack/list-resource-discovery-services.html)` command and required parameters to list services for resource discovery.
Copy
```
oci resource-manager stack list-resource-discovery-services [OPTIONS]
```

For a complete list of parameters and values for CLI commands, see the [Command Line Reference for Resource Manager](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/resource-manager.html).
  * Use the [ListResourceDiscoveryServices](https://docs.oracle.com/iaas/api/#/en/resourcemanager/latest/Stack/ListResourceDiscoveryServices) operation to list services for resource discovery.


Was this article helpful?
YesNo

