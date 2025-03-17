Updated 2025-01-15
# Creating a Remote Peering Connection
Create a new remote peering connection (RPC) for a specified DRG.
To establish remote peering, each administrator creates an RPC object for their own VCN's DRG, which includes a DRG attachment with the RPC type. "You" in the following procedure means an administrator (either the [acceptor or requestor](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/remoteVCNpeering.htm#Importan)).
**Note**
Required IAM Policy to Create RPCs
If the administrators already have broad network administrator permissions (see [Let network admins manage a cloud network](https://docs.oracle.com/iaas/Content/Identity/Concepts/commonpolicies.htm#network-admins-manage-cloud-network)), then they have permission to create, update, and delete RPCs. Otherwise, here's an example policy giving the necessary permissions to a group called RPCAdmins. The second statement is required because creating an RPC affects the DRG it belongs to, so the administrator must have permission to manage DRGs.
Copy
```
Allow group RPCAdmins to manage remote-peering-connections in tenancy
Allow group RPCAdmins to manage drgs in tenancy

```

  * [Console](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/drg-rpc-create.htm)
  * [CLI](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/drg-rpc-create.htm)
  * [API](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/drg-rpc-create.htm)


  *     1. Open the **navigation menu** and select **Networking**. Under **Customer connectivity** , select **Dynamic routing gateway**.
    2. Under **List Scope** , select the compartment that contains the DRGfor which you want to create an RPC.
The page updates to display only the resources in that compartment. If you're not sure which compartment to use, contact an administrator. For more information, see [Access Control](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/accesscontrol.htm#Access_Control).
    3. Click the name of the DRG you're interested in.
    4. Under **Resources** , click **Remote Peering Connections**.
    5. Click **Create Remote Peering Connection**.
    6. Enter the following:
       * **Name:** A friendly name for the RPC. It doesn't have to be unique, and it can be changed later. Avoid entering confidential information.
       * **Create in compartment** : The compartment where you want to create the RPC, if different from the compartment you're currently working in. 
    7. Click **Create Remote Peering Connection**.
The RPC is then created and displayed on the **Remote Peering Connections** page in the compartment you chose. 
    8. If you're the acceptor, record the RPC's region and OCID to later give to the requestor. 
  * Use the [network remote-peering-connection create](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/network/remote-peering-connection/create.html) command and required parameters to create a new RPC for a specified DRG:
Command
CopyTry It
```
oci network remote-peering-connection create --compartment-id compartment-ocid --drg-id drg-ocid ... [OPTIONS]
```

For a complete list of parameters and values for CLI commands, see the [CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest).
  * Run the [CreateRemotePeeringConnection](https://docs.oracle.com/iaas/api/#/en/iaas/latest/RemotePeeringConnection/CreateRemotePeeringConnection) operation to create a new RPC for a specified DRG.


Was this article helpful?
YesNo

