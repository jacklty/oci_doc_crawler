Updated 2024-02-13
# Develop a Custom SCIM Gateway
If your custom application doesn't provide a SCIM-based interface, then you can develop a custom SCIM gateway to act as the interface between IAM and your custom application. This gateway exposes your application's identity store as SCIM-based REST APIs, and then you can use the Generic SCIM App Template to integrate IAM with your application for provisioning or synchronization purposes.
Before developing your custom SCIM gateway, if you're a new developer who isn't familiar with the SCIM standard, then you must first understand the SCIM protocol. Then, see which identity attributes are available for your custom application and model them as SCIM-based attributes. Next, utilize open-standard libraries to expose your custom application's APIs as SCIM APIs. Last, familiarize yourself with the create, read, update, and delete (CRUD) operations that you want your custom SCIM gateway to perform.
  * [Supported Operations](https://docs.oracle.com/en-us/iaas/Content/Identity/scim/supported-operations.htm#supported-operations "Manage user resources in SCIM applications in an OCI IAM identity domain.")
  * [Securing the Custom SCIM Gateway](https://docs.oracle.com/en-us/iaas/Content/Identity/scim/how-do-you-secure-custom-scim-gateway.htm#how-do-you-secure-custom-scim-gateway "Secure the custom SCIM gateway in an OCI IAM identity domain.")
  * [Sample Implementation of a Custom SCIM Gateway](https://docs.oracle.com/en-us/iaas/Content/Identity/scim/sample-implementation-custom-scim-gateway.htm#sample-implementation-custom-scim-gateway "Oracle provides a sample application that conforms to SCIM specifications, and which you can use to develop a custom SCIM gateway to integrate it with your custom application.")
  * [Configuring and Running the Custom SCIM Gateway Sample Application](https://docs.oracle.com/en-us/iaas/Content/Identity/scim/configure-and-run-custom-scim-gateway-sample-application.htm#configure-and-run-custom-scim-gateway-sample-application "Configure and run the custom SCIM gateway sample application in an OCI IAM identity domain to work with the GenericScim - Basic template.")
  * [Registering the Custom SCIM Gateway Application](https://docs.oracle.com/en-us/iaas/Content/Identity/scim/register-custom-scim-gateway-application.htm#register-custom-scim-gateway-application "Register the custom SCIM gateway sample application with IAM.")
  * [Using REST APIs to Update the Custom SCIM Gateway Application](https://docs.oracle.com/en-us/iaas/Content/Identity/scim/update-custom-scim-gateway-application-using-rest-api.htm#update-custom-scim-gateway-application-using-rest-api "Use REST APIs to update the port, and sslEnabled parameters of the custom SCIM gateway application.")
  * [Testing Your Custom SCIM Gateway Sample Application](https://docs.oracle.com/en-us/iaas/Content/Identity/scim/test-your-custom-scim-gateway-sample-application.htm#test-your-custom-scim-gateway-sample-application "Test your custom SCIM gateway sample application in an OCI IAM identity domain by provisioning users in an identity domain with it.")


Was this article helpful?
YesNo

