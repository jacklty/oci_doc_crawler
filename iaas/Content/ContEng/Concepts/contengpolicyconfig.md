Updated 2025-01-15
# Policy Configuration for Cluster Creation and Deployment
_Find out about the IAM policies to create before using Kubernetes Engine (OKE)._
When a tenancy is created, an Administrators group is automatically created for the tenancy. Users that are members of the Administrators group can perform any operation on resources in the tenancy. If all the users that will be working with Kubernetes Engine are already members of the Administrators group, there's no need to create other policies. 
However, if you want to enable users that are not members of the Administrators group to use Kubernetes Engine, you must create policies to enable the groups to which those users do belong to perform operations on resources in the tenancy or in individual compartments. Some policies are required, some are optional. See [Create Required Policy for Groups](https://docs.oracle.com/en-us/iaas/Content/ContEng/Concepts/contengpolicyconfig.htm#policyforgroupsrequired) and [Create One or More Additional Policies for Groups](https://docs.oracle.com/en-us/iaas/Content/ContEng/Concepts/contengpolicyconfig.htm#policyforgroups).
You also have to create additional policies if you want to:
  * Create and use clusters with virtual nodes and virtual node pools. See [Create Policy to Set Up and Use Virtual Nodes](https://docs.oracle.com/en-us/iaas/Content/ContEng/Concepts/contengpolicyconfig.htm#contengpolicyconfig_topic-Create_Policies_for_Virtual-Nodes).
  * Encrypt data in boot volumes and block volumes using your own master encryption keys from the [Vault](https://docs.oracle.com/iaas/Content/KeyManagement/Concepts/keyoverview.htm) service. See [Create Policy to Access User-Managed Encryption Keys for Encrypting Boot Volumes, Block Volumes, and/or File Systems](https://docs.oracle.com/en-us/iaas/Content/ContEng/Concepts/contengpolicyconfig.htm#contengpolicyconfig_topic_Create_Policies_for_User_Managed_Encryption).


If you want groups of users in one tenancy to access cluster-related resources in other tenancies, you have to create special cross-tenancy policy statements that explicitly state the resources that can be accessed and shared. See [Accessing Cluster-Related Resources Across Tenancies](https://docs.oracle.com/en-us/iaas/Content/ContEng/Concepts/contengaccessingokeresourcesacrosstenancies.htm#contengaccessingokeresourcesacrosstenancies "Find out about the IAM policies required to enable one tenancy to access cluster-related resources in other tenancies.").
Note that as well as the above policies managed by IAM, you can also use the Kubernetes RBAC Authorizer to enforce additional fine-grained access control for users on specific clusters via Kubernetes RBAC roles and clusterroles. See [About Access Control and Kubernetes Engine (OKE)](https://docs.oracle.com/en-us/iaas/Content/ContEng/Concepts/contengaboutaccesscontrol.htm#About_Access_Control_and_Container_Engine_for_Kubernetes "Find out about the permissions required to access clusters you've created using Kubernetes Engine \(OKE\).").
## Create Required Policy for Groups 🔗 
To create, update, and delete clusters and node pools, users that are not members of the Administrators group must have permissions to work with cluster-related resources. To give users the necessary access, you must create a policy with a number of required policy statements for the groups to which those users do belong:
  1. Open the **navigation menu** and select **Identity & Security**. Under **Identity** , select **Policies**. A list of the policies in the compartment you're viewing is displayed.
  2. Select the tenancy's root compartment or an individual compartment containing cluster-related resources from the list on the left. 
  3. Click **Create Policy**. 
  4. Enter the following:
     * **Name:** A name for the policy (for example, `acme-dev-team-oke-required-policy`) that is unique within the compartment. If you are creating the policy in the tenancy's root compartment, the name must be unique across all policies in your tenancy. You cannot change this later. Avoid entering confidential information.
     * **Description:** A friendly description. You can change this later if you want to.
     * **Statement:** The following required policy statements to enable users to use Kubernetes Engine to create, update, and delete clusters and node pools:
Copy
```
Allow group <group-name> to manage instance-family in <location>
```

Copy
```
Allow group <group-name> to use subnets in <location>
```

Copy
```
Allow group <group-name> to manage virtual-network-family in <location>
```

Copy
```
Allow group <group-name> to inspect compartments in <location>
```

Copy
```
Allow group <group-name> to use vnics in <location>
```

Copy
```
Allow group <group-name> to use network-security-groups in <location>
```

Copy
```
Allow group <group-name> to use private-ips in <location>
```

Copy
```
Allow group <group-name> to manage public-ips in <location>
```

The following required policy statement to enable users to perform any operation on cluster-related resources (this 'catch-all' policy effectively makes all users administrators insofar as cluster-related resources are concerned):
Copy
```
Allow group <group-name> to manage cluster-family in <location>
```

In the above policy statements, replace `<location>` with either `tenancy` (if you are creating the policy in the tenancy's root compartment) or `compartment <compartment-name>` (if you are creating the policy in an individual compartment).
**Note** Note that depending on the type of cluster, some required policy statements might not be necessary:
       * To work with "VCN-native" clusters (where the Kubernetes API endpoint is fully integrated with your VCN), the `use private-ips` is always required. However, the `use public-ips` policy statement is only necessary if the clusters' public IP address option is selected. For more information about VCN-native clusters, see [Kubernetes Cluster Control Plane and Kubernetes API](https://docs.oracle.com/en-us/iaas/Content/ContEng/Concepts/contengclustersnodes.htm#processes).
       * To work with clusters where the public Kubernetes API endpoint is in an Oracle-managed tenancy, the `use vnics`, `use private-ips`, and `use public-ips` policy statements are unnecessary.
Note that if a group is not in the default identity domain, prefix the group name with the identity domain name, in the format `group '<identity-domain-name>'/'group-name'`. You can also specify a group using its OCID, in the format `group id <group-ocid>`.
     * **Tags:** If you have permissions to create a resource, then you also have permissions to apply free-form tags to that resource. To apply a defined tag, you must have permissions to use the tag namespace. For more information about tagging, see [Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). If you're not sure whether to apply tags, skip this option or ask an administrator. You can apply tags later. 
  5. Click **Create**. 


## Create One or More Additional Policies for Groups 🔗 
To enable users that are not members of the Administrators group to use Kubernetes Engine, create additional policies to enable the groups to which those users do belong to perform operations on cluster-related resources as follows:
  1. Open the **navigation menu** and select **Identity & Security**. Under **Identity** , select **Policies**. A list of the policies in the compartment you're viewing is displayed.
  2. Select the tenancy's root compartment or an individual compartment containing cluster-related resources from the list on the left. 
  3. Click **Create Policy**. 
  4. Enter the following:
     * **Name:** A name for the policy (for example, `acme-dev-team-oke-additional-policy`) that is unique within the compartment. If you are creating the policy in the tenancy's root compartment, the name must be unique across all policies in your tenancy. You cannot change this later. Avoid entering confidential information.
     * **Description:** A friendly description. You can change this later if you want to.
     * **Statement:** A suitable policy statement to allow existing groups to perform operations on cluster-related resources. In the example policy statements below, replace `<location>` with either `tenancy` (if you are creating the policy in the tenancy's root compartment) or `compartment <compartment-name>` (if you are creating the policy in an individual compartment):
       * To enable users in the acme-dev-team group to automatically create and configure associated new network resources when creating new clusters in the 'Quick Create' workflow, policies must also grant the group:
         * VCN_READ and VCN_CREATE permissions. Enter a policy statement like:
Copy
```
Allow group acme-dev-team to manage vcns in <location>
```

         * SUBNET_READ and SUBNET_CREATE permissions. Enter a policy statement like:
Copy
```
Allow group acme-dev-team to manage subnets in <location>
```

         * INTERNET_GATEWAY_CREATE permission. Enter a policy statement like:
Copy
```
Allow group acme-dev-team to manage internet-gateways in <location>
```

         * NAT_GATEWAY_CREATE permission. Enter a policy statement like:
Copy
```
Allow group acme-dev-team to manage nat-gateways in <location>
```

         * ROUTE_TABLE_UPDATE permission. Enter a policy statement like:
Copy
```
Allow group acme-dev-team to manage route-tables in <location>
```

         * SECURITY_LIST_CREATE permission. Enter a policy statement like:
Copy
```
Allow group acme-dev-team to manage security-lists in <location>
```

       * To enable users in the acme-dev-team-cluster-viewers group to simply list the clusters, enter a policy statement like:
Copy
```
Allow group acme-dev-team-cluster-viewers to inspect clusters in <location>
```

       * To enable users in the acme-dev-team-pool-admins group to list, create, update, and delete node pools, enter a policy statement like:
Copy
```
Allow group acme-dev-team-pool-admins to use cluster-node-pools in <location>
```

       * To enable users in the acme-dev-team-auditors group to see details of operations performed on clusters, enter a policy statement like:
Copy
```
Allow group acme-dev-team-auditors to read cluster-work-requests in <location>
```

       * To enable users in the acme-dev-team-sgw group to create a service gateway to enable worker nodes to access other resources in the same region without exposing data to the public internet, enter a policy statement like:
Copy
```
Allow group acme-dev-team-sgw to manage service-gateways in <location>
```

       * To enable users in the acme-dev-team group to access clusters using Cloud Shell, enter a policy statement like:
Copy
```
Allow group acme-dev-team to use cloud-shell in <location>
```

Note that to access clusters using Cloud Shell, you'll also need to set up the kubeconfig file appropriately (see [Setting Up Cloud Shell Access to Clusters](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengdownloadkubeconfigfile.htm#cloudshelldownload)). For more information about Cloud Shell, see [Cloud Shell](https://docs.oracle.com/iaas/Content/API/Concepts/devcloudshellintro.htm).
       * To enable users in the acme-dev-team group to select master encryption keys and vaults in the Vault service when creating and modifying clusters using the Console:
Copy
```
Allow group acme-dev-team to read vaults in <location>
```

Copy
```
Allow group acme-dev-team to read keys in <location>
```

       * To enable users in the acme-dev-team group to use capacity reservations:
Copy
```
Allow group acme-dev-team to use compute-capacity-reservations in <location>
```

For more information, see [Using Capacity Reservations to Provision Managed Nodes](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengmakingcapacityreservations.htm#contengmakingcapacityreservations "Find out how to reserve compute capacity for clusters you've created using Kubernetes Engine \(OKE\).")
       * To enable users in the acme-dev-team group to use metrics (for example, to observe the condition of nodes in a Kubernetes cluster):
Copy
```
Allow group acme-dev-team to read metrics in <location>
```

For more information, see [Kubernetes Engine (OKE) Metrics](https://docs.oracle.com/en-us/iaas/Content/ContEng/Reference/contengmetrics.htm#Container_Engine_for_Kubernetes_Metrics "Find out about the metrics emitted by Kubernetes Engine \(OKE\).").
**Note**
Note that if a group is not in the default identity domain, prefix the group name with the identity domain name, in the format `group '<identity-domain-name>'/'group-name'`. You can also specify a group using its OCID, in the format `group id <group-ocid>`.
     * **Tags:** If you have permissions to create a resource, then you also have permissions to apply free-form tags to that resource. To apply a defined tag, you must have permissions to use the tag namespace. For more information about tagging, see [Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). If you're not sure whether to apply tags, skip this option or ask an administrator. You can apply tags later. 
  5. Click **Create**. 


## Create Policy to Set Up and Use Virtual Nodes 🔗 
Administrator users do not require additional permissions to create and use clusters with virtual nodes and virtual node pools.
To enable non-administrator users to use virtual nodes, you must set up an additional policy to give such users the required permissions. For more information about the policy statements to enter, see [Required IAM Policies for Using Virtual Nodes](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengvirtualnodes-Required_IAM_Policies.htm#contengvirtualnodes-Required_IAM_Policies "Find out about the IAM policies to create to use virtual nodes with Kubernetes Engine \(OKE\).").
## Create Policy to Access User-Managed Encryption Keys for Encrypting Boot Volumes, Block Volumes, and/or File Systems 🔗 
To specify a particular user-managed master encryption key from the [Vault](https://docs.oracle.com/iaas/Content/KeyManagement/Concepts/keyoverview.htm) service to encrypt data in boot volumes, block volumes, and/or file systems, you have to create a policy to allow access to that master encryption key. For more information about specifying user-managed encryption keys:
  * for boot volumes, see [Using the Console to create a Cluster with Explicitly Defined Settings in the 'Custom Create' workflow](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengcreatingclusterusingoke_topic-Using_the_Console_to_create_a_Custom_Cluster_with_Explicitly_Defined_Settings.htm#create-custom-cluster "Find out how to use the 'Custom Create' workflow to create a Kubernetes cluster with explicitly defined settings and existing network resources using Kubernetes Engine \(OKE\).") and [Modifying Node Pool and Worker Node Properties](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengmodifyingnodepool.htm#top "Find out how to modify properties of existing node pools and worker nodes you've created using Kubernetes Engine \(OKE\).") as appropriate.
  * for block volumes, see [Encrypting Data At Rest and Data In Transit with the Block Volume Service](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengcreatingpersistentvolumeclaim_topic-Provisioning_PVCs_on_BV.htm#contengcreatingpersistentvolumeclaim_topic_Provisioning_PVCs_on_BV_Encrypting_data)
  * for file systems, see [Encrypting Data At Rest and Data In Transit with the File Storage Service](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengcreatingpersistentvolumeclaim_Provisioning_PVCs_on_FSS.htm#contengcreatingpersistentvolumeclaim_topic-Provisioning_PVCs_on_new_FSS-Encrypting_data.dita)


Note that before you can create the policy, you have to know the master encryption key's OCID (see [Managing Keys](https://docs.oracle.com/iaas/Content/KeyManagement/Tasks/managingkeys.htm)).
To create a policy to allow access to a user-managed master encryption key:
  1. Open the **navigation menu** and select **Identity & Security**. Under **Identity** , select **Policies**. A list of the policies in the compartment you're viewing is displayed.
  2. A list of the policies in the compartment you're viewing is displayed.
  3. Select the tenancy's root compartment or an individual compartment containing cluster-related resources from the list on the left. 
  4. Click **Create Policy** , follow the instructions in [To create a policy](https://docs.oracle.com/iaas/Content/Identity/Tasks/managingpolicies.htm#To_create_a_policy), and give the policy a name (for example, `acme-oke-keys-policy`).
  5. **For boot volumes:** To use a master encryption key from the Vault service to encrypt data in boot volumes, enter the following policy statements to grant access to the master encryption key:
Copy
```
Allow group <group-name> to read keys in compartment <compartment-name> where target.key.id = '<key_OCID>'
```

Copy
```

Allow service oke to use key-delegates in compartment <compartment-name> where target.key.id = '<key_OCID>'
```

Copy
```

Allow service blockstorage to use keys in compartment <compartment-name> where target.key.id = '<key_OCID>'
```

Copy
```

Allow any-user to use key-delegates in compartment <compartment-name> where ALL {request.principal.type='nodepool', target.key.id = '<key_OCID>'}
```

where:
     * `<group-name>` is a group to which you belong. Note that if a group is not in the default identity domain, prefix the group name with the identity domain name, in the format `group '<identity-domain-name>'/'group-name'`. You can also specify a group using its OCID, in the format `group id <group-ocid>`.
     * `<compartment-name>` is the name of the compartment containing the master encryption key.
     * `<key-OCID>` is the OCID of the master encryption key in Vault.
For example:
```
Allow group acme-dev-team to read keys in compartment acme-kms-key-compartment where target.key.id = 'ocid1.key.oc1.iad.anntl______usjh'
Allow service oke to use key-delegates in compartment acme-kms-key-compartment where target.key.id = 'ocid1.key.oc1.iad.anntl______usjh'
Allow service blockstorage to use keys in compartment acme-kms-key-compartment where target.key.id = 'ocid1.key.oc1.iad.anntl______usjh'
Allow any-user to use key-delegates in compartment acme-kms-key-compartment where ALL {request.principal.type='nodepool', target.key.id = 'ocid1.key.oc1.iad.anntl______usjh'}
```

**Note**
After August 15, 2024, create the `Allow any-user...` policy statement as shown, namely: 
```
Allow any-user to use key-delegates in <compartment-name> where ALL {request.principal.type='nodepool', target.key.id = '<key_OCID>'}
```

Note that before August 15, 2024, you had to define the following `Allow service oke...` policy statement:
```
Allow service oke to use key-delegates in compartment <compartment-name> where target.key.id = '<key_OCID>' 
```

If such an `Allow service oke...` policy statement already exists, keep this existing policy statement, and create the new `Allow any-user...` policy statement in addition to the existing policy statement.
  6. **For block volumes:** To use a master encryption key from the Vault service to encrypt data in block volumes, enter policy statements to grant access to the master encryption key in the format:
Copy
```
Allow service blockstorage to use keys in compartment <compartment-name> where target.key.id = '<key-ocid>'
```

Copy
```

Allow any-user to use key-delegates in compartment <compartment-name> where ALL {request.principal.type = 'cluster', target.key.id = '<key-ocid>'}
```

where:
     * `<compartment-name>` is the name of the compartment containing the master encryption key.
     * `<key-OCID>` is the OCID of the master encryption key in Vault.
For example:
Copy
```
Allow service blockstorage to use keys in compartment acme-kms-key-compartment where target.key.id = 'ocid1.key.oc1.iad.anntl______usjh'
Allow any-user to use key-delegates in compartment acme-kms-key-compartment where ALL {request.principal.type = 'cluster', target.key.id = 'ocid1.key.oc1.iad.anntl______usjh'}
```

  7. **For file systems:** To use a master encryption key from the Vault service to encrypt data in file systems, enter policy statements to grant access to the master encryption key in the format:
Copy
```
Allow dynamic-group <dynamic-group-name> to use keys in compartment <key-compartment-name>
```

Copy
```

Allow any-user to use key-delegates in compartment <compartment-name> where ALL {request.principal.type = 'cluster', target.key.id = '<key_OCID>'}
```

where:
     * `<dynamic-group-name>` is the name of the [dynamic group](https://docs.oracle.com/iaas/Content/Identity/dynamicgroups/managingdynamicgroups.htm) of file systems in the compartment. 
An example rule for the dynamic group follows:
Copy
```
ALL { resource.type='filesystem', resource.compartment.id = '<file_system_compartment_OCID>' }
```

Note that if a dynamic group is not in the default identity domain, prefix the dynamic group name with the identity domain name, in the format `dynamic-group '<identity-domain-name>'/'<dynamic-group-name>'`. You can also specify the dynamic group using its OCID, in the format `dynamic-group id <dynamic-group-ocid>`.
     * `<compartment-name>` is the name of the compartment containing the master encryption key.
     * `<key_OCID>` is the OCID of the master encryption key in Vault.
For example:
Copy
```
Allow dynamic-group FssFileSystems to use keys in compartment acme-kms-key-compartment
Allow any-user to use key-delegates in compartment acme-kms-key-compartment where ALL {request.principal.type = 'cluster', target.key.id = 'ocid1.key.oc1.iad.anntl______usjh'}
```

  8. Click **Create**. 


Was this article helpful?
YesNo

