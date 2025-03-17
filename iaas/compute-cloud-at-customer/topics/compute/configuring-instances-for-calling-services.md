Updated 2025-02-21
# Configuring Instances for Calling Services
A Compute Cloud@Customer compute instance can be configured to enable applications running on the instance to call services and manage resources similar to the way Compute Cloud@Customer users call services to manage resources.
The IAM service feature that enables instances to be authorized actors (or principals) to perform actions on service resources is called an _instance principal_.
Perform the following steps to set up and use an instance as a principal:
  * Configure the instance firewall to enable the instance to access service endpoints. See [Configuring Instance Firewalls to Allow Calling Services](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/compute/configuring-instances-for-calling-services.htm#configuring-instance-firewalls-to-allow-calling-services).
  * Ensure the instance is included in a dynamic group (configured in your tenancy) that grants permissions to access the required resources. See [Managing Dynamic Groups](https://docs.oracle.com/iaas/Content/Identity/Tasks/managingdynamicgroups.htm).
The instance must be created in or moved to a compartment that's named in a matching rule of the dynamic group, or the instance must have a resource tag assigned that's named in a matching rule. See [Writing Matching Rules to Define Dynamic Groups](https://docs.oracle.com/iaas/Content/Identity/Tasks/managingdynamicgroups.htm#Writing).


## Configuring Instance Firewalls to Allow Calling Services 🔗 
This section describes how to modify the instance firewall configuration and how to create a `systemd` service to restore the changes if the system reboots. 

Modify the Firewall Configuration
    
  1. As a privileged user, modify the instance firewall configuration to enable the instance to access service endpoints such as `iaas` and `identity`.
  2. Use the `iptables` command to add the following `BareMetalInstanceServices` rules to the instance firewall:
```
iptables -I BareMetalInstanceServices 14 -p tcp -d 169.254.169.254 --dport 443 -j ACCEPT
iptables -I BareMetalInstanceServices 14 -p tcp -d 169.254.240.254 --dport 443 -j ACCEPT
```

The first entry is required for all endpoints. The second entry is required to contact the Object Storage endpoint.



Make the Configuration Changes Persistent
    
Use the following procedure to make these firewall configuration changes persist across instance reboots.
  1. Save the updated IP tables configuration.
```
iptables-save > /etc/sysconfig/iptables.rules
```

  2. Create a script to automatically restore the current (modified) firewall configuration on reboot.
In this example, the script is named `/sbin/restore-iptables.sh`. The following is the content of the file `/sbin/restore-iptables.sh`:
```
#!/bin/sh
/sbin/iptables-restore < /etc/sysconfig/iptables.rules
```

  3. Set the executable bit on the script.
```
chmod +x /sbin/restore-iptables.sh
```

  4. Create a `systemd oneshot` service to execute the `/sbin/restore-iptables.sh` script at boot time.
In this example, the service is named `/etc/systemd/system/restore-iptables.service`. The following is the content of the file `/etc/systemd/system/restore-iptables.service`:
```
[Unit]
Description=Restore IP Tables
After=cloud-final.service
[Service]
ExecStart=/sbin/restore-iptables.sh
User=root
Group=root
Type=oneshot
[Install]
WantedBy=multi-user.target
```

  5. Reload the `systemd` manager configuration, and enable the service to run at boot time.
```
systemctl daemon-reload
systemctl enable restore-iptables
```



## Configuring Instance Certificates to Allow Calling Services 🔗 
On Compute Cloud@Customer, by default, endpoints (such as `iaas` and `identity`) offer a certificate that's signed by a CA that's specific to that Compute Cloud@Customer. By default, OSs don't trust certificates that are signed by a CA that's specific to this Compute Cloud@Customer. If the OS doesn't trust the certificates that are offered, attempts to use the OCI SDK or CLI fail with a `CERTIFICATE_VERIFY_FAILED` error.
Implement one of the solutions described in this topic to successfully use the OCI SDK or CLI on the instance.
**Important**
Any user who can SSH to the instance automatically inherits the privileges granted to the instance.
### Option 1: Bring Your Own Certificate (BYOC) 🔗 
On Compute Cloud@Customer, you can provide your own Certificate Authority (CA) certificates which enables you to use your CA trust chain. To use your own certificates, open a Support Request, and request to use your own certificates. See [Creating a Support Request](https://docs.oracle.com/iaas/Content/GSG/support/create-incident.htm). To access support, sign in to the Oracle Cloud Console as described in [Sign In to the OCI Console](https://docs.oracle.com/iaas/Content/GSG/Tasks/signingin.htm#Signing_In_to_the_Console).
On a Linux OS, the following command lists CAs that are trusted by default:
```
trust list --filter=ca-anchors
```

### Option 2: Specify in the SDK Code the CA Bundle to Use 🔗 
This method copies the Compute Cloud@Customer-specific CA bundle to the instance, but doesn't verify the server's certificate (`--insecure`). To ensure security, verify the content of the retrieved bundle (`external_ca.crt`).
  1. Retrieve the certificate from the `iaas` endpoint of the Compute Cloud@Customer infrastructure.
```
curl --insecure -sS -o external_ca.crt --noproxy "*" https://iaas.**_ccc_name_**.**_domain_name_**/cachain
```

This command could be in a script that is passed to the instance at launch time by using either the `--user-data-file` option or the `--metadata` option with a `user_data` field. The script will be run by cloud-init inside the instance during init, saving the effort of manually retrieving this certificate file on many instances.
  2. Verify the content of the CA bundle saved in the `external_ca.crt` file.
  3. Specify the CA bundle in the Python SDK code.
```
signer = oci.auth.signers.InstancePrincipalsSecurityTokenSigner(
  federation_client_cert_bundle_verify="/home/opc/external_ca.crt"
)
identity_client = oci.identity.IdentityClient(config={}, signer=signer)
identity_client.base_client.session.verify = "/home/opc/external_ca.crt"
```



### Option 3: Globally Trust the Oracle Compute Cloud@Customer CA Bundle 🔗 
This method is the same as the preceding method with the following difference: Instead of specifying the CA bundle in the SDK code, this method adds the CA bundle to the trust chain.
**Important**
When the CA bundle is added to the trust chain, every application on this compute instance will trust certificates signed with the CA specified in this bundle. Consider whether this is an acceptable security risk.
  1. Retrieve the certificate from the `iaas` endpoint of the Compute Cloud@Customer infrastructure.
```
curl --insecure -sS -o external_ca.crt --noproxy "*" https://iaas.**_ccc_name_**.**_domain_name_**/cachain
```

  2. Verify the content of the CA bundle saved in the `external_ca.crt` file.
  3. Update the global CA trust chain.
```
cp external_ca.crt /etc/pki/ca-trust/source/anchors/
update-ca-trust extract
```



Steps 1 and 3 in this method could be in a script that's passed to the instance at launch time by using either the `--user-data-file` option or the `--metadata` option with a `user_data` field. The script runs by cloud-init inside the instance during init, saving the effort of performing these steps manually on many instances.
Was this article helpful?
YesNo

