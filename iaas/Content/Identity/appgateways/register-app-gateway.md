Updated 2025-01-14
# Creating an App Gateway
Create an app gateway in IAM, add hosts, and associate each host with enterprise applications, which the app gateway protects.
Part of setting up app gateway is to register the app gateway in IAM with the following actions:
  * Defining host identifiers. Each host identifier represents a domain name and port number that the app gateway uses to proxy the enterprise application.
  * Associating an existing enterprise application with a host identifier.


You use the client ID and client secret from the app gateway you create when you set up the app gateway server. See [Setting up App Gateway](https://docs.oracle.com/en-us/iaas/Content/Identity/appgateways/set-app-gateway.htm#set-app-gateway "The tasks you need to perform to set up and manage app gateway in IAM."). 
You must be assigned to either the Identity Domain Administrator role or the Security Administrator role.
  1. Open the **navigation menu** and select **Identity & Security**. Under **Identity** , select **Domains**.
  2. Select the name of the identity domain that you want to work in. You might need to change the compartment to find the domain that you want.
  3. Select **Security** and then **App gateways**.
  4. Select **Create app gateway**.
  5. Enter a name for the app gateway and an optional description.
  6. Select **Add app gateway**.
  7. On the Add hosts page, select **Add host**.
    1. For **Host Identifier** , enter a name.
    2. Enter the **Host** and **Port** values that the app gateway server uses to respond to HTTP requests.
    3. For the app gateway to listen to HTTP requests in secure mode (HTTPS), select **SSL Enabled**.
For the app gateway to listen only to nonsecure HTTP requests, leave the checkbox clear.
    4. If you select **SSL Enabled** , you can optionally add more properties to specify the certificate key pair the app gateway server uses, and protocols and ciphers for SSL, such as the following examples:
```
ssl_certificate **/usr/local/example.com.rsa.crt**;
ssl_certificate_key **/usr/local/example.com.rsa.key**;
ssl_protocols TLSv1 TLSv1.1 TLSv1.2;
ssl_ciphers HIGH:!aNULL:!MD5;
```

       * **/usr/local/example.com.rsa.crt** is the full path of a certificate in the app gateway server.
       * The **/usr/local/example.com.rsa.key** is the secret key of that certificate file.
You must upload both certificate files to the app gateway server after you install the app gateway binary file.
    5. Select **Add host**.
  8. Select **Next**.
  9. Select **Add apps**.
The following image shows the mappings that you configure between the app gateway and your enterprise application:
![example values used to configure an enterprise application, and an App Gateway in the IAM console](https://docs.oracle.com/en-us/iaas/Content/Resources/Images/iam-myappgateway_example.png)
    1. **Application:** Select the enterprise application you want to protect with this app gateway.
**Note** The enterprise application must be in **Active** status.
    2. **Select a host** : Select the host identifier to which the app gateway proxies the enterprise application.
    3. **Resource prefix:** Enter the URL prefix used by the app gateway to proxy the enterprise application. For example, to have every request after the root path forwarded to the enterprise application, use `/` .
You can assign many enterprise applications to the same app gateway.
Ensure that, for each application, the value of the resource prefix is different. For example, if you have `http://myapp.internal.example.com:3266/myapp1/page.jsp` and `http://myapp.internal.example.com:6355/myapp2/page.jsp`, both accessible through `http://myappgateway.example.com:4443/` app gateway URL, enter `/myapp1` as resource prefix when you register application 1, and `/myapp2` as resource prefix when you register application 2.
    4. **Origin server:** This is the base URL where the application is hosted. If the application isn't directly accessible but accessible through a web proxy, enter the URL of the web proxy.
    5. **Additional properties:** Add other properties to provide more configuration for the application. The values specified into the field are NGINX directives or statements which are part of location block in `nginx.conf`. Some examples:
      1. If protected applications need to do further redirects or to access resources after successful authentication with the app gateway, you can use this field to populate the host header with correct value and pass it to the application.
For example, if a user accesses the application using `https://myappgateway.example.com:4443/home`, the browser passes the host header to the app gateway with the value set to `Host: myappgateway.example.com:4443`. This value is passed by the app gateway to the downstream application. To do this, add either of these values as additional properties:
```
proxy_set_header host "myappgateway.example.com:4443";
```

or
```
proxy_set_header host $http_host;
```

`$http_host` is a variable and its value is populated with the host header the app gateway receives from the browser or from a client.
**Note** If the there are load balancers sitting behind the app gateway, it's the load balancer's job to forward the actual host header to app gateway so that `$http_host` is populated with the correct value and the app gateway can forward it to the application.
      2. If the application is accessible through a web proxy, use the following command:
```
proxy_set_header host "myapp.internal.example.com";
```

`"myapp.internal.example.com"` is the domain name where the application is hosted, also known as origin server.
In this case, the app gateway can't pass the host header received from browser or other client and applications can't do further redirects using the app gateway.
  10. Select **Add app**.
  11. Select **Close**.
  12. On the app gateway details page, note the value of the client ID and client secret, which you use when you configure the app gateway server.


Was this article helpful?
YesNo

