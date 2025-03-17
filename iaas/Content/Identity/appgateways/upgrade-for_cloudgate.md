Updated 2024-12-18
# Upgrade Path for High Availability Deployments Using App Gateway Docker Image
Upgrade path for deployments using App Gateway Docker Image.
Cloud Gate has updated its Block Cipher mode of operation which changes how data is encrypted. The change is being rolled out over three patch releases, R1, R2, and R3 so that you can upgrade without service interruptions.
**Note** This upgrade path only applies when you have enabled high availability and are using multi node deployments.
If you are using high-availability with multiple App Gateways and using a load balancer, you must follow a specific upgrade path. If you perform the upgrades in the wrong order, or miss an upgrade, then you might have problems, such as:
  * Unexpected redirects to IAM sign-in page, because of Cloud Gate failing to decrypt its session cookie.
  * Failures after sign in, because of Cloud Gate being unable to decrypt its state cookie or the data returned by IAM.
  * Incomplete logouts, because of Cloud Gate being unable to decrypt the data sent by IAM.


## R1 Patch Release
The R1 patch release encrypts using the old Block Cipher mode of operation, but it adds fail over logic to Cloud Gate's decryption operation. If Cloud Gate fails to decrypt using the current Block Cipher mode of operation, it tries again using the new Block Cipher mode of operation. This fail over lets Cloud Gate to maintain backward compatibility with session data created by older Cloud Gate clients, and support decrypting new session data created by Cloud Gate clients running the R2 or R3 patch release of this upgrade path.
## R2 Patch Release
The R2 patch release encrypts and decrypts using the new Block Cipher mode of operation. Decryption supports failing over using the old Block Cipher mode of operation. The R2 patch release isn't backward compatible with Cloud Gate clients from before the R1 patch release. These older Cloud Gate clients can't decrypt the new session data created by R2 release Cloud Gate clients.
## R3 Patch Release
The R3 patch release removes all support for the old Block Cipher mode of operation. An existing deployment must upgrade from the R2 patch release to avoid decryption issues.
## Patch Release Downloads
The table shows how the patch release relates to the Cloud Gate release, and to the App Gateway Docker image. Open a support ticket and ask to have the appropriate patch made available to you. See [Support Requests](https://docs.oracle.com/iaas/Content/GSG/Tasks/contactingsupport.htm).
**Note** Only the patch release downloads for R1 and R2 are currently available. When R3 is available, this page will be updated.
Patch Release | Cloud Gate Release | Cloud Gate Build | App Gateway Docker  
---|---|---|---  
R1 | 22.1.49 | 22.1.49-2201171005 | 22.1.49-2201040708  
R2 | 22.2.63 | 22.2.63-2203141550 | 22.2.57-2202180045  
R3 | To be announced | To be announced | To be announced  
## Configuration Override 🔗 
You can disable the encryption change in Cloud Gate using the configuration setting:`encryptWithGcm`. This is a Boolean setting that's set to `false` to disable the encryption change.
After making the change, restart the NGINX server. For example, in a WTSS deployment, use 
```
/u01/data/idcs-cloudgate/bin/cg-reload.
```

**Example of a cloudgate.config file**
```
{
 "cloudgateConfig" : {
  "version"         : "2.9",
  "comment"         : "Sample Cloud Gate Configuration (HTTPS)",
  "enabled"         : true,
...
  "general" : {
   "encryptWithGcm": false,
...
  },
...
}
```

Was this article helpful?
YesNo

