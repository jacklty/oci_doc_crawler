Updated 2024-05-13
# Choosing Whether an Ephemeral Public IP is Assigned at Instance Creation
You can choose whether to assign an ephemeral public IP address to an instance when you create it.
  * [Console](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/assign-public-ip-instance-launch.htm)
  * [CLI](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/assign-public-ip-instance-launch.htm)
  * [API](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/assign-public-ip-instance-launch.htm)


  * When you [launch an instance](https://docs.oracle.com/iaas/Content/Compute/Tasks/launchinginstance.htm) into a [public subnet](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/overview.htm#Public), there's an **Assign a public IPv4 address** checkbox on the **Create Compute Instance** page. By default, the checkbox is selected, and the instance gets an ephemeral public IP. 
If you don't want an ephemeral public IP assigned, you can either:
    * Select the **Do not assign a public IPv4 address** option
    * [Delete the ephemeral public IP after instance launch](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/deleting-ephemeral-public-ip-from-instance.htm#top "Deleting an ephemeral public IP automatically unassigns it from its private IP.")
  * Use the [network public-ip create](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/network/public-ip/create.html) command and required parameters to assign a public IP:
Command
CopyTry It
```
oci network public-ip create --compartment-id compartment_OCID --lifetime EPHEMERAL
 --private-ip-id private_IP_OCID ... [OPTIONS]
```

For a complete list of parameters and values for CLI commands, see the [CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest).
  * Run the [CreatePublicIp](https://docs.oracle.com/iaas/api/#/en/iaas/latest/PublicIp/CreatePublicIp) operation to create a public IP.


Was this article helpful?
YesNo

