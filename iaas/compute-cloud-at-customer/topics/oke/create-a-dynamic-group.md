Updated 2024-12-16
# Create a Dynamic Group and Policies (Using the Oracle Cloud Console)
In your OCI tenancy that's associated with Compute Cloud@Customer, create a dynamic group and policies to authorize member instances to manage OKE resources. 
These procedures use the OCI Oracle Cloud Console. Or, you can create the group and policies [using Terraform scripts](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/oke/create-a-dynamic-group-using-terraform-scripts.htm#create-a-dynamic-group-using-terraform-scripts "You can use Terraform scripts to automate the creation of a dynamic group and policies to authorize member instances to manage OKE resources."). 
## Create a Dynamic Group 🔗 
If your tenancy uses IAM with Identity Domains, use the procedure in this section.
If your tenancy uses IAM without Identity Domains, instead, see [Managing Dynamic Groups](https://docs.oracle.com/iaas/Content/Identity/Tasks/managingdynamicgroups.htm), and follow the steps under Using the Console to create a dynamic group.
  1. In the OCI Oracle Cloud Console, open the navigation menu and click **Identity & Security**. Under **Identity** , click ****Domains** **.
  2. Select the identity domain you want to work in.
You might need to select a different compartment to find the domain.
  3. In the left panel, click **Dynamic groups.**
  4. Click **Create Dynamic Group**. 
  5. Enter the following information: 
     * **Name:** Enter a unique name for the group. The name must be unique across all groups in your tenancy (dynamic groups and user groups). You can't change this later. Avoid entering confidential information.
     * **Description:** Enter a description.
Enter the following **Matching Rule** , exactly as shown, to define the group:
Copy
```
tag.OraclePCA-OKE.cluster_id.value
```

All cluster nodes that have this tag are members of the dynamic group. 
  6. Click **Create**.


**What's Next:** [Create a Policy for the Dynamic Group](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/oke/create-a-dynamic-group.htm#create-a-dynamic-group__create-dynamic-group-policy)
## Create a Policy for the Dynamic Group 🔗 
If your tenancy uses IAM with Identity Domains, use the procedure in this section.
If your tenancy uses IAM without Identity Domains, instead, see [Managing Policies, Using the Console](https://docs.oracle.com/iaas/Content/Identity/Tasks/managingpolicies.htm#three).
  1. Open the navigation menu, and click **Identity & Security**. Under **Identity** , click **Policies**.
  2. Click **Create Policy**.
For a full description of the ways you can enter policies, see [Creating a Policy](https://docs.oracle.com/iaas/Content/Identity/policymgmt/managingpolicies_topic-To_create_a_policy.htm#To_create_a_policy).
  3. In the **Create Policy** panel, enter the following information:
     * **Name:** Enter a name for the policy. Avoid entering confidential information.
     * **Description:** Enter a description.
     * **Compartment:** Select the compartment for the policy.
     * **Policy Builder:** Define the policies for the dynamic group:
       1. Click the slider to **Show manual editor**.
       2. Enter the following policy rules. 
Replace <dynamic-group-name> with the dynamic group name you created:
```
allow dynamic-group <dynamic-group-name> to use instance-family in tenancy
allow dynamic-group <dynamic-group-name> to use virtual-network-family in tenancy
allow dynamic-group <dynamic-group-name> to manage load-balancers in tenancy
allow dynamic-group <dynamic-group-name> to manage volume-family in tenancy
allow dynamic-group <dynamic-group-name> to manage file-family in tenancy
```

       3. Click **Create**.


The OKE service is now ready for OKE users to manage OKE resources. To get started, see [Cluster Administrator Tasks](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/oke/user-tasks.htm#user-tasks "Perform a set of tasks to create OKE clusters on Compute Cloud@Customer.").
To learn how certificate authority bundles are handled, see [Certificate Authority Bundles](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/oke/updating-the-certificate-authority-bundle.htm#updating-the-certificate-authority-bundle "The Certificate Authority \(CA\) bundle for Compute Cloud@Customer is downloaded and made available to a cluster when the cluster is created. The CA bundle includes the certificate, private and public keys, and other authorization information.").
Was this article helpful?
YesNo

