Updated 2023-11-20
# Using Oracle Repositories on Oracle Linux Instances for Roving Edge Infrastructure
Update an Oracle Linux instance's repository settings to work with Roving Edge Infrastructure.
If you are using an Oracle Linux image, change the repository settings to update the instance for Roving Edge Infrastructure:
  1. Go to the following location:
`/etc/yum/vars/`
  2. Remove the `ociregion` file from the directory.
  3. Perform one of the following tasks:
     * If you are using a proxy server, set the proxy in `/etc/yum.conf` file. For example: 
`proxy=http://www-proxy.us.oracle.com:80`
     * If you are using your own repo, update all repos in `/etc/yum/repos.d`.


## Using Unbreakable Linux Network 🔗 
Access to Unbreakable Linux Network (ULN), including Ksplice, is included with Roving Edge Infrastructure devices. Obtain the Customer Support Identifier (CSI) from your Roving Edge Infrastructure purchase contract. See [ULN Access for Oracle Cloud Infrastructure](https://docs.oracle.com/en/operating-systems/oracle-linux/uln-user/uln-AbouttheUnbreakableLinuxNetwork.html) for more information.
Was this article helpful?
YesNo

