Updated 2025-01-14
# Creating a Bridge for Microsoft Active Directory
Create a bridge between IAM and Microsoft Active Directory.
To create an AD bridge that provides a link between a Microsoft Active Directory enterprise directory structure and IAM, you must be assigned to either the identity domain administrator role or the security administrator role. You must also have administrative rights to access the Microsoft Active Directory domain that you want to monitor by using the bridge.
Part of creating the bridge is providing administrative credentials for both Microsoft Active Directory and IAM. The bridge requires these credentials to communicate with Microsoft Active Directory and IAM as an administrator.
**Important**
The Microsoft Active Directory account used to install the bridge must have the following permissions:
  * **Generic Read** for the users and groups in the Microsoft Active Directory domain that you want to import into IAM
  * **Generic Read** for all organizational units (OUs) in the domain
  * **Generic Read** for the **cn=Configuration** container in the domain
  * The **List Children** and **Read** properties for the **cn=Deleted Objects** container with inheritance


If this account is also used to configure delegated authentication for the bridge, then the account should have the following permissions:
  * **Change Password**
  * **Reset Password**
  * **Read pwdLastSet**
  * **Write pwdLastSet**
  * **Read lockoutTime**
  * **Write lockoutTime**


You can access the [Managing security settings](http://apexapps.oracle.com/pls/apex/f?p=44785:112:0::::P112_CONTENT_ID:13047) infographic to see how to create a AD bridge.
  1. Open the **navigation menu** and select **Identity & Security**. Under **Identity** , select **Domains**.
  2. Click the name of the identity domain that you want to work in. You might need to change the compartment to find the domain that you want. Then, click **Settings** and then **Directory integration**.
  3. Select **Add**.
  4. In the **Install a bridge for Microsoft Active Directory** page, make a note of the identity domain URL, client ID, and client secret.
The identity domain URL contains the name and port number for your IAM identity domain. The client ID and client secret are used by the bridge to access IAM as an administrator.
**Note** The client secret is encrypted for security reasons. To see the secret in clear text, select **Show Secret**. To regenerate a secret for the bridge, select **Regenerate**.
  5. Select **Download**.
IAM downloads the client for the bridge.
**Note** Don't close the **Install a bridge for Microsoft Active Directory** page. You'll need to reference the identity domain URL, client ID, and client secret when creating the bridge.
  6. To install the client for the AD bridge, double-click the `ad-id-bridge....exe` file.
The **Welcome to AD Bridge Installer** window appears.
  7. In the **Language Selection** area, select the language that you want to use to install the client for the AD Bridge, and then select **OK**. 
The IAM AD Bridge Installer appears.
**Tip** While you're installing the client for the AD bridge, IAM generates log files for the bridge automatically, and stores them in the `%Temp%` directory.
**Note** You can only installe the AD bridge on a machine that's connected to a Microsoft Active Directory domain, otherwise installation will not proceed.
  8. If the **Open File — Security Warning** dialog box appears, then select **Run**. Otherwise, go to step 8.
  9. In the **Welcome** dialog box, select **Next**.
  10. In the **Destination Folder** dialog box, choose one of the following install choices:
     * To install the client in the default directory, select **Next**.
     * To select another directory to install the client:
       1. Select **Browse**. 
       2. In the **Browse For Folder** dialog box, select the directory where IAM installs the client.
       3. Select **OK**. 
       4. Select **Next**.
  11. In the **Specify Proxy Server** dialog box:
    1. If your organization has a firewall in place and requires communication to be handled using an HTTP Proxy Server, then select **Use Proxy Server**. If you select this checkbox, then provide the full path (or address) of the proxy server and the administrator credentials for connecting to the proxy server.
    2. If your organization doesn't require communication to be handled using an HTTP Proxy Server, then don't select **Use Proxy Server**.
    3. Select **Next**.
  12. In the **Specify Credentials** dialog box:
    1. Provide the identity domain URL, client ID, and client secret.
**Tip** These credentials appear on the **Install Bridge** page of the IAM Console.
    2. Select **Test**.
The bridge attempts to connect to the IAM server.
If a connection can be established, then a `Connection Successful!` confirmation message appears.
Otherwise, you'll receive an error message, indicating that you entered an incorrect identity domain URL, client ID, or client secret. Modify the incorrect values, and select **Test** again.
    3. Select **Next**.
  13. In the **Specify Microsoft Active Directory Credentials** dialog box, provide the following connection details to the Microsoft Active Directory server: 
    1. **Username:** The Microsoft Active Directory account that the bridge uses to access the Microsoft Active Directory server.
    2. **Password:** The password for the Microsoft Active Directory account.
    3. **Use SSL:** If you're connecting to the server through an SSL connection, then leave this checkbox selected. Otherwise, clear it.
**Note** We recommend that you keep the **Use SSL** checkbox selected because this results in a faster and more-secure connection. After you select or clear this checkbox, and install the client for the bridge, you can't modify this setting.
    4. Select **Test**.
The bridge tries to connect to the Microsoft Active Directory server.
If a connection can be established, then a `Connection Successful!` confirmation message appears.
Otherwise, you'll receive an error message, indicating that:
       * You entered an incorrect username or password. Change the incorrect values, and select **Test** again.
       * You're trying to connect to the Microsoft Active Directory server through an SSL connection, but the certificate for the server isn't trusted. Ensure that this certificate is valid, and is present in the trust store of your machine. Then, select **Test** again.
**Note**
We recommend that you enable **Password Never Expires** option for the Microsoft Active Directory account that the bridge uses. Otherwise, if the password for the account expires subsequent communication between the bridge and Microsoft Active Directory will fail until the password is updated in the bridge. See [Change Administrator Account Credentials for AD Bridge](https://docs.oracle.com/en-us/iaas/Content/Identity/msadbridge/change-administrator-account-credentials-ad-bridge.htm#enter-topic-id "Use the AD Bridge client to update administrator account details.").
    5. Select **Next**.
  14. In the **Summary** dialog box, select **Close**.
  15. In the IAM Console, access the **Directory integrations** page. 
The bridge that you created for the Microsoft Active Directory domain appears with a status of **Partially configured**. The bridge is created, but not configured. See [Configure a Microsoft Active Directory (AD) Bridge](https://docs.oracle.com/en-us/iaas/Content/Identity/msadbridge/configure-microsoft-active-directory-ad-bridge.htm#configure-microsoft-active-directory-ad-bridge "Configure a bridge between Microsoft Active Directory and an IAM identity domain.") for more information about configuring this bridge.
**Note** If you don't see the bridge in the **Directory integrations** page, then refresh your web browser. Also, you can create only one bridge per Microsoft Active Directory domain.


Was this article helpful?
YesNo

