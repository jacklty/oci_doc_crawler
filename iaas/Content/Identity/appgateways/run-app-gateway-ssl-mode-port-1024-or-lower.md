Updated 2025-01-14
# Run App Gateway in SSL mode on port `1024` or lower
You can configure App Gateway to run in SSL mode on port number `1024` or lower.
**Note** To run your App Gateway server in Secure Sockets Layer (SSL) mode, you need to have a valid certificate. 
## Configuring App Gateways in the IAM Console 🔗 
Update your App Gateway configuration to enable the server to listen on port number 443 and in Secure Sockets Layer (SSL) mode.
  1. Open the **navigation menu** and select **Identity & Security**. Under **Identity** , select **Domains**.
  2. Click the name of the identity domain that you want to work in. You might need to change the compartment to find the domain that you want. Then, click **Security** and then **App gateways**.
  3. Select the name of the App gateway you want.
  4. In **Hosts** select the name of the host you created.
  5. in the Edit Hosts window, update the following parameters as in the example below:
Parameter | Value  
---|---  
**Port** |  `443`  
**SSL Enabled** | Selected.  
**Additional Properties** |  ```
ssl_certificate /scratch/myappgateway.example.com.cert;
ssl_certificate_key /scratch/myappgateway.example.com.key;
ssl_protocols TLSv1 TLSv1.1 TLSv1.2;
ssl_ciphers HIGH:!aNULL:!MD5;
```
  
**Note** Generate a valid certificate to be used as the SSL certificate. The certificate file (`myappgateway.example.com.cert`) and the certificate key file (`myappgateway.example.com.key` ) are referenced as an example.
  6. Select **Save**.


## Configuring the App Gateway Server 🔗 
Enable your App Gateway server to run on port 443 in SSL mode.
**Note** Generate a valid certificate to your App Gateway to run on SSL mode, and copy the certificate file and the certificate key file to your desktop.
  1. Use an SSH client such as `PuTTY` to sign in to the App Gateway server.
  2. Run the following commands to update a privileged user.
```
sed -i "s/touch \$source_log/touch \$source_log \&\& chown \$NGINX_USER:\$NGINX_USER \$source_log/g" /scratch/oracle/cloudgate/ova/bin/jobs/manage-logs.sh 
sudo sed -i "s/ oracle / root /g" /etc/cron.d/cloudgate-jobs 
sudo sed -i "s/sudo -u oracle//g" /etc/init.d/cloudgate-nginx 
sudo sed -i "s/sudo -u oracle//g" /etc/init.d/cloudgate-agent
```

  3. Run the following commands to change permission of the folders.
```
sudo chmod -R 755 /scratch/
sudo chown root:root /scratch/oracle/cloudgate/home/bin/nginx
cd /usr/local/nginx/sbin/
rm nginx
sudo ln -sf /scratch/oracle/cloudgate/home/bin/nginx
```

  4. Copy the certificate file (for example, `myappgateway.example.com.cert`) and the certificate key file (for example, `myappgateway.example.com.key`) from your desktop to the `/scratch/` folder.
  5. Add user `oracle` to the `nginx.conf` file by running the following command.
```
sudo sed -i "/working_directory.*/a user oracle;" /usr/local/nginx/conf/nginx.conf
```

  6. Edit the `/scratch/oracle/cloudgate/ova/bin/setup/cloudgate-env` file. You can use the following command or any other text editor of your choice: `vi           /scratch/oracle/cloudgate/ova/bin/setup/cloudgate-env`
  7. Replace the value of the `CG_CALLBACK_PREFIX` parameter with the following `https://%hostid%`
  8. Save the `/scratch/oracle/cloudgate/ova/bin/setup/cloudgate-env` file.
  9. Run the following `sed` commands to enable running the server with `sudo` command:
```
sed -i s/verify_running_as_user/#verify_running_as_user/g /scratch/oracle/cloudgate/ova/bin/setup/setup-cloudgate
sudo sed -i "/create_wallet || .*/a chmod -R 755 /scratch/oracle/cloudgate/wallet/" /scratch/oracle/cloudgate/ova/bin/setup/setup-cloudgate
```

  10. Confirm the `setup-cloudgate` file is configured with the values of your IAM tenant, and the values of the **Client ID** and **Client Secret** of the App Gateway you registered in the IAM Console.
  11. Run the following command to reconfigure App Gateway according to the parameters registered in the IAM Console (in this case, port number `443` and **SSL Enabled**.
```
sudo -E /scratch/oracle/cloudgate/ova/bin/setup/setup-cloudgate
```


After the `setup-cloudgate` script finishes, the App Gateway server starts automatically. You can access any application protected by your App Gateway using HTTPs, App Gateway domain, and port number `443` (default HTTPs port). For example, `https://myappgateway.example.com/myapp/index`
## Starting and Stopping App Gateway Server Using `sudo` 🔗 
Because you set up your App Gateway server to run on port `443`, you need to start and stop App Gateway server and agent using `sudo` command.
  1. To stop the App Gateway server and agent use the following command:
```
sudo -E /scratch/oracle/cloudgate/home/bin/cg-stop
sudo -E /scratch/oracle/cloudgate/home/bin/agent-stop

```

  2. To start the App Gateway server and agent use the following command:
```
sudo -E /scratch/oracle/cloudgate/home/bin/cg-start
sudo -E /scratch/oracle/cloudgate/home/bin/agent-start

```



Was this article helpful?
YesNo

