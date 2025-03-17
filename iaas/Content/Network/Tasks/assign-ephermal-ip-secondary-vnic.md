Updated 2024-04-12
# Assigning an Ephemeral Public IP When Creating a Secondary VNIC
When you add a secondary VNIC to an instance, you choose whether the primary private IP on the new VNIC gets an ephemeral public IP. 
This choice is available only if the secondary VNIC is in a [public subnet](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/overview.htm#Public). 
  * [Console](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/assign-ephermal-ip-secondary-vnic.htm)
  * [CLI](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/assign-ephermal-ip-secondary-vnic.htm)
  * [API](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/assign-ephermal-ip-secondary-vnic.htm)


  * In the **Create VNIC** dialog box, there's an **Assign a public IPv4 address** checkbox. By default, the checkbox is unselected, which means the secondary VNIC doesn't get an ephemeral public IP. You must select **Assign a public IPv4 address**.
  * Use the [network public-ip create](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/network/public-ip/create.html) command and required parameters to assign a public IP:
Command
CopyTry It
```
oci network public-ip create --compartment-id compartment_ID --lifetime EPHEMERAL
 --private-ip-id private_IP_OCID ... [OPTIONS]
```

For a complete list of parameters and values for CLI commands, see the [CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest).
  * Run the [CreatePublicIp](https://docs.oracle.com/iaas/api/#/en/iaas/latest/PublicIp/CreatePublicIp) operation to create a public IP.


Was this article helpful?
YesNo

