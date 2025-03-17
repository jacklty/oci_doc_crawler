Updated 2025-01-14
# Viewing Details About an AD Bridge
You can see the domain name and status for each AD bridge in an IAM identity domain. But you might want to see other information about the AD bridge, such as its configuration information, attribute mappings, and a synchronization log of the communication between IAM and Microsoft Active Directory.
  1. Open the **navigation menu** and select **Identity & Security**. Under **Identity** , select **Domains**.
  2. Click the name of the identity domain that you want to work in. You might need to change the compartment to find the domain that you want. Then, click **Settings** and then **Directory integration**.
  3. Select the AD bridge about which you want to see more information.
     * To view configuration information about the bridge, select the **Configuration** tab. See [Configure a Microsoft Active Directory (AD) Bridge](https://docs.oracle.com/en-us/iaas/Content/Identity/msadbridge/configure-microsoft-active-directory-ad-bridge.htm#configure-microsoft-active-directory-ad-bridge "Configure a bridge between Microsoft Active Directory and an IAM identity domain.").
     * To view attribute mappings for the bridge, open the **Edit Attribute Mappings** window. See [Define Attribute Mappings for a Microsoft Active Directory (AD) Bridge](https://docs.oracle.com/en-us/iaas/Content/Identity/msadbridge/define-custom-attribute-mappings-microsoft-active-directory-ad-bridge.htm#define-custom-attribute-mappings-microsoft-active-directory-ad-bridge "When you create an AD bridge, attribute mappings are defined between Microsoft Active Directory and IAM. Attribute mappings enable the AD bridge to pass values associated with user accounts between Microsoft Active Directory and IAM.").
     * To view a synchronization log of all traffic between IAM and Microsoft Active Directory the last time the bridge ran, select the **Import** tab. See [Synchronizing IAM with an AD Bridge](https://docs.oracle.com/en-us/iaas/Content/Identity/msadbridge/run-microsoft-active-directory-ad-bridge.htm#run-microsoft-active-directory-ad-bridge "You can run an bridge to synchronize IAM with Microsoft Active Directory immediately.").


Was this article helpful?
YesNo

