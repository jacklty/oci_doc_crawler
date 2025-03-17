Updated 2024-12-16
# Creating an Instance Console Connection
On Compute Cloud@Customer, before you can connect to an instance VNC console or serial console, you need to create an instance console connection.
**Note** Instance console connections are limited to one client at a time. If the client attempts to connect but fails to connect within five minutes, the connection is closed and a different client can connect. During the five-minute timeout, any attempt to connect a different client fails.
The instance console connection resource provides the command that you need to create the secure tunnel. The command is a little different depending on whether your local system is UNIX or Windows and whether you want to connect to the VNC console or the serial console on the instance.
## Console Connection Prerequisites 🔗 
Ensure that you have the following resources on the system that you plan to use to connect to the instance console.
  * The console connection needs access to port 1443. Previously, port 443 was used for VM console access. For more information, see [Network Port and Protocol Matrix](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/security/network-port-and-protocol-matrix.htm#network-port-and-protocol-matrix "Compute Cloud@Customer requires access permissions to be granted for certain IP addresses, ports, and protocols.").
  * SSH key pair
If you don't already have an SSH key pair, you can use the `ssh-keygen` utility on UNIX systems or PuTTY `puttygen.exe` on Windows systems. Specify a key size of 2048 bits (this value should be the default). Give the key a name. You don't need to provide a passphrase; using a passphrase makes it more difficult to automate connecting. 
  * Command-line shell and SSH client
On Windows systems, use one of the following:
    * Windows PowerShell
If you use PowerShell to connect to the VNC server on the instance, `plink.exe` is required. `plink.exe` is the command link connection tool included with PuTTY. You can install PuTTY or install `plink.exe` separately.
    * Git for Windows
Git for Windows includes OpenSSH.
    * Windows Subsystem for Linux (WSL)
WSL includes OpenSSH.
  * VNC viewer to connect to the VNC console
  * Ensure that you belong to a group that has the following permissions. Note – groups and policies are managed in your OCI tenancy, and not managed directly on Compute Cloud@Customer. See [IAM Overview](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/iam/identify-learn.htm#identify-learn "On Compute Cloud@Customer, the Oracle Cloud Infrastructure Identity and Access Management \(IAM\) service lets you control who has access to the cloud resources within your tenancies.").
```
Allow group **_group_name_** to manage instance-console-connection in tenancy
Allow group **_group_name_** to read instance in tenancy
```



  * [Console](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/compute/creating-an-instance-console-connection.htm)
  * [CLI](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/compute/creating-an-instance-console-connection.htm)
  * [API](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/compute/creating-an-instance-console-connection.htm)


  *     1. In the [Compute Cloud@Customer Console](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/overview/compute-cloud-customer-console.htm#accessing-the-console "Use the Compute Cloud@Customer Console to create and manage compute, storage and other resources on a Compute Cloud@Customer infrastructure.") navigation menu, click **Compute** , then click **Instances**.
    2. At the top of the page, select the compartment that contains the instance.
    3. Click the name of the instance where you want to create a console connection.
    4. On the instance details page, under **Resources** , click **Console Connection**.
    5. If a console connection doesn't already exist, click **Create Console Connection**.
    6. Provide the public key portion of your SSH key.
In the **Create Console Connection** dialog box, do one of the following to enter your public SSH key:
       * Select the key file(s).
         * Click inside the Drag and Drop box to open a file browser and select the file.
         * Drag the file from your file browser listing and drop the file on the Drag and Drop box.
       * Paste the public key(s). Copy your public SSH key text, and paste the text into the field.
    7. Click **Create Console Connection** in the dialog.
When the console connection is created and is available, the state changes to **Active**.
**What's Next**
Continue to [Connecting to the VNC Console](https://docs.oracle.com/iaas/Content/Compute/References/serialconsole.htm#Connecti) or [Making a Local Connection to the Serial Console](https://docs.oracle.com/iaas/Content/Compute/References/serialconsole.htm#Connecti2).
  * Use the [oci compute instance-console-connection create](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/compute/instance-console-connection/create.html) command and required parameters to create a new serial console connection to the specified instance. Once the serial console connection is created and is available, you connect to the serial console using an SSH client.
Copy
```
oci compute instance-console-connection create --instance-id <instance_OCID> --ssh-public-key-file public_SSH_key_path [OPTIONS]
```

For a complete list of CLI commands, flags, and options, see the [Command Line Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/index.html).
**Procedure**
    1. Get the following information:
       * The OCID of the instance where you want to create the console connection: `oci compute instance list`
       * Your SSH public key file.
    2. Determine whether a console connection already exists for this instance.
```
oci compute instance-console-connection list -c compartment_OCID --instance-id instance_OCID
```

    3. Run the create console connection command.
```
oci compute instance-console-connection create --instance-id ocid1.instance._unique_ID_ --ssh-public-key-file _public_SSH_key_path_
{
 "data": {
  "compartment-id": "ocid1.compartment.**_unique_ID_**",
  "connection-string": "ssh -i **_private_SSH_key_path_** -t -p 443 **_user_name_**@**_proxy_host_** tty@**_instance_OCID_**",
  "defined-tags": {},
  "fingerprint": "SHA256:**_unique_ID_**",
  "freeform-tags": {},
  "id": "ocid1.instanceconnectionconsole.**_unique_ID_**",
  "instance-id": "ocid1.instance.**_unique_ID_**",
  "lifecycle-state": "ACTIVE",
  "service-host-key-fingerprint": null,
  "vnc-connection-string": "ssh -i **_public_SSH_key_path_** -p 443 -L **_local_vnc_port_**:localhost:**_remote_vnc_port_** **_user_name_**@**_proxy_host_** vnc@ocid1.instance.**_unique_ID_**"
 },
 "etag": "afc7eb68-5f1a-40cc-8dc3-8a1cae237230"
}
```

The value of `connection-string` is the SSH connection string for the instance serial console connection. The value of `vnc-connection-string` is the SSH connection string for the instance VNC console connection.
    4. When you're finished using this instance console connection, use the following command to delete the connection.
```
$ oci compute instance-console-connection delete --instance-console-connection-id instance_console_connection_OCID
```

**What's Next**
Continue to [Connecting to the VNC Console](https://docs.oracle.com/iaas/Content/Compute/References/serialconsole.htm#Connecti) or [Making a Local Connection to the Serial Console](https://docs.oracle.com/iaas/Content/Compute/References/serialconsole.htm#Connecti2).
  * This task can't be performed using the API.
For information about using the API and signing requests, see [REST APIs](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm#REST_APIs) and [Security Credentials](https://docs.oracle.com/iaas/Content/General/Concepts/credentials.htm). For information about SDKs, see [Software Development Kits and Command Line Interface](https://docs.oracle.com/iaas/Content/API/Concepts/sdks.htm#Software_Development_Kits_and_Command_Line_Interface).


Was this article helpful?
YesNo

