Updated 2025-01-23
# Inspecting Resources
Inspecting resources in a compartment allows you to confirm existence of a resource that you provisioned (by running an apply job) or absence of a resource that you released (by running a destroy job).
For information about apply and destroy jobs, see [Creating an Apply Job](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/create-job-apply.htm#top "Create an apply job in Resource Manager.") and [Creating a Destroy Job](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/create-job-destroy.htm#top "Create a destroy job in Resource Manager to release \(tear down\) resources associated with a stack and clean up the tenancy. Released resources are eventually deleted by the related OCI service. For example, a released compute instance is eventually deleted by the OCI Compute service.").
  * [Console](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/inspect-resources.htm)
  * [CLI](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/inspect-resources.htm)
  * [API](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/inspect-resources.htm)


  *     1. Go to the page that lists the resources that you want.
For example, to inspect VCNs: Open the **navigation menu** , select **Networking** , and then select **Virtual cloud networks**.
    2. To view the resources in a different compartment, use the **Compartment** filter to switch compartments.
You must have permission to work in a compartment to see the resources in it. If you're not sure which compartment to use, contact an administrator. For more information, see [Understanding Compartments](https://docs.oracle.com/iaas/Content/GSG/Concepts/settinguptenancy.htm#Understa).
  * Use the command corresponding to the resources that you want to inspect. 
For example, to inspect VCN resources, use the `oci network vcn list` command and required parameters.
Copy
```
oci network vcn list [OPTIONS]
```

For a complete list of parameters and values for CLI commands, see the [CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest).
  * Use the command corresponding to the resources that you want to inspect. 
For example, use the [ListVcns](https://docs.oracle.com/iaas/api/#/en/iaas/latest/Vcn/ListVcns) command to inspect VCN resources in the specified compartment.


Was this article helpful?
YesNo

