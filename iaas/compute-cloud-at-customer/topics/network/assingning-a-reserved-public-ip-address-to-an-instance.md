Updated 2023-08-15
# Assigning a Reserved Public IP Address to an Instance
On Compute Cloud@Customer, you can assign a public IP address to an instance, you assign the public IP address object to a private IP address object.
An ephemeral public IP address can be assigned only to the primary private IP address of a VNIC. See [Assigning an Ephemeral Public IP Address to an Instance](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/network/assingning-an-ephemeral-public-ip-address-to-an-instance.htm#assingning-an-ephemeral-public-ip-address-to-an-instance "On Compute Cloud@Customer, you assign a public IP address to an instance by assigning the public IP address object to a private IP address object."). A reserved public IP address can be assigned to any private IP address.
See [Reserving a Public IP Address](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/network/reserving-a-public-ip-address.htm#reserving-a-public-ip-address "On Compute Cloud@Customer, you can reserve a public IP address that's available to assign to a private IP address object at a later time.") to create a reserved public IP address that is available to assign to a private IP address object at a later time.
Use the procedures in [Updating a Public IP Address](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/network/updating-a-public-ip-address.htm#updating-a-public-ip-address "On Compute Cloud@Customer, you can manage public IPs.") to assign an existing reserved public IP address object to the specified private IP address object or to create and assign a reserved public IP address in one step.
A reserved public IP address object remains available for reassignment when its private IP address object is deleted, its VNIC is detached or terminated, or its instance is terminated.
Avoid entering confidential information in names.
Was this article helpful?
YesNo

