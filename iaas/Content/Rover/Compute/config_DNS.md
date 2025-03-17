Updated 2023-05-18
# Updating DNS on Roving Edge Infrastructure Instances
Update the Domain Name Service (DNS) settings on your system to include the nameservers the instance can reach.
To preserve your edits to the `/etc/resolv.conf` file, run the following command:
```
chattr +i /etc/resolv.conf
```

Inclusion of the `+i` attribute in the command protects the `/etc/resolv.conf` file on Linux so that no one can modify it, not even the root user.
To remove the write protect attribute, run the following command:
```
chattr -i /etc/resolv.conf
```

Was this article helpful?
YesNo

