Updated 2024-05-23
# Querying For a Private Zone After Creation Returns an NXDOMAIN Error Message or Public IP Address
Querying a private zone returns an NXDOMAIN error message or a public IP address.
  * If a query is sent before the private **zone** is published, the query recurses to the internet. An error message stating that the **domain** doesn't exist or a public name response is returned for the query.
  * Because the **NXDOMAIN** or non-private answer might be cached, you might need to wait until the Time To Live (TTL) expires before getting the expected answer.


Was this article helpful?
YesNo

