Updated 2025-01-10
# Managing TSIG Keys
Transaction signature (TSIG), also referred to as Secret Key Transaction Authentication, ensures that domain name service (DNS) packets originate from an authorized sender by using shared secret keys and one-way hashing to add a cryptographic signature to the DNS packets.
TSIG keys are used to enable DNS to authenticate updates to secondary zones. TSIG keys provide an added layer of security for **IXFR** and **AXFR** transactions. A TSIG key consists of a key name, a signing algorithm, and a secret. See [RFC 2845](http://www.rfc-editor.org/rfc/rfc2845.txt) for more information. TSIG keys can also be managed in DNS Zone Management. See [Managing DNS Service Zones](https://docs.oracle.com/en-us/iaas/Content/DNS/Tasks/managingdnszones.htm#managing-zones "The Oracle Cloud Infrastructure DNS service lets you manage zones using the Console, CLI, or API.") for more information.
## TSIG Key Tasks 🔗 
You can perform the follwing TSIG key tasks:
  * [Creating a TSIG Key](https://docs.oracle.com/en-us/iaas/Content/DNS/Tasks/tsig-key-create.htm#top "Create a TSIG key to enable the domain name service \(DNS\) to authenticate updates to secondary zones.")
  * [Listing TSIG Keys](https://docs.oracle.com/en-us/iaas/Content/DNS/Tasks/tsig-key-list.htm#top "View a list of all TSIG keys in a compartment")
  * [Getting a TSIG Key's Details](https://docs.oracle.com/en-us/iaas/Content/DNS/Tasks/tsig-key-get.htm#top "View details for a specific TSIG key.")
  * [Editing a TSIG Key](https://docs.oracle.com/en-us/iaas/Content/DNS/Tasks/tsig-key-update.htm#top "Update the information for a TSIG key.")
  * [Moving a TSIG Key Between Compartments](https://docs.oracle.com/en-us/iaas/Content/DNS/Tasks/tsig-key-move.htm#top "You can move a TSIG key from one compartment to another.")
  * [Deleting a TSIG Key](https://docs.oracle.com/en-us/iaas/Content/DNS/Tasks/tsig-key-delete.htm#top "Delete a TSIG key.")


Was this article helpful?
YesNo

