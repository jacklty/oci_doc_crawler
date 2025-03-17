Updated 2025-01-13
# Upgrading and Patching App Gateway
The App Gateway patch is installed when you run the upgrade script when you're performing a patch upgrade. 
As patches become available they're listed on the Downloads page, which is available from the Settings page for an identity domain.
See the first steps in [Downloading and Extracting the App Gateway Binary File](https://docs.oracle.com/en-us/iaas/Content/Identity/appgateways/download-and-extract-app-gateway-open-virtual-applicance-file.htm#download-and-extract-app-gateway-open-virtual-applicance-file "The app gateway binary file you download from the IAM Console is a compressed \(.zip\) file. This file contains an Open Virtual Appliance \(.ova\) file which you use to install the App Gateway server.").
## App Gateway Installed as VM 🔗 
App Gateway versioning uses the following convention: `<release           version>-<major version>.<minor version>.<build           number>`. For example, App Gateway version `19.3.3-1.0.1`, means release `19.3.3`, major version `1`, minor version `0`, and patch version `1`.
If you have multiple App Gateway instances, then repeat the following procedure for each App Gateway server.
  1. Use an SSH client such as `PuTTY` to sign in to the App Gateway server.
  2. Run `cd /scratch/oracle/cloudgate`, and verify two information in this folder:
     * In the command prompt, run the following command `cat /scratch/oracle/cloudgate/INSTALLED_VERSION` to verify the version of the App Gateway.
The following example shows that the version of the App Gateway is `19.3.3-1.0.0`:```
$ cd /scratch/oracle/cloudgate
$ cat INSTALLED_VERSION**
OVA Base Version: 19.3.3-1.0.0**
OVA Patch Version:**
Cloud Gate Version: 19.3.3-1910012252**
```

     * Run the following command `ls -la` and verify that the `home` folder links to the folder named the App Gateway version:
The following example shows that the `home` folder is linked to the `19.3.3.-1.0.0` folder:```
$ cd /scratch/oracle/cloudgate
$ ls -la
total 16
drwx------. 6 oracle oracle 4096 Oct 2 00:23 19.3.3-1.0.0
lrwxrwxrwx. 1 oracle oracle  38 Oct 2 01:38 **home -> /scratch/oracle/cloudgate/19.3.3-1.0.0**
-rw-------. 1 oracle oracle  89 Oct 2 01:38 INSTALLED_VERSION
drwx------. 3 oracle oracle 4096 Oct 2 01:38 ova
drwxr-x---. 2 oracle oracle 4096 Oct 7 09:45 wallet
```

  3. Run `cd /scratch/oracle/cloudgate/home/bin`, and then `./cg-upgrade` to start the upgrade process.
During the upgrade process, App Gateway contacts IAM to verify if a patch for your App Gateway is available. If so, then the process downloads the patch and applies the patch to your App Gateway server.
  4. After the upgrade process finishes, Run the commands described in step 2 and verify whether their return refers to the App Gateway patch or the upgraded version.
  5. (Optional) Configure App Gateway in SSL mode. If you ran the `cg-upgrade` script, and App Gateway was configured in non SSL mode, then after running the `cg-upgrade` script, complete the following steps. **Note:** If App Gateway was already configured in SSL mode, then don't complete the following steps.
    1. Get the SSL certificates.
    2. Log in to App Gateway and copy the certificates, for example, to `/scratch/certificates/`.
    3. Open the **navigation menu** and select **Identity & Security**. Under **Identity** , select **Domains**.
    4. Click the name of the identity domain that you want to work in. You might need to change the compartment to find the domain that you want. Then, click **Security** and then **App gateways**.
    5. Navigate to **Hosts** , and then open the required host. Navigate to **Additional Properties** and then add the path of the certificates and other information, such as `ssl_protocols` and `ssl_ciphers`.
```
ssl_certificate /scratch/certificates/myappgateway.example.com.cert;
ssl_certificate_key /scratch/certificates/myappgateway.example.com.key;
ssl_protocols TLSv1 TLSv1.1 TLSv1.2; ssl_ciphers HIGH:!aNULL:!MD5;

```

    6. Open `/usr/local/nginx/conf/cloudgate.config`, search for `callbackPrefix` and change its value from `HTTP` to `HTTPS`.
    7. Run the following commands so that you can see all changes reflected in App Gateway:
      1. cg-stop 
      2. cg-start 
      3. agent-stop
      4. agent-start
Now the application can be accessed only through the HTTPS protocol and not the HTTP protocol.

During this procedure, App Gateway restarts. Access to your application through this App Gateway server might be affected.
## App Gateway Installed as Docker Container 🔗 
To upgrade to a new App Gateway version, delete the existing container and re-create the container with a new version of the image. The wallet files are automatically used by the container, provided the files aren't deleted in the local folder, and the same local folder is used for the volume mount.
Was this article helpful?
YesNo

