Updated 2023-05-30
# Moving a Resolver Between Compartments
You can move a resolver from one compartment to another.
See [Private DNS resolvers](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/dns-topic-Private-resolver.htm#Private_resolver "A private DNS resolver answers DNS queries for a VCN per a configuration you create.") for more information and a feature overview.
See [Managing Compartments](https://docs.oracle.com/iaas/Content/Identity/compartments/managingcompartments.htm) for information about compartments and access control.
  * [Console](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/resolver-move.htm)
  * [CLI](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/resolver-move.htm)
  * [API](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/resolver-move.htm)


  * You can only edit the resolver name using the console.
    1. From the **Virtual Cloud Network Details** screen for your VCN, look in the VCN Information tab and click the name of the DNS resolver for the VCN. The **Private Resolver Details** screen appears.
    2. Click **Move resource**.
    3. Select a destination compartment from the list.
    4. Click **Move resource**.
  * Use the [resolver change-compartment](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/dns/resolver/change-compartment.html) command and required parameters to move a resolver from one compartment to another:
Command
CopyTry It
```
oci dns resolver change-compartment --resolver-id resolver_OCID 
--compartment-id compartment_OCID... [OPTIONS]
```

For a complete list of flags and variable options for CLI commands, see the [CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest).
  * Run the [ChangeResolverCompartment](https://docs.oracle.com/iaas/api/#/en/dns/latest/Resolver/ChangeResolverCompartment) operation to move a resolver from one compartment to another.


Was this article helpful?
YesNo

