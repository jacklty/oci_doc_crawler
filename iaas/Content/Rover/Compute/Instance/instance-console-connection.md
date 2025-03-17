Updated 2025-02-21
# Instance Console Connection for Roving Edge Infrastructure
Describes how to create and manage instance console connections on a Roving Edge Infrastructure device.
Use the instance console connection feature to add support for console access to compute instances. This access lets you troubleshoot malfunctioning instances remotely via the following types of SSH-tunneled connections:
  * Serial
  * Virtual Network Computing (VNC)


You can have only one active console connection. If you want to create and use a different console connection than the one that is currently active (as indicated by it being listed as in an **Active** state), you must delete the currently-active console connection first, then create a new console connection. Any deleted console connection is listed as being in a **Deleted** state for a limited period of time, before it is removed permanently. You cannot revert a deleted console connection back to being active.
You can perform the following instance console connection tasks:
  * [Creating an Instance Console Connection](https://docs.oracle.com/en-us/iaas/Content/Rover/Compute/Instance/create-instance-console-connection.htm#top "Describes how to create an instance console connection for a Roving Edge Infrastructure device.")
  * [Listing the Instance Console Connections](https://docs.oracle.com/en-us/iaas/Content/Rover/Compute/Instance/list-instance-console-connection.htm#top "Describes how to list the instance console connections for a Roving Edge Infrastructure device.")
  * [Getting an Instance Console Connection's Details](https://docs.oracle.com/en-us/iaas/Content/Rover/Compute/Instance/get-instance-console-connection.htm#top "Describes how to get an instance console connection's details for a Roving Edge Infrastructure device.")
  * [Editing an Instance Console Connection](https://docs.oracle.com/en-us/iaas/Content/Rover/Compute/Instance/update-instance-console-connection.htm#top "Describes how to edit an instance console connection for a Roving Edge Infrastructure device.")
  * [Deleting an Instance Console Connection](https://docs.oracle.com/en-us/iaas/Content/Rover/Compute/Instance/delete-instance-console-connection.htm#top "Describes how to delete an instance console connection from a Roving Edge Infrastructure device.")
  * [Connecting to the Console of an Instance](https://docs.oracle.com/en-us/iaas/Content/Rover/Compute/Instance/console-connection-instance.htm#top "Describes how to connect to the serial or VNC console of an instance for a Roving Edge Infrastructure device using the console connection you create.")


## Unsupported CLI Commands and Parameters 🔗 
The Roving Edge Infrastructure instance console connection feature does not support all the CLI commands and parameters that are supported by the Oracle Cloud Infrastructure Cloud-based version of this feature:
  * Plink command (`oci compute instance-console-connection get-plink-connection-string`)
  * Defined tags parameter for all commands (`--defined-tags`)


## Exiting the Instance Console Connection 🔗 
**To exit the serial console connection** :
When using SSH, the `~` character at the beginning of a new line is used as an escape character.
  * To exit the serial console, enter:
Copy
```
~.
```

  * To suspend the SSH session, enter:
Copy
```
~^z
```

The `^` character represents the **CTRL** key
  * To see all the SSH escape commands, enter:
Copy
```
~?
```



**To exit the VNC console connection** :
  1. Close the VNC client. 
  2. Open the Terminal or PowerShell window and enter `CTRL C`


When you are finished using the console connection, delete the connection for the instance.
Was this article helpful?
YesNo

