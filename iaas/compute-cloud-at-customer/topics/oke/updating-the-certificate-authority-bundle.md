Updated 2025-02-05
# Certificate Authority Bundles
The Certificate Authority (CA) bundle for Compute Cloud@Customer is downloaded and made available to a cluster when the cluster is created. The CA bundle includes the certificate, private and public keys, and other authorization information.
The CA bundle is automatically updated when regular certificate rotation occurs or when Compute Cloud@Customer is upgraded.
A process runs every hour to check the validity of the CA bundle and updates the CA bundle if needed.
When the CA bundle is updated on the infrastructure, it must be updated on the local system that you use to manage the OKE service. For example, the CA bundle authorizes the use of `cluster-api`. This is similar to replacing the CA bundle in your `~/.oci` configuration so that you can run CLI commands.
To obtain the CA bundle for your local system, contact Oracle for support. See [Creating a Support Request](https://docs.oracle.com/iaas/Content/GSG/support/create-incident.htm). To access support, sign in to the Oracle Cloud Console as described in [Sign In to the OCI Console](https://docs.oracle.com/iaas/Content/GSG/Tasks/signingin.htm#Signing_In_to_the_Console).
Was this article helpful?
YesNo

