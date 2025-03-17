Updated 2024-02-13
# Updating the E-Business Suite Asserter Configuration File
After you register the IAM E-Business Suite Asserter (EBS Asserter), you can configure the asserter configuration file to connect with IAM during authentication.
Starting from IAM E-Business Suite Asserter version 19.1.4-1.4.0 onward, the asserter contains a properties file called `bridge.properties`. This file is located inside the `ebs.war` file. You must update the information in the `bridge.properties` file, and then regenerate the `ebs.war` file, before deploying it to a WebLogic Server.
**Note** For E-Business Suite Asserter versions before 19.1.4-1.4.0 release, the war file might not contain the `bridge.properties` file inside. You must create this file in a folder of the E-Business Suite Asserter's WebLogic server, update its content as described in step 3, save the file, and then set an environment variable, as in the following example: `export ebs_property_file="/opt/ebssdk/bridge.properties"`
  1. In the server where you downloaded the E-Business Suite Asserter zip file, navigate to the location where you decompressed the `ebs.war` file.
  2. Using a zip utility, decompress the `ebs.war` file, locate the `bridge.properties` file, and open the file for editing.
  3. Uncomment the following properties by removing the # from the beginning of each line, and update their values as follows:
```

###########################################################
## SSO Bridge for E-Business Suite
###########################################################
# Properties File
app.url=_https://ebsasserter.example.com:7002_/ebs
app.serverid=_APPL_SERVER_ID_value_
ebs.url.homepage=_https://ebs.example.com:8001_/OA_HTML/OA.jsp?OAFunc=OANEWHOMEPAGE
ebs.ds.name=visionDS
ebs.user.identifier=username
idcs.iss.url=https://identity.oraclecloud.com
idcs.aud.url=_https://idcs-example.identity.oraclecloud.com_
#post.logout.url=_https://ebs.example.com:8001_/OA_HTML/OA.jsp?OAFunc=OANEWHOMEPAGE
wallet.path=[FULL_PATH_OF_THE_WALLET_FILE]
whitelist.urls=_https://ebs.example.com:8001_/OA_HTML/RF.jsp,_https://ebs.example.com:8001_/OA_HTML/OA.jsp,_https://ebs.example.com:8001_/OA_HTML/BneApplicationService,_https://ebs.example.com:8001_/OA_HTML/jsp/fnd/close.jsp
ebs.renew.session=true
proxy.mode=true
proxy.home.url=_https://ebs.example.com:8001_/OA_HTML/RF.jsp?function_id=1031198&resp_id=-1&resp_appl_id=0&security_group_id=0&lang_code=US
#istore.pages=ibeCZzdMinisites.jsp,ibeCAcpSSOLoginR.jsp
#idcs.user.identifier=email/username
###########################################################

```

