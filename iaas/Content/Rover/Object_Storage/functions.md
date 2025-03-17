Updated 2023-07-05
# Running Functions on Object Storage for Roving Edge Infrastructure
Describes how to assign a function to an object storage event for Roving Edge Infrastructure.
You can assign a function to an object storage event. For example, you can configure the function to update any bucket object, including the object that triggered the event. When triggered, the Events service attempts to call the function indefinitely until it succeeds. You can see pending events and the calls statistics in the Device Console. You can cancel any pending event.
  1. Launch the `orei-function-server-image-vi.oci` functions platform image as a virtual machine compute instance. See [Instances for Roving Edge Infrastructure Devices](https://docs.oracle.com/en-us/iaas/Content/Rover/Compute/Instance/instance_management.htm#ComputeInstanceManagement "Describes how to perform compute instance management tasks, including creating, updating, and deleting instances, on your Roving Edge Infrastructure devices.") for more information.
  2. Set up your functions within this instance.
  3. Follow the steps to begin creating an event. See [Creating an Events Rule](https://docs.oracle.com/en-us/iaas/Content/Rover/Events/create_rule.htm#top "Describes how to create an events rule on your Roving Edge Infrastructure device.") for more information.
  4. Provide a name and description for the function-based event.
  5. Configure the following in the **Rule Conditions** section of the Create Rule dialog box:
**Condition** : Select **Event Type** from the list.
**Service Name** : Select **Object Storage** from the list.
**Event Type** : Select **Object - Create** from the list.
**Rule Logic** : Enter the function.
  6. Click **+ Another Condition** to add another function-based condition entry, or any other type of condition.
  7. Complete the event rule creation.


Was this article helpful?
YesNo

