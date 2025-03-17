Updated 2023-09-25
# Required IAM Policy for Compute Scanning Targets
To use Oracle Cloud Infrastructure, you must be granted the required type of access in a **policy (IAM)** written by an administrator, whether you're using the Console or the REST API with an SDK, CLI, or other tool.
**Tip**
If you try to perform an action and get a message that you don’t have permission or are unauthorized, confirm with your administrator the type of access you were granted and which **compartment** you’re supposed to work in.
For example, to allow users in the group `SecurityAdmins` to create, update, and delete all Vulnerability Scanning resources in the compartment `SalesApps`:
Copy
```
Allow group SecurityAdmins to manage vss-family in compartment SalesApps
```

**Important** If you're setting up _Agent-Based Qualys Policies_ : First set up the _Agent-Based Standard Policies_ , and then set up _Agent-Based Qualys Policies_.
## Agent-Based Standard Policies 🔗 
**Read the Repositories for VSS OCIR Container Image Scans**
To allow users in a group to read repositories for VSS OCIR container image scans: 
Copy
```
Allow group VSSAdmins to read repos in tenancy
```

**Deploy the Oracle Cloud Agent **
If you enable agent-based scanning in your recipe, then you must give the Vulnerability Scanning service permission to deploy the Oracle Cloud Agent to your target Compute instances.
**Read the**VNIC (virtual network interface card)****
The Vulnerability Scanning service must also be able to read the **VNIC (virtual network interface card)** on your target Compute instances.
For example, to grant this permission for all Compute instances in the entire tenancy:
Copy
```
Allow service vulnerability-scanning-service to manage instances in tenancy
Allow service vulnerability-scanning-service to read compartments in tenancy
Allow service vulnerability-scanning-service to read vnics in tenancy
Allow service vulnerability-scanning-service to read vnic-attachments in tenancy
```

To grant this permission for all Compute instances in a specific compartment:
Copy
```
Allow service vulnerability-scanning-service to manage instances in compartment <compartment_name>
Allow service vulnerability-scanning-service to read compartments in compartment <compartment_name>
Allow service vulnerability-scanning-service to read vnics in compartment <compartment_name>
Allow service vulnerability-scanning-service to read vnic-attachments in compartment <compartment_name>
```

A VNIC might be in a different compartment from your Compute instance. Either grant VNIC permissions for the entire tenancy or for the specific compartment that the VNIC is in as well as the compartments of the Compute instances:
Copy
```
Allow service vulnerability-scanning-service to read vnics in compartment <vnic_compartment_name>
Allow service vulnerability-scanning-service to read vnic-attachments in compartment <vnic_compartment_name>
```

## Agent-Based Qualys Policies 🔗 
**Prerequisites:**
  * Setting up _Agent-Based Qualys Policies_.
  * Create a dynamic group of instances that you want to scan. See [Managing Dynamic Groups](https://docs.oracle.com/iaas/Content/Identity/dynamicgroups/managingdynamicgroups.htm). Instances that meet the criteria defined by any of these rules are included in the dynamic group. For example: 
Copy
```
All {instance.compartment.id = <compartment_ocid>}
```

**Note** You can specify an entire tenancy.


**Grant Dynamic Group Access to Secrets and to the Data Sent Back from Qualys**
To use Qualys agent-based scanning in your recipe, write a policy that grants permission for the dynamic group to access secrets and to access to the data sent back from Qualys.
To grant permission for the dynamic group to access secrets: 
Copy
```
Allow dynamic-group <dynamic_group_name> to read vaults in tenancy
Allow dynamic-group <dynamic_group_name> to read keys in tenancy
Allow dynamic-group <dynamic_group_name> to read secret-family in tenancy

```

To access the data sent back from Qualys:
Copy
```
Define tenancy ocivssprod as ocid1.tenancy.oc1..aaaaaaaa6zt5ejxod5pgthsq4apr5z2uzde7dmbpduc5ua3mic4zv3g5ttma 
Endorse dynamic-group <dynamic_group_name> to read objects in tenancy ocivssprod

```

For more information and examples, see:
  * [Vulnerability Scanning IAM Policies](https://docs.oracle.com/en-us/iaas/scanning/using/iam-policies.htm#iam_policies "Create IAM policies to control who has access to Oracle Cloud Infrastructure Vulnerability Scanning Service resources, and to control the type of access for each group of users.")
  * [Policy Reference for Core Services](https://docs.oracle.com/iaas/Content/Identity/policyreference/corepolicyreference.htm)


Was this article helpful?
YesNo

