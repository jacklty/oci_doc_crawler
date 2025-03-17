Updated 2023-08-16
# Uploading Certificate Chains
Use the following process for certificate chains on Compute Cloud@Customer.
If there are multiple certificates that form a single certification chain – for example when intermediate certificate authority (CA) certificates are used –, then include all relevant certificates in a single PEM file in the correct order before uploading them to the system. The correct order begins with the certificate directly signed by the trusted root certificate authority at the bottom of the list. Any additional certificates are pasted above the signed certificate.
Combine the server certificate (`ssl-certificate.crt`) and the intermediate CA certificate (`intermediate-ca-cert.crt`) files into a single, concatenated PEM file:
```
cat ssl_certificate.crt intermediate-ca-cert.crt >> certbundle.pem
```

Was this article helpful?
YesNo

