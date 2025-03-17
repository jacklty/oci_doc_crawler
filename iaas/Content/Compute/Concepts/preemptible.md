Updated 2025-02-11
# Preemptible Instances
Preemptible instances behave the same as regular compute instances, but the capacity is reclaimed when it's needed elsewhere, and the instances are terminated. If your workloads are fault-tolerant and can withstand interruptions, then preemptible instances can reduce your costs. For example, you can use preemptible instances to optimize costs for workloads that can tolerate interruptions, such as tests that can be stopped and resumed later.
## How Preemptible Instances Work 🔗 
Preemptible instances are designed for short-term usage. The capacity is reclaimed when it's needed elsewhere. The capacity is not guaranteed for a minimum amount of time, so instances can be reclaimed at any time. The benefit is that preemptible capacity [costs less than on-demand capacity](https://docs.oracle.com/en-us/iaas/Content/Compute/Concepts/preemptible.htm#howitworks__billing). Therefore, for workloads that can be interrupted, preemptible capacity can lower your costs.
### Using Preemptible Capacity 🔗 
To use preemptible capacity, follow the standard process for [creating an instance](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/launchinginstance.htm#top "Create a bare metal or virtual machine \(VM\) compute instance by using Compute service."), and for **Capacity type** , select **Preemptible capacity**.
When preemptible capacity is reclaimed, the instance is terminated. Use the Events service to [receive notifications](https://docs.oracle.com/en-us/iaas/Content/Compute/Concepts/preemptible.htm#howitworks__events) when this event occurs.
### Support and Limitations 🔗 
Preemptible instances have the following limitations and restrictions:
  * Preemptible instances can be terminated (deleted) at any time. As a result, they are not suitable for long-running workloads.
  * Preemptible capacity cannot be used with capacity reservations or with the dedicated virtual machine host feature.
  * Preemptible capacity does not support bare metal instances, burstable instances, or instances that have a minimum billing time.
  * When you [edit an instance](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/edit-instance.htm#edit-instance "You can edit the properties of a compute instance without having to rebuild the instance or redeploy your applications. When you edit an instance, the instance's OCID remains the same.") that uses preemptible capacity, only the name of the instance can be changed. You cannot change the shape of the instance after it is launched, and you cannot convert a preemptible instance to an on-demand instance.
  * After you create a preemptible instance, you cannot start, stop, or reboot the instance.
  * Preemptible instances do not support sending diagnostic interrupts.
  * Preemptible instances do not support confidential computing.
  * You cannot use preemptible instances to create [instance configurations](https://docs.oracle.com/en-us/iaas/Content/Compute/Concepts/instancemanagement.htm#config), and preemptible instances cannot be used in [instance pools](https://docs.oracle.com/en-us/iaas/Content/Compute/Concepts/instancemanagement.htm#Instance).
  * Preemptible instances do not support instance migration after infrastructure maintenance events. During maintenance events that impact the underlying infrastructure, the capacity is reclaimed, and the instance is terminated.
  * The standard [compute instance service limits](https://docs.oracle.com/iaas/Content/General/Concepts/servicelimits.htm#Compute_Instances) and compartment quotas apply to preemptible instances. If your request for compute instances will exceed your service limits, request a service limit increase before you create the instance. For more information, see [Service Limits](https://docs.oracle.com/iaas/Content/General/Concepts/servicelimits.htm).
  * Preemptible instances do not support [extended memory VM instances](https://docs.oracle.com/en-us/iaas/Content/Compute/References/extended-memory-vm-instances.htm#extended-memory-vm-instances "Extended memory virtual machine \(VM\) instances are VM instances that provide more memory and cores than available with standard shapes.").


### Supported Shapes 🔗 
The following shapes support preemptible instances.
  * VM.Standard1 series
  * VM.Standard.B1 series
  * VM.Standard2 series
  * VM.Standard3.Flex
  * VM.Standard.E2 series (the VM.Standard.E2.1.Micro series is not supported)
  * VM.Standard.E3.Flex
  * VM.Standard.E4.Flex
  * VM.Standard.E5.Flex
  * VM.Standard.A1.Flex
  * VM.DenseIO1 series
  * VM.DenseIO2 series
  * VM.GPU2 series
  * VM.GPU3 series
  * VM.Optimized3.Flex


### Billing and Cost Management 🔗 
Preemptible capacity costs 50% less than on-demand capacity in all regions.
  * To see the costs associated with your capacity usage, [view cost and usage reports](https://docs.oracle.com/iaas/Content/Billing/Concepts/costusagereportsoverview.htm) in the Console, or use the [cost analysis](https://docs.oracle.com/iaas/Content/Billing/Concepts/costanalysisoverview.htm) feature.
  * For more information about billing, see the Oracle Compute Cloud Services section of [Oracle PaaS and IaaS Universal Credits Service Descriptions](https://www.oracle.com/assets/paas-iaas-universal-credits-3940775.pdf).
  * For details about monitoring your costs, see [To monitor costs](https://docs.oracle.com/en-us/iaas/Content/Compute/Concepts/preemptible.htm#costs).


### Tracking Instance Preemption Events 🔗 
You can use the Events service to receive notifications when a preemptible instance is terminated. An `instancepreemptionaction` event is emitted two minutes before the instance termination begins. For details about instance preemption event types and an example event, see [Instance Event Types](https://docs.oracle.com/iaas/Content/Events/Reference/eventsproducers.htm#computeevents__compute_instance).
For background information about creating automation to track events and steps to create event notifications, see [Getting Started with Events](https://docs.oracle.com/iaas/Content/Events/Concepts/eventsgetstarted.htm).
To create an event notification for when a preemptible instance is terminated, when you [create the event rule](https://docs.oracle.com/iaas/Content/Events/Task/create-events-rule.htm), do the following:
  1. For **Condition** , select **Event Type**.
  2. For **Service Name** , select **Compute**.
  3. For **Event Type** , select **Instance - Preemption Action**.


You can also use the Events service to [invoke a function](https://docs.oracle.com/iaas/Content/Functions/Concepts/functionsoverview.htm) when a preemptible instance is terminated.
## Required IAM Policy 🔗 
The policies that let users create instances also allow them to create preemptible instances. For details, see [Required IAM Policy for Working with Instances](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/instances.htm#permissions).
## Tagging Resources 🔗 
Apply tags to resources to help organize them according to business needs. Apply tags at the time you create a resource, or update the resource later with the wanted tags. For general information about applying tags, see [Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm).
## Using the Console 🔗 
Use the Console to manage preemptible instances.
[To create a preemptible instance](https://docs.oracle.com/en-us/iaas/Content/Compute/Concepts/preemptible.htm)
  1. Perform the initial steps to [create an instance](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/launchinginstance.htm#top "Create a bare metal or virtual machine \(VM\) compute instance by using Compute service.").
  2. In the **Placement** section, click **Show advanced options**.
  3. For **Capacity type** , select **Preemptible capacity**.
  4. Choose whether to permanently delete the attached boot volume when the capacity is reclaimed.
  5. For **Image and shape** , choose a [shape](https://docs.oracle.com/en-us/iaas/Content/Compute/Concepts/preemptible.htm#howitworks__supported-preemptible-shapes) that supports preemptible instances.
  6. Finish creating your instance, and then click **Create**.


[To edit a preemptible instance](https://docs.oracle.com/en-us/iaas/Content/Compute/Concepts/preemptible.htm)
When you [edit an instance](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/edit-instance.htm#edit-instance "You can edit the properties of a compute instance without having to rebuild the instance or redeploy your applications. When you edit an instance, the instance's OCID remains the same.") that uses preemptible capacity, only the name of the instance can be changed. You cannot change the shape of the instance after it is launched, and you cannot convert a preemptible instance to an on-demand instance.
  1. Open the **navigation menu** and select **Compute**. Under **Compute** , select **Instances**.
  2. Click the instance that you're interested in.
  3. Select **More Actions** , and then select **Edit**.
  4. Enter a new name. Avoid entering confidential information.
  5. Click **Save Changes**.


[To stop a preemptible instance](https://docs.oracle.com/en-us/iaas/Content/Compute/Concepts/preemptible.htm)
Preemptible instances cannot be started, stopped, or rebooted.
[To terminate a preemptible instance](https://docs.oracle.com/en-us/iaas/Content/Compute/Concepts/preemptible.htm)
See [Terminating an Instance](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/terminatinginstance.htm#top "You can permanently delete \(terminate\) instances that you no longer need. Any attached VNICs and volumes are automatically detached when the instance terminates. Eventually, the instance's public and private IP addresses are released and become available for other instances.").
[To track instance preemption events](https://docs.oracle.com/en-us/iaas/Content/Compute/Concepts/preemptible.htm)
You can use the Events service to receive notifications when a preemptible instance is terminated. An `instancepreemptionaction` event is emitted two minutes before the instance termination begins. For details about instance preemption event types and an example event, see [Instance Event Types](https://docs.oracle.com/iaas/Content/Events/Reference/eventsproducers.htm#computeevents__compute_instance).
For background information about creating automation to track events and steps to create event notifications, see [Getting Started with Events](https://docs.oracle.com/iaas/Content/Events/Concepts/eventsgetstarted.htm).
To create an event notification for when a preemptible instance is terminated, when you [create the event rule](https://docs.oracle.com/iaas/Content/Events/Task/create-events-rule.htm), do the following:
  1. For **Condition** , select **Event Type**.
  2. For **Service Name** , select **Compute**.
  3. For **Event Type** , select **Instance - Preemption Action**.


You can also use the Events service to [invoke a function](https://docs.oracle.com/iaas/Content/Functions/Concepts/functionsoverview.htm) when a preemptible instance is terminated.
[To monitor costs](https://docs.oracle.com/en-us/iaas/Content/Compute/Concepts/preemptible.htm)
In the Console, you can access [cost and usage reports](https://docs.oracle.com/iaas/Content/Billing/Concepts/costusagereportsoverview.htm) to see the breakdown of costs for your preemptible instances, and you can use the [cost analysis](https://docs.oracle.com/iaas/Content/Billing/Concepts/costanalysisoverview.htm) feature to track and optimize your spending.
  * To view cost and usage reports: Open the **navigation menu** and select **Billing & Cost Management**. Under **Cost Management** , select **Cost and Usage Reports**. For more information, see [Accessing Cost and Usage Reports](https://docs.oracle.com/iaas/Content/Billing/Concepts/usagereportsoverview.htm#Accessing_Cost_and_Usage_Reports).
  * To view cost analysis: Open the **navigation menu** and select **Billing & Cost Management**. Under **Cost Management** , select **Cost Analysis**. For details instructions explaining how to work with the cost analysis tool, see [Cost Analysis Overview](https://docs.oracle.com/iaas/Content/Billing/Concepts/costanalysisoverview.htm).


In the cost and usage report, for preemptible instances, the description column includes the word **Preemptible**. The report shows the bill rate per hour for each resource. If the capacity is reclaimed in less than a minute, you are not charged for that time.
## Using the API 🔗 
For information about using the API and signing requests, see [REST API documentation](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm) and [Security Credentials](https://docs.oracle.com/iaas/Content/General/Concepts/credentials.htm). For information about SDKs, see [SDKs and the CLI](https://docs.oracle.com/iaas/Content/API/Concepts/sdks.htm).
Use these API operations to manage preemptible instances: 
  * [ListInstances](https://docs.oracle.com/iaas/api/#/en/iaas/latest/Instance/ListInstances)
  * [LaunchInstance](https://docs.oracle.com/iaas/api/#/en/iaas/latest/Instance/LaunchInstance)
  * [GetInstance](https://docs.oracle.com/iaas/api/#/en/iaas/latest/Instance/GetInstance)
  * [UpdateInstance](https://docs.oracle.com/iaas/api/#/en/iaas/latest/Instance/UpdateInstance)
  * [TerminateInstance](https://docs.oracle.com/iaas/api/#/en/iaas/latest/Instance/TerminateInstance)


Was this article helpful?
YesNo

