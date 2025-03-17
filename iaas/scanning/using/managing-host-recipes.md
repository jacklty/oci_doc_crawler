Updated 2023-09-25
# Compute Scan Recipes
Use Oracle Cloud Infrastructure Vulnerability Scanning Service to create and manage recipes that scan target compute **instances** (hosts) for potential security vulnerabilities.
A recipe determines which types of security issues that you want scanned:
  * Port scanning: check for open ports using a network mapper that searches your **public IP addresses**
  * Agent-based scanning:
    * Check for open ports on all attached **VNICs** , including VNICs for both public and private IP addresses
    * Check for OS vulnerabilities like missing patches
    * Check for compliance with industry-standard benchmarks published by the [Center for Internet Security](https://www.cisecurity.org/cis-benchmarks/) (CIS)
    * Check for vulnerabilities in third-party application files


The Vulnerability Scanning service checks hosts for compliance with the section 5 (Access, Authentication, and Authorization) benchmarks defined for [Distribution Independent Linux](https://www.cisecurity.org/benchmark/distribution_independent_linux).
A host scan recipe also defines a schedule, or how often scanning is performed.
This section contains the following topics:
  * [Creating a Compute Scan Recipe](https://docs.oracle.com/en-us/iaas/scanning/using/create-host-recipe.htm#create_host_recipe "Create a Compute \(host\) scan recipe with or without a host agent.")
  * [Creating a Compute Scan Recipe with an OCI Agent](https://docs.oracle.com/en-us/iaas/scanning/using/create-host-recipe-oci-agent.htm#create-host-recipe-oci-agent "Create a Compute \(host\) scan recipe using the OCI agent included with your Oracle Cloud Infrastructure account and then view the results in the Console.")
  * [Creating a Compute Scan Recipe with a Qualys Agent](https://docs.oracle.com/en-us/iaas/scanning/using/create-host-recipe-qualys-agent.htm#create-host-recipe-qualys-agent "Create a Compute \(host\) scan recipe using your own Qualys license and then view the results in the Console or the Qualys dashboard.")
  * [Listing Compute Scan Recipes](https://docs.oracle.com/en-us/iaas/scanning/using/list-host-recipe.htm#list-host-recipe "View a list of Compute \(host\) scan recipes for a compartment.")
  * [Getting a Compute Scan Recipe's Details](https://docs.oracle.com/en-us/iaas/scanning/using/get-host-recipe.htm#get-host-recipe "Get a Compute \(host\) scan recipe's details.")
  * [Editing a Compute Scan Recipe](https://docs.oracle.com/en-us/iaas/scanning/using/update-host-recipe.htm#update_host_recipe "Edit an existing Compute \(host\) scan recipe.")
  * [Defining a Secret for a Compute Scan Recipe](https://docs.oracle.com/en-us/iaas/scanning/using/define-secret-for-scan-recipe.htm#define-secret-for-scan-recipe "Create a secret for a Compute \(host\) scan recipe to store the Qualys license information.")
  * [Moving a Compute Scan Recipe Between Compartments](https://docs.oracle.com/en-us/iaas/scanning/using/move_host_recipe.htm#move_host_recipe "Move a Compute \(host\) scan recipe from one compartment to another.")
  * [Deleting a Compute Scan Recipe](https://docs.oracle.com/en-us/iaas/scanning/using/delete_host_recipe.htm#delete_host_recipe "Delete a Compute \(host\) scan recipe.")


Was this article helpful?
YesNo

