Updated 2024-09-16
# Getting a Windows Instance's Credentials for a Roving Edge Infrastructure Device
Describes how to get Windows instance credentials on your Roving Edge Infrastructure device.
See [Connecting to Your Windows Instance](https://docs.oracle.com/iaas/Content/GSG/Tasks/testingconnectionWindows.htm) in the Oracle Cloud Infrastructure documentation for more information on this feature.
Use the [oci compute instance get-windows-initial-creds](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/compute/instance/get-windows-initial-creds.html) command and required parameters to get Windows instance credentials on your Roving Edge Infrastructure devices:
Copy
```
oci compute instance get-windows-initial-creds --instance-id instance_ocid [OPTIONS]
```

Refer to your Roving Edge Infrastructure device's CLI help for a list of parameters available for this command. See [Accessing Command Line Interface Help](https://docs.oracle.com/en-us/iaas/Content/Rover/Access/cli_install.htm#CLIAccessHelp).
For CLI setup information on your Roving Edge Infrastructure device, see [Using the Command Line Interface.](https://docs.oracle.com/en-us/iaas/Content/Rover/Access/cli_install.htm#CLI "Describes how to use the Command Line Interface to access a a Roving Edge Infrastructure device.")
Was this article helpful?
YesNo

