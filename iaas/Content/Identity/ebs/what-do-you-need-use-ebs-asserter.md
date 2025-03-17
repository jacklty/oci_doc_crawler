Updated 2025-01-14
# What do You Need to Use the E-Business Suite Asserter
Verify which services, roles, components, and information are required to perform the configurations to integrate your Oracle E-Business Suite environment with IAM using the Identity Cloud Service E-Business Asserter.
## Before You Begin 🔗 
Before you begin using E-Business Suite Asserter, understand how to enable it, and how it works with other components.
  * If your Oracle E-Business Suite is integrated with Oracle Access Manager, Oracle Internet Directory, E-Business Suite AccessGate, or uses any other SSO profile, then remove the integration between these components and Oracle E-Business Suite, and then restart the servers before using the IAM E-Business Suite Asserter.
  * Know what's supported. All Oracle E-Business modules which use browser-based login works with E-Business Suite Asserter for SSO. Excel-based login of Web ADI is supported. Mobile Apps for EBS, such as approvals and expenses, are supported. Modules which do not use browser-based login, such as Mobile Web Applications (MWA) and E-Signature, are not supported.


## About Required Services and Roles 🔗 
An IAM administrator must be able to access the IAM Console to download E-Business Suite Asserter and configure and activate applications.
You must have access to the following services and products:
  * IAM
  * Oracle E-Business Suite


You must have the following roles:
Role | Required to...  
---|---  
IAM: Security administrator |  Access the **Downloads** page of the IAM Console. From this page, you can download the Identity Cloud Service E-Business Suite Asserter.  
IAM: Application administrator |  Manage applications in IAM, which includes registering the sample mobile app with IAM.  
Oracle E-Business Suite: Server administrator |  Access the Oracle E-Business Suite installation folder, the Oracle WebLogic Server where you deploy the E-Business Suite Asserter, and the E-Business Suite Asserter machine as an operating system user.  
See [Learn how to get Oracle Cloud services for Oracle Solutions](https://docs.oracle.com/en/solutions/get-cloud-services/index.html).
## Downloading the E-Business Suite Asserter from the IAM Console 🔗 
Access the Downloads page from the IAM Console. From this page, you can download the IAM E-Business Suite Asserter.
  1. Open the **navigation menu** and select **Identity & Security**. Under **Identity** , select **Domains**.
  2. Click the name of the identity domain that you want to work in. You might need to change the compartment to find the domain that you want. Then, click **Settings** and then **Downloads**.
  3. On the **Downloads** page, select the **Identity Cloud Service Asserter for E-Business Suite** download button.
For instances of Identity Cloud Service EBS Asserter Release 20.1.3, the feature for EBS Asserter has to be enabled.
     * If the EBS Asserter is disabled and you try to use it you see an error message.
     * Check the feature state by going to `_tenant base url_/admin/v1/FeatureInfos`.`oracle.idaas.ebs.asserter` should be marked as enabled.
  4. Save the `.zip` file to a temporary folder on your local machine (for example, `c:\temp` for Windows or `/temp` for UNIX).
  5. Extract the contents of the `.zip` file and find the location of the `ebs.war` and `idcs-wallet-<version>.jar` files.
The name of the files might vary accordingly to the version.
  6. Copy the `ebs.war` and `idcs-wallet-<version>.jar` files to a working folder into the E-Business Suite Asserter's WebLogic Server machine. For example, `/opt/ebssdk` (create this folder if it doesn't exist).


## Provide Environment Information 🔗 
Record the environment information that you need when you configure the E-Business Suite Asserter configuration file.
  * Oracle WebLogic Server host name where the E-Business Suite Asserter is deployed. For example, `ebsasserter.example.com`
  * Oracle WebLogic Server HTTPS address (including port number if not default one) where the E-Business Suite Asserter is deployed. For example,`                          https://ebsasserter.example.com:7002`
  * Oracle E-Business Suite host name. For example, `ebs.example.com`
  * Oracle E-Business Suite HTTPS address. For example, `https://ebs.example.com:8001/`
  * IAM HTTPS address (including port number if not using the default one). For example, `https://idcs-example.identity.oraclecloud.com`
  * Oracle E-Business Suite Database name. For example, `EBSDB`
  * Oracle E-Business Suite Database host. For example, `ebs.example.com`
  * Oracle E-Business Suite Database port. For example, `1521`
  * Oracle E-Business Suite APPS user password. For example, `apps`


Was this article helpful?
YesNo

