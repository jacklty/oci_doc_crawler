Updated 2025-01-14
# Quick Start
Quickly get started with the identity domains REST API by completing prerequisites, installing curl, and setting up authorization to manage your identity domain resources such as users, groups, and applications. 
## Prerequisites 🔗 
  1. Buy an Oracle Cloud Subscription: See [Buy an Oracle Cloud Subscription](https://docs.oracle.com/iaas/Content/GSG/Tasks/buysubscription.htm).
  2. Activate your order: Set up your account or activate your order. See _Activate Your Order from Your Welcome Email_ in [Buy an Oracle Cloud Subscription](https://docs.oracle.com/iaas/Content/GSG/Tasks/buysubscription.htm).
  3. Obtain the appropriate account credentials and authorization to access identity domain APIs from your identity domain administrator: 
     * **To sign in to your identity domain.** See your identity domain administrator to obtain your username, password, and identity domain name.
     * **To use the API without a user account.** Administrators can use the identity domains API without a user account in the identity domain. To use the identity domains API without a user account, request a client ID and a client secret from the identity domain administrator.


## Step 1: Sign In to Your Identity Domain 🔗 
After you activate your account, you're sent sign-in credentials and a link to the home page of your identity domain. Select the link in the email, and then enter the provided sign-in credentials. Your identity domain home page appears. See [Sign In to the Console](https://docs.oracle.com/iaas/Content/GSG/Tasks/signingin.htm). 
## Step 2: Install cURL 🔗 
The examples within this document use the `cURL` command line tool to demonstrate how to access the identity domains REST API.
To connect securely to the server, you must install a version of cURL that supports SSL and provide an SSL certificate authority (CA) certificate file or bundle to authenticate against the Verisign CA certificate. For more information about:
  * Using cURL, see [Using cURL](https://docs.oracle.com/en-us/iaas/Content/Identity/api-getstarted/UsecURL.htm "cURL is an open source, command line tool for transferring data with URL syntax, supporting various protocols including HTTP and HTTPS. The examples within this document use cURL to demonstrate how to access the identity domains REST API.").
  * Authorization, see [Managing Authorization Using the API](https://docs.oracle.com/en-us/iaas/Content/Identity/api-getstarted/api-managing-authorization.htm "The identity domains REST API supports both token-based authorization and OCI request signatures. For security reasons, the identity domains REST API isn't accessible using only the username and password that you use to sign in to the identity domain. To access the identity domains REST API, you need an OAuth2 access token or an API key to use for authorization.").


The following procedure demonstrates how to install cURL on a Windows 64-bit system.
  1. In a browser, navigate to the cURL home page at <http://curl.haxx.se/download.html>.
  2. On the cURL Releases and Downloads page, find the SSL-enabled version that corresponds to your OS, and then select the link to download the ZIP file.
  3. Install the software.
  4. Navigate to the cURL CA Certs page at <http://curl.haxx.se/docs/caextract.html>, and then download the **ca-bundle.crt** SSL certificate authority (CA) certificate bundle into the folder where you installed cURL.
  5. Set the cURL environment variable: 
    1. Open a command window.
    2. Navigate to the directory where you installed cURL.
    3. Set the cURL environment variable (CURL_CA_BUNDLE) to the SSLCA certificate bundle location. For example: `C:\curl> set CURL_CA_BUNDLE=ca-bundle.crt`.


## Step 3: Understand the Resource URL Format 🔗 
You access the identity domains REST API using a URL, which includes the REST endpoint, the resource that you want to access, and any query parameters that you want to include in a request.
The basic endpoint for the identity domains REST API is:
```
https://<domainURL>/admin/v1/
```

See [Send Requests](https://docs.oracle.com/en-us/iaas/Content/Identity/api-getstarted/SendRequests.htm#SendRequests "Follow these guidelines when you build send requests using the identity domains REST API.") for specific details on building these URLs.
## Step 4: Set Up Authorization 🔗 
You need to generate the access token that you can then use to authorize requests that you send to the identity domains REST API. See [Managing Authorization Using the API](https://docs.oracle.com/en-us/iaas/Content/Identity/api-getstarted/api-managing-authorization.htm "The identity domains REST API supports both token-based authorization and OCI request signatures. For security reasons, the identity domains REST API isn't accessible using only the username and password that you use to sign in to the identity domain. To access the identity domains REST API, you need an OAuth2 access token or an API key to use for authorization.").
You're now ready to send requests to an identity domain using `cURL`.
## Step 5: Manage Your Identity Domain Resources 🔗 
Begin using the REST API to manage overall identity domain configurations and identities and resources.
Was this article helpful?
YesNo

