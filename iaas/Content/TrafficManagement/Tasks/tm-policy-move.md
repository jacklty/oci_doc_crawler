Updated 2025-03-10
# Moving a Steering Policy Between Compartments
Move a steering policy from one compartment to another. 
See [Managing Compartments](https://docs.oracle.com/iaas/Content/Identity/compartments/managingcompartments.htm) for information about compartments and access control.
See [Overview of Traffic Management](https://docs.oracle.com/en-us/iaas/Content/TrafficManagement/Concepts/overview.htm#overview "Traffic Management helps you guide traffic to endpoints based on various conditions, including endpoint health and the geographic origins of DNS requests.") for a feature overview and more information about traffic management steering policies.
  * [Console](https://docs.oracle.com/en-us/iaas/Content/TrafficManagement/Tasks/tm-policy-move.htm)
  * [CLI](https://docs.oracle.com/en-us/iaas/Content/TrafficManagement/Tasks/tm-policy-move.htm)
  * [API](https://docs.oracle.com/en-us/iaas/Content/TrafficManagement/Tasks/tm-policy-move.htm)


  *     1. Open the **navigation menu** and select **Networking**. Under **DNS management** , select **Traffic management steering policies**.
    2. Select a compartment from the list.
All steering policies are listed in tabular form.
    3. Select the policy in the list you want to edit, and then select **Move resource** from the Actions menu (![Actions Menu](https://docs.oracle.com/en-us/iaas/Content/libraries/global-images/actions-menu.png)).
    4. Select a destination compartment from the list.
    5. Select **Move resource**.
  * Use the [steering-policy change-compartment](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/dns/steering-policy/change-compartment.html) command and required parameters to move a steering policy to a different compartment:
Command
CopyTry It
```
oci dns steering-policy change-compartment --steering-policy-id steering_policy_OCID --compartment-id compartment_OCID ... [OPTIONS]
```

For a complete list of flags and variable options for CLI commands, see the [CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest).
  * Run the [ChangeSteeringPolicyCompartment](https://docs.oracle.com/iaas/api/#/en/dns/latest/SteeringPolicy/ChangeSteeringPolicyCompartment) operation to move a steering policy from one compartment to another.


Was this article helpful?
YesNo

