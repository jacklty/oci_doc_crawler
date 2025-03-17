Updated 2024-02-13
# Using App Gateways: FAQ
This topic provides information about using App Gateways.
[Can I install App Gateway in an OS of my choice?](https://docs.oracle.com/en-us/iaas/Content/Identity/appgateways/faq_using-app-gateways-faq.htm)
App Gateway comes as an appliance, and as a Docker image containing Linux. You can't install App Gateway directly into your OS.
To run the App Gateway appliance you need to install a tool, for example, Oracle virtual box or VMWare(r) VSphere. To run the App Gateway Docker image you need to install Docker.
[I have App Gateway version X installed, will it be de-supported? Can I get bug fix for my older version of the App Gateway?](https://docs.oracle.com/en-us/iaas/Content/Identity/appgateways/faq_using-app-gateways-faq.htm)
App Gateway is backward compatible and will be supported until Oracle communicates otherwise. We recommend that you use the latest version of the App Gateway. We don't back-port fixes to older versions.
[How do I get the latest version of App Gateway?](https://docs.oracle.com/en-us/iaas/Content/Identity/appgateways/faq_using-app-gateways-faq.htm)
You can download the latest version of app gateway from the Console. See [Creating an App Gateway](https://docs.oracle.com/en-us/iaas/Content/Identity/appgateways/register-app-gateway.htm#register-app-gateway "Create an app gateway in IAM, add hosts, and associate each host with enterprise applications, which the app gateway protects.").
[How do I upgrade App Gateway docker image? Do I need to create a new environment with latest appliance, or just replace the files in an existing appliance?](https://docs.oracle.com/en-us/iaas/Content/Identity/appgateways/faq_using-app-gateways-faq.htm)
To upgrade the App Gateway docker image, you must stop the running container and then create the container with the latest image. You can reuse the existing wallet that you have created for the existing app gateway container. If you have changed files in the existing container, for example, `nginx.conf` then you can copy files from the existing container and use it to create new container. 
Using Docker, run pass files using the volume flag. For example:
```
--volume /opt/appgateway/cwallet.sso:/usr/local/nginx/conf/cwallet.sso
```

or
```
--volume /opt/appgateway/nginx.conf:/usr/local/nginx/conf/nginx.conf

```

[How do I upgrade App Gateway Appliance? Do I create a new environment with latest appliance, or replace the files in an existing appliance?](https://docs.oracle.com/en-us/iaas/Content/Identity/appgateways/faq_using-app-gateways-faq.htm)
You need to create a fresh environment with the latest App Gateway appliance. App Gateways are backward compatible so older versions of App Gateway work with the newer OCI IAM version. However, bugs fixes aren't back-ported to older versions. We recommend that always you use the latest version.
[Is cg-upgrade CLI an upgrade tool for App Gateway?](https://docs.oracle.com/en-us/iaas/Content/Identity/appgateways/faq_using-app-gateways-faq.htm)
CLI `/scratch/oracle/cloudgate/home/bin/cg-upgrade` starts the upgrade process for patches. This CLI only looks for available patches, for example, a security fix. It won't upgrade App Gateway to the latest version.
During the upgrade process App Gateway contacts the IAM identity domain to verify whether a patch for your App Gateway is available. If it is, then the process downloads the patch and applies the patch to your App Gateway server.
See [Upgrading and Patching App Gateway](https://docs.oracle.com/en-us/iaas/Content/Identity/appgateways/upgrade-and-patch-app-gateway.htm#upgrade-and-patch-app-gateway "The App Gateway patch is installed when you run the upgrade script when you're performing a patch upgrade.").
[How do I display the headers sent from the App Gateway in my UI? I don't see them in the response header](https://docs.oracle.com/en-us/iaas/Content/Identity/appgateways/faq_using-app-gateways-faq.htm)
App Gateway sends headers in the request to the upstream app. The app reads the headers from the request and serves them back to the UI.
[Can I install other packages on the App Gateway VM?](https://docs.oracle.com/en-us/iaas/Content/Identity/appgateways/faq_using-app-gateways-faq.htm)
We don't recommend that you install any additional components within our certified Oracle VM Virtual Appliances (OVA). This is to ensure the stability of the offering and to ensure that the upgrades are safe. Oracle support cannot address issues arising from third-party components loaded to OVA.
[While creating an enterprise application, what is the value I need to define in the application URL?](https://docs.oracle.com/en-us/iaas/Content/Identity/appgateways/faq_using-app-gateways-faq.htm)
Enter the App gateway URL, or the URL of the load balancer front ending the App Gateway.
[Where do I define the application URL protected by App Gateway?](https://docs.oracle.com/en-us/iaas/Content/Identity/appgateways/faq_using-app-gateways-faq.htm)
It is the origin server configuration of the App Gateway when you add the enterprise application to the App Gateway.
[Which URL do I use in the load balancer to check if App Gateway is up and running?](https://docs.oracle.com/en-us/iaas/Content/Identity/appgateways/faq_using-app-gateways-faq.htm)
To check whether App Gateway is up and running, use:
```
/cloudgate/v1/about
```

When the App Gateway is up, the output is `RUNNING`.
[Can I use one App Gateway to protect multiple enterprise applications?](https://docs.oracle.com/en-us/iaas/Content/Identity/appgateways/faq_using-app-gateways-faq.htm)
Yes, you can assign multiple enterprise applications to the same App Gateway server. Register the applications with App Gateway using a different Resource Prefix for each application.
[I have a load balance in front of the App Gateway and want to terminate SSL at the load balancer. What header should pass from the load balancer to the App Gateway nodes?](https://docs.oracle.com/en-us/iaas/Content/Identity/appgateways/faq_using-app-gateways-faq.htm)
The load balancer must pass the header _is_ssl_ with a value _ssl_.
[Does the App Gateway need to be hosted on the server with the Web/Application server to work? ](https://docs.oracle.com/en-us/iaas/Content/Identity/appgateways/faq_using-app-gateways-faq.htm)
App Gateway can be hosted on a different server. You must have connectivity between the AppGateway server and web application server.
[How often are patches, updates, or new versions for App Gateway released?](https://docs.oracle.com/en-us/iaas/Content/Identity/appgateways/faq_using-app-gateways-faq.htm)
App Gateway patches are typically released only for security fixes. Release cycles for newer versions is ad-hoc and customers are notified in the release notes or What's New section of the OCI documentation.
[App gateway is not able to reach the identity domain.](https://docs.oracle.com/en-us/iaas/Content/Identity/appgateways/faq_using-app-gateways-faq.htm)
App Gateway connects to IAM on SSL port 443. Ensure that the machine where App Gateway is running can communicate to external services on this SSL port. For example, if App Gateway is running in OCI Compute, you might have to enable ports in the security list and at OS level.
[Does App Gateway support proxy configuration?](https://docs.oracle.com/en-us/iaas/Content/Identity/appgateways/faq_using-app-gateways-faq.htm)
No, it doesn't. If the connectivity to the internet is through a proxy, App Gateway can't work. App Gateway needs to access the internet to reach OCI IAM on cloud to access identity information. A direct connection from App Gateway to the internet is required.
Was this article helpful?
YesNo

