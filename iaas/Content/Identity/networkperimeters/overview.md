Updated 2025-02-28
# Managing Network Perimeters
Network perimeters in an identity domain in IAM restrict the IP addresses that users can use to sign in.
You can perform the following tasks related to network perimeters:
  * [Listing Network Perimeters](https://docs.oracle.com/en-us/iaas/Content/Identity/networkperimeters/listing_network_perimeters.htm#listing_network_perimeters "Retrieve a list of network perimeters.")
  * [Creating a Network Perimeter](https://docs.oracle.com/en-us/iaas/Content/Identity/networkperimeters/add-network-perimeter.htm#add-network-perimeter "Create a network perimeter in an identity domain in IAM and configure it to restrict the IP addresses that users can use to sign in.")
  * [Getting a Network Perimeter's Details](https://docs.oracle.com/en-us/iaas/Content/Identity/networkperimeters/view-details-network-perimeter.htm#view-details-network-perimeter "View the name and the IP addresses for a network perimeter in an identity domain in IAM.")
  * [Updating a Network Perimeter](https://docs.oracle.com/en-us/iaas/Content/Identity/networkperimeters/modify-network-perimeter.htm#modify-network-perimeter "Update the name and the IP addresses for a network perimeter in an identity domain in IAM.")
  * [Deleting a Network Perimeter](https://docs.oracle.com/en-us/iaas/Content/Identity/networkperimeters/remove-network-perimeters.htm#remove-network-perimeters "Delete one or more network perimeters in an identity domain in IAM.")


## Introduction 🔗 
After creating a network perimeter, you can prevent users from signing in to IAM if they use one of the IP addresses in the network perimeter. This is known as blocking. A blocklist contains IP addresses or domains that are suspicious. As an example, a user might be trying to sign in to IAM with an IP address that comes from a country where hacking is rampant. 
An IP address is a string of numbers that identifies the network of any device connected to the internet. It's similar to a return address on an envelope, and is associated with a human-readable domain. Because the IP address tells other devices where data is coming from, it can be a good way to track bad content.
Blocklists can list a single IP address or a (set) range of IPs. IAM can use this information to block users who try to sign in from suspicious IP addresses.
You can also configure IAM so that users can sign in, using only IP addresses contained in the network perimeter. This is known as allowlisting, where users who try to sign in to IAM with these IP addresses will be accepted. allowlisting is the reverse of blocklisting, the practice of identifying IP addresses that are suspicious, and as a result, will be denied access to IAM.
You can configure IAM so that only users who use a particular IP address or IP address in a specific range will be allowed to sign in to IAM. Or, you can configure IAM to monitor for suspicious IP addresses or IP address ranges, and prevent users who use these IP addresses from signing in to IAM.
With a network perimeter, you can define, in a standard format, an exact IP address, a range of IP addresses, or a set of masked IP addresses. Both Internet Protocol version 4 (IPv4) and Internet Protocol version 6 (IPv6) protocols are supported. 
  * Exact IP address. You can enter a single IP address or multiple IP addresses. If you enter multiple exact IP addresses, then put a comma between each one.
  * Two IP addresses, separated by a hyphen, which is an IP range. For example, if you specify the IP range of `10.10.10.1-10.10.10.10`, any user who tries to sign in to IAM with an IP address from `10.10.10.1` through `10.10.10.10` will be using an IP address that falls within the IP range.
  * Masked IP address range. Each number of an IP address is 8 bits. For example, if you have a masked range of `10.11.12.18/24`, then the first three numbers (24 bits) is the mask that must be applied to see if an IP address falls in this range. For this example, valid IP addresses will be those that begin with `10.11.12`.


**Note** The examples listed above are using IP addresses with the IPv4 protocol. However, you can apply the same formats to IP addresses that use the IPv6 protocol (for example, `B138:C14:52:8000:0:0:4D8`).
After defining network perimeters, you can assign them to a sign-on policy, and configure the policy so that if you're trying to sign in to IAM using an IP address that's defined in the network perimeter, you can sign in to IAM or you'll be prevented from accessing IAM.
See [Add a Sign-On Policy](https://docs.oracle.com/en-us/iaas/Content/Identity/signonpolicies/add-sign-policy.htm#add-sign-policy "Add a sign-on policy to an identity domain in IAM.") for more information about assigning network perimeters to a sign-on policy.
Was this article helpful?
YesNo

