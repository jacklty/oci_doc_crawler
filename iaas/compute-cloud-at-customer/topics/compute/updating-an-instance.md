Updated 2025-01-27
# Updating an Instance
On Compute Cloud@Customer, you can change instance parameters.
In addition to updating the properties of an instance, you might want to attach additional block volumes or secondary VNICs. See [Creating and Attaching Block Volumes](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/block/creating-and-attaching-block-volumes.htm#creating-and-attaching-block-volumes "You can create and attach a block volume to an instance to expand the available storage on the instance. The topics in this section describe how to administer the Block Volume Storage service for Compute Cloud@Customer.") and [Creating and Attaching a Secondary VNIC](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/network/creating-and-attaching-a-secondary-vnic.htm#creating-and-attaching-a-secondary-vnic "On Compute Cloud@Customer, you can add more VNICs to an instance."). You can also specify block volumes and secondary VNICs when you use an instance configuration to create an instance.
If you didn't add a public IP address when you created the instance, and you want to assign a public IP address now, see [Assigning an Ephemeral Public IP Address to an Instance](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/network/assingning-an-ephemeral-public-ip-address-to-an-instance.htm#assingning-an-ephemeral-public-ip-address-to-an-instance "On Compute Cloud@Customer, you assign a public IP address to an instance by assigning the public IP address object to a private IP address object.") for instructions.
You can update the display name, fault domain, shape, instance options, availability configuration, and tags of an instance. Using the CLI, you can also update the instance metadata. See the descriptions of these properties in [Creating an Instance](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/compute/creating-an-instance.htm#creating-an-instance "On Compute Cloud@Customer, you can create an instance using the Compute Cloud@Customer Console, CLI, and API.").
Avoid entering confidential information in names and tags.
  * [Console](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/compute/updating-an-instance.htm)
  * [CLI](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/compute/updating-an-instance.htm)
  * [API](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/compute/updating-an-instance.htm)


  * When you update an instance using the Compute Cloud@Customer Console, you can change the following instance parameters:
    * **Instance display name**
Avoid entering confidential information
    * **Fault domain**
When you change the fault domain of a stopped instance, the new fault domain is set in the instance properties. When you change the fault domain of a running instance, the instance is stopped, moved, and started on a new compute node in the new fault domain. See [Stopping, Starting, and Resetting an Instance](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/compute/stopping-starting-and-resetting-an-instance.htm#stopping-starting-and-resetting-an-instance "On Compute Cloud@Customer, you can control the state of an instance using the Compute Cloud@Customer Console, CLI, and API.") for how to prepare for an instance to stop. Stopping and starting an instance can take up to five minutes.
If you specify a fault domain, and the requested fault domain can't accommodate the instance, instance restart fails; the instance remains stopped. The new fault domain specification remains in the instance properties.
    * **Shape**
When you change the shape of a stopped instance, the new shape and shape configuration are set in the instance properties. When you change the shape of a running instance, the instance is stopped, reconfigured, and restarted. See [Stopping, Starting, and Resetting an Instance](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/compute/stopping-starting-and-resetting-an-instance.htm#stopping-starting-and-resetting-an-instance "On Compute Cloud@Customer, you can control the state of an instance using the Compute Cloud@Customer Console, CLI, and API.") for how to prepare for an instance to stop. Stopping and starting an instance can take up to five minutes.
If you're using the VM.PCAStandard.E5.Flex shape, you must specify the number of OCPUs you want and you can specify the total amount of memory you want. See [Compute Shapes](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/compute/compute-shapes.htm#compute-shapes "A shape is a template that determines the type and amount of resources that are allocated to a compute instance. Compute Cloud@Customer offers a choice between a flexible shape for generic workloads, and dedicated shapes for GPU-accelerated workloads.").
If the specified shape and shape configuration can't be accommodated in the fault domain, instance restart fails; the instance remains stopped. The new shape and shape configuration remain in the instance properties.
    * **Instance Options**
If you have upgraded your applications to use `/v2` Instance Metadata Service (IMDS) endpoints, check this box to disable `/v1` endpoints. For more information about the Instance Metadata Service, see [Retrieving Instance Metadata from Within the Instance](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/compute/retrieving-instance-metadata-from-within-the-instance.htm#retrieving-instance-metadata-from-within-the-instance "On Compute Cloud@Customer, the Instance Metadata Service \(IMDS\) serves information about a running instance to users who are logged in to that instance. IMDS also provides information to cloud-init that you can use for various system initialization tasks.").
    * **Availability configuration**
This sets whether an instance that has been stopped by the Compute service is restarted when resources become available (the default) or remains stopped.
    * **Tagging:** (Optional) Add one or more tags to this resource. Tags can also be applied later. For more information about tagging resources, see [Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm).
    1. On the [Compute Cloud@Customer Console](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/overview/compute-cloud-customer-console.htm#accessing-the-console "Use the Compute Cloud@Customer Console to create and manage compute, storage and other resources on a Compute Cloud@Customer infrastructure.") **Dashboard** , in the **Compute** block, click **Instances**.
    2. At the top of the page, select the compartment that contains the instance.
    3. For the instance that you want to update, click the Actions menu (![An image of the three dot icon.](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/images/three-dots.png)), then click **Edit**.
    4. In the **Edit** `**_instance_name_**`dialog box, make the changes.
    5. Click **Save Changes**.
If you changed the fault domain, shape, or shape configuration of a running instance, you must confirm that you understand that the instance must be rebooted. For these changes, the instance is stopped, reconfigured, and restarted.
  * Use the [oci compute instance update](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/compute/instance/update.html) command and required parameters to update the specified instance.
Copy
```
oci compute instance update --instance-id <instance_OCID> <options_with_values_to_update> [OPTIONS]
```

For descriptions of instance properties that you can change using the CLI, enter the following command and scroll to Optional Parameters:
```
$ oci compute instance update -h
```

For a complete list of CLI commands, flags, and options, see the [Command Line Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/index.html).
**Procedure**
    1. Get the OCID of the instance that you want to update: ```
oci compute instance list
```

If you want to change the fault domain of the instance, get the OCID of the fault domain:
```
$ oci iam fault-domain list --compartment-id <compartment_OCID> --availability-domain AD-1
```

If you want to change the shape of the instance, get the name of the shape:
```
$ oci compute shape list --compartment-id <compartment_OCID> --image-id <image_OCID>
```

    2. Run the instance update command.
Syntax:
```
oci compute instance update --instance-id <instance_OCID> <options_with_values_to_update>
```

  * Use the[UpdateInstance](https://docs.oracle.com/iaas/api/#/en/iaas/latest/Instance/UpdateInstance) operation to update the specified instance.
For information about using the API and signing requests, see [REST APIs](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm#REST_APIs) and [Security Credentials](https://docs.oracle.com/iaas/Content/General/Concepts/credentials.htm). For information about SDKs, see [Software Development Kits and Command Line Interface](https://docs.oracle.com/iaas/Content/API/Concepts/sdks.htm#Software_Development_Kits_and_Command_Line_Interface).


Was this article helpful?
YesNo

