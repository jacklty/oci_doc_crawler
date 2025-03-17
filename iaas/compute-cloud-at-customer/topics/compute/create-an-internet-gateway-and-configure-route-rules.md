Updated 2023-09-28
# Task 4: Create an Internet Gateway and Configure Route Rules
An internet gateway is an optional virtual router you can add to your VCN to enable access to your data center network.
The gateway supports connections initiated from within the VCN (egress) and connections initiated from the internet (ingress).
Security list rules control the types of traffic allowed in and out of resources in that subnet. Ensure to only permit the required types of internet traffic.
Each public subnet that needs to use the internet gateway must have a route table rule that specifies the gateway as the target.
Avoid entering confidential information in names and tags.
  1. Navigate to your VCN details page.
  2. In the **Resources** panel, select **Internet Gateways**.
  3. Click **Create Internet Gateway**.
  4. Enter the required information:
     * **Name:** Enter a descriptive name for your internet gateway.
     * **Create in Compartment:** Select the Sandbox compartment.
     * **Enabled:** Select whether you want this internet gateway to be enabled upon creation.
     * **Tagging:** Leave blank. This tutorial doesn't use tags.
  5. Click **Create**.
  6. Under **Resources** , click **Route Tables**.
  7. Click the name of the default route table.
  8. Scroll down to the **Resources** panel and click **Add Route Rules**.
  9. On the**Create Route Table Rule** dialog box, enter the required information:
     * **Target Type:** From the menu, select Internet Gateway.
     * **CIDR Block:** Enter: `0.0.0.0/0` (which means that all nonintra-VCN traffic that isn't already covered by other rules in the route table will go to the target specified in this rule).
     * **Internet Gateway:** From the menu, select the name of the Internet Gateway that you created.
     * **Description:** An optional description of the rule.
  10. Click **Create Route Table Rule**.


**Perform the next task:**
[Task 5: Launch an Instance](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/compute/5-launch-an-instance.htm#_5-launch-an-instance "In this task, launch an instance with an image and a shape.")
Was this article helpful?
YesNo

