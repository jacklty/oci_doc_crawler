Updated 2024-10-18
# Connecting to an Instance on a Private Subnet Using a Bastion
Use Oracle Cloud Infrastructure Bastion to connect to compute instances that don't have public IP addresses.
A subnet attached to an instance is either public or private. Instances on a private subnet can't have public IP addresses. [Bastion](https://docs.oracle.com/iaas/Content/Bastion/Concepts/bastionoverview.htm) provides restricted and time-limited access to instances that don't have public IP addresses.
Bastions let authorized users connect from specific IP addresses to instances using SSH sessions. When connected to a session, users can interact with the instance by using any software or protocol supported by SSH.
The Bastion service recognizes the following [types of sessions](https://docs.oracle.com/iaas/Content/Bastion/Concepts/bastionoverview.htm#session_types):
  * Managed SSH sessions provide administrative access to the instance's operating system. To connect to an instance using this session type the Bastion plugin must be enabled on the instance, and plugins must be running.
  * Port forwarding sessions (also known as SSH tunneling) create a secure connection between a specific port on the client machine and a specific port on the instance. Using this SSH connection you can relay other protocols, such as the Remote Desktop Protocol (RDP).
  * Dynamic port forwarding (SOCKS5) sessions have the same benefits of an SSH port forwarding session, but let you dynamically connect to any target resource in a private subnet. Unlike other session types that you configure to connect to a specific target resource (IP address or DNS name), with a dynamic port forwarding (SOCKS5) session you create a tunnel to a target subnet and the client decides which resource and port to connect to.


For information on Bastion, see: [Bastion](https://docs.oracle.com/iaas/Content/Bastion/Concepts/bastionoverview.htm)
For information about connecting to instances that have public IP addresses, see [Connecting to an Instance](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/accessinginstance.htm#top "You can connect to a running compute instance by using a Secure Shell \(SSH\) or Remote Desktop connection.").
Was this article helpful?
YesNo

