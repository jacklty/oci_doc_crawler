Updated 2023-06-02
# Start and Stop App Gateway
You can start and stop App Gateway server and App Gateway agent using scripts, or using the services installed in the server where your App Gateway runs.
## Using a Script to Start and Stop App Gateway 🔗 
start and stop the App Gateway server and agent using scripts provided in the server. Sign in to the App Gateway server and then run the following command:
  1. To start App Gateway server.
```
/scratch/oracle/cloudgate/home/bin/cg-start
```

  2. To start App Gateway agent.
```
/scratch/oracle/cloudgate/home/bin/agent-start
```

  3. To stop App Gateway server.
```
/scratch/oracle/cloudgate/home/bin/cg-stop
```

  4. To stop App Gateway agent.
```
/scratch/oracle/cloudgate/home/bin/agent-stop
```



When you start the App Gateway server, App Gateway contacts IAM to retrieve the port number you configured during the App Gateway registration in the IAM Console. The App Gateway server starts using this port number.
The App Gateway agent is responsible for synchronizing the App Gateway configuration (hosts and applications) from IAM to the App Gateway server.
To check the running status of the App Gateway server, run the following command: `/scratch/oracle/cloudgate/home/bin/cg-status`
## Using the Service to Start and Stop App Gateway 🔗 
You can start and stop the App Gateway server and agent as services running on the server. Sign in to the App Gateway server and then run the following command:
  1. To start App Gateway server.
```
service cloudgate-nginx start
```

  2. To start App Gateway agent.
```
service cloudgate-agent start
```

  3. To stop App Gateway server.
```
service cloudgate-nginx stop
```

  4. To stop App Gateway agent.
```
service cloudgate-agent stop
```



To check the running status of the App Gateway server, run the following command: `/scratch/oracle/cloudgate/home/bin/cg-status`
Was this article helpful?
YesNo

