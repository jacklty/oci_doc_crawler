Updated 2025-01-31
# Adding Domains
Add domains in **Domain Management**.
  * [Console](https://docs.oracle.com/en-us/iaas/Content/General/domain/create-domain.htm)
  * [CLI](https://docs.oracle.com/en-us/iaas/Content/General/domain/create-domain.htm)
  * [API](https://docs.oracle.com/en-us/iaas/Content/General/domain/create-domain.htm)


  * For existing customers, use the following instructions to add and verify a domain.
    1. In the **navigation menu** , select ****Governance & Administration****. Under ****Tenancy Management**** , select **Domain Management**.
    2. Select **Add and Verify Domain**. The **Add and Verify Domain** panel opens.
If a policy hasn't already been created, an **Add Policy** notification is displayed, informing you that a default policy must first be created, to allow **Domain Management** to write [notifications](https://docs.oracle.com/iaas/Content/Notification/home.htm) in the particular tenancy and compartment.
To confirm, select **Add Policy**. For more information on viewing the list of policies, see [Using the Console](https://docs.oracle.com/iaas/Content/Identity/Tasks/managingpolicies.htm#three), where a new **Domain_Governance_Policy** is present on the **Policies** page after the policy has been added.
After the policy has been added, **Domain Management** can create [notifications](https://docs.oracle.com/iaas/Content/Notification/home.htm), which are sent to the email address in the **Add and Verify Domain** panel. If you don't agree to policy creation, you can't proceed with the rest of the domain setup steps.
    3. In the **Add and Verify Domain** panel, enter the email address of the domain to be added. This email address is used when someone with the verified domain tries to create an OCI account.
    4. Agree to the Oracle Notification Service rates. For more information, see [Notifications](https://www.oracle.com/devops/notifications/).
    5. Under **Domain** , enter the domain you want to add and verify. Don't include the protocol (http:// or https://).
    6. Select **Add and Verify Domain**.
The domain is added, and the **TXT Record** field is populated with a generated name and value. Copy the TXT file so you can sign in to the domain's account and add the TXT record information to the domain's registrar.
After you have completed adding the TXT record, Oracle verifies that you own the domain. After verification, you receive an email notification that the status has changed from **Pending** to **Verified**. This process can take up to 72 hours to complete. For more information on TXT records, see [Domains Help on GoDaddy](https://www.godaddy.com/help/add-a-txt-record-19232).
    7. To return to the **Domain Management** page, select **Close**.
After refreshing the page, the **Domain Management** page displays the new domain you have added according to the following parameters:
    * **Domain** : The name of the domain and its associated OCID.
    * **Notifications** : Links to the Notifications [topic](https://docs.oracle.com/iaas/Content/Notification/Concepts/notificationoverview.htm#concepts). Topics aren't created until verification has occurred.
**Important** When a domain has been verified and the [topics](https://docs.oracle.com/iaas/Content/Notification/Concepts/notificationoverview.htm#concepts) have been created, you receive an email to confirm the subscription. You must confirm the email subscription before you can start receiving email notifications.
    * **TXT Record** : The generated TXT record.
    * **Email** : The domain email.
    * **Status** : The domain verification status:
      * **Pending** : Verification in process.
      * **Failed** : Verification no good after 72 hours.
      * **Active** : Verified and governance enabled.
      * **Disabled** : Verified but not governed.
      * **Releasing** : Customer requested removal (work request triggered).
      * **Released** : The [work request](https://docs.oracle.com/en-us/iaas/Content/General/Concepts/workrequestoverview.htm#Work_Requests "Work requests help you monitor long-running operations such as database backups or the provisioning of compute instances.") is complete and is removed from the **Domain Management** page after seven days.
    * **Date** : The last change date. This field updates when verified, enabled, disabled, or if the email was updated.
After a domain's status is **Active** , you can perform the following tasks:
    * [Enable](https://docs.oracle.com/en-us/iaas/Content/General/domain/create-domaingov.htm#create_domaingov "Enable domain governance for a claimed domain.") or [disable](https://docs.oracle.com/en-us/iaas/Content/General/domain/delete-domaingov.htm#delete_domaingov "Disable domain governance on a claimed domain.") domain governance.
    * [Update](https://docs.oracle.com/en-us/iaas/Content/General/domain/update-domain.htm#update_domain "Edit a domain.") the email.
    * [Remove](https://docs.oracle.com/en-us/iaas/Content/General/domain/delete-domain.htm#delete_domain "Release a domain, making it available to be claimed again by another tenancy.") the domain.
  * Use the [oci organizations domain create](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/organizations/domain/create.html) command and required parameters to start the registration process to claim a domain:
Command
CopyTry It
```
oci organizations domain create --compartment-id, -c [text] --domain-name [text] ... [OPTIONS]
```

For a complete list of parameters and values for CLI commands, see the [CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest).
  * Run the [CreateDomain](https://docs.oracle.com/iaas/api/#/en/organizations/latest/Domain/CreateDomain) operation to start the registration process to claim a domain.


Was this article helpful?
YesNo

