Updated 2023-06-06
# Configuring the SDK, CLI, or Terraform
Learn about the Oracle Cloud Infrastructure Software Development Kits (SDKs) and Command Line Interface (CLI) which you can use to facilitate development of custom solutions.
For information about SDKs, see [Software Development Kits and Command Line Interface](https://docs.oracle.com/iaas/Content/API/Concepts/sdks.htm)
## For the SDK for Java: 🔗 
In your SDK for Java, create an `InstancePrincipalsAuthenticationDetailsProvider` object. For example:
Copy
```
public static void main(String[] args) throws Exception {
  InstancePrincipalsAuthenticationDetailsProvider provider =
   InstancePrincipalsAuthenticationDetailsProvider.builder().build();
  IdentityClient identityClient = new IdentityClient(provider);
...
```

## For the SDK for Python: 🔗 
In your SDK for Python, create an `oci.auth.signers.InstancePrincipalsSecurityTokenSigner` object. For example:
Copy
```
# By default this will hit the auth service in the region returned by http://169.254.169.254/opc/v1/instance/region on the instance.
			
signer = oci.auth.signers.InstancePrincipalsSecurityTokenSigner()
identity_client = oci.identity.IdentityClient(config={}, signer=signer)
...
```

To refresh the token without waiting, use the following command:
`signer.refresh_security_token()`
## Enabling Instance Principal Authorization for the CLI 🔗 
To enable instance principal authorization from the CLI, you can set the authorization option (`--auth`) for a command. For example:
Command
CopyTry It
```
oci os ns get --auth instance_principal
```

Alternatively, you can set the following environment variable:
```
OCI_CLI_AUTH=instance_principal
```

Note that if both are set, the value set for `--auth` takes precedence over the environment variable.
For information about using the CLI, see [Working with the Command Line Interface](https://docs.oracle.com/iaas/Content/API/Concepts/cliconcepts.htm).
## Enabling Instance Principal Authorization for Terraform 🔗 
To enable instance principal authorization in Terraform, you can set the `auth` attribute to "InstancePrincipal" in the provider definition as shown in the following sample:
Copy
```
variable "region" {}
provider "oci" {
  auth = "InstancePrincipal" 
  region = "${var.region}"
}

```

Note that when you use instance principal authorization you do not need to include the `tenancy_ocid`, `user_ocid`, `fingerprint`, and `private_key_path` attributes.
Was this article helpful?
YesNo

