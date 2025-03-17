Updated 2025-02-19
# How-to: Resolving 502 Errors for Instance Web Applications
An HTTP 502 error is a generic error indicating an issue with a server. Use the following steps to help resolve HTTP 502 application errors on a Compute instance.
## Verify that the Instance is Running
To verify the instance is running:
  * In OCI console main menu go to **Compute** then **Instances**.
  * Select the instance and verify that the instance is in a `running` state.
  * If status is `stopped`, start the instance.


## Verify Application is Running
Next, verify the application is running on the instance.
  * Use `ssh` to connect to the instance.
  * Check the application listening port. ```
netstat -tulnp | grep LISTEN | grep <PORT>
```

Substitute <PORT> with the application's port number.
  * If the command returns no matches, this indicates the application isn't running. Start the application.


## Verify Connectivity on the Same Network
Use a VM on the same network to test connectivity.
  * Use `ssh` to connect to an instance on the same network. 
**Note** In this example, the IP address of the machine to test is 10.0.0.5.
  * Use `curl` to test the target VM. For example: ```
curl -Ik https://10.0.0.5:8443
```

If no response is returned, this could indicate a firewall configuration issue on the instance.


## Check Load Balancer Configuration
If you're using a Load Balancer, ensure the backend sets are in a healthy state and attached. 

Option 1
    
From the main menu go to **Networking** under **Load Balancers** select **Load Balancer**.
  * Select the load balancer to review.
  * On the **Load Balancer Details** page, check **Backend set health** status.



Option 2
    
From the main menu go to **Networking** under **Load Balancers** select **Load Balancer**.
  * Select the load balancer to review.
  * On the **Load Balancer Details** page, under resources, select **Backend Sets**.
  * Select the backend set to review.
  * Check **Backend health** status.


For more information, see [Troubleshooting Load Balancer](https://docs.oracle.com/iaas/Content/Balance/Reference/troubleshooting_load_balancer.htm).
Was this article helpful?
YesNo

