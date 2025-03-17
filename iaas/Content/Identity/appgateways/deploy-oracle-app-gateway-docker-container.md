Updated 2025-01-14
# Deploy the Oracle App Gateway Docker Container
App Gateway can be deployed by using OVA or using Docker. Learn how to deploy the Oracle App Gateway Docker container.
## Prerequisites 🔗 
  * Download the App Gateway docker image. Open the **navigation menu** and select **Identity & Security**. Under **Identity** , select **Domains**. Click the name of the identity domain that you want to work in. You might need to change the compartment to find the domain that you want. Then, click **Settings** and then **Downloads**.
  * Create a wallet file containing the Client ID and Client Secret of the App Gateway that was created in the Admin Console. Name the wallet file **cwallet.sso** and copy it to the local folder so that the container can uptake the file. **Note:** The wallet tool can be downloaded from the IAM Console. In the IAM Console, expand the **Navigation Drawer** , select **Settings** , and then select **Downloads**.
  * Install Docker (Command: `$ yum install                      docker-engine`).
  * Add the current user to the Docker group (Command: `$ sudo                      usermod -a -G docker $USER`).


## Extract the Docker Image 🔗 
If the Docker image is in `.tar.gz` format, then you must use the following commands to extract the image before you can create the container. 
  1. Load the `.tar.gz` file to the local Docker registry. Command: `$ docker load -i <.tar.gz file>`
  2. Verify that you see the image in the local Docker registry. Command: `$ docker images`


## Create the App Gateway Container 🔗 
**Set the App Gateway Environment Variables**
To run the App Gateway Docker container, the following environment variables must be set in the `appgateway-env` file. **Important:** No validation is performed on these values. If you configure invalid values, App Gateway Docker container creation fails. 
  * `CG_APP_TENANT=<tenant name>`
  * `IDCS_INSTANCE_URL=<idcs instance url>`. The URL required to access the IAM instance.
  * `NGINX_DNS_RESOLVER=<resolver ip>`. Configure the nameserver found in the file `/etc/resolv.conf`. The default value is `127.0.0.1`.


**Run Docker**
Use the following command to run Docker.
**Note**
The local folder is mounted as volume and is accessible within the Docker container.
The wallet file (which contains the Client ID and Client Secret) you created as a prerequisite (`cwallet.sso`) must be copied to the local folder, so that the container can reference the file.
```
$ docker run -it -d 
--name <container name> 
--env-file <path to env file> 
--env HOST_MACHINE=`hostname -f` 
--volume <local folder>/cwallet.sso:/usr/local/nginx/conf/cwallet.sso
--net=host/<User-defined bridge name> <image name>
```

_**Example Container with Host Networking with No Port Mapping** _
The following is an example of Host Networking with no port mapping. This is only for port numbers greater than 1024.
**Note** If the port number configured for the App Gateway host is less than 1024, then you must use Bridge Networking for the Docker, along with the port mapping. See the _Bridge Networking with Port Mapping_ command example below to run the Docker container.
```
$ docker run -it -d 
--name appgateway 
--env-file appgateway-env 
--env HOST_MACHINE=`hostname -f` 
--volume /opt/appgateway/cwallet.sso:/usr/local/nginx/conf/cwallet.sso 
--net=host opc-delivery.docker.acme.com/idcs/appgateway:RELEASE-BUILDNUMBER
```

_**Example Bridge Networking with Port Mapping** _
The following is an example of Bridge Networking with port mapping (ports 80 to 65535).
**Prerequisite:** Before you use the Bridge Network configuration, add/update `iptables` to `true`, in the file `/etc/docker/daemon.json`. This allows the Docker daemon to edit the iptables filter rules required for port mapping.
```
$ docker run -it -p 80:9000 -d 
--name appgateway 
--env-file /home/<username>/dev/appgateway_pool/appgateway_env --env HOST_MACHINE=`hostname -f`
--volume /opt/appgateway/cwallet.sso:/usr/local/nginx/conf/cwallet.sso  
--net=bridge-net idcs.docker.acme.com/idcs/appgateway: RELEASE-BUILDNUMBER
```

**Note:** Docker internally updates the iptables/firewalld with the routes for the port, when the above command is run.
## Extra Container Steps 🔗 
If the host is configured as HTTPS, the following extra steps are required to copy the certificates to the container.
  1. Configured SSL certificates must be copied to the location that is specified in **Additional Properties**. Go to **Security** , **App Gateways** , **< Gateway>**, **Hosts** , **Additional Properties** and note the location. 
  2. Run commands like the following. **Note:** The location of the certificate depends on the location you specified in the App Gateways Host.```
$ docker cp deploy/docker/nginx/build/test-config/certs/my-appgateway.cert appgateway:/scratch/docker/cloudgate/certs/my-appgateway.cert
```
```
$ docker cp deploy/docker/nginx/build/test-config/certs/my-appgateway.key appgateway:/scratch/docker/cloudgate/certs/my-appgateway.key
```



## Find Out More
  * **How do I know if my container was created successfully?**
Run the command: `$ docker ps -a` and ensure that the `STATUS` is **Up** in the list corresponding to your container name.
  * **If the container STATUS shows exited, how do I check the logs to determine why the container was terminated?**
Run the command: `$ docker logs <container name>`. This command prints the log messages, which contain the log messages printed by App Gateway.
  * **How to do edit the cloudgate.config file inside the container?**
Run the command: `$ docker exec -it <container                         name> bash`.
Run this command to access the container if the container is running with a Bash shell. Once inside the container, you can edit the files using Nano editor.
  * **Can we print the access logs in JSON format?**
Yes, you can print the access logs in JSON format. Add the lines below to the file `/usr/local/nginx/conf/nginx.conf`, inside an HTTP block and then restart App Gateway. ```
log_format jsonf escape=json '{"remote_addr": "$remote_addr", "remote_user":
   "$remote_user", "time": [$time_local], "request": "$request", "status": $status,
   "body_bytes_sent": $body_bytes_sent, "http_referer": "$http_referer", "user_agent":
   "$http_user_agent", "x_forwarded_for": "$http_x_forwarded_for"}'; access_log          
   /usr/local/nginx/logs/access.log jsonf;
```

**Note:** You can edit the JSON fields that you're interested in by removing or adding the NGINX variable. 


Was this article helpful?
YesNo

