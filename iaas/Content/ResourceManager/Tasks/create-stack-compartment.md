Updated 2025-01-07
# Creating a Stack from an Existing Compartment
Using resource discovery, create a stack in Resource Manager based on an existing compartment to generate a Terraform configuration that describes the compartment's resources.
For more information about resource discovery, see [Resource Discovery](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Concepts/resource-discovery.htm#top "Discover already deployed Oracle Cloud Infrastructure resources using Resource Manager.").
  * [Console](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/create-stack-compartment.htm)
  * [CLI](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/create-stack-compartment.htm)
  * [API](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/create-stack-compartment.htm)


  *     1. On the **Stacks** list page, select **Create stack**. If you need help finding the list page or the stack, see [Listing Stacks](https://docs.oracle.com/iaas/Content/ResourceManager/Tasks/list-stacks.htm).
    2. On the **Create stack** page, under **Choose the origin of the Terraform configuration** , select **Existing compartment**.
    3. Select the compartment and region that contain the resources that you want to [capture](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Concepts/resource-discovery.htm#top "Discover already deployed Oracle Cloud Infrastructure resources using Resource Manager.").
    4. (Optional) To filter for specific [services supported for resource discovery](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Reference/services-reference.htm#supported-services), select **Selected** and then select the services you want.
**Note** This setting can't be changed when editing the stack later.
    5. (Optional) To use [custom providers](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/update-stack-custom-providers.htm#top "Update a stack to fetch custom providers from Object Storage buckets."), select **Use custom providers** and then select the bucket that contains the custom provider.
    6. (Optional) Edit the default stack name and enter a stack description. Avoid entering confidential information.
    7. Select the compartment that you want to store the stack in.
    8. To add a defined tag, select the namespace and key, then enter a value.
    9. To add a free-form tag, enter a key and value.
    10. Select **Next** twice.
No variables are listed for the **Existing compartment** stack origin because no Terraform configuration exists yet.
    11. In the **Review** panel, verify the stack configuration.
    12. Select **Create**.
A work request runs on the stack. When the work request finishes, a job runs to generate a [Terraform configuration file](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Concepts/terraformconfigresourcemanager.htm#top "Review requirements and recommendations for Terraform configurations used with Resource Manager. Use Terraform and Resource Manager to install, configure, and manage resources using the infrastructure-as-code model.") for the stack. When the job finishes, the resources in the selected compartment are captured in the generated configuration. You can [recreate these resources in another compartment](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/recreate-infra.htm#top "Using resource discovery in Resource Manager, re-create existing infrastructure from an existing compartment.").
  * Use the `oci resource-manager stack create-from-compartment[](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/resource-manager/stack/create-from-compartment.html)` command and required parameters to create a stack from a compartment.
Copy
```
oci resource-manager stack create-from-compartment --compartment-id <compartment_OCID> --config-source-compartment-id <source_compartment_OCID> --config-source-region <region>
```

[Example Request](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/create-stack-compartment.htm)
For example (discovers [supported resources](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Concepts/resource-discovery.htm#supported-resources) from the `core` and `database` services; the source compartment is not a root compartment):
Command
CopyTry It
```
oci resource-manager stack create-from-compartment --config-source-compartment-id ocid1.tenancy.oc1..uniqueid1 --config-source-region PHX --config-source-services-to-discover [core,database] –-compartment-id ocid1.tenancy.oc1..uniqueid2 --terraform-version 0.13.X --display-name "Stack From Compartment ABC" --description "List of Resources to Duplicate"
```

[Example Response](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/create-stack-compartment.htm)
```
{
 "data": {
  "config-source": {
   "config-source-type": "COMPARTMENT_CONFIG_SOURCE"
  },
  "defined-tags": {},
  "display-name": "Stack from Compartment ABC",
  "freeform-tags": {},
  "id": "ocid1.ormstack.oc1..uniqueid",
  "lifecycle-state": "CREATING",
  "time-created": "2019-04-03T18:26:56.299000+00:00",
  "variables": {
   "compartment_ocid": "ocid1.compartment.oc1..uniqueid1", 
   "region": "us-phoenix-1"
  }
 }
}
```
```
{
 "data": {
  "compartment-id": "ocid1.compartment.oc1..uniqueid2",
  "config-source": {
   "compartment-id": "ocid1.compartment.oc1..uniqueid1",
   "config-source-type": "COMPARTMENT_CONFIG_SOURCE",
   "region": "PHX",
   "working-directory": null
  },
  "defined-tags": {},
  "description": "List of Resources to Duplicate",
  "display-name": "Stack From Compartment ABC",
  "freeform-tags": {},
  "id": "ocid1.ormstack.oc1.phx.uniqueid",
  "lifecycle-state": "CREATING",
  "stack-drift-status": "NOT_CHECKED",
  "terraform-version": "0.12.x",
  "time-created": "2020-06-01T18:25:56.102000+00:00",
  "time-drift-last-checked": null,
  "variables": {}
 },
 "etag": "009010cb57f5162655c6a34f5ef8834f204a734df81e4baa696a7d830488ea25",
 "opc-work-request-id": "ocid1.ormworkrequest.oc1.phx.uniqueid"
}
```

For a complete list of parameters and values for CLI commands, see the [Command Line Reference for Resource Manager](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/resource-manager.html).
  * Use the [CreateStack](https://docs.oracle.com/iaas/api/#/en/resourcemanager/latest/Stack/CreateStack) operation to create a stack from a compartment.
For an example of the `configSource` part of the request, see [CreateCompartmentConfigSourceDetails](https://docs.oracle.com/iaas/api/#/en/resourcemanager/latest/datatypes/CreateCompartmentConfigSourceDetails).
[Example request](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/create-stack-compartment.htm)
```
POST /20180917/stacks
Host: resourcemanager.us-phoenix-1.oraclecloud.com
<authorization and other headers>
{
 "compartmentId": "ocid1.compartment.oc1..<unique_ID>",
 "displayName": "My Compartment Configuration",
 "configSource": {
  "configSourceType": "COMPARTMENT_CONFIG_SOURCE",
  "compartmentId": "ocid1.compartment.oc1..<unique_ID>",
  "region": "us-phoenix-1"
 }
}
```



## What to Do Next 🔗 
You can [download](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/get-stack-tf-config.htm#top "Download the Terraform configuration used by a stack in Resource Manager. The Terraform configuration file for a stack is the one associated with the most recent successful job.") the generated Terraform configuration file. You can also [re-create](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/recreate-infra.htm#top "Using resource discovery in Resource Manager, re-create existing infrastructure from an existing compartment.") infrastructure in another compartment.
**Note** Alternatively, you can view the generated Terraform configuration file in Code Editor. For more information, see [Editing a Configuration Using Code Editor](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/code-editor.htm#top "Use Code Editor to edit the Terraform configuration associated with a stack in Resource Manager.").
Was this article helpful?
YesNo

