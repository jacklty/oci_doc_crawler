Updated 2025-01-17
# Creating a Local Peering Gateway
Create a local peering gateway (LPG) that instances, load balancers, and other resources can use to connect to resources in other virtual cloud networks (VCNs) in the same Oracle Cloud Infrastructure (OCI) region. 
LPGs require a specific IAM policy setting. After you create an LPG, you must establish a connection to another LPG, and configure routing rules and security settings before the VCN can connect to resources in another VCN.
The administrator of each VCN that you're trying to peer with creates an LPG for their own VCN. "You" in the following procedure means an administrator (either the [acceptor or requestor](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/localVCNpeering.htm#Importan)).
**Required IAM Policy to Create LPGs**
If both administrators already have broad network administrator permissions (see [Let network admins manage a cloud network](https://docs.oracle.com/iaas/Content/Identity/Concepts/commonpolicies.htm#network-admins-manage-cloud-network)), then they have permission to create, update, and delete LPGs. Otherwise, here's an example policy giving the necessary permissions to a group called `LPGAdmins`. The second statement is required because creating an LPG affects the VCN that it belongs to, so the administrator must have permission to manage VCNs.
Copy
```
Allow group LPGAdmins to manage local-peering-gateways in tenancy
Allow group LPGAdmins to manage vcns in tenancy

```

  * [Console](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/create-lpg.htm)
  * [CLI](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/create-lpg.htm)
  * [API](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/create-lpg.htm)


  *     1. In the Console, confirm you're viewing the compartment that contains the VCN that you want to add the LPG to. For information about compartments and access control, see [Access Control](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/accesscontrol.htm#Access_Control). 
    2. Open the **navigation menu** , select **Networking** , and then select **Virtual cloud networks**.
    3. Select the name of the VCN that you want to create the LPG in.
    4. Under **Resources** , select **Local Peering Gateways**. 
    5. Select **Create Local Peering Gateway**.
    6. Enter the following values:
       * **Name:** A friendly name for the LPG. It doesn't have to be unique, and it can't be changed later in the Console (but you can change it with the API or CLI). Avoid entering confidential information.
       * **Create in Compartment** : The compartment in which you want to create the LPG, if different from the compartment you're working in. 
       * **Associate with Route Table (Advanced option)** : Specify this option only if you're setting up the advanced routing scenario called [transit routing](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/transitrouting.htm#Transit_Routing_Access_to_Multiple_VCNs_in_the_Same_Region). Select the compartment that contains the route table that you want to associate with the LPG, and then select the route table. You can skip this part and associate the LPG with a route table later.
       * **Tags:** If you have permissions to create a resource, then you also have permissions to apply free-form tags to that resource. To apply a defined tag, you must have permissions to use the tag namespace. For more information about tagging, see [Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). If you're not sure whether to apply tags, skip this option or ask an administrator. You can apply tags later. 
    7. Select **Create Local Peering Gateway**.
The LPG is then created and displayed on the **Local Peering Gateways** page in the compartment that you chose. The next step in creating a local peering is to [share information](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/localVCNpeering.htm#share_info) with the administrator of the other VCN, if they have also created an LPG for their VCN.
  * Use the [network local-peering-gateway create](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/network/local-peering-gateway/create.html) command and required parameters to create an LPG:
Command
CopyTry It
```
oci network local-peering-gateway create --compartment-id ocid --vcn-id ocid ... [OPTIONS]
```

For a complete list of parameters and values for CLI commands, see the [CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest).
  * Run the [CreateLocalPeeringGateway](https://docs.oracle.com/iaas/api/#/en/iaas/latest/LocalPeeringGateway/CreateLocalPeeringGateway) operation to create a local peering gateway.


Was this article helpful?
YesNo

