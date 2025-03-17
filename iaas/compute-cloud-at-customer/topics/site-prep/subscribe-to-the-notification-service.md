Updated 2024-05-07
# Subscribing to Upgrade Notifications 
To receive email notifications when an upgrade starts and is finished, perform this procedure. The procedure involves creating a notification topic, then subscribing to the topic with an email address.
To use the Notification service for other purposes, see [Notifications](https://docs.oracle.com/iaas/Content/Notification/home.htm).
**Important** Create only one topic called `ComputeCloudCustomer-InfraWatch`, and at least one subscription to that topic.
**Prerequisite**
You must have notification policies configured as described in [Add Required Policies](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/site-prep/preparing-your-tenancy.htm#add-required-policies "Certain IAM policies must be configured before Compute Cloud@Customer is connected to your tenancy.").
  1. Open the Oracle Cloud Console navigation menu and click **Developer Services**. Under **Application Integration** , click **Notifications**.
  2. On the **Topics** page, select the Compute Cloud@Customer infrastructure root compartment. 
  3. Click **Create Topic**.
  4. In the **Create Topic** panel, enter the following information:
     * **Name:** Enter the following string exactly as shown. The string is case-sensitive:
```
ComputeCloudCustomer-InfraWatch
```

     * **Description:** Enter a description such as "Upgrade notification topic." Avoid entering confidential information.
**Note** Ignore the message about creating an identity policy. The policies for this topic were created when the tenancy was prepared. See [Add Required Policies](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/site-prep/preparing-your-tenancy.htm#add-required-policies "Certain IAM policies must be configured before Compute Cloud@Customer is connected to your tenancy.").
  5. Click **Create**. 
  6. Click the topic named **ComputeCloudCustomer-InfraWatch**. 
The Topic Details page is displayed.
  7. Click **Create Subscription**. 
  8. In the **Create Subscription** panel, enter the following information
     * **Protocol:** Select Email.
     * **Email** : Enter an email address.
  9. Click **Create**. 
The Notifications service creates the email subscription and sends a confirmation URL to the email address. The subscription is pending until confirmation is received.


**What's Next?**
Learn about typical postinstallation administration. See [Postinstallation Administration](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/infrastructure/starting-to-manage-resources.htm#starting-to-manage-resources "After the Compute Cloud@Customer infrastructure is installed and connected to Oracle Cloud Infrastructure \(OCI\), you need to perform additional administrative tasks before you can create resources such as virtual cloud networks, instances, and storage on the Compute Cloud@Customer infrastructure.")
.
Was this article helpful?
YesNo

