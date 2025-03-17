Updated 2024-10-08
# Listing Drift Status for a Stack
List drift status for each resource in a stack in Resource Manager. Drift status is available for completed drift detections.
For information about drift detection, see [Detecting Drift in a Stack](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/detect-drift.htm#top "Detect drift in a stack in Resource Manager. Drift is the difference between the actual, real-world state of your infrastructure and the stack's last executed configuration.").
  * [Console](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/list-drift.htm)
  * [CLI](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/list-drift.htm)
  * [API](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/list-drift.htm)


  *     1. On the **Stacks** list page, select the stack that you want to work with. If you need help finding the list page or the stack, see [Listing Stacks](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/list-stacks.htm#top "List stacks in Resource Manager.").
    2. To view the latest drift detection report: On the **Stack information** tab of the stack's details page, select **View drift detection report**. 
A panel lists the drift status of the specified resources defined by the stack. Resources are identified by resource names.
    3. To view an older drift detection report: On the **Work requests information** tab, select the Actions menu (![Actions Menu](https://docs.oracle.com/en-us/iaas/Content/libraries/global-images/actions-menu.png)) for the related work request and then select **View drift detection report**.
A panel lists the drift status of the specified resources defined by the stack. Resources are identified by resource names.
    4. To view details of drift status for a resource, expand the resource.
Actual and expected properties are listed.
To generate a drift detection report (if the stack doesn't have one, or you want to create a new report): Go to **More actions** and select **Run drift detection**.
  * Use the `oci resource-manager stack list-resource-drift-details[](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/resource-manager/stack/list-resource-drift-details.html)` command and required parameters to list drift status.
Copy
```
oci resource-manager stack list-resource-drift-details --stack-id <stack_OCID>
```

For a complete list of parameters and values for CLI commands, see the [Command Line Reference for Resource Manager](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/resource-manager.html).
  * Use the [ListStackResourceDriftDetails](https://docs.oracle.com/iaas/api/#/en/resourcemanager/latest/StackResourceDriftSummary/ListStackResourceDriftDetails) operation to list drift status for each resource in a stack, for a completed [drift detection](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/detect-drift.htm#top "Detect drift in a stack in Resource Manager. Drift is the difference between the actual, real-world state of your infrastructure and the stack's last executed configuration.").


## Making Resources Match 🔗 
After listing drift status, if drift was detected, optionally make the stack's managed resources match the properties of the stack's Terraform configuration.
To make resources match the properties of the Terraform configuration, [run an apply job](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/create-job-apply.htm#top "Create an apply job in Resource Manager.").
Was this article helpful?
YesNo

