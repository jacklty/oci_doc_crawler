Updated 2025-01-15
# Getting a List of DRG Attachments
Get a list of DRG attachments that belong to a particular dynamic routing gateway (DRG).
This task functions somewhat differently in the Console than in the API or CLI. The Console distinguishes by attachment type while the other methods don't. 
  * [Console](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/drg-get-all-drg-attachments.htm)
  * [CLI](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/drg-get-all-drg-attachments.htm)
  * [API](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/drg-get-all-drg-attachments.htm)


  *     1. Open the **navigation menu** and select **Networking**. Under **Customer connectivity** , select **Dynamic routing gateway**.
    2. Under **List Scope** , select the compartment containing the DRG you want to list attachments for.
The page updates to display only the resources in that compartment. If you're not sure which compartment to use, contact an administrator. For more information, see [Access Control](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/accesscontrol.htm#Access_Control).
    3. Click the name of the DRG.
Under **Resources** , the attachments are sorted according to their type. The number of attachments with a given type is listed.
    4. Click one of the following depending on which attachment type you're interested in: 
       * **VCN attachments**
       * **Virtual circuit attachments**
       * **IPSec tunnel attachments**
       * **Remote peering connection attachments**
       * **Cross-tenancy attachments**
A list of attachments wit hthat type is shown in the Console. 
  * Use the [network drg get-all-drg-attachments](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/network/drg/get-all-drg-attachments.html) command and required parameters to get a list of DRG attachments that belong to a particular DRG:
Command
CopyTry It
```
oci network drg get-all-drg-attachments --drg-id ocid ... [OPTIONS]
```

Use the parameters shown to get a list of attachments with a certain type that belong to a particular DRG:
Command
CopyTry It
```
oci network drg get-all-drg-attachments --drg-id ocid --attachment-type [ALL | IPSEC_TUNNEL | REMOTE_PEERING_CONNECTION | VCN | VIRTUAL_CIRCUIT ] ... [OPTIONS]
```

Use the parameters shown to get a list of all attachments that belong to a different tenancy:
Command
CopyTry It
```
oci network drg get-all-drg-attachments --drg-id ocid --is-cross-tenancy [true | false] ... [OPTIONS]
```

For a complete list of parameters and values for CLI commands, see the [CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest).
  * Run the [GetAllDrgAttachments](https://docs.oracle.com/iaas/api/#/en/iaas/latest/Drg/GetAllDrgAttachments) operation to get a list of DRG attachments that belong to a particular DRG.


Was this article helpful?
YesNo

