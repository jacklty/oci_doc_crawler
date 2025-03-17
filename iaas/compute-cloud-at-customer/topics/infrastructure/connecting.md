Updated 2024-08-06
# Connecting a Compute Cloud@Customer Infrastructure to OCI
The Compute Cloud@Customer infrastructure in the data center needs to be connected to Oracle Cloud Infrastructure (OCI) before it can be used. This task involves a bootstrap process during which a secure connection is established.
**Important**
A connected system moves to a REJECT state after 90 days of continuous operation to force a refresh of the connection. After the system is moved to REJECT, you must reconnect the infrastructure.
When the infrastructure is in a REJECT state, your Compute Cloud@Customer workloads continue to run. However, the synchronization of the information between the infrastructure and OCI stops until the connection is reestablished.
Use the instructions in this section to connect the Compute Cloud@Customer infrastructure that's in your data center to your OCI tenancy. 
Connecting an infrastructure applies to the following situations:
  * After a new Compute Cloud@Customer infrastructure is installed in your data center.
  * If a prolonged connection outage occurs, lasting more than 15 minutes.
  * You're coming up on 90 days of uninterrupted connectivity and you want to proactively refresh the connection to avoid the forced connection refresh.
  * You believe the security of the connection has been compromised.


**Prerequisites:**
  * A Compute Cloud@Customer infrastructure must be set up in OCI. Follow the steps in [Creating a Compute Cloud@Customer Infrastructure in OCI](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/infrastructure/create-infrastructure.htm#create-infrastructure "Create a Compute Cloud@Customer infrastructure in Oracle Cloud Infrastructure \(OCI\) to communicate with the corresponding infrastructure in the data center.").
  * The Compute Cloud@Customer infrastructure must be installed in your data center. Oracle does this by using the information that you have provided.
  * The connection must be in the **REJECT** connection state for a minimum of 20 minutes before you reconnect an infrastructure. See [Viewing the Connection State](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/infrastructure/viewing-the-connection-state.htm#viewing-the-connection-state "You can view the connection state of a Compute Cloud@Customer infrastructure. The connection state indicates the condition of the connection of the Compute Cloud@Customer infrastructure in your data center to your OCI tenancy.").
Newly installed infrastructures are in the REJECT state by default. If you need to put the infrastructure into a REJECT state (for example, if you believe the security of the connection has been compromised), see [Rejecting a Connection](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/infrastructure/rejecting-a-connection.htm#rejecting-a-connection "If the Compute Cloud@Customer infrastructure connection is broken, or you believe the security of the connection has been compromised, or you want to make a new connection, reject the connection. This puts the connection into a REJECT state.").


  * [Console](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/infrastructure/connecting.htm)
  * [CLI](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/infrastructure/connecting.htm)
  * [API](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/infrastructure/connecting.htm)


  * To connect an infrastructure to OCI, follow these steps:
    1. In the Oracle Cloud Console, open the navigation menu, click **Hybrid** , and then click **Oracle Compute Cloud@Customer**.
    2. Click **Infrastructures**.
    3. In the list of infrastructures, find the one that you want to use to connect to the infrastructure in your data center. If you don't see the infrastructure that you want, you might need to change compartments.
The connection state is **REJECT** at this stage.
    4. Click the display name to open the infrastructure details page. 
    5. Copy the **Provisioning PIN**. 
    6. In a terminal window, use the `curl` command to provide the PIN and return the fingerprint:
```
curl -k -sS --header "Content-Type: application/json" --request POST --data '{"pin":"<Provisioning_PIN>"}' https://rps.<system>.<domain>/rps_pin
```

The connection state is now **Request** and the bootstrap process starts.
The fingerprint is returned in SHA 512 format as the value of a JSON key/value pair. For example `{"fingerprint":             "<provisioning_fingerprint>"}`
    7. Make note of the infrastructure fingerprint from the JSON output from the command in the previous step.
    8. Back on the infrastructure details page in the Oracle Cloud Console, view the provisioning fingerprint.
    9. Compare the fingerprints. 
       * If the fingerprints match, continue to the next step. 
       * If they don't match, go back to the infrastructures list page, click the Actions menu for the infrastructure, and select **Reject connection** to set the state back to **REJECT**. Then start again with a new provisioning PIN.
    10. Click **Accept connection**.
    11. In the **Accept connection** dialog box, click **Yes** to confirm that the fingerprints match and you want the connection to be made.
The connection state is now **Ready** and changes to **Connected** when the secure link is fully established.
**What's Next?**
Create an upgrade schedule. See [Creating a Compute Cloud@Customer Upgrade Schedule](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/infrastructure/create-upgrade-schedule.htm#create-upgrade-schedule "Create an upgrade schedule to allow Oracle to upgrade Compute Cloud@Customer hardware and software during defined time periods. After the upgrade schedule is created, attach the schedule to the infrastructures you want upgraded with the schedule.").
  *     1. Use the [ccc infrastructure get](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/ccc/infrastructure/get.html) command and required parameters to obtain the infrastructure details, including the **Provisioning PIN** : 
```
oci ccc infrastructure get --infrastructure-id <OCID of infrastructure to connect to> ... [OPTIONS]
```

    2. Copy the **Provisioning PIN**. 
    3. Connect to the infrastructure using `curl` to provide the PIN and return the fingerprint: 
```
curl -k -sS --header "Content-Type: application/json" --request POST --data '{"pin":"<Provisioning_PIN>"}' https://rps.<system>.<domain>/rps_pin
```

The fingerprint is returned in SHA 512 format as the value of a JSON key/value pair. For example `{"fingerprint":                 "<provisioning_fingerprint>"}`
    4. Use the [ccc infrastructure get](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/ccc/infrastructure/get.html) command again to query the infrastructure in OCI. Confirm that the state is **REQUEST** , and obtain the **Provisioning Fingerprint**.
    5. Compare the fingerprints.
       * If they match, use the [ccc infrastructure update](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/ccc/infrastructure/update.html) command to update the state to READY and accept the connection. 
```
oci ccc infrastructure update <OCID for infrastructure> --connection-state READY
```

       * If the fingerprints don't match, use the [ccc infrastructure update](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/ccc/infrastructure/update.html) command to update the state to REJECT and start again.```
oci ccc infrastructure update <OCID for infrastructure> --connection-state REJECT
```

For a complete list of CLI commands, flags, and options, see the [Command Line Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/index.html).
**What's Next?**
Create an upgrade schedule. See [Creating a Compute Cloud@Customer Upgrade Schedule](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/infrastructure/create-upgrade-schedule.htm#create-upgrade-schedule "Create an upgrade schedule to allow Oracle to upgrade Compute Cloud@Customer hardware and software during defined time periods. After the upgrade schedule is created, attach the schedule to the infrastructures you want upgraded with the schedule.").
  *     1. Use the [**GetCccInfrastructure**](https://docs.oracle.com/iaas/api/#/en/compute-cloud-at-customer/latest/CccInfrastructure/GetCccInfrastructure) operation to obtain the infrastructure details, including the **Provisioning PIN**.
    2. Copy the **Provisioning PIN**.
    3. Connect to the infrastructure using `curl` to provide the PIN and return the fingerprint: 
```
curl -k -sS --header "Content-Type: application/json" --request POST --data '{"pin":"<Provisioning_PIN>"}' https://rps.<system>.<domain>/rps_pin
```

The fingerprint is returned in SHA 512 format as the value of a JSON key/value pair. For example `{"fingerprint":             "<provisioning_fingerprint>"}`
    4. Use the [**GetCccInfrastructure**](https://docs.oracle.com/iaas/api/#/en/compute-cloud-at-customer/latest/CccInfrastructure/GetCccInfrastructure) operation again to query the infrastructure in OCI. Confirm that the state is **REQUEST** , and obtain the **Provisioning Fingerprint**.
    5. Compare the fingerprints.
       * If they match, use the [**UpdateInfrastructure**](https://docs.oracle.com/iaas/api/#/en/compute-cloud-at-customer/latest/CccInfrastructure/UpdateCccInfrastructure) operation to update the state to READY and accept the connection.
       * If the fingerprints don't match, use the use the [**UpdateInfrastructure**](https://docs.oracle.com/iaas/api/#/en/compute-cloud-at-customer/latest/CccInfrastructure/UpdateCccInfrastructure) operation to update the state to REJECT and start again.
For information about using the API and signing requests, see [REST APIs](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm#REST_APIs) and [Security Credentials](https://docs.oracle.com/iaas/Content/General/Concepts/credentials.htm). For information about SDKs, see [Software Development Kits and Command Line Interface](https://docs.oracle.com/iaas/Content/API/Concepts/sdks.htm#Software_Development_Kits_and_Command_Line_Interface).
**What's Next?**
Create an upgrade schedule. See [Creating a Compute Cloud@Customer Upgrade Schedule](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/infrastructure/create-upgrade-schedule.htm#create-upgrade-schedule "Create an upgrade schedule to allow Oracle to upgrade Compute Cloud@Customer hardware and software during defined time periods. After the upgrade schedule is created, attach the schedule to the infrastructures you want upgraded with the schedule.").


Was this article helpful?
YesNo

