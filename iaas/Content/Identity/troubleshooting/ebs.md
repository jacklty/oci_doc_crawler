Updated 2023-10-02
# E-Business Suite Asserter
Learn how to troubleshoot common E-Business Suite Asserter issues.
## Resolving an Insufficient Privileges Error 🔗 
After IAM authentication, instead of getting access to Oracle E-Business Suite, the user gets redirected back to Oracle E-Business Suite with the error message "You have insufficient privileges for the current operation." and prompts the user to sign in again.
Generally, when the Oracle E-Business Suite application throws this error, it means that the cookie is set with an incorrect domain. To confirm this, check the E-Business Suite Asserter debug log (`<HOME           DIR>/ebsasserter.log`). The E-Business Suite Asserter debug log shows that the `sessionCookieDomain` has an incorrect value. The `CookieDomain` was set to `.oracle.com`.
```
Aug 22, 2018 2:26:34 PM oracle.apps.fnd.ext.common.EBiz init
FINE: Ebiz init(): sessionCookieDomain =.oracle.com ; protocol=https:; ssoCookieName= ORASSO_AUTH_HINT
```

The ICX_PARAMETERS.SESSION_COOKIE_DOMAIN must not be set to a value of any kind. You must update the SESSION_COOKIE_DOMAIN setting in ICX_PARAMETERS.
  1. Update the SESSION_COOKIE_DOMAIN value in ICX_PARAMETERS:
```
SQL> select SESSION_COOKIE_DOMAIN from ICX_PARAMETERS;
SESSION_COOKIE_DOMAIN
------------------------------
.oracle.com
```

  2. Set `session_cookie_domain` to `NULL` in the `ICX_PARAMETERS`:
```
update ICX_PARAMETERS set SESSION_COOKIE_DOMAIN = NULL;
commit;
```

  3. Restart all services.
  4. Retest the issue.


## Resolving an Internal Server Error While Logging Out 🔗 
When you are logging out from Oracle E-Business Suite, the browser throws an error message "Internal Server Error".
This issue was because of an older version of `AppsLogoutRedirect.java` in the Oracle E-Business Suite side. 
Check the header for `AppsLogoutRedirect.java` in the Oracle E-Business Suite side:
```
adident Header $JAVA_TOP/oracle/apps/fnd/sso/AppsLogoutRedirect.class
$Header AppsLogoutRedirect.java 120.10.12010000.7 2010/01/19 20:18:52 rsantis ship $
```

Apply the latest Oracle E-Business Suite Release 12 Critical Patch Update Jan 2013 or above to fix this issue. This Critical Patch Update enables `AppsLogoutRedirect.java` to use the `APPS_SSO` and `APPS_AUTH_AGENT` profiles. Check the Knowledge Document (July 2018) (Doc ID 2379675.1) for all the details to apply this patch.
## Fixing a Time Sync Issue 🔗 
While you are accessing the E-Business Suite Asserter application URL, the Oracle E-Business Suite application login flow resulted in an internal server error.
The HTTP header trace looks like this:
```
GET https://xxxxxxxxxxxxxxxxxx.oracle.com:7002/ebs/response?code=AQIDBAVcZbun_M5qU4-t9LUCYDjAOgWYiDOrf1Kb5ndbWAEYd05C-uxDfSwP8Ejfn51WT-gTuYj6bLFFYAFHQEqgYy26MTEgRU5DUllQZZIIFFVElPTl9LRVkxNCB7djF9NCAFFFABCDEF= HTTP/1.1
Error 500--Internal Server Error
From RFC 2068 Hypertext Transfer Protocol -- HTTP/1.1:
10.5.1 500 Internal Server Error
The server encountered an unexpected condition which prevented it from fulfilling the request
```

The E-Business Suite Asserter domain log looks like this:
```
####<Sep 23, 2018 6:53:31,380 PM AST> <Error> <HTTP> <ebshost01.oracle.com>
<AdminServer> <[ACTIVE] ExecuteThread: '6' for queue: 'weblogic.kernel.Default (self-
tuning)'> <<WLS Kernel>> <> <0b38f1ae-a3cb-48f6-80d9-00e3f3bdb263-000000a0>
<1537718011380> <[severity-value: 8] [rif: 0] [partition-id: 0] [partition-name:
DOMAIN]> <BEA-101020> <[ServletContext@44159983[app:ebs module:ebs.war
path:null spec-version:3.1]] Servelet failed with an Exception
```

The E-Business Suite Asserter log looks like this:
```
FINE: validateToken return with result {"user_result":"America\/New_York",
"at_hash":"1A3gT4BT0WoWCTLE3IFa5A","sub":"john.doe@oracle.com","user_locale":"en",
"idp_name":"localIDP","idp_guid":"localIDP","a mr":["USERNAME_PASSWORD"],
"iss":"https: \/\/identity.oraclecloud.com\/","user_tenantname":"idcs-a61feab148e248508205cd98cdea4232",
"client_id":"67179f2609ab46309a75e5ca1f582a53","sid":"18ee87ea-04cf-4469-a565-48ccc763caf9",
"authn_strength":"2","azp":"67179f2609ab46309a75e5ca1f582a53","auth_time":"1536180435",
"session_exp":1537715029,"user_lang":"en","exp":1536209235,"iat":1536180437"idp_type":"LOCAL",
"tenant":"idcs-a61feab148e248508205cd98cdea4232","jti":"ed7be32b-d4e1-4e72-9868-6df142f07c6b",
"user_displayname":"John Doe","sub_mappingattr":"userName","tok_type":"IT",
"aud":["https:\/\/identity.oraclecloud.com\/","67179f2609ab46309a75e5ca1f582a53"],
"user_id":"63bf3d3f96094a66a6b7714218338116"}
```