The following table provides the description for each `bridge.properties` parameter and optional parameters supported by each EBS Asserter version.
Parameter | Description | EBS Asserter Version  
---|---|---  
`app.url` | The URL and port number for the E-Business Suite Asserter application. | 19.1.4 onward  
`app.serverid` | Corresponds to the APPL_SERVER_ID value in the `.dbc` file generated while registering the E-Business Suite Asserter. | 19.1.4 onward  
`ebs.url.homepage` | The URL address for the Oracle E-Business Suite home page. | 19.1.4 onward  
`ebs.ds.name` | The data source name to be created in the Oracle WebLogic Server where the E-Business Suite Asserter is deployed. | 19.1.4 onward  
`ebs.user.identifier` | Oracle E-Business Suite field used to match the IAM username. Allowed values are username (representing the FND_USERS.USER_NAME column) or email (representing the FND_USERS.EMAIL_ADDRESS column). Ensure that the attribute chosen here has unique values in FND_USERS otherwise the login fails. | 19.1.4 onward  
`idcs.iss.url` |  IAM issuer URL. This value can be found in the IAM Discovery Doc endpoint. The default value is `https://identity.oraclecloud.com`. This value must match the Issuer value set in the IAM OAuth settings. See [Updating OAuth Settings](https://docs.oracle.com/en-us/iaas/Content/Identity/oauth/oauth-settings.htm#managing-oauth-settings "Configure OAuth settings an identity domain in IAM so that the client always has access to any resource within the tenant regardless of the trust scope settings at the application level."). | 19.1.4 onward  
`post.logout.url` | This is an optional parameter. Uncomment this parameter so that E-Business Asserter redirects to this URL after logging the user out from the Single Sign-On. This value must match the value of the **Post Logout Redirect URL** parameter in IAM App Configuration. | 19.1.4 onward  
`wallet.path` | The full path of the wallet file, including the file name. | 19.1.4 onward  
`whitelist.urls` | Lists the URL E-Business Suite Asserter can accept as the `requestUrl` parameter value. If the `requestUrl` value doesn't match one of the `whitelist.urls` values, then the test scenario for **SSO Using the E-Business Suite Asserter Direct URL with a Redirect Parameter** fails. | 19.1.4 onward  
`ebs.renew.session` | This is an optional parameter. Use this parameter to control how the E-Business Suite Asserter manages the Oracle E-Business Suite session when the Oracle E-Business Suite cookie has expired. If you add this parameter to the `bridge.properties` file, and set the value to `true`, then the asserter refreshes the Oracle E-Business Suite Forms session after having reach the configured limit (ICX:Session Timeout). If the parameter is set to `false`, then after reaching the configured limit, the Forms session is invalidated closing all active Forms, however the Oracle E-Business Suite session in the browser will be active, allowing the user to reopen a new Forms session. | 19.2.1 onward  
`proxy.mode` | This is an optional parameter. Add this parameter to the `bridge.properties` file, and set the value to `true` to enable Oracle E-Business Suite Proxy User feature. Users trying to sign in as a proxy user, are redirected to the URL you provide in the `proxy.home.url` parameter. | 19.3.3-1.7.0 onward  
`proxy.home.url` | This attribute is mandatory if `proxy.mode=true`. After the user signs in to IAM, the EBS Asserter redirects the proxy user to this URL. Typically this URL is Oracle E-Business Suite's **Switch User** page. For example: `https://ebs.example.com:8001/OA_HTML/RF.jsp?function_id=1031198&resp_id=-1&resp_appl_id=0&security_group_id=0&lang_code=US` | 19.3.3-1.7.0 onward  
`istore.pages` | Lists the comma-separated value of iStore pages E-Business Suite Asserter accepts. If the requestUrl matches one of the `istore.pages` values, then user will be redirected to the requested iStore page post login. Add the iStore pages to the existing list of `istore.pages`. | 19.3.3-1912170009 onward  
`idcs.user.identifier` |  This is an optional parameter. The IAM user attribute used to match with `ebs.user.identifier`. Allowed values are username (representing the username attribute in IAM), email (representing the email attribute in IAM), custom attribute name (representing the custom attribute of a user in IAM e.g: `employee_no`). If this value is not provided in `bridge.properties`, then it is defaulted to the value of `ebs.user.identifier`. Ensure that there is one-to-one mapping between the `idcs.user.identifier` attribute in IAM to the `ebs.user.attribute` attribute in `FND_USERS` otherwise the login fails. **Note:** Ensure that the custom attribute used in `idcs.user.identifier` is added to the user schema in IAM. The custom attribute feature is available in EBS Asserter version 20.1.3 onwards. | 19.3.3-1912170009 onward  
`base.lang` |  The Oracle Identity Cloud Service EBS Asserter supports the user's language configuration provided in EBS. If the `FND_OVERRIDE_SSO_LANG` profile option is enabled for a user in EBS, Asserter creates an EBS session based on the value of the `ICX_LANGUAGE` profile option of this user. If no language configuration is present for the users in EBS and the browser language needs to be overwritten across all the users of the application, the `base.lang` property can be set in the `bridge.properties` file. For example, if `base.lang` is set to US and the user does not possess any language-specific configuration in EBS, irrespective of the browser (with local languages) from which the user tries to sign in into EBS with Asserter, the EBS session is created in American English. **Note:** The `base.lang` configuration is relevant in case the EBS is enabled with multiple languages. If there's only one language enabled in EBS, the asserter creates the EBS session with the base installed language even without a `base.lang` configuration. | Oracle Identity Cloud Service release version  
  4. Rebuild the `ebs.war` file and ensure it contains the updated version of the `bridge.properties` file. The structure of the `ebs.war` file is as follows:
```
META-INF/
  MANIFEST.MF
WEB-INF/
  classes/
  lib/
  bridge.properties
  web.xml
  weblogic.xml
```



Was this article helpful?
YesNo

