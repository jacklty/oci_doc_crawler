Updated 2023-01-20
# App Gateway
Learn how to troubleshoot common App Gateway issues.
## My Response Error Message Contains: 400 Bad Request: invalid header value 🔗 
Learn the common cause when a response error message contains: `400 Bad Request: invalid header value`.
App Gateway adds headers to the requests that are proxied to an upstream Application Server. One of these headers, `idcs_user_display_name`, might have invalid characters as defined by the newer RFC - depending on the values set for the **First Name** and **Last Name** of the identity domain user. This new RFC limits the allowed characters to printable US-ASCII characters (that is, 0x21 - 0x7E and the space and horizontal tab characters). See [RFC 7230 HTTP/1.1 Message Syntax and Routing](https://www.rfc-editor.org/rfc/rfc7230#page-22).
Application Servers that enforce the newer RFC will reject the request with the response: 400 Bad Request: invalid header value. Note: The exact response depends on the Application Server being used.
Remove any nonprintable characters.
## App Gateway Server Doesn't Reflect Changes 🔗 
When you can't see the changes you've made in IAM in the App Gateway server, try the following.
Changes you make to enterprise applications and App Gateway definitions in Identity Domains might not be reflected immediately on App Gateway because App Gateway caches Identity Domains information, such as resources, authentication policies, and header values of enterprise applications.
App Gateway contacts IAM using agents to collect host and port information. When you start App Gateway, its NGINX server is automatically configured with this information. Any changes to IAM are periodically polled by the agents.
By default the policy and headers refresh time are 3,600 seconds (1 hour) each. To change these values, sign in to the App Gateway server, and edit the `/usr/local/nginx/conf/cloudgate.config` file. Change the `ttl` value for `policy` and `headers` in the `caching` section as per the following example, and then restart both App Gateway server and the agent.```
"caching" : {
 "minimumTtl"      : 300,
 **"headers"        : { "ttl": 3600 }**,
 "discovery"       : { "ttl": 3600 },
 **"policy"        : { "ttl": 3600}**,
 "tenantKeys"      : { "ttl": 86400 }
}
```

You can also change the poll interval of the agents. By default, the agent's refresh time to get new App Gateway configuration from IAM is 60 seconds, which is the minimum amount of time supported. In the `/usr/local/nginx/conf/cloudgate.config` file, change the `pollIntervalSecs` value in the `agentConfig` section as in the example:```
"agentConfig": {
  **"pollIntervalSecs"  : 60**,
  "daemon"     : true,
  "logLevel"    : "warn",
  "logFolder"    : "" 
}
```

If you want the changes in the Enterprise Application configuration to be reflected immediately, stop the App Gateway server and then start the server.```
/scratch/oracle/cloudgate/home/bin/cg-stop
/scratch/oracle/cloudgate/home/bin/cg-start
```

If you want the changes in the App Gateway configuration to be reflected immediately, stop the agent and then start the agent.```
/scratch/oracle/cloudgate/home/bin/agent-stop
/scratch/oracle/cloudgate/home/bin/agent-start
```

## Invalid_session Message 🔗 
When App Gateway can't communicate correctly with IAM, you find `invalid_session` messages in the App Gateway error log files.
The following is an example of a message`invalid_session` in `error.log` file:
```
www-authenticate: Bearer error="invalid_session", error_description="Authentication Failure
```

This can be because of the way App Gateway processes a client request to a protected resource. App Gateway uses `NGINX` sub requests to make requests to IAM, and then App Gateway requires Linux `NGINX` resolver to be configured appropriately to allow these sub requests to function correctly.
  1. Verify that the resolver setting in the file `/usr/local/nginx/conf/nginx-cg-sub.conf` is set to the correct IP.
  2. Verify that the tenant name in `/usr/local/nginx/conf/cloudgate.config` file is configured correctly.


## GET 127.0.0.1:53 Command Error 🔗 
The error log files contain GET 127.0.0.1:53 command responding to error number 500.
Because App Gateway makes sub requests to an internal servlet, App Gateway requires your virtual machine to listen to port `53`.
The App Gateway server must communicate to itself through IP address `127.0.0.1` and port `53`.
If you're running App Gateway in a virtual machine software, configure port forward for this port from the host to the guest. See [Configuring Port Forwarding Rules](https://docs.oracle.com/en-us/iaas/Content/Identity/appgateways/install-app-gateway-oracle-vm-virtual-box-software.htm#configure-port-forwarding-rules).
## App Gateway Server Can't Communicate With IAM 🔗 
When your A[[ Gateway server can't communicate with IAM, follow these steps to use an SSH client such as `PuTTY` and the following credentials to sign in to the App Gateway server.
  1. Run the `sudo su -` command to sign in as `root`, and when prompted provide the oracle password.
  2. Install telnet by running the following command:```
yum install telnet
```

  3. Run the following telnet command and try to establish a connection to your IAM instance and your application from the App Gateway server.```
telnet <idcs-tenant>.identity.oraclecloud.com 443
```

If telnet can't connect to your IAM, then contact your network administrator to apply any other network configuration to enable the App Gateway server to establish connection with your IAM instance.
  4. Run the `exit` command, to log out from root account.


Was this article helpful?
YesNo

