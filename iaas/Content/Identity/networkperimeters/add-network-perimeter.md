Updated 2025-02-28
# Creating a Network Perimeter
Create a network perimeter in an identity domain in IAM and configure it to restrict the IP addresses that users can use to sign in.
  1. On the **Network perimeters** list page, select **Create network perimeter**. If you need help finding the list page, see [Listing Network Perimeters](https://docs.oracle.com/en-us/iaas/Content/Identity/networkperimeters/listing_network_perimeters.htm#listing_network_perimeters "Retrieve a list of network perimeters.").
  2. Enter the name of the network perimeter and the exact IP address or IP addresses, IP range, or masked IP address range for the network perimeter. To learn about IP address formats, see [Managing Network Perimeters](https://docs.oracle.com/en-us/iaas/Content/Identity/networkperimeters/overview.htm#understand-network-perimeters "Network perimeters in an identity domain in IAM restrict the IP addresses that users can use to sign in.").
  3. Select **Create**.

Now, create a sign-on policy rule that includes the network perimeter. To learn about using this network perimeter in sign-on policy rules, see [Creating a Sign-On Policy](https://docs.oracle.com/en-us/iaas/Content/Identity/signonpolicies/add-sign-policy.htm#add-sign-policy "Add a sign-on policy to an identity domain in IAM.").
Was this article helpful?
YesNo

