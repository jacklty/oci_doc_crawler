Updated 2025-01-14
# Updating a Network Source
Update a network source in IAM to change the set of IP ranges from which users can sign in.
  1. Open the **navigation menu** and select **Identity & Security**. Under **Identity** , select **Network Sources**. 
A list of the network sources in the tenancy is displayed.
  2. Locate the network source in the list and select its name to view its details.
  3. To edit the description of the network source, select **Edit** , enter a new description, and select **Save Changes**.
  4. To add more allowed IP addresses to this network source, under **Networks** , select **Add Networks**. In the **Add Networks** panel, specify a network as follows, and then select **Update** :
     * **Virtual Cloud Network:** Select this option and enter the following information:
       * **Select VCN:** Choose the VCN that you want to allow. If needed, select **Change Compartment** to find a VCN in a different compartment.
       * **IP Address/CIDR Block:** Enter an IP address from the VCN or a subnet CIDR block. For example: 10.0.0.0/16 or 10.0.0.4.
If you want to allow all subnets from the specified VCN, enter 0.0.0.0/0.
Select **+ Another IP Address/CIDR Block** to add another allowed address or range from the same VCN
     * **Public Network:** Select **IP Address/CIDR Block** and enter a specific IP address or CIDR block range. For example: 192.0.2.143.
Select **+ Another IP Address/CIDR Block** to add another allowed address or range.
  5. To remove an allowed source, under **Networks** , select the Actions menu (![Actions Menu](https://docs.oracle.com/en-us/iaas/Content/libraries/global-images/actions-menu.png)) and select **Delete**.


Was this article helpful?
YesNo

