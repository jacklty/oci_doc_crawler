Updated 2025-02-27
# Launching Custom Images
Launch a Compute custom image in an Oracle Cloud Infrastructure compartment.
  * [Console](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/custom-images-launch.htm)
  * [CLI](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/custom-images-launch.htm)
  * [API](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/custom-images-launch.htm)


  *     1. On the Compute custom images list page, select the custom image that you want to delete. If you need help finding the custom images list page, see [Listing Custom Images](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/custom-images-list.htm#listing-custom-images "Get a list of the Compute custom images in an Oracle Cloud Infrastructure compartment.").
    2. Select the custom image that you're interested in.
    3. Select **Create instance**.
    4. Provide additional details as described in [Creating an Instance](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/launchinginstance.htm#top "Create a bare metal or virtual machine \(VM\) compute instance by using Compute service.").
  * Use the [instance launch](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/compute/instance/launch.html) command and required parameters to create an instance:
Copy
```
oci compute instance launch --from-json <file://path/to/file.json>
```

<file://path/to/file.json> is the path to a JSON file that defines the instance details. For information about how to generate an example of the JSON file, see [Advanced JSON Options](https://docs.oracle.com/iaas/Content/API/SDKDocs/cliusing.htm#AdvancedJSON).
For a complete list of flags and variable options for the Compute service CLI commands, see the [command line reference for Compute](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/compute.html).
  * For information about using the API and signing requests, see [REST API documentation](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm) and [Security Credentials](https://docs.oracle.com/iaas/Content/General/Concepts/credentials.htm). For information about SDKs, see [SDKs and the CLI](https://docs.oracle.com/iaas/Content/API/Concepts/sdks.htm).
Use these API operations to launch instances:
    * [LaunchInstance](https://docs.oracle.com/iaas/api/#/en/iaas/latest/Instance/LaunchInstance)
    * [GetInstanceDefaultCredentials](https://docs.oracle.com/iaas/api/#/en/iaas/latest/InstanceCredentials/GetInstanceDefaultCredentials)


Was this article helpful?
YesNo

