Updated 2025-02-13
# Capacity Reservations
Capacity reservations enable you to reserve instances in advance so that the capacity is available for your workloads when you need it. Capacity reservations provide the following benefits:
  * Assurance that you have the capacity necessary to manage your workload. Reserved capacity is available for your tenancy to consume at any time.
  * No size or time commitments. Create a reservation with as little or as much capacity as you need, and delete the reservation at any time to stop paying for it.


Capacity reservations are helpful in the following scenarios:
  * **Disaster recovery:** Ensure that capacity is available when you need to failover to your secondary location.
  * ****Unplanned growth** :** Reserve capacity as a buffer for unexpected workload spikes.
  * **Planned migrations and new launches:** When you have large capacity requirements for migrations or new project launches, capacity reservations ensure that you'll have the capacity that you need.
  * **Committed capacity for long-running projects:** When maintenance or seasonal adjustments cause your usage to vary, capacity reservations provide the needed capacity.


## How Reserved Capacity Works 🔗 
Capacity reservations allow you to reserve compute capacity in advance and use this capacity when you create instances against the reservation. There is no minimum time or size commitment. You can create, modify, and terminate your capacity reservation at any time. When instances that use the reserved capacity are terminated, the capacity is returned to the reservation, and the unused capacity in the reservation increases. Unused reserved capacity is metered differently than used reserved capacity. For more information, see the Oracle Compute Cloud Services section of [Oracle PaaS and IaaS Universal Credits Service Descriptions](https://www.oracle.com/assets/paas-iaas-universal-credits-3940775.pdf).
### Using Reservations 🔗 
When you create your capacity reservation, you specify the availability domain in the tenancy where you want to reserve capacity. You can then add a capacity configuration, which defines the amount of space that you want to reserve and the shape to use when creating instances against that capacity configuration. Optionally, you can specify the fault domain to reserve capacity in. Each capacity reservation can have multiple capacity configurations.
To use reserved capacity, specify the reservation ID when creating an instance. The instance being created must have the same availability domain, shape, and fault domain as one of the capacity configurations in the reservation.
As an advanced option, you can create [default reservations](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/reserve-capacity.htm#advanced), which allow you to configure your capacity reservation once for the availability domain within the root tenancy and use this reservation every time you create an instance in that availability domain and tenancy.
When instances that use reserved capacity are terminated, the capacity is returned to the reservation. When instances that use reserved capacity are stopped, the capacity is held by that instance for use when that instance is restarted.
Use instance pools to create multiple instances that use reserved capacity at the same time. In the Console, the reservation is automatically applied to the instance pool based on the instance configuration. In the API, specify the capacity reservation ID in the instance configuration for the pool. As long as sufficient capacity is available, the pool creates instances using capacity from the associated reservation. You can also use the pool to simultaneously stop, start, or terminate multiple instances that use capacity from the associated reservation.
### Support and Limitations 🔗 
Capacity reservations have the following limitations and restrictions:
  * When you create your capacity reservation, you specify the availability domain in the tenancy where you want to reserve capacity. Reservations are specific to that availability domain and tenancy. They cannot be shared between availability domains and tenancies, and they do not span entire regions and realms.
  * Capacity reservations cannot be moved from one availability domain to another, nor can they be moved from one tenancy to another.
  * Capacity reservations are not available with Free Tier accounts.
  * Capacity reservations are not available with confidential computing.
  * Capacity reservations cannot be used with preemptible instances or with the dedicated virtual machine host feature.
  * Capacity reservations do not support burstable instances.
  * Capacity is allocated when the reservation is created. If sufficient capacity isn't available to complete the request, the capacity reservation is created with as many instances as possible.
For example, if you request 50 instances and only 40 are available, a capacity reservation with 40 instances is created. If no capacity is available, a reservation with capacity for zero instances is made. If the requested shape does not exist in the region, the reservation is not made, and an error occurs. To see how much capacity is reserved, use the [GetComputeCapacityReservation](https://docs.oracle.com/iaas/api/#/en/iaas/latest/ComputeCapacityReservation/GetComputeCapacityReservation) operation.
  * Capacity reservations can have up to 50 capacity configurations. See the following known issue: [Creating more than 50 capacity configurations results in an internal error](https://docs.oracle.com/en-us/iaas/Content/Compute/known-issues.htm#capacity_reservation_error).
  * After you create a capacity configuration for a flexible shape, you cannot change the number of OCPUs or amount of memory assigned to the instances in that configuration. To include instances with a different number of OCPUs or amount of memory, create new capacity configurations in the reservation.
  * In order to move an instance that uses on-demand capacity into a capacity reservation, the reservation must contain a capacity configuration for that shape, and the capacity configuration must contain enough unused capacity to accommodate the instance. If the capacity configuration doesn't have sufficient capacity for the instance, [add capacity](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/reserve-capacity.htm#editcapacityconfiguration) before moving the instance into the reservation.
  * Service limits and compartment quotas apply to reserved capacity. If your request for reserved capacity will exceed your [service limits](https://docs.oracle.com/iaas/Content/General/Concepts/servicelimits.htm), request a service limit increase before you reserve the capacity. When viewing limits, quotas, and usage in the Console, **Reservable Cores** and **Reservable Memory** indicate the service limit. **Reserved Cores** and **Reserved Memory** indicate current usage. Capacity reservations have the following known issues with service limits: [No service category for capacity reservations when requesting service limit increases](https://docs.oracle.com/en-us/iaas/Content/Compute/known-issues.htm#servicecategor_capacityreservations) and [Capacity reservation service limits are inaccurate](https://docs.oracle.com/en-us/iaas/Content/Compute/known-issues.htm#capacityreservationlimits).
  * For [shielded instances](https://docs.oracle.com/en-us/iaas/Content/Compute/References/shielded-instances.htm#shielded) and instances with [Windows Defender Credential Guard](https://docs.oracle.com/en-us/iaas/Content/Compute/References/shielded-instances.htm#credential-guard): When creating the instance, if there is no available host in the [availability domain](https://docs.oracle.com/iaas/Content/General/Concepts/regions.htm#About) that is compatible with shielded instances or Credential Guard, the create operation will not be successful. You can try a different availability domain, wait and try the operation later, or try again without enabling the shielded instance or Credential Guard feature.
  * Capacity reservations are not available with [extended memory VM instances](https://docs.oracle.com/en-us/iaas/Content/Compute/References/extended-memory-vm-instances.htm#extended-memory-vm-instances "Extended memory virtual machine \(VM\) instances are VM instances that provide more memory and cores than available with standard shapes.").


### Billing and Cost Management 🔗 
When you create a reservation, you are immediately charged for the reserved resources. When you no longer need a reservation, delete the reservation to stop incurring charges. Because reservations consume resources, reserved capacity incurs charges even when the capacity is unused. Unused reserved capacity is metered differently than used reserved capacity. 
  * To see the costs associated with your capacity reservation, [view cost and usage reports](https://docs.oracle.com/iaas/Content/Billing/Concepts/costusagereportsoverview.htm) in the Console.
  * For more information about billing, see the Oracle Compute Cloud Services section of [Oracle PaaS and IaaS Universal Credits Service Descriptions](https://www.oracle.com/assets/paas-iaas-universal-credits-3940775.pdf).
  * For details about monitoring your costs, see [To monitor costs](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/reserve-capacity.htm#costandusage).


## Required IAM Policy 🔗 
To use Oracle Cloud Infrastructure, an administrator must be a member of a group granted security access in a **policy** by a tenancy administrator. This access is required whether you're using the Console or the REST API with an SDK, CLI, or other tool. If you get a message that you don't have permission or are unauthorized, verify with the tenancy administrator what type of access you have and which **compartment** your access works in.
For administrators: The following examples shows typical policies that gives access to capacity reservations. Create the policy in the tenancy so that the access is easily granted to all compartments by way of [policy inheritance](https://docs.oracle.com/iaas/Content/Identity/Concepts/policies.htm#Policy2). To reduce the scope of access to just the autoscaling configurations in a particular compartment, specify that compartment instead of the tenancy.
**Type of access:** Ability to create an instance in a reservation.
Copy
```
Allow group <group_name> to use compute-capacity-reservations in tenancy

```

**Type of access:** Ability to manage capacity reservations.
Copy
```
Allow group <group_name> to manage compute-capacity-reservations in tenancy

```

## Tagging Resources 🔗 
Apply tags to resources to help organize them according to business needs. Apply tags at the time you create a resource, or update the resource later with the wanted tags. For general information about applying tags, see [Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm).
## Advanced Options 🔗 
In addition to the standard capacity reservation features, advanced configuration options are available, such as default capacity reservations.
### Default Capacity Reservations 🔗 
With default reservations, you can configure your capacity reservation once and use this reservation every time you create an instance in the availability domain and tenancy associated with the default reservation. To create a default reservation, when you create the capacity reservation, select the option to use this reservation as the default reservation. After you create the default reservation, all instances created in that availability domain and tenancy use capacity from this reservation if possible.
Sometimes the instance cannot be created using capacity from the default reservation. For example, the reservation might not have sufficient capacity, or the user might not have permission to use the reservation. In those situations, the instance is created using [on-demand capacity](https://docs.oracle.com/en-us/iaas/Content/Compute/Concepts/computeoverview.htm#capacity_types).
#### Requirements
To use default reservations:
  * The default capacity reservation must be in the root compartment.
  * You can only have one default reservation in each availability domain.
  * You must grant users who create instances permission to use this reservation. For more information, see [Required IAM Policy](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/reserve-capacity.htm#reservecapacity_topic-required_iam_policy).


## Using the Console 🔗 
Use the Console to manage capacity reservations and capacity configurations. Capacity reservations can have multiple capacity configurations within them.
### Managing Capacity Reservations 🔗 
In the Console, you can create and edit capacity reservations, create and stop instances in a capacity reservation, and move instances in and out of capacity reservations.
[To create a capacity reservation](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/reserve-capacity.htm)
For large capacity reservations, [contact support](https://docs.oracle.com/iaas/Content/GSG/Tasks/contactingsupport.htm). For smaller capacity reservations, follow these steps.
Capacity is allocated when the reservation is created. If sufficient capacity isn't available to complete the request, the capacity reservation is created with as many instances as possible. For example, if you request 50 instances and only 40 are available, a capacity reservation with 40 instances is created. If no capacity is available, a reservation with capacity for zero instances is made. If the requested shape does not exist in the region, the reservation is not made, and an error occurs.
To see how much capacity is reserved, after the reservation request completes, [view capacity usage](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/reserve-capacity.htm#viewcapacityusage) in the Console or use the [GetComputeCapacityReservation](https://docs.oracle.com/iaas/api/#/en/iaas/latest/ComputeCapacityReservation/GetComputeCapacityReservation) operation. To know when the capacity reservation request is complete, use [work requests](https://docs.oracle.com/iaas/Content/General/Concepts/workrequestoverview.htm).
  1. Open the **navigation menu** and select **Compute**. Under **Compute** , select **Capacity Reservations**.
  2. Click **Create capacity reservation**.
  3. On the **Add basic details** page, do the following:
    1. Enter a name for the capacity reservation. Avoid entering confidential information.
    2. Select the compartment for the reservation and all instances created with this reservation.
    3. For **Availability domain** , select the availability domain for the reservation and all instances created with this reservation.
    4. To make this the default reservation, select the **Make this capacity reservation the default for this availability domain** check box. If selected, when an instance is created in this availability domain, it counts against this reservation, regardless of which compartment the instance is in. If a different capacity reservation is already set as the default in this availability domain, this capacity reservation replaces it as the default.
    5. Click **Next**.
  4. On the **Add capacity configurations** page, create one or more capacity configurations. Do the following:
    1. For **Fault domain** , enter a fault domain. Alternately, you can select **First available** instead of a specific fault domain.
    2. For **Shape** , select the shape to use for instances created against this capacity configuration. If you select a flexible shape, enter values for **Cores** and **Memory (GB)**.
    3. For **Count** , enter the total number of instances that can be created with this capacity configuration.
    4. Optionally, to add capacity configurations for more shapes, click **+ Another shape** , and then repeat the previous steps. To remove a row, click the **Remove row (X)** button.
    5. Click **Next**.
  5. Review the capacity reservation and capacity configuration information, and then click **Create**.


[To create instances in a capacity reservation](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/reserve-capacity.htm)
  1. Follow the steps to [create an instance](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/launchinginstance.htm#top "Create a bare metal or virtual machine \(VM\) compute instance by using Compute service."), until the **Placement** section.
  2. In the **Placement** section, click **Show advanced options**.
  3. For **Capacity type** , select **Capacity reservation**.
  4. For **Capacity reservation** , select the capacity reservation that you want to create the instance in.
  5. Finish configuring the instance, and then click **Create**.


[To stop instances in a capacity reservation](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/reserve-capacity.htm)
See [Stopping, Starting, or Restarting an Instance](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/restartinginstance.htm#top "You can stop, start, or restart an instance as needed to update software or resolve error conditions.").
[To move instances into a capacity reservation](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/reserve-capacity.htm)
  1. Open the **navigation menu** and select **Compute**. Under **Compute** , select **Instances**.
  2. Click the instance that you're interested in.
  3. Select **More Actions** , and then select **Edit**.
  4. Click **Show advanced options** , and then select the **Placement** tab.
  5. Select the **Apply a capacity reservation** check box.
  6. For **Capacity reservation** , select the capacity reservation that you want to move the instance into.
  7. Click **Save changes**.


[To move instances out of a capacity reservation](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/reserve-capacity.htm)
  1. Open the **navigation menu** and select **Compute**. Under **Compute** , select **Instances**.
  2. Click the instance that you're interested in.
  3. Select **More Actions** , and then select **Edit**.
  4. Click **Show advanced options** , and then select the **Placement** tab.
  5. Clear the **Apply a capacity reservation** check box.
  6. Click **Save changes**.


[To edit a capacity reservation](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/reserve-capacity.htm)
You can change the name of the capacity reservation. If the capacity reservation is in the root compartment for the tenancy, you can decide whether the reservation should be the default reservation.
  1. Open the **navigation menu** and select **Compute**. Under **Compute** , select **Capacity Reservations**.
  2. Click the capacity reservation that you're interested in.
  3. Click **Edit**.
  4. Optionally, edit the name. Avoid entering confidential information.
  5. Select or clear the **Make this reservation the default for this availability domain** check box.
  6. Click **Save changes**.


[To delete a capacity reservation](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/reserve-capacity.htm)
  1. Either [terminate (delete) all the instances](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/terminatinginstance.htm#top "You can permanently delete \(terminate\) instances that you no longer need. Any attached VNICs and volumes are automatically detached when the instance terminates. Eventually, the instance's public and private IP addresses are released and become available for other instances.") in the capacity reservation, or [move the instances out of the capacity configuration](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/reserve-capacity.htm#move_instances_out_of_a_capacity_reservation).
  2. Open the **navigation menu** and select **Compute**. Under **Compute** , select **Capacity Reservations**.
  3. Click the capacity reservation that you're interested in.
  4. Click **Delete** , and then confirm when prompted.


### Managing Capacity Configurations 🔗 
You can add and edit capacity configurations in the Console. Each capacity configuration must be unique within the reservation. Multiple configurations with the same fault domain and instance shape are not allowed.
[To add a capacity configuration](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/reserve-capacity.htm)
  1. Open the **navigation menu** and select **Compute**. Under **Compute** , select **Capacity Reservations**.
  2. Click the capacity reservation that you're interested in.
  3. Click **Add capacity configuration**.
  4. For **Fault domain** , enter a fault domain. Alternately, you can select **First available** instead of a specific fault domain.
  5. For **Shape** , select the shape to use for instances created against this capacity configuration. If you select a flexible shape, enter values for **Cores** and **Memory (GB)**.
  6. For **Count** , enter the number of instances that can be created with this capacity configuration.
  7. Optionally, to add capacity configurations for more shapes, click **+ Another shape** , and then repeat the previous steps. To remove a row, click the **Remove row (X)** button.
  8. Click **Add configuration**.


[To edit a capacity configuration](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/reserve-capacity.htm)
You can edit the number of instances that can be created with a capacity configuration. To reserve capacity for different fault domains or shapes, add a new capacity configuration.
  1. Open the **navigation menu** and select **Compute**. Under **Compute** , select **Capacity Reservations**.
  2. Click the capacity reservation that you're interested in.
  3. On the Actions menu (![Actions Menu](https://docs.oracle.com/en-us/iaas/Content/libraries/global-images/actions-menu.png)) for the capacity configuration that you want to edit, click **Edit**.
  4. For **Count** , enter a new value. The value must be greater than or equal to the number of instances currently created in this configuration.
  5. Click **Save changes**.


[To delete a capacity configuration and release capacity](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/reserve-capacity.htm)
  1. Either [terminate (delete) all the instances](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/terminatinginstance.htm#top "You can permanently delete \(terminate\) instances that you no longer need. Any attached VNICs and volumes are automatically detached when the instance terminates. Eventually, the instance's public and private IP addresses are released and become available for other instances.") in the capacity configuration, or [move the instances out of the capacity configuration](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/reserve-capacity.htm#move_instances_out_of_a_capacity_reservation).
  2. Open the **navigation menu** and select **Compute**. Under **Compute** , select **Capacity Reservations**.
  3. Click the capacity reservation that you're interested in.
  4. On the Actions menu (![Actions Menu](https://docs.oracle.com/en-us/iaas/Content/libraries/global-images/actions-menu.png)) for the capacity configuration that you want to delete, click **Delete configuration**. Confirm when prompted.
The capacity configuration is deleted and the associated capacity is released from the reservation.


### Monitoring Capacity Reservations 🔗 
Monitor capacity usage and see the costs associated with your capacity reservation.
[To view capacity usage](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/reserve-capacity.htm)
  1. Open the **navigation menu** and select **Compute**. Under **Compute** , select **Capacity Reservations**.
  2. Click the capacity reservation that you're interested in.
  3. In the **Capacity configurations** section, you can see the total reserved capacity and the total used capacity for each configuration.
  4. (Optional) To see the instances that are created in the capacity reservation, under **Resources** , click **Created instances**.


[To monitor costs](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/reserve-capacity.htm)
In the Console, you can access [cost and usage reports](https://docs.oracle.com/iaas/Content/Billing/Concepts/costusagereportsoverview.htm) to see the breakdown of costs for your capacity reservation, and you can use the [cost analysis](https://docs.oracle.com/iaas/Content/Billing/Concepts/costanalysisoverview.htm) feature to track and optimize your spending.
  * To view cost and usage reports: Open the **navigation menu** and select **Billing & Cost Management**. Under **Cost Management** , select **Cost and Usage Reports**. For more information, see [Accessing Cost and Usage Reports](https://docs.oracle.com/iaas/Content/Billing/Concepts/usagereportsoverview.htm#Accessing_Cost_and_Usage_Reports).
  * To view cost analysis: Open the **navigation menu** and select **Billing & Cost Management**. Under **Cost Management** , select **Cost Analysis**. For details instructions explaining how to work with the cost analysis tool, see [Cost Analysis Overview](https://docs.oracle.com/iaas/Content/Billing/Concepts/costanalysisoverview.htm).


In the cost and usage report, for capacity reservations, the _product/Description_ column includes the words **Capacity Reservation**. If no capacity remains in the reservation because instances have been created against all of the reserved capacity, the cost for the capacity reservation is zero. Instances are billed at the standard rate for the given shape.
The report shows the bill rate per hour for each resource. Resources are aggregated by the number of cores.
  * Unused reserved capacity is billed at 85%. Instances created against a capacity reservation are billed at 100%.
  * If you create an instance against a capacity reservation thirty minutes into the hour, you're billed at the reserved capacity rate for the first half of the hour and at the standard rate for the second half of the hour. These rates appear as separate line items.
  * When an instance is created from reserved capacity at the beginning of an hour for the whole hour, the instance is billed at the standard rate for the full hour.


For example, you have a capacity reservation with capacity for a single instance that uses one core. Fifteen minutes into the hour, you create an instance against that reservation. The cost and usage report has two lines for this reservation:
  * The first line shows reserved capacity billed at 85% for 15 minutes. The number in the _usage/billedQuantity_ column is calculated by multiplying 85% by ¼ of an hour and the number of cores.
  * The second line shows a standard instance billed at 100% for 45 minutes. The number in the _usage/billedQuantity_ column is calculated by multiplying 100% by ¾ of an hour and the number of cores.


In the cost analysis report, the bar chart shows costs associated with capacity reservations. The legend indicates which bars represent capacity reservations. If no capacity remains in the reservation because instances have been created against all of the reserved capacity, the cost for the capacity reservation is zero. Instances are billed at the standard rate for the given shape and are grouped with standard instances in the chart.
## Using the API 🔗 
For information about using the API and signing requests, see [REST API documentation](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm) and [Security Credentials](https://docs.oracle.com/iaas/Content/General/Concepts/credentials.htm). For information about SDKs, see [SDKs and the CLI](https://docs.oracle.com/iaas/Content/API/Concepts/sdks.htm).
Use these API operations to manage capacity reservations: 
  * [ListComputeCapacityReservations](https://docs.oracle.com/iaas/api/#/en/iaas/latest/ComputeCapacityReservation/ListComputeCapacityReservations)
  * [ListComputeCapacityReservationInstances](https://docs.oracle.com/iaas/api/#/en/iaas/latest/CapacityReservationInstanceSummary/ListComputeCapacityReservationInstances)
  * [ListComputeCapacityReservationInstanceShapes](https://docs.oracle.com/iaas/api/#/en/iaas/latest/ComputeCapacityReservationInstanceShapeSummary/ListComputeCapacityReservationInstanceShapes)
  * [CreateComputeCapacityReservation](https://docs.oracle.com/iaas/api/#/en/iaas/latest/ComputeCapacityReservation/CreateComputeCapacityReservation)
  * [GetComputeCapacityReservation](https://docs.oracle.com/iaas/api/#/en/iaas/latest/ComputeCapacityReservation/GetComputeCapacityReservation)
  * [UpdateComputeCapacityReservation](https://docs.oracle.com/iaas/api/#/en/iaas/latest/ComputeCapacityReservation/UpdateComputeCapacityReservation)
  * [ChangeComputeCapacityReservationCompartment](https://docs.oracle.com/iaas/api/#/en/iaas/latest/ComputeCapacityReservation/ChangeComputeCapacityReservationCompartment)
  * [DeleteComputeCapacityReservation](https://docs.oracle.com/iaas/api/#/en/iaas/latest/ComputeCapacityReservation/DeleteComputeCapacityReservation)
**Note** To delete a capacity reservation, you must first terminate all the instances in the capacity reservation or move the instances out of the capacity configuration.


## Known Issues 🔗 
  * [Creating more than 50 capacity configurations results in an internal error](https://docs.oracle.com/en-us/iaas/Content/Compute/known-issues.htm#capacity_reservation_error)
  * [No service category for capacity reservations when requesting service limit increases](https://docs.oracle.com/en-us/iaas/Content/Compute/known-issues.htm#servicecategor_capacityreservations)
  * [Capacity reservation service limits are inaccurate](https://docs.oracle.com/en-us/iaas/Content/Compute/known-issues.htm#capacityreservationlimits)


Was this article helpful?
YesNo

