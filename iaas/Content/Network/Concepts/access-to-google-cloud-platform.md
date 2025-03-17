Updated 2025-01-06
# Access to Google Cloud Platform
Use Oracle Interconnect for Google Cloud to connect your Google Cloud resident applications or services with Oracle Cloud Infrastructure resident services. That way, you'll have a provisioned, secure, and low-latency network link between Oracle Cloud and Google Cloud.
## About Oracle Interconnect paired regions
Google Cloud regions are paired to specific OCI regions. When you create Google Cloud resources in a particular region, you must create OCI resources in the paired OCI region. For example, if you have created Google Cloud resources in the asia-northeast1 Google Cloud region, then you must configure OCI resources in the ap-tokyo-1 OCI region. The following table lists the Google Cloud region and paired OCI region.
For the latest list of Oracle Interconnect paired regions, see [Oracle Interconnect for Google Cloud](https://www-sites.oracle.com/cloud/google/interconnect/).
Google Cloud region | Paired Oracle Cloud Infrastructure region  
---|---  
asia-northeast1 | ap-tokyo-1  
asia-south1 | ap-mumbai-1  
asia-southeast1 | ap-singapore-1  
australia-southeast1 | ap-sydney-1  
australia-southeast2 | ap-melbourne-1  
europe-southwest1 | eu-madrid-1  
europe-west2 | uk-london-1  
europe-west3 | eu-frankfurt-1  
europe-west6 | eu-zurich-1  
northamerica-northeast1 | ca-montreal-1  
northamerica-northeast2 | ca-toronto-1  
southamerica-east1 | sa-saopaulo-1  
us-east4 | us-ashburn-1   
## Connecting Google Cloud to Oracle Cloud
  1. In Google Cloud, provision a Partner Cross-Cloud Interconnect connection. You’ll need a single or redundant pair of VLAN attachments in your virtual private cloud (VPC) network. Notate the pairing key you receive from Google Cloud. To provision Partner Cross-Cloud Interconnect connections, see [Partner Cross-Cloud Interconnect for Oracle Cloud Infrastructure (OCI) provisioning overview](https://cloud.google.com/network-connectivity/docs/interconnect/how-to/partner-cci-for-oci/provisioning-overview) in Google Cloud help. 
  2. Create a FastConnect port for your Partner Cross-Cloud Interconnect connection. To create FastConnect ports, see [FastConnect: With an Oracle Partner](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/fastconnectprovider.htm#FastConnect_With_an_Oracle_Partner "This topic is for customers who want to use Oracle Cloud Infrastructure FastConnect by connecting to an Oracle Partner.").
  3. [Configure OCI resources](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/access-to-google-cloud-platform.htm#Configure_OCI_Resources "Configure OCI resources to connect with Google Cloud platform."). You’ll need a VCN with subnet, and a DRG attached to the VCN. Then with your pairing key, you’ll create private circuits for your VLAN attachments. 


## Configure OCI Resources 🔗 
Configure OCI resources to connect with Google Cloud platform.
OCI resources must be created in the OCI region paired to the Google Cloud region. For a list of Oracle Interconnect paired regions, see [Access to Google Cloud Platform](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/access-to-google-cloud-platform.htm#Access_to_Google_Cloud_Platform "Use Oracle Interconnect for Google Cloud to connect your Google Cloud resident applications or services with Oracle Cloud Infrastructure resident services. That way, you'll have a provisioned, secure, and low-latency network link between Oracle Cloud and Google Cloud.").
  1. Create a Virtual Cloud Network (VCN). To create a VCN, see [Creating a VCN](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/create_vcn.htm).
  2. Create a subnet in the VCN. To create a subnet, see [Creating a subnet](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/create_vcn.htm).
  3. Create a Dynamic Routing Gateway (DRG) and attach it to your VCN. To create a DRG, see [Create a DRG](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/drg-create.htm).
  4. Create a private virtual circuit for each VLAN attachment. You'll need the pairing key generated when you created the VLAN attachment earlier. If you created a pair of VLAN attachments, complete the following steps for each one.
    1. Go to the Oracle Cloud console, and on the toolbar, select the Oracle Interconnect paired region.
    2. On the main menu, click **Networking**. Under **Customer connectivity** , click **FastConnect**.
    3. In the **Compartment** list, select the compartment that contains the DRG you created earlier. This compartment, along with a corresponding IAM policy, controls who can access the virtual circuit
    4. Click **Create FastConnect**.
    5. Select **FastConnect partner**.
    6. In the **Partner** list, select **Google Cloud: OCI Interconnect**.
    7. Click **Next**.
    8. In the **Name** box, enter the name of the circuit. The value does not need to be unique across your virtual circuits, and you can change it later.
    9. In the **Compartment** list, leave it as is (the compartment you're currently in).
    10. Select **Private virtual circuit**.
    11. Select **All traffic**.
    12. In the **Dynamic routing gateway** list, the DRG you created earlier displays. If it doesn't display, try checking your compartment.
    13. In the **Provisioned bandwidth** list, select the capacity that you chose for your VLAN attachment (or the closest value available).
    14. In the **Partner service key** box, enter the pairing key you received from Google Cloud when you created the VLAN attachment.
    15. In the **MTU** list, select **1500**.
    16. Click **Create**. The virtual circuit is provisioned. Check the status of provisioning virtual circuits in FastConnect. After the virtual circuit is provisioned, the connection to Google Cloud will be active. Then you can activate any VLAN attachments that you didn’t pre-activate when you created them.


Was this article helpful?
YesNo