The `session_exp` is set to `1537715029`. Use `EpochConverter` to convert the current UNIX epoch time to a human readable date and time. Hence, the expiry time in the token is set to `Sunday, September 23, 2018 3:03:49 PM GMT`. However, the time in the E-Business Suite Asserter domain log is `Sep 23, 2018 6:53:31,380 PM AST`. Note that Greenwich Mean Time is 4 hours ahead of Atlantic Standard Time. Hence the time set is `Sep 23, 2018 10:53:31 PM GMT`. The system where the E-Business Suite Asserter is deployed, is not in time sync with IAM, as a result the token passed by IAM is effectively out of the validity period and hence the error "Token Expired".
Ensure the date and time on the system where the E-Business Suite Asserter is deployed is in time sync with NTP servers and hence the IAM host.
## Handling Java Error ExceptionInInitializerError 🔗 
While you are accessing the E-Business Suite Asserter application URL, the Oracle E-Business Suite application throws the java.lang.ExceptionInInitializerError error.
The E-Business Suite Asserter debug log shows the following Java error:
```
<Feb 26, 2019 2:17:16,884 PM PST> <Error> <HTTP> <BEA-101020> 
<[ServletContext@2100554246[app:ebs module:ebs.war path:null spec-version:3.1]] Servlet failed with an Exception
java.lang.ExceptionInInitializerError
at com.oracle.ebs.sso.ConnectionProvider.getConnection(ConnectionProvider.java:36)
at com.oracle.ebs.sso.RequestWrapperFilter.doFilter(RequestWrapperFilter.java:34)
at weblogic.servlet.internal.FilterChainImpl.doFilter(FilterChainImpl.java:78)
```

This occurs because of incorrect settings in the `bridge.properties` file. Verify the `bridge.properties` file and check that it has the required configuration. Also, check that the path specified in `wallet.path` in the `bridge.properties` file is valid.
## Handling Java Error RuntimeException 🔗 
While you are accessing the E-Business Suite Asserter application URL, the Oracle E-Business Suite application throws java.lang.RuntimeException.
The E-Business Suite Asserter debug log shows the following Java error:
```
<Feb 26, 2019 2:01:33,454 PM PST> <Error> <HTTP> <BEA-101020> 
<[ServletContext@1207779454[app:ebs module:ebs.war path:null spec-version:3.1]] Servlet failed with an Exception
java.lang.RuntimeException: javax.naming.NameNotFoundException: Unable to resolve 'visionDS1'. Resolved ''; remaining name 'visionDS1'
at com.oracle.ebs.sso.ConnectionProvider.getConnection(ConnectionProvider.java:42)
at com.oracle.ebs.sso.RequestWrapperFilter.doFilter(RequestWrapperFilter.java:34)
```

Check that the `ebs.ds.name` value set corresponds to the datasource name created in WebLogic.
## Fixing a Deep Link Issue 🔗 
After IAM authentication, instead of getting access to Oracle E-Business Suite, the user gets redirected back to Oracle E-Business Suite and prompts the user to sign in again.
This occurs because the deep link is not working.
Check that the `whitelist.urls` bridge property is configured. If the issue persists, specify the port numbers explicitly in the `whitelist.urls` configuration. For example, `whitelist.urls=http://ebs.oracle.com:80/OA_HTML…`. You can also check the JSESSION ID Cookie Name of the E-Business Suite Asserter App in the `weblogic.xml` file. If there is any other web app in the WebLogic with the same cookie name, there is a conflict.
## Resolving Issues During Log Out 🔗 
If you find issues during the logout process verify the **Post Logout Redirect URL** parameter value in IAM and the **post.logout.url** parameter value in the `bridge.properties` file.
The **post.logout.url** in the `bridge.properties` file is an optional parameter and by default you don't need to provide a value. You use this parameter to make the E-Business Suite Asserter application redirect the user browser to the specified URL after E-Business Suite Asserter finishes the logout process.
If enabled, the value of the **post.logout.url** in the `bridge.properties` file must match the value of the **Post Logout Redirect URL** parameter for E-Business Suite Asserter application in IAM.
  1. Open the E-Business Suite Asserter application in IAM and update the **Post Logout Redirect URL** value.
  2. Open the `ebs.war` file, update the `bridge.properties` file, regenerate the war file, and redeploy the file to the WebLogic server. Ensure the value of this parameter matches the **Post Logout Redirect URL** parameter in IAM.


## Data Source Creation Error 🔗 
If you see `Connection test failed` when you are creating the data source in the EBS Asserter's WebLogic Server machine, you may need to set the following profile options to correspond to the information in the desktop DBC file.
**Profile Option Name:** `FND`: Validate User Type
**Profile Option Code:** `FND_SERVER_SEC`
**Recommended Setting:** Desktop Only (internal value D) at the site level
**Profile Option Name:** `FND`: Validate IP address
**Profile Option Code:** `FND_SERVER_IP_SEC`
**Recommended Setting:** Desktop Only (internal value D) at the site level
**Profile Option Name:**`FND` : Desktop Nodes allowed
**Profile Option Code:** `FND_SERVER_DESKTOP_USER`
**Recommended Setting:** _< comma separated list of external nodes for which IP restriction is required>_.
For example: `NODENAME1, NODENAME2` where `NODENAME1` and `NODENAME2` are values for column `NODE_NAME` in the `fnd_nodes` table for the desktop nodes. Set this option at the user level for the user with the Apps Schema Connect role (that is, the `AppsDataSource` user).
Was this article helpful?
YesNo

