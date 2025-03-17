Updated 2025-02-13
# Working with Instances
Oracle Cloud Infrastructure Compute lets you provision and manage compute hosts, known as instances. You can create instances as needed to meet your compute and application requirements. After you create an instance, you can access it securely from your computer, restart it, attach and detach volumes, and terminate it when you're done with it.
  * [Creating an Instance](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/launchinginstance.htm#top "Create a bare metal or virtual machine \(VM\) compute instance by using Compute service."): Follow the steps in this topic to create a bare metal or virtual machine (VM) compute instance.
    * Instances launched using Oracle Linux, CentOS, or Ubuntu images use an SSH key pair instead of a password to authenticate a remote user. Therefore, to connect to an instance, you might need to [create an SSH key pair](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/managingkeypairs.htm#Managing_Key_Pairs_on_Linux_Instances).
    * You can create [burstable instances](https://docs.oracle.com/en-us/iaas/Content/Compute/References/burstable-instances.htm#burstable-instances), [shielded instances](https://docs.oracle.com/en-us/iaas/Content/Compute/References/shielded-instances.htm#shielded), and [confidential instances](https://docs.oracle.com/en-us/iaas/Content/Compute/References/confidential_compute.htm#confidential_compute "Confidential computing encrypts and isolates in-use data and the applications processing that data.").
    * You can configure your instances to use different [capacity types](https://docs.oracle.com/en-us/iaas/Content/Compute/Concepts/capacity-types.htm#capacity_types).
    * You can add extended memory and cores to instances with [extended memory VM instances](https://docs.oracle.com/en-us/iaas/Content/Compute/References/extended-memory-vm-instances.htm#extended-memory-vm-instances "Extended memory virtual machine \(VM\) instances are VM instances that provide more memory and cores than available with standard shapes.").
  * [Connecting to an Instance](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/accessinginstance.htm#top "You can connect to a running compute instance by using a Secure Shell \(SSH\) or Remote Desktop connection."): You can connect to a running instance by using a Secure Shell (SSH) or Remote Desktop connection.
  * [Editing an Instance](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/edit-instance.htm#edit-instance "You can edit the properties of a compute instance without having to rebuild the instance or redeploy your applications. When you edit an instance, the instance's OCID remains the same."): You can edit the properties of a compute instance without having to rebuild the instance or redeploy your applications.
  * [Stopping, Starting, or Restarting an Instance](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/restartinginstance.htm#top "You can stop, start, or restart an instance as needed to update software or resolve error conditions."): You can stop and start an instance as needed to update software or resolve error conditions.
  * [Replacing a Boot Volume](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/replacingbootvolume.htm#enter-topic-id "You can automatically replace the boot volume of an instance without terminating and recreating the instance. The instance stops, replaces the boot volume, and returns the instance to the state prior to the volume replacement process. This feature allows the replacement of boot volumes if an issue is detected or an upgrade is needed to implement new features."): You can automatically replace the boot volume of an instance without terminating and recreating the instance. 
  * [Setting Up Contextual Notifications for an Instance](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/contextual-notifications-compute.htm#top "You can get messages when something happens with a compute instance. Use contextual notifications in the Console to create event rules and alarms for an instance. Quick start templates are available."): You can get messages when something happens with a compute instance.
  * [Adding Users to an Instance](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/addingusers.htm#Adding_Users_on_an_Instance): You can add users to a compute instance.
  * [Running Commands on an Instance](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/runningcommands.htm#runningcommands): You can remotely configure, manage, and troubleshoot compute instances by running scripts within the instance using the run command feature.
  * [Disabling Simultaneous Multithreading](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/disablesmt.htm#disablesmt "You can disable simultaneous multithreading \(SMT\) on your instances through the console or by using CLI commands."): You can disable simultaneous multithreading (SMT) on your instances through the console or by using CLI commands.
  * [Getting Instance Metadata](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/gettingmetadata.htm#Getting_Instance_Metadata): The instance metadata service (IMDS) provides information about a running instance, including details about the instance, its attached virtual network interface cards (VNICs), its attached multipath-enabled volume attachments, and any custom metadata that you define. IMDS also provides information to cloud-init that you can use for various system initialization tasks.
  * [Updating Instance Metadata](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/updatinginstancemetada.htm#Updating_Instance_Metadata): You can add and update custom metadata for a compute instance using the CLI or REST APIs.
  * [Moving a Compute Instance to a New Host](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/movinganinstance.htm#Moving_a_Compute_Instance_to_a_New_Host): You can relocate instances using [reboot migration](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/movinganinstance.htm#reboot) or a [manual process](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/movinganinstance.htm#manual).
  * [Terminating an Instance](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/terminatinginstance.htm#top "You can permanently delete \(terminate\) instances that you no longer need. Any attached VNICs and volumes are automatically detached when the instance terminates. Eventually, the instance's public and private IP addresses are released and become available for other instances."): You can permanently delete (terminate) instances that you no longer need. Any attached VNICs and volumes are automatically detached when the instance terminates.


## Managing Tags for an Instance 🔗 
Apply tags to resources to help organize them according to business needs. Apply tags at the time you create a resource, or update the resource later with the wanted tags. For general information about applying tags, see [Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm).
To manage tags for an instance:
  1. Open the **navigation menu** and select **Compute**. Under **Compute** , select **Instances**.
  2. Click the instance that you're interested in.
  3. Click the **Tags** tab to view or edit the existing tags. Or click **More Actions** , and then click **Add tags** to add new ones.


## Security Zones 🔗 
[Security Zones](https://docs.oracle.com/iaas/security-zone/home.htm) ensure that your cloud resources comply with Oracle security principles. If any operation on a resource in a security zone compartment violates a [policy for that security zone](https://docs.oracle.com/iaas/security-zone/using/security-zone-policies.htm), then the operation is denied.
The following security zone policies affect the ability to create instances:
  * The boot volume for a compute instance in a security zone must also be in the same security zone.
  * A compute instance that isn't in a security zone can't use a boot volume that is in a security zone.
  * A compute instance in a security zone must use subnets that are also in the same security zone.
  * All compute instances in a security zone must be created using [platform images](https://docs.oracle.com/en-us/iaas/Content/Compute/References/images.htm#OracleProvided_Images). You can't create a compute instance from a custom image in a security zone.


**Important** Failing to implement one of the listed security zone policies might prevent the creation of an instance.
## Required IAM Policy for Working with Instances 🔗 
To use Oracle Cloud Infrastructure, an administrator must be a member of a group granted security access in a **policy** by a tenancy administrator. This access is required whether you're using the Console or the REST API with an SDK, CLI, or other tool. If you get a message that you don't have permission or are unauthorized, verify with the tenancy administrator what type of access you have and which **compartment** your access works in.
**Tip** When you create an instance, several other resources are involved, such as an image, a cloud network, and a subnet. Those other resources can be in the same **compartment** with the instance or in other compartments. You must have the required level of access to each of the compartments involved in order to launch the instance. This is also true when you attach a volume to an instance; they don't have to be in the same compartment, but if they're not, you need the required level of access to each of the compartments. 
For administrators: The simplest policy to let users [create](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/launchinginstance.htm#top "Create a bare metal or virtual machine \(VM\) compute instance by using Compute service."), [edit](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/edit-instance.htm#edit-instance "You can edit the properties of a compute instance without having to rebuild the instance or redeploy your applications. When you edit an instance, the instance's OCID remains the same."), and [terminate (delete)](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/terminatinginstance.htm#top "You can permanently delete \(terminate\) instances that you no longer need. Any attached VNICs and volumes are automatically detached when the instance terminates. Eventually, the instance's public and private IP addresses are released and become available for other instances.") instances is listed in [Let users launch compute instances](https://docs.oracle.com/iaas/Content/Identity/Concepts/commonpolicies.htm#launch-instances). It gives the specified group general access to manage instances and images, along with the required level of access to attach existing block volumes to the instances. If the specified group doesn't need to launch instances or attach volumes, you could simplify that policy to include only `manage instance-family`, and remove the statements involving `volume-family` and `virtual-network-family`.
If the group needs to _create_ block volumes, they'll need the ability to _manage_ block volumes. See [Let volume admins manage block volumes, backups, and volume groups](https://docs.oracle.com/iaas/Content/Identity/Concepts/commonpolicies.htm#volume-admins-manage-volumes-and-backups).
If the group needs access to community images specifically, they'll need the ability to _read_ community images. See [Publishing Community Applications](https://docs.oracle.com/iaas/Content/Marketplace/Tasks/publishingcommunityapplications.htm).
If you're new to policies, see [Managing Identity Domains](https://docs.oracle.com/iaas/Content/Identity/domains/overview.htm) and [Common Policies](https://docs.oracle.com/iaas/Content/Identity/Concepts/commonpolicies.htm). For reference material about writing policies for instances, cloud networks, or other Core Services API resources, see [Details for Core Services](https://docs.oracle.com/iaas/Content/Identity/Reference/corepolicyreference.htm). 
Some Compute tasks require additional policies, as described in the following sections.
### Partner Image Catalog 🔗 
If the group needs to create instances based on partner images, they'll need the _manage_ permission for app-catalog-listing to create subscriptions to images from the Partner Image catalog. See [Let users list and subscribe to images from the Partner Image catalog ](https://docs.oracle.com/iaas/Content/Identity/Concepts/commonpolicies.htm#subscribe-catalog).
### SSH and Remote Desktop Access 🔗 
For users: To [connect to a running instance](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/accessinginstance.htm#top "You can connect to a running compute instance by using a Secure Shell \(SSH\) or Remote Desktop connection.") with a Secure Shell (SSH) or Remote Desktop connection, you don't need an IAM policy to grant you access. However, you do need the public IP address of the instance.
For administrators: If there's a policy that lets users launch an instance, that policy probably also lets users get the instance's IP address. The simplest policy that does both is listed in [Let users launch compute instances](https://docs.oracle.com/iaas/Content/Identity/Concepts/commonpolicies.htm#launch-instances).
Here's a more restrictive policy that lets the specified group get the IP address of existing instances and use power actions on the instances (for example, stop or start the instance), but not launch or terminate instances. The policy assumes the instances and the cloud network are together in a single compartment (XYZ).
Copy
```
Allow group InstanceUsers to read virtual-network-family in compartment XYZ
Allow group InstanceUsers to use instance-family in compartment XYZ
```

### Before You Begin 🔗 
For administrators: To set up contextual notifications for an instance, use the following policy.
Copy
```
allow group ContextualNotificationsUsers to manage alarms in tenancy
allow group ContextualNotificationsUsers to read metrics in tenancy
allow group ContextualNotificationsUsers to manage ons-topics in tenancy
allow group ContextualNotificationsUsers to manage cloudevents-rules in tenancy
```

### Instance Metadata Service (IMDS) 🔗 
For users: No IAM policy is required if you're logged in to the instance and using cURL to [get the instance metadata](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/gettingmetadata.htm#Getting_Instance_Metadata).
For administrators: Users can also get instance metadata through the Compute API (for example, with [GetInstance](https://docs.oracle.com/iaas/api/#/en/iaas/latest/Instance/GetInstance)). The policy in [Let users launch compute instances](https://docs.oracle.com/iaas/Content/Identity/Concepts/commonpolicies.htm#launch-instances) covers that ability.
To require that [legacy IMDSv1 endpoints are disabled](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/gettingmetadata.htm#upgrading-v2) on any new instances that are created, use the following policy:
Copy
```
Allow group InstanceLaunchers to manage instances in compartment ABC
 where request.instanceOptions.areLegacyEndpointsDisabled= 'true'
```

### Capacity Reservations 🔗 
For administrators: The following examples show typical policies that give access to [capacity reservations](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/reserve-capacity.htm#reserve-capacity). Create the policy in the tenancy so that the access is easily granted to all compartments by way of [policy inheritance](https://docs.oracle.com/iaas/Content/Identity/Concepts/policies.htm#Policy2). To reduce the scope of access to just the capacity reservations in a particular compartment, specify that compartment instead of the tenancy.
**Type of access:** Ability to launch an instance in a reservation.
Copy
```
Allow group InstanceLaunchers to use compute-capacity-reservations in tenancy

```

**Type of access:** Ability to manage capacity reservations.
Copy
```
Allow group InstanceLaunchers to manage compute-capacity-reservations in tenancy

```

### Run Command 🔗 
For administrators: To write policy for the [run command feature](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/runningcommands.htm#runningcommands), do the following:
  1. [Create a group](https://docs.oracle.com/iaas/Content/Identity/Tasks/managinggroups.htm) that includes the users who you want to allow to issue commands, cancel commands, and view the command output for the instances in a compartment. Then, write the following policy to grant access for the group:
Copy
```
Allow group RunCommandUsers to manage instance-agent-command-family in compartment ABC
```

  2. [Create a dynamic group](https://docs.oracle.com/iaas/Content/Identity/Tasks/managingdynamicgroups.htm) that includes the instances that you want to allow commands to run on. For example, a rule inside the dynamic group can state:
Copy
```
any { instance.id = 'ocid1.instance.oc1.phx.<unique_ID_1>', 'ocid1.instance.oc1.phx.<unique_ID_2>' }
```

  3. Write the following policy to grant access for the dynamic group:
**Note** If you create an instance and then add it to a dynamic group, it takes up to 30 minutes for the instance to start to poll for commands. If you create the dynamic group first and then create the instance, the instance starts to poll for commands as soon as the instance is created.
Copy
```
Allow dynamic-group RunCommandDynamicGroup to use instance-agent-command-execution-family in compartment ABC where request.instance.id=target.instance.id
```

  4. To allow the dynamic group to access the script file from an Object Storage bucket and save the response to an Object Storage bucket, write the following policies:
Copy
```
Allow dynamic-group RunCommandDynamicGroup to read objects in compartment ABC where all {target.bucket.name = '<bucket_with_script_file>'}
Allow dynamic-group RunCommandDynamicGroup to manage objects in compartment ABC where all {target.bucket.name = '<bucket_for_command_output>'}
```



Was this article helpful?
YesNo

