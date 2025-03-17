Updated 2023-09-25
# Compute Targets
Use Oracle Cloud Infrastructure Vulnerability Scanning Service to create and manage compute (host) targets and to assign them to Compute scan recipes. A target is a collection of **instances** that you want routinely scanned for security vulnerabilities.
The Vulnerability Scanning service detects vulnerabilities in the following platforms and using the following vulnerability sources.
Platform | [National Vulnerability Database](https://nvd.nist.gov/) (NVD) | Open Vulnerability and Assessment Language (OVAL) | [Center for Internet Security](https://www.cisecurity.org/cis-benchmarks/) (CIS)  
---|---|---|---  
Oracle Linux | Yes | Yes | Yes  
CentOS | Yes | Yes | Yes  
Ubuntu | Yes | Yes | Yes  
Windows | Yes | No | No  
You have two options when selecting the Compute instances for a target.
  * Scan one or more specific instances within a compartment.
  * Scan all instances within a compartment and its subcompartments.


If you create a target for the root compartment, then all Compute instances in the entire tenancy are scanned.
The Vulnerability Scanning service saves the results for a Compute instance in the same compartment as the instance's Vulnerability Scanning target.
Consider the following example.
  * The Compute instance `MyInstance` is in `CompartmentA`.
  * `MyInstance` is specified in `Target1`.
  * `Target1` is in `CompartmentB`.
  * All reports related to `MyInstance` are in `CompartmentB`.


Cloud Guard targets are separate resources from Vulnerability Scanning targets. To use Cloud Guard to detect problems in Vulnerability Scanning reports, the Vulnerability Scanning target compartment must be the same as the Cloud Guard target compartment, or be a subcompartment of the Cloud Guard target compartment.
This section contains the following topics:
  * [Creating a Compute Target](https://docs.oracle.com/en-us/iaas/scanning/using/create-host-target.htm#create_host_target "Create a Compute \(host\) scan target.")
  * [Editing a Compute Target](https://docs.oracle.com/en-us/iaas/scanning/using/update-host-target.htm#update_host_target "Use the Console to update an existing Compute \(host\) scan target.")
  * [Listing the Compute Instances for a Target](https://docs.oracle.com/en-us/iaas/scanning/using/view-host-target-instances.htm#view_host_target_instances "View the Compute instances \(hosts\) associated with an existing target.")
  * [Listing the Compute Instance Errors for a Target](https://docs.oracle.com/en-us/iaas/scanning/using/view_host_target_instance_erros.htm#view_host_target_instance_erros "View the Compute instance \(hosts\) errors associated with an existing target.")
  * [Getting a Compute Target's Details](https://docs.oracle.com/en-us/iaas/scanning/using/get-host-target.htm#get-host-target "View a Compute target's details.")
  * [Moving a Compute Target Between Compartments](https://docs.oracle.com/en-us/iaas/scanning/using/move_host_target.htm#move_host_target "Move a compute \(host\) target into a different compartment.")
  * [Deleting a Compute Target](https://docs.oracle.com/en-us/iaas/scanning/using/delete_host_target.htm#delete_host_target "Delete a compute \(host\) target.")


Was this article helpful?
YesNo

