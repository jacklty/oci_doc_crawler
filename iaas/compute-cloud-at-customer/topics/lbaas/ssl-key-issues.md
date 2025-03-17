Updated 2023-08-16
# SSL Key Issues
On Compute Cloud@Customer, the following key-related problems are known to occur when configuring SSL for a load balancer.
## Submitting Private Keys
If an error is returned when you submit a private key, these are the most common causes:
  * You provided an incorrect passphrase.
  * Your private key is malformed.
  * The system does not recognize the encryption method used for your key.


## Key Pair Mismatch
If the private and public key do not match, attempting to upload them results in a mismatch error. Use the following OpenSSL commands to confirm that the public and private key are part of the same pair:
```
openssl x509 -in certificate_name.crt -noout -modulus | openssl sha1
openssl rsa -in private_key_name.key -noout -modulus | openssl sha1
```

The `sha1` hash values returned from these commands must match exactly. If they are different, then the private key is not used to sign the public certificate, and this key cannot be used.
## Private Key Consistency
In general, when errors occur that are related to a private key, you can use the OpenSSL utility to check the key's consistency. This command verifies that the key is intact, the passphrase is correct, and the file contains a valid RSA private key:```
openssl rsa -check -in **_private_key.pem_**
```

## Private Key Decryption
If the system does not recognize the encryption technology used for a private key, you should decrypt the key and upload the unencrypted version of the key with your certificate bundle. You can use the OpenSSL utility to decrypt a private key:```
openssl rsa -in **_private_key.pem_** -out _**private_key_decrypted.pem**_
```

Was this article helpful?
YesNo

