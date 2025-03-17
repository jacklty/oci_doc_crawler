Updated 2025-02-13
# Replacing a Boot Volume
You can automatically replace the boot volume of an instance without terminating and recreating the instance. The instance stops, replaces the boot volume, and returns the instance to the state prior to the volume replacement process. This feature allows the replacement of boot volumes if an issue is detected or an upgrade is needed to implement new features.
## Boot Volume Replacement Requirements and Options
The following are the key OS and images requirements to use boot volume replacement:
  * Only Linux operating systems and images are supported.
  * Windows and marketplace images are not supported.
  * Boot volumes can only be replaced with block volumes and images that use the same Linux distribution. For example, you cannot switch from Oracle Linux to Ubuntu or vice versa.
  * Image limitations apply for launch options associated with the image and what is currently on the instance. If for example the boot volume attachment type of the image doesn't match the instance launch options then the image is considered invalid.


In regard to instances you must have:
  * A virtual machine or bare metal instance.
  * And one of the following: 
    * A formatted block volume with a compatible operating system.
    * A backup image that is compatible with your instance.


## Required IAM Policy
To use Oracle Cloud Infrastructure, an administrator must be a member of a group granted security access in a **policy** by a tenancy administrator. This access is required whether you're using the Console or the REST API with an SDK, CLI, or other tool. If you get a message that you don't have permission or are unauthorized, verify with the tenancy administrator what type of access you have and which **compartment** your access works in.
To enable boot volume replacement, add the required policies for your compartment or tenancy. The following are examples of administration level instance policies that allow boot volume replacement for a compartment and a tenancy.
**Example Policies for a Compartment**
```
allow group InstanceUpdaters to manage instances in compartment instanceCompartment
OR
allow group InstanceUpdaters to manage instance-family in compartment instanceCompartment
```

**Example Policies for a Tenancy**
```
allow group InstanceUpdaters to manage instances in TENANCY
OR
allow group InstanceUpdaters to manage instance-family in TENANCY
```

For an existing set of policies, the following policy is the minimum required change to allow boot volume replacement.
```
allow group InstanceUpdaters to {INSTANCE_BOOT_VOLUME_REPLACE} in instanceCompartment
```

**Note** In the examples, `InstanceUpdaters` is a policy group that allows updates to instances.
## Rollback for Boot Volume Replacement
If a problem is encountered performing a block volume replacement, the system attempts to rollback the instance to it's original state. The steps performed include:
  * Restore the instance metadata.
  * Restore the instance state.
  * Restore the attached volumes state.
  * Restart the instance.


Ideally, this restores the instance to its prior state. This might not be possible in all circumstances.
**Note** When a rollback occurs, the new destination volume is handled as follows: 
  * When an image is used, rollback deletes the generated boot volume.
  * When a volume OCID is used, rollback doesn't delete the destination boot volume.


## Using the Console 🔗 
### Select the Boot Volume Options
To replace the boot volume for an instance, do the following.
  1. Open the **navigation menu** and select **Compute**. Under **Compute** , select **Instances**.
  2. Click the name of the instance.
  3. From the **More Actions** menu item, select **Replace Boot Volume.**
  4. Configure replace boot volume options: 
     * **Preserve Boot Volume** : If **Enabled** , the previous boot volume is preserved after successful replacement. Otherwise, the boot volume is terminated.


### Select a Replacement Boot Volume
Select your replacement volume using one of the following methods.
[Replace with a Boot Volume using a List](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/replacingbootvolume.htm)
  1. Under **Replace by** select **Boot Volume**.
  2. Under **Apply boot volume by** then select **Select from list**.
  3. Click the list to select the volume. 
**Note** You have the option to change the compartment.


[Replace with a Boot Volume using an OCID](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/replacingbootvolume.htm)
  1. Under **Replace by** select **Boot Volume**.
  2. Under **Apply boot volume by** then select **Input OCID**.
  3. Enter the OCID for the boot volume.


[Replace with an Image using a List](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/replacingbootvolume.htm)
  1. Under **Replace by** select **Image**.
  2. Under **Apply image by** then select **Select from list**.
  3. Click the list to select the image. 
**Note** You have the option to change the compartment.


[Replace with an Image using an OCID](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/replacingbootvolume.htm)
  1. Under **Replace by** select **Image**.
  2. Under **Apply image by** then select **Input OCID**.
  3. Enter the OCID for the image.


### Confirm your Choice
Click **Replace** to make your selection.
## Using the CLI 🔗 
Use the [instance update](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/compute/instance/update.html) command and required parameters to update an instance:
Command
CopyTry It
```
oci compute instance update --from-json <file://path/to/file.json>
```

<file://path/to/file.json> is the path to a JSON file that defines the instance details. For information about how to generate an example of the JSON file, see [Advanced JSON Options](https://docs.oracle.com/iaas/Content/API/SDKDocs/cliusing.htm#AdvancedJSON).
For a complete list of flags and variable options for the Compute Service CLI commands, see the [command line reference for Compute](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/compute.html).
## Using the API 🔗 
For information about using the API and signing requests, see [REST API documentation](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm) and [Security Credentials](https://docs.oracle.com/iaas/Content/General/Concepts/credentials.htm). For information about SDKs, see [SDKs and the CLI](https://docs.oracle.com/iaas/Content/API/Concepts/sdks.htm).
Use this API operation to replace the boot volume for an instance:
  * [UpdateInstance](https://docs.oracle.com/iaas/api/#/en/iaas/latest/Instance/UpdateInstance)


Was this article helpful?
YesNo

