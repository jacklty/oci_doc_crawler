Updated 2025-03-10
# Viewing Details for an Attached Domain
View details about a domain attached to a Traffic Management steering policy.
See [Overview of Traffic Management](https://docs.oracle.com/en-us/iaas/Content/TrafficManagement/Concepts/overview.htm#overview "Traffic Management helps you guide traffic to endpoints based on various conditions, including endpoint health and the geographic origins of DNS requests.") for a feature overview and more information about traffic management steering policies and domain attachments.
  * [Console](https://docs.oracle.com/en-us/iaas/Content/TrafficManagement/Tasks/tm-policy-attach-get.htm)
  * [CLI](https://docs.oracle.com/en-us/iaas/Content/TrafficManagement/Tasks/tm-policy-attach-get.htm)
  * [API](https://docs.oracle.com/en-us/iaas/Content/TrafficManagement/Tasks/tm-policy-attach-get.htm)


  * Use these steps to view information about the domain (zone) attached to a policy.
    1. Open the **navigation menu** and select **Networking**. Under **DNS management** , select **Traffic management steering policies**.
    2. Select a compartment from the list.
    3. Select the name of the policy you want to view domain attachments for.
**Tip** You can use search for a policy by name in the **Search** field. You can also use the **Time Created** sort filter to sort the policies chronologically in ascending or descending order.
    4. Under **Resources** , select **Attached domains**.
Domain attachments are listed in tabular form.
    5. Select the domain name to view details about it. 
The domain's zone details page contains information about the domain zone, both general information and links to its resources. Items in this page are read-only.
  * Use the [steering-policy get](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/dns/steering-policy/get.html) command and required parameters to view details about a steering policy attachment.
Command
CopyTry It
```
oci dns steering-policy-attachment get --steering-policy-id steering_policy_OCID ... [OPTIONS]
```

For a complete list of flags and variable options for CLI commands, see the [CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest).
  * Run the [GetSteeringPolicy](https://docs.oracle.com/iaas/api/#/en/dns/latest/SteeringPolicy/GetSteeringPolicy) operation to view details about a steering policy domain attachment.


Was this article helpful?
YesNo

