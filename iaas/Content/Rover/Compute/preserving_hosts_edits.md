Updated 2023-05-18
# Preserving Hosts File Edits for Roving Edge Infrastructure
Preserve your edits to the `/etc/hosts` file on a compute instance on your Roving Edge Infrastructure device.
To preserve your edits to the `/etc/hosts` file on a compute instance in Roving Edge Infrastructure, open the following file:
```
/etc/oci-hostname.conf
```

Update the `PRESERVE_HOSTINFO` value at the bottom of the configuration from the default `0` to `2` or `3`. For example:
```
# This configuration file controls the hostname persistence behavior for Oracle Linux
# compute instance on Oracle Cloud Infrastructure (formerly Baremetal Cloud Services)
# Set PRESERVE_HOSTINFO to one of the following values
#  0 -- default behavior to update hostname, /etc/hosts and /etc/resolv.conf to 
#    reflect the hostname set during instance creation from the metadata service
#  1 -- preserve user configured hostname across reboots; update /etc/hosts and 
#      /etc/resolv.conf from the metadata service 
#  2 -- preserve user configured hostname across instance reboots; no custom 
#    changes to /etc/hosts and /etc/resolv.conf from the metadata service,
#    but dhclient will still overwrite /etc/resolv.conf
#  3 -- preserve hostname and /etc/hosts entries across instance reboots; 
#    update /etc/resolv.conf from instance metadata service
PRESERVE_HOSTINFO=2
```

Updating the `PRESERVE_HOSTINFO` value prevents the metadata service from overwriting the changes to the `/etc/hosts` file.
Was this article helpful?
YesNo

