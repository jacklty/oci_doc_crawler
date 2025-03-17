Updated 2024-05-31
# Troubleshooting Object Storage Console Connections
Learn troubleshooting solutions for issues you might encounter regarding connecting with the Console.
When the Console displays error messages that begin with "Error retrieving" followed by a resource name, it means that the Console can't connect to the Object Storage APIs to retrieve and display the requested resources. There are many reasons why this can happen. Walk through these steps to determine why the Console can't connect to the APIs.
## Step 1: Try to connect to the Object Storage API endpoint in the region containing the buckets you're trying to access using the Console.
  1. Open a browser.
  2. Go to the API endpoint: `https://objectstorage.<region_identifier>.oraclecloud.com`.
See [https://docs.oracle.com/iaas/api/#/en/objectstorage/latest/](https://docs.oracle.com/iaas/api/#/en/objectstorage/latest/) for the list of API endpoints. If you are able to connect to the API endpoint, a JSON object is returned. For example:
```
{"code":"NotFound","message":"Not Found"}
```

  3. If you **can** connect to the API endpoint, [create a support ticket](https://docs.oracle.com/iaas/Content/GSG/Tasks/contactingsupport.htm). If you **can't** connect to the API endpoint, continue to **Step 2**.


## Step 2: Ensure your VPN isn't blocking Console access to the Object Storage APIs.
  1. Disconnect from any connected VPNs.
  2. Open a browser.
  3. Go to the API endpoint that contains the buckets you are trying to access in the Console: `https://objectstorage.<region_identifier>.oraclecloud.com`. 
See [https://docs.oracle.com/iaas/api/#/en/objectstorage/latest/](https://docs.oracle.com/iaas/api/#/en/objectstorage/latest/) for the list of API endpoints. If you are able to connect to the API endpoint, a JSON object is returned. For example:
```
{"code":"NotFound","message":"Not Found"}
```

  4. If you **can** connect to the API endpoint, contact your security team about your VPN blocking URL access to the Object Storage APIs. If you **cannot** connect to the API endpoint, continue to **Step 3**.


## Step 3: Ensure your Web proxy servers aren't blocking Console access to the Object Storage APIs.
  1. Disable any configured proxies.
  2. Open a browser.
  3. Go to the API endpoint that contains the buckets you are trying to access in the Console: `https://objectstorage.<region_identifier>.oraclecloud.com`. 
See [https://docs.oracle.com/iaas/api/#/en/objectstorage/latest/](https://docs.oracle.com/iaas/api/#/en/objectstorage/latest/) for the list of API endpoints. If you are able to connect to the API endpoint, a JSON object is returned. For example:
```
{"code":"NotFound","message":"Not Found"}
```

  4. If you **can** connect to the API endpoint, contact your security team about your proxies blocking URL access to the Object Storage APIs. If you **cannot** connect to the API endpoint, continue to **Step 4**.


## Step 4: Ensure DNS filtering isn't blocking Console access to the Object Storage APIs.
  1. Open a terminal window.
  2. Run the following command to test DNS resolution to the API region: ```
host objectstorage.<region_identifier>.oraclecloud.com
```

  3. If the hostname resolves successfully, [create a support ticket](https://docs.oracle.com/iaas/Content/GSG/Tasks/contactingsupport.htm). If the hostname does not resolve successfully, contact your security team about your DNS-based security filtering blocking access to the Object Storage APIs. 


Was this article helpful?
YesNo

