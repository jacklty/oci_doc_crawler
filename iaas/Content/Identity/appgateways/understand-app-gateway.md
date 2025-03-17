Updated 2024-02-13
# Understanding App Gateway
App Gateway is a software appliance that lets you integrate applications hosted either on a compute instance, in a cloud infrastructure, or in an on-premises server with IAM for authentication purposes.
App Gateway acts as a reverse proxy protecting web applications by restricting unauthorized network access to them. App Gateway intercepts any HTTP request to these applications and ensures that the users are authenticated with IAM before forwarding the request to these applications. App Gateway propagates the authenticated user's identity to the applications.
If the user isn't authenticated with IAM, then App Gateway redirects the user to the sign-in page for credential validation.
**Note**
If you are using Cloud Gate, it's important that a user's name only contains the characters shown in [Creating a User](https://docs.oracle.com/en-us/iaas/Content/Identity/users/create-user-accounts.htm#top "Create a user account for a user in an OCI IAM identity domain.") because the display name is sent as an HTTP header. If non printable ASCII characters are used, Cloud Gate considers the request invalid and returns a 400 error.
## Uses for App Gateway 🔗 
Use App Gateway to:
  * Integrate enterprise applications hosted either on-premises or in a cloud infrastructure with IAM for authentication purposes.
For example, if you have a web application hosted on-premises or in a cloud infrastructure, you can integrate this application with any other cloud-based applications for single sign-on. Use App Gateway to integrate a web application with IAM, and then ensure that the other cloud-based applications use IAM as their authentication mechanism. All these applications use the single sign-on provided by IAM.
  * Expose intranet web applications to internet access.
If the web application is hosted and accessed over an intranet and you want to expose access to this application over the internet, use App Gateway to proxy any internet request and to require users to authenticate with IAM before accessing the intranet web application. In this case, you deploy App Gateway in the network DMZ while the application remains in the intranet zone.
  * Integrate with applications that lack a native authentication mechanism and don't support SAML federation, OAuth, or OpenID Connect integration methods.
If the application doesn't support the standards for authentication that IAM supports (SAML, OAuth, and OpenID Connect), and you can't use IAM's SDKs in the application, then you can use App Gateway to integrate the web application with IAM.
  * Integrate with applications that support the HTTP Header-based authentication.
For web applications that support HTTP Header-based authentication, the App Gateway integration method requires no change to the web application's source code. You must configure the application's authentication policies in IAM to add header variables in the request before App Gateway forwards the request to the application. By doing so, the application can identify the user authenticated with IAM.


## How App Gateway works 🔗 
The App Gateway is deployed within a customer's infrastructure, regardless of whether the infrastructure is in the cloud, on-premises, or a hybrid one. It works as a reverse proxy, intercepting all requests from the client to the application. The App Gateway then verifies if a user is already signed in to IAM. If the user has signed in, then App Gateway adds header variables to the request so that the application being protected can access the header variable. The application trusts App Gateway has identified the signed in user in identity domain values and create the user session.
Ensure that the communication between App Gateway and application is secure to avoid changes in the header variable values before the request is sent to the application.
[![shows how the application, App Gateway, the identity domain, and the user browser interacts when a user tries to access any application resource but the user isn't signed in to an identity domain](https://docs.oracle.com/en-us/iaas/Content/Resources/Images/iam-appgateway_architecture.png)](https://docs.oracle.com/en-us/iaas/Content/Resources/Images/iam-appgateway_architecture.png)
The following steps explain the form-based authentication flow between the web browser, App Gateway, and an enterprise application:
Step | Description  
---|---  
![Callout 1](https://docs.oracle.com/en-us/iaas/Content/Resources/Images/callout_iamtable1.png) | In a web browser, a user requests access to an application through a URL exposed by App Gateway.  
![Callout 2](https://docs.oracle.com/en-us/iaas/Content/Resources/Images/callout_iamtable2.png) |  App Gateway intercepts the request, verifies that the user doesn't have a session with IAM, and then redirects the user's browser to the sign-in page. In step 2, if the user has a session with IAM, it means that the user has already signed in. If so, then an access token is sent to App Gateway, and then the remaining steps are skipped.  
![Callout 3](https://docs.oracle.com/en-us/iaas/Content/Resources/Images/callout_iamtable3.png) |  IAM presents the sign-in page or whichever sign-in mechanism has been configured for the domain.  
![Callout 4](https://docs.oracle.com/en-us/iaas/Content/Resources/Images/callout_iamtable4.png) | The user signs in to IAM.  
![Callout 5](https://docs.oracle.com/en-us/iaas/Content/Resources/Images/callout_iamtable5.png) | Upon successful authentication, IAM creates a session for the user and issues an access token to App Gateway.  
![Callout 6](https://docs.oracle.com/en-us/iaas/Content/Resources/Images/callout_iamtable6.png) | App Gateway uses the token to identify the user. It then adds header variables to the request and forwards the request to the application.  
![Callout 7](https://docs.oracle.com/en-us/iaas/Content/Resources/Images/callout_iamtable7.png) | The application receives the header information, validates the user's identity, and starts the user session.  
App Gateway intercepts any subsequent request to the application's protected resources. App Gateway identifies the user, adds header variables to the request, and forwards the request to the application.
To sign out, the user calls an application's logout URL. The App Gateway identifies the logout URL and redirects the user to the identity domain's OAuth log out endpoint (`/oauth2/v1/userlogout`). After IAM signs the user out, IAM can redirect the user's browser to a URL of the application which can then remove the application's user session.
## How App Gateway Logout Works 🔗 
Users can log out from the applications protected by App Gateway using two different mechanisms: App Gateway Log out URL or by calling a resource protected by a logout authentication method.
### Use App Gateway logout URL 🔗 
App Gateway provides a central logout URL which can be used to log the user out from the single sign-on provided by IAM. Any call to this endpoint triggers the logout process. After the user is logged out, then any subsequent access to a protected application resource will require the user to sign in to IAM again.
This endpoint supports two parameters appended to the URL: 
  * **postlogouturl** : The URL of a post logout landing page. This value must be URL-encoded. If the parameter isn't specified, then App Gateway redirects the user browser to the **Logout URL** specified in the Console's **Session Settings**.
  * **state** : This is an optional parameter to be used by the enterprise application, after the logout process finishes.


**Syntax**
`http(s)://<appgateway_host>:<appgateway_port>/cloudgate/logout.html?postlogouturl=<url_encoded>&state=<state_value>`
### Log out Endpoint With Parameters
If the App Gateway base URL is `https://myappgateway.example.com:4443`, then use the following URL to log the user out from the single sign-on: `https://myappgateway.example.com:4443/cloudgate/logout.html?postlogouturl=http%3A%2F%2Fwww.oracle.com&state=123`
### Use Resource Protected by Logout authentication method 🔗 
You can create a resource in your enterprise application and configure an authentication policy for this resource using **Forms+Logout** authentication method. When the user accesses this resource, App Gateway invokes the log out process and logs the user out from the single sign-on provided by IAM.
**Syntax**
`http(s)://<appgateway_host>:<appgateway_port>/<logout_resource>`
### Resource Protected by Logout authentication method
If you created `/myapp/logout` resource in your enterprise application, and assigned **Forms+Logout** as **Authentication Method** for this resource in **Authentication Policy** section, then when users access the URL `https://myappgateway.example.com:4443/myapp/logout`, they're logged out from the single sign-on provided by IAM.
Was this article helpful?
YesNo

