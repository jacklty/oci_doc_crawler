Updated 2025-03-10
# Creating a TSIG Key
Create a TSIG key to enable the domain name service (DNS) to authenticate updates to secondary zones.
See [Managing TSIG Keys](https://docs.oracle.com/en-us/iaas/Content/DNS/Tasks/tsig.htm#manage-tsig "Transaction signature \(TSIG\), also referred to as Secret Key Transaction Authentication, ensures that domain name service \(DNS\) packets originate from an authorized sender by using shared secret keys and one-way hashing to add a cryptographic signature to the DNS packets.") for more information about TSIG keys and how they're used in zones.
For general service information, see the [DNS service overview](https://docs.oracle.com/en-us/iaas/Content/DNS/Concepts/dnszonemanagement.htm#overview "The DNS service helps you create and manage DNS zones.").
  * [Console](https://docs.oracle.com/en-us/iaas/Content/DNS/Tasks/tsig-key-create.htm)
  * [CLI](https://docs.oracle.com/en-us/iaas/Content/DNS/Tasks/tsig-key-create.htm)
  * [API](https://docs.oracle.com/en-us/iaas/Content/DNS/Tasks/tsig-key-create.htm)


  *     1. Open the **navigation menu** and select **Networking**. Under **DNS management** , select **TSIG keys**.
    2. Under **List scope** , select the compartment to create the key in.
    3. Select **Create TSIG key**.
    4. In the **Create TSIG Key** panel, enter the following information:
       * **Name:** The name of the key used in domain name syntax. We recommend that the name you use reflect the names of the hosts and uniquely identify the key among a set of keys these two hosts might share at any particular time.
       * **Compartment:** The compartment to create the TSIG key in, if it's different than the one you selected before.
       * **Algorithm:** The public key's algorithm used to encrypt or decrypt data. Applicable algorithms include hmac-md5, hmac-sha1, hmac-sha224, hmac-sha256, hmac-h384, and hmac-sha512.
       * **Secret:** The base64 string encoding the binary shared secret that corresponds to the key. A maximum value of 255 characters is allowed.
       * **Show Advanced Options:** Optionally, add tags to the key. If you have permissions to create a resource, you also have permissions to apply free-form tags to that resource. To apply a defined tag, you must have permissions to use the tag namespace. For more information about tagging, see [Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm).
    5. Select **Create TSIG Key**.
The TSIG key details page opens.
  * Use the [tsig create](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/dns/tsig-key/create.html) command and required parameters to create a TSIG key:
Command
CopyTry It
```
oci dns tsig-key create --compartment-id compartment_id --name tsig_key_name
--algorithm tsig_key_algorithm ... [OPTIONS]
```

TSIG key algorithms are encoded as domain names, but most consist of only one label that isn't empty, which isn't required to be explicitly absolute. Applicable algorithms include: `hmac-sha1`,` hmac-sha224`,` hmac-sha256`, `hmac-sha512`.
For a complete list of flags and variable options for CLI commands, see the [CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest).
  * Run the [CreateTsigKey](https://docs.oracle.com/iaas/api/#/en/dns/latest/TsigKey/CreateTsigKey) operation to create a TSIG key.


Was this article helpful?
YesNo

