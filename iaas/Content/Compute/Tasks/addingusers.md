Updated 2024-02-13
# Adding Users to an Instance
You can add additional users to a compute instance.
If you created your instance using a Linux or CentOS platform image, you can use SSH to access your instance from a remote host as the `opc` user. If you created your instance using an Ubuntu platform image, you can use SSH to access your instance from a remote host as the `ubuntu` user. After signing in, you can add users to the instance.
If you created your instance using a Windows platform image, you can create new users after you sign in to the instance through a Remote Desktop client.
## Creating Additional Users on a Linux Instance 🔗 
If you do not want to share your SSH key, you can create additional SSH-enabled users for a Linux instance. At a high level, you do the following things:
  * Generate SSH key pairs for the users offline.
  * Add the new users.
  * Append a public key to the `~/.ssh/authorized_keys` file for each new user.


The new users then can SSH to the instance using the appropriate private keys.
**Tip**
If you re-create an instance from a platform image, users and SSH public keys that you added or edited manually (that is, users that weren't defined in the machine image) must be added again.
If you need to edit the `~/.ssh/authorized_keys` file of a user on your instance, start a second SSH session before you make any changes to the file and ensure that it remains connected while you edit the file. If the `~/.ssh/authorized_keys` file becomes corrupted or you inadvertently make changes that lock you out of the instance, you can use the backup SSH session to fix or revert the changes. Before closing the backup SSH session, test all changes you made by logging in with the new or updated SSH key.
**To create an additional SSH-enabled user:**
  1. [Generate an SSH key pair](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/managingkeypairs.htm#Managing_Key_Pairs_on_Linux_Instances) for the new user.
  2. Copy the public key value to a text file for use later in this procedure.
  3. [Sign in to the instance](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/connect-to-linux-instance.htm#top "You can connect to a running Linux instance by using a Secure Shell \(SSH\) connection.").
  4. Become the root user:
Copy
```
sudo su
```

  5. Create the new user:
Copy
```
useradd <new_user>
```

  6. Create a `.ssh` directory in the new user's home directory:
Copy
```
mkdir /home/<new_user>/.ssh
```

  7. Copy the SSH public key from the text file into the `/home/new_user/.ssh/authorized_keys` file:
**Note** <public_key> should be the SSH public key itself, not the name of the file containing the key.
Copy
```
echo <public_key> >> /home/<new_user>/.ssh/authorized_keys
```

  8. Change the owner and group of the `/home/username/.ssh` directory to the new user:
Copy
```
chown -R <new_user>:<group> /home/<new_user>/.ssh
```

  9. To enable `sudo` privileges for the new user, run the `visudo` command and edit the `/etc/sudoers` file as follows:
    1. In `/etc/sudoers`, look for:
```
%<username> ALL=(ALL) NOPASSWD: ALL
```

    2. Add the following line immediately after the preceding line:
Copy
```
%<group> ALL=(ALL) NOPASSWD: ALL
```

The new user can now sign in to the instance.


## Creating Additional Users on a Windows Instance 🔗 
For the most current steps, see [Manage User Accounts](https://docs.microsoft.com/en-us/windows-server-essentials/manage/manage-user-accounts-in-windows-server-essentials) in the Microsoft documentation.
  1. [Sign in to the instance](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/connect-to-windows-instance.htm#top "You connect to a Windows instance by using a Remote Desktop connection. Most Windows systems include a Remote Desktop client by default.") using a Remote Desktop client.
  2. On the **Start** menu, click **Control Panel**.
  3. Click **User Accounts** , and then click **User Accounts** again.
  4. Click **Manage another account**.
  5. Click **Add a user account**.
  6. Enter a **User name** and **Password**.
  7. Confirm the password, and then create a **Password hint**.
  8. Click **Next**.
  9. Verify the account, and then click **Finish**.
The new user can now sign in to the instance.


Was this article helpful?
YesNo

