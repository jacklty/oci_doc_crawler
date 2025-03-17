Updated 2025-03-10
# Delegating a Public DNS Zone
Make an OCI public domain name service (DNS) zone accessible through the internet.
In this step, **delegate** the **domain** with a registrar. A domain name registrar is a company that manages the reservation of internet domain names. Delegating a domain with a registrar makes the OCI hosted **zone** accessible through the internet.
OCI isn't a registrar. However, you can delegate OCI DNS zones with registrars such as VeriSign or GoDaddy. 
See [Overview of DNS](https://docs.oracle.com/en-us/iaas/Content/DNS/Concepts/dnszonemanagement.htm#overview "The DNS service helps you create and manage DNS zones.") and [Public DNS](https://docs.oracle.com/en-us/iaas/Content/DNS/Concepts/gettingstarted.htm#getting-started "Get started with the Oracle Cloud Infrastructure DNS service.") for more information. 
## Using the Console 🔗 
  1. Open the **navigation menu** and select **Networking**. Under **DNS management** , select **Zones**.
  2. Select the **Zone name** for the zone you want to delegate. The zone details page appears.
  3. In **Resources** , select **Records**. A list of records appear.
  4. Use the **Type** sort filter to find the NS records for the zone.
  5. Note the name servers in the **RDATA** field within each [NS](https://docs.oracle.com/en-us/iaas/Content/DNS/Reference/supporteddnsresource.htm#types__dlentry_ns) record.
  6. Visit the third-party registrar you chose and follow the registrar vendor's specific documentation to change the domain's DNS delegation. You need the name servers noted in step 5 to complete the process.
**Note** After delegation has completed, it can take 24 to 48 hours for resolvers to recognize that a new set of NS records is in delegation. This is because NS records can have long TTL values and they must expire before the new NS records can replace them.


**Tip**
Use the Domain Information Groper (dig) command line tool to test against the **delegation** where the **domain** is hosted. You can immediately see whether the change took place without waiting for the cache or TTL (Time to Live) that you have configured.
For more information on using dig to test DNS, see [Testing DNS Using dig](https://docs.oracle.com/en-us/iaas/Content/DNS/Tasks/testingdnsusingdig.htm#test-bind-dig "Use BIND'S Domain Information Groper \(dig\) command line tool to test against the delegation where the domain is hosted. Immediately see whether changes took place without accounting for the cache or TTL \(Time to Live\) that you have configured.").
Was this article helpful?
YesNo

