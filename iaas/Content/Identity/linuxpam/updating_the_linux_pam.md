Updated 2023-06-23
# Updating the Linux PAM
Use the following steps to update to a new Linux Pluggable Authentication Module (PAM) version.
  1. Confirm that PAM is installed by running the following command:
`$ rpm -qa | grep oracle-cloud`
You should see: ```
pam_oracle-cloud-<version>.x86_64authn-oracle-cloud-<version>.x86_64
```

  2. Update the RPM using the `rpm-U` command:
```
$ rpm -U authn-oracle-cloud-<version>.rpm
$ rpm -U pam_oracle-cloud-<version>.rpm
```

  3. Restart sssd: 
`$ service sssd restart`


Was this article helpful?
YesNo

