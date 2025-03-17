Updated 2025-01-13
# Creating an Instance Configuration
Instance configurations let you define the settings to use when creating compute instances. Use an instance configuration in the following scenarios:
  * To create one or more instances in an [instance pool](https://docs.oracle.com/en-us/iaas/Content/Compute/Concepts/instancemanagement.htm#Managing_Compute_Instances).
  * As a template for launching individual instances that are not part of a pool.


When you create an instance configuration, you can use an existing compute instance as a template, or you can provide a list of configuration settings.
You can optionally specify a [secondary virtual network interface card (VNIC)](https://docs.oracle.com/iaas/Content/Network/Tasks/managingVNICs.htm) and [block volumes](https://docs.oracle.com/iaas/Content/Block/Tasks/attachingavolume.htm) to attach to the instances that are created from an instance configuration. To do this, create the instance configuration by providing a list of configuration settings.
## Limitations and Considerations 🔗 
  * If you use an existing instance as a template to create an instance configuration, be aware of the following information:
    * The instance configuration does not include any information from the instance's boot volume, such as installed applications, binaries, and files on the instance. To create an instance configuration that includes the custom setup from an instance, you must first [create a custom image from the instance](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/custom-images-create.htm#listing-custom-images "Create a Compute custom image in an Oracle Cloud Infrastructure compartment.") and then [use the custom image to create a new instance](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/managingcustomimages.htm#Managing_Custom_Images__console-custom-image-tasks). Finally, create the instance configuration based on the instance that you created from the custom image.
    * The instance configuration does not include the contents of any block volumes that are attached to the instance.
    * Any instances created from the instance configuration are placed in the same compartment as the instance that was used as the basis for the instance configuration, regardless of the compartment of the instance configuration. For example, an instance in compartment A is used to create an instance configuration. For example, you use an instance in compartment A as the basis to create an instance configuration. You place the instance configuration in compartment B. Any instances created using that instance configuration will be located in compartment A, the same compartment as the original instance.
  * If you provide a list of configuration settings to create an instance configuration, be aware of the following information:
    * When you create an instance from the instance configuration, many of the settings defined in the instance configuration cannot be changed. For example, the availability domain, compartment, image, shape, and subnet cannot be changed when you create the instance.
    * Many of the settings for creating instance configurations are the same as the settings in the [create compute instance](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/launchinginstance.htm#top "Create a bare metal or virtual machine \(VM\) compute instance by using Compute service.") workflow. However, not all settings are available for instance configurations. For some settings, you can provide a value when you create an instance from the instance configuration.
    * For Linux instances: Using Secure Shell (SSH) keys with instance configurations:
      * If you add an SSH key when you create the instance configuration, that SSH key must be used to connect to all instances created from the instance configuration.
      * After you create the instance configuration, you cannot change the SSH key.
      * If you create an instance configuration without an SSH key, you can add an SSH key to individual instances created from the instance configuration.
      * If you use the instance configuration to create an instance pool, you should add an SSH key when you create the instance configuration.
  * When an instance pool creates instances in the pool based on an instance configuration, the pool's settings define the availability domain and subnet, regardless of the settings in the instance configuration.
  * If the instance configuration is associated with a [capacity reservation](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/reserve-capacity.htm#reserve-capacity), that reservation is automatically applied to any instances or instance pools created using that instance configuration. As long as sufficient capacity is available, when the instances launch, they use capacity from the associated reservation.


## Before You Begin 🔗 
If you're providing a list of configuration settings, prepare the following items:
  * Set up a virtual cloud network (VCN) in which to launch the instances that are created from the instance configuration. For information about setting up cloud networks, see [Networking](https://docs.oracle.com/iaas/Content/Network/Concepts/landing.htm).
  * (For Linux instances) If you want to use your own SSH key to connect using SSH to the instances that are created from the instance configuration, you need the public key from the SSH key pair that you plan to use. The key must be in OpenSSH format. For more information, see [Managing Key Pairs on Linux Instances](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/managingkeypairs.htm#Managing_Key_Pairs_on_Linux_Instances).
  * If you want to launch instances from the instance configuration by using a [host capacity type](https://docs.oracle.com/en-us/iaas/Content/Compute/Concepts/computeoverview.htm#capacity_types) other than on-demand capacity, prepare the capacity:
    * To launch an instance and have it count against a [capacity reservation](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/reserve-capacity.htm#reserve-capacity), you must have a capacity reservation in the same availability domain as the instance.
    * To place an instance on a [dedicated virtual machine host](https://docs.oracle.com/en-us/iaas/Content/Compute/Concepts/dedicatedvmhosts.htm#Dedicated_Virtual_Machine_Hosts), you must have a dedicated virtual machine host in the same availability domain and fault domain that you want to launch the instance in.
The capacity types are mutually exclusive.


If you want to attach block volumes to the instances that are created from the instance configuration, perform one of the following actions:
  * Prepare a [shareable volume that can be attached to multiple instances](https://docs.oracle.com/iaas/Content/Block/Tasks/attachingvolumetomultipleinstances.htm).
  * If the volume is attached to an existing instance but is not shareable, [create a backup of the volume](https://docs.oracle.com/iaas/Content/Block/Tasks/backingupavolume.htm). Then, include the boot volume backup in the instance configuration's settings.


  * [Console](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/creatinginstanceconfig.htm)
  * [CLI](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/creatinginstanceconfig.htm)
  * [API](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/creatinginstanceconfig.htm)


  * When you create an instance configuration, you can use an existing compute instance as a template, or you can provide a list of configuration settings.
#### Create an Instance Configuration Using an Existing Instance as a Template 🔗 
    1. Open the **navigation menu** and select **Compute**. Under **Compute** , select **Instances**. 
    2. Under **List scope** , select the compartment that contains the instance that you want to use as a template. 
    3. Click the name of the instance that you want to use as a template.
    4. Click **More Actions** , and then select **Create instance configuration**.
    5. Select the compartment that you want to create the instance configuration in.
    6. Specify a name for the instance configuration. It doesn't have to be unique, and you can change it later. Avoid entering confidential information.
    7. To add tags to the instance configuration, click **Show tagging options** and enter the tagging values. 
If you have permissions to create a resource, then you also have permissions to apply free-form tags to that resource. To apply a defined tag, you must have permissions to use the tag namespace. For more information about tagging, see [Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). If you're not sure whether to apply tags, skip this option or ask an administrator. You can apply tags later.
    8. To add Zero Trust Packet Routing Security Attributes to the instance configuration, click **Show security attributes** and enter your values. If you have permissions to create a resource, then you might also have permissions to apply security attributes to that resource. To apply a security attribute, you must have permissions to use the security attribute namespace. For more information about security attributes and security attribute namespaces, see [Zero Trust Packet Routing](https://docs.oracle.com/iaas/Content/zero-trust-packet-routing/home.htm). If you're not sure whether to apply security attributes, skip this option or ask an administrator. You can apply security attributes later.
    9. Click **Create instance configuration**.
#### Create an Instance Configuration by Providing a List of Settings 🔗 
    1. Open the navigation menu and click **Compute**. Under **Compute** , click **Instance Configurations**.
    2. Click **Create instance configuration**.
    3. Specify a name for the instance configuration. It doesn't have to be unique, and you can change it later. Avoid entering confidential information.
    4. Select the compartment that you want to create the instance configuration in.
    5. To add tags to the instance configuration, click **Show tagging options** and enter the tagging values. 
If you have permissions to create a resource, then you also have permissions to apply free-form tags to that resource. To apply a defined tag, you must have permissions to use the tag namespace. For more information about tagging, see [Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). If you're not sure whether to apply tags, skip this option or ask an administrator. You can apply tags later.
    6. In the **Compartment to create instances in** list, select the compartment where you want to place the instances that are created from this instance configuration.
    7. In the **Define Instance Details** , **Select an Image** , **Select a Shape** , and **Configure Primary VNIC** sections, specify the details for the instances that are created from this instance configuration.
For more information about the settings in these sections, see [Creating an Instance](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/launchinginstance.htm#top "Create a bare metal or virtual machine \(VM\) compute instance by using Compute service.").
    8. If you want to create a secondary VNIC to attach to the instances that are created from this instance configuration, in the **Networking** section, click **Create additional VNIC**. Then, specify the configuration details for the secondary VNIC.
For more information about the settings in this section, see [To create and attach a secondary VNIC](https://docs.oracle.com/iaas/Content/Network/Tasks/managingVNICs.htm#create_sec_vnic).
    9. (For Linux instances) In the **Add SSH keys** section, generate an SSH key pair or upload the public key for the instances that are created from this instance configuration.
**Important**
       * If you add an SSH key when you create the instance configuration, that SSH key must be used to connect to all instances created from the instance configuration.
       * After you create the instance configuration with an SSH key, you can't change the SSH key.
       * If you create an instance configuration without an SSH key, you can add an SSH key to individual instances created from the instance configuration.
       * If you use the instance configuration to create an instance pool, add the SSH key when you create the instance configuration.
For more information about the settings in this section, see [Creating an Instance](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/launchinginstance.htm#top "Create a bare metal or virtual machine \(VM\) compute instance by using Compute service."). For more information about SSH keys, see [Managing Key Pairs on Linux Instances](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/managingkeypairs.htm#Managing_Key_Pairs_on_Linux_Instances).
**Caution** Anyone who has access to the private key can connect to the instance. Store the private key in a secure location.
    10. Specify the **Boot volume** details for the instances that are created from this instance configuration.
For more information about the settings in this section, see [Creating an Instance](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/launchinginstance.htm#top "Create a bare metal or virtual machine \(VM\) compute instance by using Compute service.").
    11. If you want to attach block volumes to the instances that are created from this instance configuration, in the **Block volumes** section, click **Attach block volume**. Then, specify the configuration details for the block volume.
For more information about the settings in this section, see [Attaching a Volume](https://docs.oracle.com/iaas/Content/Block/Tasks/attachingavolume.htm).
    12. To configure advanced settings for the instances that are created from this instance configuration, such as the tags that are added to the instances, click **Show advanced options**. Then, specify the settings.
For more information about the settings in this section, see [Creating an Instance](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/launchinginstance.htm#top "Create a bare metal or virtual machine \(VM\) compute instance by using Compute service.").
    13. Click **Create**.
  * To create an instance configuration using the CLI, open a command prompt and run the [ instance-configuration create](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/compute-management/instance-configuration/create.html) command:
Command
CopyTry It
```
oci compute-management instance-configuration create --compartment-id <COMPARTMENT_OCID> --instance-details <file://path/to/file.json>
```

<file://path/to/file.json> is the path to a JSON file that defines the instance details. For information about how to generate an example of the JSON file, see [Advanced JSON Options](https://docs.oracle.com/iaas/Content/API/SDKDocs/cliusing.htm#AdvancedJSON).
For information about using the CLI, see [Command Line Interface (CLI)](https://docs.oracle.com/iaas/Content/API/Concepts/cliconcepts.htm).
  * For information about using the API and signing requests, see [REST API documentation](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm) and [Security Credentials](https://docs.oracle.com/iaas/Content/General/Concepts/credentials.htm). For information about SDKs, see [SDKs and the CLI](https://docs.oracle.com/iaas/Content/API/Concepts/sdks.htm).
Use the [CreateInstanceConfiguration](https://docs.oracle.com/iaas/api/#/en/iaas/latest/InstanceConfiguration/CreateInstanceConfiguration) operation to create an instance configuration.


Was this article helpful?
YesNo

