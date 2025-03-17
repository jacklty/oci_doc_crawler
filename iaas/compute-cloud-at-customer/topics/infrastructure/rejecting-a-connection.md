Updated 2024-04-15
# Rejecting a Connection
If the Compute Cloud@Customer infrastructure connection is broken, or you believe the security of the connection has been compromised, or you want to make a new connection, reject the connection. This puts the connection into a REJECT state.
For more information about connection states, see [Viewing the Connection State](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/infrastructure/viewing-the-connection-state.htm#viewing-the-connection-state "You can view the connection state of a Compute Cloud@Customer infrastructure. The connection state indicates the condition of the connection of the Compute Cloud@Customer infrastructure in your data center to your OCI tenancy.").
**Important**
The infrastructure connection state must remain in the REJECT state for a minimum of 20 minutes before you connect the infrastructure. See [Connecting a Compute Cloud@Customer Infrastructure to OCI](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/infrastructure/connecting.htm#connecting "The Compute Cloud@Customer infrastructure in the data center needs to be connected to Oracle Cloud Infrastructure \(OCI\) before it can be used. This task involves a bootstrap process during which a secure connection is established.").
  * [Console](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/infrastructure/rejecting-a-connection.htm)
  * [CLI](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/infrastructure/rejecting-a-connection.htm)
  * [API](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/infrastructure/rejecting-a-connection.htm)


  *     1. In the Oracle Cloud Console, open the navigation menu, click **Hybrid** , and then click **Oracle Compute Cloud@Customer**.
    2. Click **Infrastructures**.
    3. In the list of infrastructures, find the one that you want to disconnect from the infrastructure in your data center. If you don't see the infrastructure that you want, you might need to change compartments.
    4. Click the Actions menu (![An image of the three dot icon.](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/images/three-dots.png)), and select **Reject connection**.
The connection state changes to **REJECT**.
To reconnect the infrastructure, see [Connecting a Compute Cloud@Customer Infrastructure to OCI](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/infrastructure/connecting.htm#connecting "The Compute Cloud@Customer infrastructure in the data center needs to be connected to Oracle Cloud Infrastructure \(OCI\) before it can be used. This task involves a bootstrap process during which a secure connection is established.").
  * Use the [ccc infrastructure update](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/ccc/infrastructure/update.html) command and required parameters to update a Compute Cloud@Customer infrastructure, including the connection state.
Copy
```
oci ccc infrastructure update --infrastructure-id <infrastructure_OCID> --connection-state REJECT [OPTIONS]
```

For a complete list of CLI commands, flags, and options, see the [Command Line Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/index.html).
  * Use the [UpdateCccInfrastructure](https://docs.oracle.com/iaas/api/#/en/compute-cloud-at-customer/latest/CccInfrastructure/UpdateCccInfrastructure) operation to update a Compute Cloud@Customer infrastructure, including the connection state.
For information about using the API and signing requests, see [REST APIs](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm#REST_APIs) and [Security Credentials](https://docs.oracle.com/iaas/Content/General/Concepts/credentials.htm). For information about SDKs, see [Software Development Kits and Command Line Interface](https://docs.oracle.com/iaas/Content/API/Concepts/sdks.htm#Software_Development_Kits_and_Command_Line_Interface).


Was this article helpful?
YesNo

