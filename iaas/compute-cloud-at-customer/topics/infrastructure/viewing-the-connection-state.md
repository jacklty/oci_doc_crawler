Updated 2024-04-01
# Viewing the Connection State
You can view the connection state of a Compute Cloud@Customer infrastructure. The connection state indicates the condition of the connection of the Compute Cloud@Customer infrastructure in your data center to your OCI tenancy.
These are the possible states:
  * `REJECT`
  * `REQUEST`
  * `READY`
  * `CONNECTED`
  * `DISCONNECTED`


You can only update the state from `REQUEST` to `READY` (see [Connecting a Compute Cloud@Customer Infrastructure to OCI](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/infrastructure/connecting.htm#connecting "The Compute Cloud@Customer infrastructure in the data center needs to be connected to Oracle Cloud Infrastructure \(OCI\) before it can be used. This task involves a bootstrap process during which a secure connection is established.")), or from any state back to `REJECT` (see [Rejecting a Connection](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/infrastructure/rejecting-a-connection.htm#rejecting-a-connection "If the Compute Cloud@Customer infrastructure connection is broken, or you believe the security of the connection has been compromised, or you want to make a new connection, reject the connection. This puts the connection into a REJECT state.")). 
The system automatically handles the `REJECT` to `REQUEST`, `READY` to `CONNECTED`, or `CONNECTED` to `DISCONNECTED` transitions.
  * [Console](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/infrastructure/viewing-the-connection-state.htm)
  * [CLI](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/infrastructure/viewing-the-connection-state.htm)
  * [API](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/infrastructure/viewing-the-connection-state.htm)


  *     1. In the Oracle Cloud Console, open the navigation menu, click **Hybrid** , and then click **Oracle Compute Cloud@Customer**.
    2. Click **Infrastructures**.
    3. In the list of infrastructures, view the Connection state column. If you don't see the infrastructure that you want, you might need to change compartments.
  * Use the [oci ccc infrastructure list](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/ccc/infrastructure/list.html) command and required parameters to view a list of Compute Cloud@Customer infrastructures and parameters such as the connection state.
Copy
```
oci ccc infrastructure list [OPTIONS]
```

Example of listing all infrastructures in a specified compartment:
```
oci ccc infrastructure list -c <compartment_OCID> --all
{
 "data": {
   "items": [
      {
        "compartment-id": "<compartment_OCID>",
        "connection-state": "REJECT",
        "defined-tags": {
           "Oracle-Tags": {
             "CreatedBy": "user",
             "CreatedOn": "2023-07-28T12:53:26.934Z"
           }
        },
        "display-name": "TestInfrastructure",
        "freeform-tags": {},
        "id": "<infrastructure_OCID>",
        "lifecycle-state": "ACTIVE",
        "short-name": "<infrastructure_SHORTNAME>",
        "subnet-id": "<subnet_OCID>",
        "system-tags": {},
        "time-created": "2023-07-28T12:53:27.141000+00:00"
      },
      {
        "compartment-id": "<compartment_OCID>",
        "connection-state": "CONNECTED",
        "defined-tags": {
           "Oracle-Tags": {
             "CreatedBy": "user",
             "CreatedOn": "2023-07-18T08:39:53.201Z"
           }
        },
        "display-name": "some text",
        "freeform-tags": {},
        "id": "<infrastructure_OCID>",
        "lifecycle-state": "ACTIVE",
        "short-name": "<infrastructure_SHORTNAME>",
        "subnet-id": "<subnet_OCID>",
        "system-tags": {},
        "time-created": "2023-07-18T08:39:53.433000+00:00"
      },
 }
}
```

For a complete list of CLI commands, flags, and options, see the [Command Line Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/index.html).
  * Use the [ListCccInfrastructures](https://docs.oracle.com/iaas/api/#/en/compute-cloud-at-customer/20221208/CccInfrastructureCollection/ListCccInfrastructures) operation to view a list of Compute Cloud@Customer infrastructures.
For information about using the API and signing requests, see [REST APIs](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm#REST_APIs) and [Security Credentials](https://docs.oracle.com/iaas/Content/General/Concepts/credentials.htm). For information about SDKs, see [Software Development Kits and Command Line Interface](https://docs.oracle.com/iaas/Content/API/Concepts/sdks.htm#Software_Development_Kits_and_Command_Line_Interface).


Was this article helpful?
YesNo

