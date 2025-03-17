Updated 2025-03-12
# Configuring the PAM using SSSD
Configure the PAM on Linux using the SSSD service.
  * The SSSD service must be installed. If it's not installed, install using `sudo yum install sssd`.
  * The service must be configured to start when the system reboots. You can perform this configuration using `sudo chkconfig sssd on`.
  * Execute the steps [Enforcing SELinux](https://docs.oracle.com/en-us/iaas/Content/Identity/linuxpam/enforcing_selinux.htm#enforcing_selinux "Set SELinux to enforcing.") when the property SELINUX is set as enforced in file `/etc/selinux/config`.
You can also set `SELINUX=permissive` or `SELINUX=disabled`, which case enforcing SELinux is not required
**Note** Restart Linux if you update `/etc/selinux/config`.


  1. Verify that the `/etc/sssd/sssd.conf` file exists, has 600 permission, and is owned by the root user. If the file doesn't exist create it as follows and run `chmod 600` `/etc/sssd/sssd.conf`. 
**`/etc/sssd/sssd.conf` **
```
[sssd]
config_file_version = 2
services = nss, pam
### domains specify the look up order, 
### which should always be LOCAL and then IDCS.
domains = LOCAL,IDCS
 
[nss]
#Backfill cache at 75%, do not cache bad lookups,
# no in-mem cache
entry_cache_nowait_percentage = 75
### 1 Hour caching for non existent user
entry_negative_timeout = 3600
 
[pam]
pam_id_timeout = 600
 
[domain/LOCAL]
# Prior to 1.15, must use older files provider
id_provider = proxy
proxy_lib_name = files
# Disable authentication, files provider 
# always provides local access, enumerate files
auth_provider = none
access_provider = permit
enumerate = true
 
[domain/IDCS]
re_expression = (?P<domain>[^\\]*?)\\?(?P<name>[^\\]+$)
auth_provider = proxy
id_provider = proxy
proxy_lib_name = oracle_cloud
proxy_pam_target = sssd_proxy_oracle_cloud
enumerate = false
cache_credentials = true
# Default cache timeout 90 mins for user/group info entries, 
#before it reaches to IDCS for new updates
entry_cache_timeout = 5400
```

Optionally, you can configure email addresses as the SSO usernames. To do this, add the line in bold to the `/etc/sssd/sssd.conf` file to specify the regular expression. ```
...
[pam]
[domain/proxy_proxy]
**re_expression = (?P<domain>[^\\]*?)\\?(?P<name>[^\\]+$)**
auth_provider = proxy
id_provider = proxy
...
```

  2. Verify the `/etc/pam.d/sssd_proxy_oracle_cloud` file exists and is owned by the root user. If the file doesn't exist, then create it as the root user and add the following:
**`/etc/pam.d/sssd_proxy_oracle_cloud file` **
```
auth     required   pam_oracle_cloud.so
account    required   pam_oracle_cloud.so
password   required   pam_oracle_cloud.so
session    required   pam_oracle_cloud.so
```

  3. Edit the `/etc/pam.d/sshd` and add the `pam_oracle_cloud` module:
**`/etc/pam.d/sshd` **
```
auth sufficient pam_oracle_cloud.so
```

**Note** Add this either before the line `auth include password-auth`, or `auth substack password-auth*`.
  4. Edit the `/etc/ssh/sshd_config` to configure `sshd` to allow the use of multifactor authentication (MFA):
**`/etc/ssh/sshd_config` **
Search for the `ChallengeResponseAuthentication` property and set it to `yes`. If the property isn't in the configuration file, add it.
  5. Edit the `/etc/opc.conf` to let the plugin to interact with IAM:
**`/etc/opc.conf` **
```
**#This is sample format of opc.conf file, please use the correct information to configure this file.**
**#Enter the Oracle Identity Cloud Service tenancy base url.**
base_url = https://identity-cloud-service-instance-url
**#There is no need to change value of scope.**
scope = urn:opc:idm:__myscopes__
**#Enter the location of the wallet.**
wallet_location = /etc/opc-wallet
**#Enter the log level, this is optional and the default is 0, which means no log. 0 - None, 1 - Error, 2 - Info, 3 - Debug.**
log_level = 0
**#Enter the log file path, this is optional and defaults to /var/log/opc/pam_nss.log**
log_file_path = /var/log/opc/pam_nss.log
**#Enter the value for proxy usage to connect to Oracle Identity Cloud Service.**
**#Set the value to 1 to use a proxy and 0 to not use a proxy.**
use_proxy=0
**#Enter the information below if you set: use_proxy=1**
**#Enter the proxy url**
**#proxy_url=http://proxy.example.com**
**#Enter the proxy port**
**#proxy_port=80#Enter the username to connect to the proxy url.**
**#proxy_username=username_example**
**#Enter the password of username to connect proxy url.**
**#proxy_pwd=pwd_example**
```

  6. Restart sssd and sshd:
    1. For OEL6 & OEL7: `authconfig --enablemkhomedir --enablepamaccess --update`.
    2. For OEL8: `authselect select sssd with-mkhomedir with-pamaccess`.
    3. Run: `service sshd restart`.
    4. Run: `service sssd restart`.


Was this article helpful?
YesNo

