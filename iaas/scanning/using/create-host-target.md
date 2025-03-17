Updated 2023-09-25
# Creating a Compute Target
Create a Compute (host) scan target.
Before you create a Compute target, review the following information:
  * At least one Compute scan recipe must be in the tenancy before creating a target. See [Compute Scan Recipes](https://docs.oracle.com/en-us/iaas/scanning/using/managing-host-recipes.htm#managing_host_recipes "Use Oracle Cloud Infrastructure Vulnerability Scanning Service to create and manage recipes that scan target compute instances \(hosts\) for potential security vulnerabilities.").
  * If the Compute scan recipe is configured for **Agent Based Scanning** , you must give the Vulnerability Scanning service permission to deploy the agent before creating a target. See [Required IAM Policy for Compute Scanning Recipes](https://docs.oracle.com/en-us/iaas/scanning/using/required-iam-policy-host-scan.htm#required_iam_policy_host_scan "To use Oracle Cloud Infrastructure, you must be granted the required type of access in a written by an administrator, whether you're using the Console or the REST API with an SDK, CLI, or other tool.").
  * A Compute instance is associated with a **virtual cloud network (VCN)** and a **subnet**. If an instance in the target is on a **private subnet** or has no public IP address, the VCN must include a **service gateway** and a route rule for the service gateway. See [Access to Oracle Services: Service Gateway](https://docs.oracle.com/iaas/Content/Network/Tasks/servicegateway.htm).


  * [Console](https://docs.oracle.com/en-us/iaas/scanning/using/create-host-target.htm)
  * [CLI](https://docs.oracle.com/en-us/iaas/scanning/using/create-host-target.htm)
  * [API](https://docs.oracle.com/en-us/iaas/scanning/using/create-host-target.htm)


  * To create a Compute target, complete the following steps:
    1. Open the navigation menu and click **Identity & Security**. Under **Scanning** , click **Targets**.
    2. Select the compartment in which you want to create the target.
**Note** The Compute instances that you assign to this target can be in a different compartment than the target.
    3. Click the **Hosts** tab if not already selected.
    4. Click **Create**.
    5. Verify that the recipe type is **Compute**.
    6. Enter a name and description for the target.
Avoid entering confidential information.
    7. Select a scan recipe for the target.
    8. Select the target compartment that contains the Compute instances that you want to scan.
    9. Choose the instances for this target.
       * **All compute instances in the selected target compartment and its subcompartments**
       * **Selected compute instances in the selected target compartment** - Select individual Compute instances.
You can't create a target with a compartment or an instance that's already specified in another target. However, multiple targets can scan the same instance.
**Note**
Cloud Guard targets are separate resources from Vulnerability Scanning targets. To use Cloud Guard to detect problems in Vulnerability Scanning reports, the Vulnerability Scanning target compartment must be the same as the Cloud Guard target compartment, or be a subcompartment of the Cloud Guard target compartment.
    10. (Optional) Click **Show advanced options** to assign tags to the target.
If you have permissions to create a resource, you also have permissions to add free-form tags to that resource.
To add a defined tag, you must have permissions to use the tag namespace.
For more information about tagging, see [Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). If you're not sure if you should add tags, skip this option or ask your administrator. You can add tags later.
    11. Save the target by using one of the following methods:
       * Click **Create target** to create the recipe in Vulnerability Scanning.
       * Click **Save as stack** to manage the stack through the Resource Manager service. On the **Save as stack** window, complete the fields, and then click **Save**. For more information about stacks, see [Managing Stacks](https://docs.oracle.com/iaas/Content/ResourceManager/Tasks/stacks.htm).
After creating a target, Vulnerability Scanning checks the instances for security vulnerabilities and open ports based on the parameters and schedule that's configured in the recipe. You can view the results of these scans in the following reports:
    * [Host Scans](https://docs.oracle.com/en-us/iaas/scanning/using/host-scan-reports.htm#host_scan_reports "View host scans in Oracle Cloud Infrastructure Vulnerability Scanning Service to identify security vulnerabilities in your compute instances like open ports, critical OS patches, and failed benchmark tests.")
    * [Vulnerability Reports](https://docs.oracle.com/en-us/iaas/scanning/using/host-vulnerabilities-reports.htm#host_vulnerabilities_reports "Oracle Cloud Infrastructure Vulnerability Scanning Service scans your targets based on the schedule and scanning properties in the recipe assigned to each target. Use vulnerabilities reports to identify security issues in your targets like critical OS patches.")
You can also use Cloud Guard to view the results of the scans. See [Scanning with Cloud Guard](https://docs.oracle.com/en-us/iaas/scanning/using/scanning-with-cloud-guard.htm#scanning_with_cloud_guard "Use Cloud Guard to detect and respond to security vulnerabilities identified by Oracle Cloud Infrastructure Vulnerability Scanning Service.").
  * Use the [oci vulnerability-scanning host scan target create](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/vulnerability-scanning/host/scan/target/create.html) command and required parameters to create a new compute (host) target:
Command
CopyTry It
```
oci vulnerability-scanning host scan target create --display-name <name> --description "<description>" --compartment-id <create_in_compartment_ocid> --host-scan-recipe-id <recipe_ocid> --target-compartment-id <target_compartment_ocid> --instance-ids <compute_instance_ocids>
```

For example, to scan all Compute instances in a compartment:
```
oci vulnerability-scanning host scan target create --display-name MyTarget --description "All instances in compartment ABC" --compartment-id ocid1.compartment.oc1..exampleuniqueID1 --host-scan-recipe-id ocid1.vsshostscanrecipe.oc1..exampleuniqueID --target-compartment-id ocid1.compartment.oc1..exampleuniqueID2
```

For a complete list of flags and variable options for CLI commands, see the [Command Line Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/index.html).
  * Run the [CreateHostScanTarget](https://docs.oracle.com/iaas/api/#/en/scanning/latest/HostScanTarget/CreateHostScanTarget) operation to create a new compute (host) target.


Was this article helpful?
YesNo

