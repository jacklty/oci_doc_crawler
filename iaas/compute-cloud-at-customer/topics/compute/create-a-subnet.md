Updated 2024-08-06
# Task 3: Create a Subnet
A subnet is a subdivision of your VCN. The subnet directs traffic according to a route table.
For this tutorial, you'll access the instance over the internet using its public IP address, so your route table directs traffic to an internet gateway. The subnet also uses a security list to control traffic in and out of the instance.
Avoid entering confidential information in names and tags.
  1. Return to the **Virtual Cloud Networks** page.
A quick way to do this is to click the name of page in the breadcrumb that's at the top of the page. For example:
![A screen shot of the breadcrumb string that's at the top of the page.](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/images/m3-9-subnet.png)
If the VCN details page isn't in your breadcrumb, in the navigation menu, click **Networking** , **Virtual Cloud Networks** , then click the name of your VCN.
  2. Scroll down to the **Resources** panel, click **Subnets** , and click **Create Subnet**.
  3. In the **Create Subnet** dialog box, enter the following information:
     * **Name:** Enter a descriptive name for your subnet.
     * **Create in Compartment:** Select the Sandbox compartment.
     * **CIDR Block:** Enter a valid CIDR block for the subnet. The value must be within the VCN CIDR block. For example, 10.0.0.0/24.
     * **Route Table:** For this tutorial, select the default route table.
     * **Subnet Access:** For this tutorial, select Public Subnet to allow public IP addresses for instances in the subnet.
     * **Use DNS Hostnames in this Subnet:** For this tutorial, leave this unselected.
     * **DHCP Options:** Leave this unselected.
     * **Security Lists:** Click Add Security List and select the default security list.
     * **Tagging:** Leave blank. This tutorial does not use tags.
  4. Click **Create Subnet**.


**Perform the next task:**
[Task 4: Create an Internet Gateway and Configure Route Rules](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/compute/create-an-internet-gateway-and-configure-route-rules.htm#create-an-internet-gateway-and-configure-route-rules "An internet gateway is an optional virtual router you can add to your VCN to enable access to your data center network.")
Was this article helpful?
YesNo

