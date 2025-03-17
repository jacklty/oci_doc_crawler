Updated 2023-08-22
# Enable and Access App Gateway Logs
App Gateway provides log files to help you monitor App Gateway's behavior. Learn how to configure and access these log files.
## Configure App Gateway Logs 🔗 
Logs are enabled by default. To disable logs or change the log levels of the App Gateway server, sign in to the server, edit the `/usr/local/nginx/conf/cloudgate.config` file, and then under the `general` section, change the value of the `logLevel` attribute, and then save the file.
The following are default values for App Gateway:```
"general":{
   "disableAuthorize":false,
   "logLevel":"warn",
   "logFolder":"",
   "policyMode":"gateway",
   "policyRefreshTime":300,
   "policyStaleTime":3600,
   "policyExpiryTime":604800
  }
```

**Note** Values for the `logLevel` attribute are: `off | crit | security | config | fail | warn | info | trace1 | trace2      | trace3`.
By Default, the log files are in the `/usr/local/nginx/logs` folder. If you want to change the default log folder, then update the value of the `logFolder` attribute under the `general` section of the `/usr/local/nginx/conf/cloudgate.config` file.
To change the log level for the agent service of the App Gateway, modify the `/usr/local/nginx/conf/cloudgate.config` file, and set the `logLevel` and `logFolder` attributes under the `agentConfig` section as follows:
For example, to change the log level to `trace3` and the log folder to `/tmp`, update the `/usr/local/nginx/conf/cloudgate.config` file with the following values, and then save the file.```
"agentConfig":{
  "pollIntervalSecs":60,
  "daemon":true,
  "logFolder":"/tmp",
  "logLevel":"trace3"
 }
```

The log level and log folder changes take effect next time you start App Gateway.
## View App Gateway Logs 🔗 
App Gateway is based on a `NGINX` Server. The following `NGIX` native log files are in the `/usr/local/nginx/logs/` directory:
NGINX Native Log Files Log File | Description  
---|---  
` **access.log** ` | `NGINX` Native access log contains information about all HTTP requests received by `NGINX`, and by App Gateway.  
` **error.log** ` | `NGINX` Native debug log.  
` **nginx.pid** ` | Contains the `NGINX` Server process ID number.  
The following App Gateway specific log files are in the `/usr/local/nginx/logs/` directory:
App Gateway Log Files Log File | Description  
---|---  
` **cg-trace-main.log** ` | App Gateway main log file.  
` **cg-trace-policy.log** ` | Logs information about a policy refresh, when App Gateway contacts IAM.  
` **cg-trace-session.log** ` | Logs information about the sessions created and handled by App Gateway.  
` **cg-trace-token.log** ` | Logs information about the access tokens received by App Gateway.  
` **cg-trace-agent.log** ` | Agent logging file.  
` **cg-trace-init.log** ` | Contains information about the initialization process.  
Was this article helpful?
YesNo

