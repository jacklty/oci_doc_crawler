Updated 2024-12-18
# Configuring Email Authentication Settings for SPF and DKIM
If you have configured a non-Oracle domain as the From Email Address for your notifications, then you must configure the email authentication settings for Sender Policy Framework (SPF) and DomainKeys Identified Mail (DKIM) so that you can certify the domain. Oracle Support must help with the configuration.
  1. You create a service request. See [Support Requests](https://docs.oracle.com/iaas/Content/GSG/Tasks/contactingsupport.htm).
  2. Oracle configures SPF. Add an SPF record to the domain of the `from` address to include the Oracle Cloud Infrastructure email delivery domain. The SPF record statement is: `include:spf_c.oraclecloud.com`.
  3. Oracle registers DKIM. Send Oracle DKIM information. In the Service Request in My Oracle Cloud Support, include the following details:
     * selector name: Oracle generates a default. Check whether your DNS/email team requires a specific format.
     * key size: The "key-size" to use for the DKIM registration. The default is 1024. Check whether your DNS/email team requires 2048.
     * from address: The address that will be used to send emails.
  4. You publish the DNS record for your domain and update the service request. Oracle provides you with the details to add the DNS record for your domain. The instructions to add the DNS record depend on your domain provider.
  5. Oracle activates the DKIM settings for your identity domain.


Was this article helpful?
YesNo

