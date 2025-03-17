Updated 2023-09-12
# Install and configure App Gateway
The tasks you need to perform to set up and manage app gateway in IAM.
The steps are:
  1. Register the app gateway in IAM from the Console and assign one or more enterprise applications.
  2. Download the App Gateway binary file from IAM, and install, configure and start the server.
  3. Test access to the application through the app gateway.


Any version of Windows server above 2012 R2 is supported. We recommend you use Windows Server 2016 or later.
  * Registering the app gateway in IAM:
    * [Creating an App Gateway](https://docs.oracle.com/en-us/iaas/Content/Identity/appgateways/register-app-gateway.htm#register-app-gateway "Create an app gateway in IAM, add hosts, and associate each host with enterprise applications, which the app gateway protects.")
    * [Activating an App Gateway](https://docs.oracle.com/en-us/iaas/Content/Identity/appgateways/activate-app-gateways.htm#activate-app-gateways "Activate an app gateway in IAM after registering it and before setting up the app gateway server.")
    * [Modifying an App Gateway](https://docs.oracle.com/en-us/iaas/Content/Identity/appgateways/modify-app-gateway.htm#modify-app-gateway "Modify an app gateway in IAM.")
    * [Viewing Details about an App Gateway](https://docs.oracle.com/en-us/iaas/Content/Identity/appgateways/view-details-app-gateway.htm#view-details-app-gateway "View the details of an app gateway in IAM.")
    * [Deleting an App Gateway](https://docs.oracle.com/en-us/iaas/Content/Identity/appgateways/remove-app-gateways.htm#remove-app-gateways "Delete an app gateway from IAM.")
  * Installing and configuring the app gateway server:
    * [Downloading and Extracting the App Gateway Binary File](https://docs.oracle.com/en-us/iaas/Content/Identity/appgateways/download-and-extract-app-gateway-open-virtual-applicance-file.htm#download-and-extract-app-gateway-open-virtual-applicance-file "The app gateway binary file you download from the IAM Console is a compressed \(.zip\) file. This file contains an Open Virtual Appliance \(.ova\) file which you use to install the App Gateway server.")
    * [Install App Gateway on OCI](https://docs.oracle.com/en-us/iaas/Content/Identity/appgateways/install-app-gateway-oracle-cloud-infrastructure.htm#install-app-gateway-oracle-cloud-infrastructure "To install App Gateway on OCI, you need to upload the App Gateway virtual disk image file to a Bucket in Oracle Cloud Infrastructure, create a Custom Image using the App Gateway virtual disk image file, and then create a Compute instance based on this custom image.")
    * [Install App Gateway Using Oracle VM Virtual Box](https://docs.oracle.com/en-us/iaas/Content/Identity/appgateways/install-app-gateway-oracle-vm-virtual-box-software.htm#install-app-gateway-oracle-vm-virtual-box-software "To install App Gateway using Oracle VM Virtual Box, import the App Gateway Open Virtual Appliance \(OVA\) file in an Oracle VM Virtual Box, and then configure the App Gateway virtual machine to receive HTTP request.")
    * [Deploy the Oracle App Gateway Docker Container](https://docs.oracle.com/en-us/iaas/Content/Identity/appgateways/deploy-oracle-app-gateway-docker-container.htm#deploy-oracle-app-gateway-docker-container "App Gateway can be deployed by using OVA or using Docker. Learn how to deploy the Oracle App Gateway Docker container.")
    * [Configuring the App Gateway Server](https://docs.oracle.com/en-us/iaas/Content/Identity/appgateways/configure-app-gateway-server.htm#configure-app-gateway-server "Before you start the App Gateway server for the first time, you need to configure the server to connect with IAM.")
    * [Start and Stop App Gateway](https://docs.oracle.com/en-us/iaas/Content/Identity/appgateways/start-and-stop-app-gateway.htm#start-and-stop-app-gateway "You can start and stop App Gateway server and App Gateway agent using scripts, or using the services installed in the server where your App Gateway runs.")
    * [Enable Session Persistence with Sticky Cookies](https://docs.oracle.com/en-us/iaas/Content/Identity/appgateways/enable-session-persistence-sticky-cookies.htm#enable-session-persistence-sticky-cookies "Enable persistent sessions using cookies in an App Gateway. The sticky cookie is forwarded to the same backend server.")
  * [Testing Access to your Application Using App Gateway](https://docs.oracle.com/en-us/iaas/Content/Identity/appgateways/test-access-your-application-using-app-gateway.htm#test-access-your-application-using-app-gateway "Test access to your enterprise application after you configure the App Gateway server to communicate with your IAM instance and start the server.")


Was this article helpful?
YesNo

