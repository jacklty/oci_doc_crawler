Updated 2025-01-14
# Removing an AD Bridge
Remove an AD bridge from an IAM identity domain.
  1. Open the **navigation menu** and select **Identity & Security**. Under **Identity** , select **Domains**.
  2. Click the name of the identity domain that you want to work in. You might need to change the compartment to find the domain that you want. Then, click **Settings** and then **Directory integration**.
  3. Select the Actions menu (![Actions Menu](https://docs.oracle.com/en-us/iaas/Content/libraries/global-images/actions-menu.png)) for the domain that contains the bridge that you want to remove.
  4. Select **Remove**.
  5. In the **Confirmation** window, select **OK**.
By removing the domain, you're removing the bridge associated with the domain. To ensure that the bridge is deleted cleanly and completely, you must delete the client associated with the bridge.
  6. Double-click the `ad-id-bridge.exe` file.
The IAM Microsoft Active Directory Bridge Installer appears.
  7. In the **Welcome** dialog box, select **Next**.
  8. In the **Removal completed** dialog box, select **Close**.


**Important** If you can't remove the client for the AD bridge or the bridge still appears in the **Directory integrations** page, then complete the following steps:
  1. Run the following cURL command to obtain the client ID that you used to install the client for the AD bridge:```
curl -X GET \
_<Identity_Cloud_Service_URL>_/admin/v1/IdentityAgents \
-H 'Authorization: Bearer _<access_token>_
```

`<Identity_Cloud_Service_URL>`is a placeholder for the identity domain URL that you used to install the client for the bridge, and`<access_token>` is a placeholder for the access token that contains the authorization credentials that are required to obtain the client ID.
See the [IAM: First REST API Call](https://www.oracle.com/webfolder/technetwork/tutorials/obe/cloud/idcs/idcs_rest_1stcall_obe/rest_1stcall.html) tutorial to learn how to get this access token.
A list of bridge clients that are installed for your identity domain appears.
  2. From this list, find the client ID of the bridge that you want to remove.
  3. Run the following cURL command to remove the client for the bridge:
```
curl -X DELETE \
_<Identity_Cloud_Service_URL>_/admin/v1/IdentityAgents/<Client_ID> \
-H 'Authorization: Bearer _<access_token>_
```

`_<Client_ID>_`represents the ID of the client for the bridge that you want to remove.
A `204 (No Content)` response appears, signifying that you removed the client for the bridge.


Was this article helpful?
YesNo

