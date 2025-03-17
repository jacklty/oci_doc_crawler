Updated 2024-10-07
# Transaction Signature (TSIG) Keys
On Compute Cloud@Customer, you can create, add, and delete TSIG keys.
A DNS transaction signature (TSIG) is a network protocol defined in RFC 2845. The main purpose of the TSIG is to allow DNS to authenticate updates to a DNS database, so that malicious users can't change name resolution records to point to a bogus IP address instead of (for example) the IP address of a bank. TSIG uses one-way hashing and shared secret keys to provide a secure means to authenticate the endpoints of a connection for processing (or responding to) DNS update requests. 
The TSIG protocol uses timestamps to prevent replay of recorded responses. Therefore, DNS servers and TSIG clients need accurate clocks to provide the timestamps. Several extensions to the basic TSIG protocol have been made to extend the types of cryptography and hashing methods that are supported by TSIG.
To use TSIG for a DNS zone, add TSIG keys to the DNS zone. The TSIG key must be base64 encoded. 
## Creating a TSIG Key 🔗 
On Compute Cloud@Customer, you can create TSIG keys to ensure that DNS packets originate from an authorized sender by using shared secret keys and one-way hashing to add a cryptographic signature to the DNS packets.
To add a TSIG key to an existing list of TSIG keys, simply create another key with a unique TSIG key name and a new algorithm or a new key value. To modify fields in an existing TSIG key, use the `update` command.
A TSIG key is a separate object from a DNS zone. You can have a `SECONDARY         DNS` zone reference a TSIG key as part of its `ExternalMaster` definition. But creating a new key doesn't do anything for a `PRIMARY` zone.
  * [Console](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/network/transaction-signature-keys.htm)
  * [CLI](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/network/transaction-signature-keys.htm)
  * [API](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/network/transaction-signature-keys.htm)


  *     1. In the [Compute Cloud@Customer Console](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/overview/compute-cloud-customer-console.htm#accessing-the-console "Use the Compute Cloud@Customer Console to create and manage compute, storage and other resources on a Compute Cloud@Customer infrastructure.") navigation menu, click **DNS** , then click **TSIG Keys**. 
    2. Click **Create Key**.
    3. Enter the required TSIG Key information:
       * **Name:** Provide a name or description for the TSIG key.
       * **Compartment:** Select the compartment in which to create the TSIG key.
       * **Algorithm:** Choose the security algorithm for the TSIG Key you are creating, such as **hmac-sha256**.
       * **Secret Key:** Provide the base64 string encoding the binary shared secret that corresponds to the key. The maximum is 255 characters. An example key in base64 encoding is shown in RFC3874. You can provide the key in one of two ways:
         * **Select the key file** : If you provide the TSIG shared secret key this way, you can drag and drop the key file into the space provided.
         * **Paste the key** : If you provide the TSIG shared secret key this way, you can copy and paste the contents of the key file into the space provided.
       * **Tagging:** (Optional) Add one or more tags to this resource. Tags can also be applied later. For more information about tagging resources, see [Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm).
    4. Click **Create TSIG Key**.
The TSIG key now available for use in the DNS zone between TSIG client and DNS server.
  * Use the [oci dns tsig-key create](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/dns/tsig-key/create.html) command and required parameters to create a new TSIG key in the specified compartment.
Copy
```
oci dns tsig-key create [OPTIONS]
```

For a complete list of CLI commands, flags, and options, see the [Command Line Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/index.html).
  * Use the [CreateTsigKey](https://docs.oracle.com/iaas/api/#/en/dns/latest/TsigKey/CreateTsigKey) operation to create a new TSIG key in the specified compartment.
For information about using the API and signing requests, see [REST APIs](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm#REST_APIs) and [Security Credentials](https://docs.oracle.com/iaas/Content/General/Concepts/credentials.htm). For information about SDKs, see [Software Development Kits and Command Line Interface](https://docs.oracle.com/iaas/Content/API/Concepts/sdks.htm#Software_Development_Kits_and_Command_Line_Interface).


## Deleting a TSIG Key 🔗 
On Compute Cloud@Customer, you can delete a TSIG key.
  * [Console](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/network/transaction-signature-keys.htm)
  * [CLI](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/network/transaction-signature-keys.htm)
  * [API](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/network/transaction-signature-keys.htm)


  *     1. In the [Compute Cloud@Customer Console](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/overview/compute-cloud-customer-console.htm#accessing-the-console "Use the Compute Cloud@Customer Console to create and manage compute, storage and other resources on a Compute Cloud@Customer infrastructure.") navigation menu, click **DNS** , then click **TSIG Keys**. 
    2. Click the Actions menu (![An image of the three dot icon.](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/images/three-dots.png)) for the TSIG key that you want to delete, and click **Delete**.
The TSIG key is removed from the list.
  * Use the [oci dns tsig-key delete](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/dns/tsig-key/delete.html) command and required parameters to delete the specified TSIG key.
Copy
```
oci dns tsig-key delete [OPTIONS]
```

For a complete list of CLI commands, flags, and options, see the [Command Line Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/index.html).
  * Use the [DeleteTsigKey](https://docs.oracle.com/iaas/api/#/en/dns/latest/TsigKey/DeleteTsigKey) operation to delete the specified TSIG key.
For information about using the API and signing requests, see [REST APIs](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm#REST_APIs) and [Security Credentials](https://docs.oracle.com/iaas/Content/General/Concepts/credentials.htm). For information about SDKs, see [Software Development Kits and Command Line Interface](https://docs.oracle.com/iaas/Content/API/Concepts/sdks.htm#Software_Development_Kits_and_Command_Line_Interface).


Was this article helpful?
YesNo

