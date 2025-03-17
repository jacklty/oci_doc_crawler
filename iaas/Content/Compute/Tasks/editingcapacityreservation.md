Updated 2025-01-13
# Changing the Capacity Reservation for an Instance
You can move instances into or out of [capacity reservations](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/reserve-capacity.htm#reserve-capacity) without having to rebuild your instances. Capacity reservations let you reserve instances in advance so that the capacity is available for your workloads when you need it.
For permissions, see [Required IAM Policy for Working with Instances](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/instances.htm#permissions).
## Before You Begin 🔗 
To move an instance into a capacity reservation, you must have an existing capacity reservation. For steps to create capacity reservations, see [Capacity Reservations](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/reserve-capacity.htm#reserve-capacity).
## Using the Console 🔗 
You can use the Console to move instance into or out of capacity reservations.
### To move instances into a capacity reservation 🔗 
  1. Open the **navigation menu** and select **Compute**. Under **Compute** , select **Instances**.
  2. Click the instance that you're interested in.
  3. Select **More Actions** , and then select **Edit**.
  4. Click **Show advanced options** , and then select the **Placement** tab.
  5. Select the **Apply a capacity reservation** check box.
  6. For **Capacity reservation** , select the capacity reservation that you want to move the instance into.
  7. Click **Save changes**.


### To move instances out of a capacity reservation 🔗 
  1. Open the **navigation menu** and select **Compute**. Under **Compute** , select **Instances**.
  2. Click the instance that you're interested in.
  3. Select **More Actions** , and then select **Edit**.
  4. Click **Show advanced options** , and then select the **Placement** tab.
  5. Clear the **Apply a capacity reservation** check box.
  6. Click **Save changes**.


## Using the API 🔗 
For information about using the API and signing requests, see [REST API documentation](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm) and [Security Credentials](https://docs.oracle.com/iaas/Content/General/Concepts/credentials.htm). For information about SDKs, see [SDKs and the CLI](https://docs.oracle.com/iaas/Content/API/Concepts/sdks.htm).
Use this API operation to move instances into and out of capacity reservations:
  * [UpdateInstance](https://docs.oracle.com/iaas/api/#/en/iaas/latest/Instance/UpdateInstance)


Was this article helpful?
YesNo

