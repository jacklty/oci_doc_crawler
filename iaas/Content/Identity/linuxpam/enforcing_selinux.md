Updated 2023-09-25
# Enforcing SELinux
Set SELinux to enforcing.
**Before you begin:**
Check that the following packages are installed on Oracle Linux:
`rpm -q selinux-policy-targeted policycoreutils libselinux-utils libselinux-python libselinux`
**Note** When you change the SELinux mode from Permissive or Disabled to Enforcing, then you must reboot.
Create a policy and ensure that PAM works when SELinux is set to enforcing:
  1. If necessary, install these packages on Oracle Linux:
Copy
```
rpm -q selinux-policy-targeted policycoreutils libselinux-utils libselinux-python libselinux
```

  2. Allow outbound communication on 443:
Copy
```
$ sudo setsebool -P nis_enabled 1
++
```

  3. Create a local policy so that `sssd_t` can create `opc` dir to create, and read and write to the `pam_nss.log` file (which is mentioned in `/etc/opc.conf`). It doesn't need to be located in a specific location because it's compiled by the SELinux utilities.
    1. Create the policy file and save it with the filename `idcs-pam.te`. This is the content:
Copy
```
module idcs-pam 1.0;
require {
	type sssd_var_log_t;
    type var_log_t;
    type sshd_t;
    type sssd_t;
    type cert_t;
	type http_port_t;
	type user_home_dir_t;
    class file { open read write };
    class dir { create write};
    class tcp_socket { name_connect };
}
#============= sssd_t ==============
allow sssd_t cert_t:file write;
allow sssd_t user_home_dir_t:dir write;
allow sssd_t var_log_t:dir create;
allow sssd_t var_log_t:file { open read };
allow sshd_t sssd_var_log_t:file { open read };
allow sshd_t http_port_t:tcp_socket { name_connect };
```

  4. Build the SELinux policy module. Run:
Copy
```
$ checkmodule -M -m -o idcs-pam.mod idcs-pam.te 
$ semodule_package -m idcs-pam.mod -o idcs-pam.pp
```

  5. Install the SELinux module. Run:
`$ semodule -i idcs-pam.pp`
  6. Reload SELinux. Run:
`$ semodule -R`
  7. Finally, authenticate the PAM user again.
The `/opc` dir and `/opc/pam_nss.log` file are created.


Was this article helpful?
YesNo

