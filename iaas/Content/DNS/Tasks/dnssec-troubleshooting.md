Updated 2024-10-16
# Troubleshooting DNSSEC Issues
Troubleshoot common issues with DNSSEC.
  * Useful tools people can use to verify their DNSSEC configuration are BIND's [Dig tool](https://www.isc.org/downloads/), [DNSViz](https://dnsviz.net/), or [DNS Analyzer](https://dnssec-analyzer.verisignlabs.com/).
  * When reaching out to support, it's helpful to indicate if the zone is DNSSEC enabled, what parent/child DS records exist, dig results using `+dnssec`, and the results of using [DNSViz](https://dnsviz.net/).
  * Maintaining a valid chain of trust is important because broken chains of trust result in data being marked as invalid, which can cause domains and subdomains to become invisible to verifying clients. Security lameness is when a parent zone has a DS record pointing to a nonexistent DNSKEY. If all DS records point to nonexistent DNSKEYs, then the child zone is marked as invalid.
  * Before uploading DS records to the parent zone, verify that all name servers correctly return the expected RRSIG records when querying domains in the zone. If some name servers still return unsigned query responses while the parent DS records indicate the data should be signed, validating resolvers won't resolve the domain name.


Was this article helpful?
YesNo

