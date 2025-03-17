Updated 2023-06-08
# Configure and Deploy the E-Business Suite Asserter
After registering the E-Business Suite Asserter in IAM, you must configure and deploy the E-Business Suite Asserter that will act as an interface between an identity token issued by IAM and a user session created in Oracle E-Business Suite.
  * [Creating a Wallet for the E-Business Suite Asserter](https://docs.oracle.com/en-us/iaas/Content/Identity/ebs/create-wallet-e-business-suite-asserter.htm#create-wallet-e-business-suite-asserter "For security purposes, the E-Business Suite Asserter component uses a wallet to register the client ID, client secret, and IAM URL as parameters.")
  * [Updating the E-Business Suite Asserter Configuration File](https://docs.oracle.com/en-us/iaas/Content/Identity/ebs/update-ebs-asserter-configuration-file.htm#update-ebs-asserter-configuration-file "After you register the IAM E-Business Suite Asserter \(EBS Asserter\), you can configure the asserter configuration file to connect with IAM during authentication.")
  * [Configuring Hostname Verification in WebLogic Console](https://docs.oracle.com/en-us/iaas/Content/Identity/ebs/configure-hostname-verification-weblogic-console.htm#configure-hostname-verification-weblogic-console "You can configure the hostname verification in Oracle WebLogic Server Administration Console.")
  * [Configuring Keystores in WebLogic Console](https://docs.oracle.com/en-us/iaas/Content/Identity/ebs/configure-keystores-weblogic-console.htm#configure-keystores-weblogic-console "Using If you are using Custom Trust Store in WebLogic for asserter deployment, instead of using Custom Identity and Custom Trust Store with WebLogic server, use Custom Identity and Java Trust Store. With this configuration, you do not need to import IAM certificate.")
  * [Defining the Data Source](https://docs.oracle.com/en-us/iaas/Content/Identity/ebs/define-data-source.htm#define-data-source "In the Oracle WebLogic Server where E-Business Suite Asserter is deployed, you must configure database connectivity by adding data sources to your WebLogic domain. WebLogic Java Database Connectivity \(JDBC\) data sources provide database access and database connection management.")
  * [Deploying the E-Business Suite Asserter on Oracle WebLogic Server](https://docs.oracle.com/en-us/iaas/Content/Identity/ebs/deploy-ebs-asserter-weblogic-server.htm#deploy-ebs-asserter-weblogic-server "You must deploy the E-Business Suite Asserter to the Administration Server instance of Oracle WebLogic Server to perform end-to-end testing of the integration.")


Was this article helpful?
YesNo

