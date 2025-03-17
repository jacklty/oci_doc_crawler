Updated 2025-01-31
# Enabling Domain Governance
Enable domain governance for a claimed domain.
  * [Console](https://docs.oracle.com/en-us/iaas/Content/General/domain/create-domaingov.htm)
  * [CLI](https://docs.oracle.com/en-us/iaas/Content/General/domain/create-domaingov.htm)
  * [API](https://docs.oracle.com/en-us/iaas/Content/General/domain/create-domaingov.htm)


  * When you first [add a new domain](https://docs.oracle.com/en-us/iaas/Content/General/domain/create-domain.htm#create_domain "Add domains in Domain Management."), governance is disabled by default, and its status is set to **Pending**. After the status has changed to **Active** , you can then enable or disable governance.
**Note** Activating **Enable Governance** prevents others from creating an OCI account with your verified domain. Oracle notifies you when someone tries to create an account with your domain using [Notifications](https://www.oracle.com/devops/notifications/). If you need to allow others to create an account with your domain, select **Disable Governance** from the Actions menu (![Actions Menu](https://docs.oracle.com/en-us/iaas/Content/libraries/global-images/actions-menu.png)). For more information, see [Disabling Domain Governance](https://docs.oracle.com/en-us/iaas/Content/General/domain/delete-domaingov.htm#delete_domaingov "Disable domain governance on a claimed domain.").
    1. In the **navigation menu** , select ****Governance & Administration****. Under ****Tenancy Management**** , select **Domain Management**.
    2. In the Actions menu (![Actions Menu](https://docs.oracle.com/en-us/iaas/Content/libraries/global-images/actions-menu.png)), select **Enable Governance**. A **Turn on Domain Governance** confirmation is displayed.
    3. Agree to the Oracle Notification service rates. For more information, see [Notifications](https://www.oracle.com/devops/notifications/).
    4. Select **Yes, turn on**. After refreshing the page, the status changes to **Active** to indicate the domain is verified and governance is enabled.
  * Use the [oci organizations domain-governance create](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/organizations/domain-governance/create.html) command and required parameters to add domain governance to a claimed domain:
Command
CopyTry It
```
oci organizations domain-governance create --compartment-id, -c [text] --domain-id [text] --ons-subscription-id [text] --ons-topic-id [text] --subscription-email [text] ... [OPTIONS]
```

For a complete list of parameters and values for CLI commands, see the [CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest).
  * Run the [CreateDomainGovernance](https://docs.oracle.com/iaas/api/#/en/organizations/latest/DomainGovernance/CreateDomainGovernance) operation to add domain governance to a claimed domain.


Was this article helpful?
YesNo

