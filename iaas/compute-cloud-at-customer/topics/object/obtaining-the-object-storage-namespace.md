Updated 2024-10-07
# Obtaining the Object Storage Namespace
On Compute Cloud@Customer, an Object Storage namespace serves as the top-level container for all buckets and objects. Each tenant is assigned one unique system-generated and immutable Object Storage namespace name. The namespace spans all compartments. The namespace name is a required argument for many Object Storage CLI commands.
## Using the Console 🔗 
  1. In the [Compute Cloud@Customer Console](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/overview/compute-cloud-customer-console.htm#accessing-the-console "Use the Compute Cloud@Customer Console to create and manage compute, storage and other resources on a Compute Cloud@Customer infrastructure."), click your user name (upper right corner), then select **Tenancy**.
The namespace string is listed under Object Storage Settings.


## Using the CLI 🔗 
Run the following command and add the `iaas` endpoint to the command. For example:
Copy
```
oci os ns get --endpoint https://iaas.<mysystem>.example.com
{
 "data": "<myobjstor_namespace_name>"
}
```

For a complete list of CLI commands, flags, and options, see the [Command Line Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/index.html).
Was this article helpful?
YesNo

