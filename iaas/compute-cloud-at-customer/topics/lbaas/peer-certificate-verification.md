Updated 2023-08-16
# Peer Certificate Verification
On Compute Cloud@Customer, peer certificate verification establishes mutual authentication between client and server.
When SSL is set up on the load balancer, the listener responds to an incoming client request with a certificate that the client can verify for authenticity. Enabling peer certificate verification adds an extra layer of security: it requires the client (peer) to present a certificate that the listener can validate. 
In case peer certificate verification is configured incorrectly, the client is unable to verify the certificate and returns a client SSL handshake failure. The error message varies by client type. You can use the OpenSSL utility to check the depth at which the validation fails:
```
$ openssl verify -verbose -CAfile _**root-cert.pem**_ _**intermediate-cert.pem**_
error 20 at 0 depth lookup: unable to get local issuer certificate
```

To resolve these verification errors, confirm that the client certificate and certificate authority certificate match, and ensure the certificates are included in the correct order.
Was this article helpful?
YesNo

