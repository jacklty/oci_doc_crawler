Updated 2025-01-14
# Creating a Network Source
Create a network source in IAM to restrict the set of IP ranges from which users can sign in.
  1. Open the **navigation menu** and select **Identity & Security**. Under **Identity** , select **Network Sources**.
A list of the network sources in your tenancy is displayed.
  2. Select **Create Network Source**. 
  3. Enter the following information: 
     * **Name:** Enter a unique name for the network source. The name must be unique in your tenancy. You can't change this later. Avoid entering confidential information.
     * **Description:** A friendly description. You can change this later.
     * **Networks:** Select one of the following network types:
       * **Virtual Cloud Network:** Enter the following information for this option:
         * **Select VCN:** Choose the VCN that you want to allow. If needed, select **Change Compartment** to find a VCN in a different compartment.
         * **IP Address/CIDR Block:** Enter an IP address from the VCN or a subnet CIDR block. For example: 10.0.0.0/16 or 10.0.0.4.
If you want to allow all subnets from the specified VCN, enter 0.0.0.0/0.
Select **+ Another IP Address/CIDR Block** to add another allowed address or range from the same VCN.
       * **Public Network:** For **IP Address/CIDR Block** , enter a specific IP address or CIDR block range. For example: 192.0.2.143.
Select **+ Another IP Address/CIDR Block** to add another allowed address or range.
  4. To add more IP ranges to this network source, select **+ Add network**.
  5. To add tags to the network resource, select **Show advanced options**.
If you have permissions to create a resource, then you also have permissions to apply free-form tags to that resource. To apply a defined tag, you must have permissions to use the tag namespace. For more information about tagging, see [Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). If you're not sure whether to apply tags, skip this option or ask an administrator. You can apply tags later. You can apply tags later.
  6. To immediately create another network source, select **Create another network source** before selecting **Create**. Otherwise just select **Create**.


Was this article helpful?
YesNo

