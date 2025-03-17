Updated 2025-03-10
# Moving a TSIG Key Between Compartments
You can move a TSIG key from one compartment to another. 
See [Managing Compartments](https://docs.oracle.com/iaas/Content/Identity/compartments/managingcompartments.htm) for information about compartments and access control.
See [Managing TSIG Keys](https://docs.oracle.com/en-us/iaas/Content/DNS/Tasks/tsig.htm#manage-tsig "Transaction signature \(TSIG\), also referred to as Secret Key Transaction Authentication, ensures that domain name service \(DNS\) packets originate from an authorized sender by using shared secret keys and one-way hashing to add a cryptographic signature to the DNS packets.") for more information about TSIG keys and how they're used in zones.
For general service information, see the [DNS service overview](https://docs.oracle.com/en-us/iaas/Content/DNS/Concepts/dnszonemanagement.htm#overview "The DNS service helps you create and manage DNS zones.").
  * [Console](https://docs.oracle.com/en-us/iaas/Content/DNS/Tasks/tsig-key-move.htm)
  * [CLI](https://docs.oracle.com/en-us/iaas/Content/DNS/Tasks/tsig-key-move.htm)
  * [API](https://docs.oracle.com/en-us/iaas/Content/DNS/Tasks/tsig-key-move.htm)


  *     1. Open the **navigation menu** and select **Networking**. Under **DNS management** , select **TSIG keys**.
    2. Under **List scope** , select the compartment that contains the key.
    3. Select the name of the TSIG key to open its details page.
    4. Select **Move Resource**. 
    5. Select the destination compartment from the list.
    6. Select **Move Resource**.
  * Use the [tsig change-compartment](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/dns/tsig-key/change-compartment.html) command and required parameters to move a TSIG key to a different compartment:
Command
CopyTry It
```
oci dns tsig-key get --tsig-key-id tsig_key_OCID --compartment-id compartment_OCID ... [OPTIONS]
```

For a complete list of flags and variable options for CLI commands, see the [CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest).
  * Run the [ChangeTsigKeyCompartment](https://docs.oracle.com/iaas/api/#/en/dns/latest/TsigKey/ChangeTsigKeyCompartment) operation to move a TSIG key to different compartment.


Was this article helpful?
YesNo

