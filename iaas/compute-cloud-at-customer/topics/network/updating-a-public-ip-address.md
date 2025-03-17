Updated 2024-08-06
# Updating a Public IP Address
On Compute Cloud@Customer, you can manage public IPs.
You can use the public IP update command to do any of the following actions:
  * Assign an existing reserved public IP address object to a private IP address object.
  * Create and assign a reserved public IP address object in one step.
  * Move a reserved public IP address object to a different private IP address object.
  * Unassign a reserved public IP address object from a private IP address object.
  * Change the display name or tags for a public IP address object.


Avoid entering confidential information in names.
  * [Console](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/network/updating-a-public-ip-address.htm)
  * [CLI](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/network/updating-a-public-ip-address.htm)
  * [API](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/network/updating-a-public-ip-address.htm)


  *     1. In the [Compute Cloud@Customer Console](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/overview/compute-cloud-customer-console.htm#accessing-the-console "Use the Compute Cloud@Customer Console to create and manage compute, storage and other resources on a Compute Cloud@Customer infrastructure.") navigation menu, click **Compute** , then click **Instances**.
    2. At the top of the page, select the compartment that contains the instance for which you want to update a public IP address.
    3. Click the name of the instance.
The instance details page is displayed.
    4. Under **Resources** , click **Attached VNICs**. 
Click the name of the VNIC for which you want to assign a public IP address.
    5. On the VNIC details page, under **Resources** , click **IP Addresses**. 
The primary private IP address and any secondary private IP addresses, and any attached public IP addresses, are shown in the table.
    6. For the private IP address for which you want to add or update a public IP address, click the Actions menu, then click **Edit Public IP**.
    7. In the **Reserve Public IP** dialog box, select one of the following choices:
       * **No public IP**
Click Reserve Public IP in the dialog to unassign this public IP address from this private IP address. You might have to refresh the page to see that the public IP address is no longer assigned.
       * **Reserve public IP**
Select one of the following choices:
         * **Reserve existing public IP**
           1. Select an existing public IP address. You might need to change the compartment.
           2. Click **Reserve Public IP** in the dialog.
If the specified public IP address object is already assigned to a different private IP address object, the public IP address object will be unassigned (moved) from the current private IP address object and reassigned to the specified private IP address object.
         * **Create public IP**
Create and assign a reserved public IP address in one step.
           1. (Optional) Provide a name for the new reserved public IP address object.
           2. Select the compartment where the new reserved public IP address object will be created.
           3. Select the **IP Address Source**.
           4. Click **Reserve Public IP**.
The new reserved public IP address shows in the **IP Addresses** table in **Resources**. You might need to refresh the page to see the new public IP address.
  * Use the [oci network public-ip update](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/network/public-ip/update.html) command and required parameters to update the specified public IP. 
Copy
```
oci network public-ip update [OPTIONS]
```

For a complete list of CLI commands, flags, and options, see the [Command Line Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/index.html).
  * Use the [UpdatePublicIp](https://docs.oracle.com/iaas/api/#/en/iaas/latest/PublicIp/UpdatePublicIp) operation to update the specified public IP. 
For information about using the API and signing requests, see [REST APIs](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm#REST_APIs) and [Security Credentials](https://docs.oracle.com/iaas/Content/General/Concepts/credentials.htm). For information about SDKs, see [Software Development Kits and Command Line Interface](https://docs.oracle.com/iaas/Content/API/Concepts/sdks.htm#Software_Development_Kits_and_Command_Line_Interface).


Was this article helpful?
YesNo

