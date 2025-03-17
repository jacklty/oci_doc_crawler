Updated 2024-10-03
# Working with Customer Secret Keys
Object Storage provides an API to enable interoperability with Amazon S3. 
To use this Amazon S3 Compatibility API, you need to generate the signing key required to authenticate with Amazon S3. This special signing key is an Access Key/Secret Key pair. Oracle provides the Access Key that is associated with your Console user login. You or your administrator generates the Customer Secret key to pair with the Access Key.
**Note** "Customer Secret keys" were previously named "Amazon S3 Compatibility API keys". Any keys you had created are now listed in the Console as Customer Secret keys. You can continue to use the existing keys.
Each user created in the IAM service automatically can create, update, and delete their own Customer Secret keys in the Console or the API. An administrator doesn't need to create a policy to give a user those abilities. Administrators (or anyone with permission to the tenancy) also have the ability to manage Customer Secret keys for other users. 
Any user of the Amazon S3 Compatibility API with Object Storage needs permission to work with the service. If you're not sure if you have permission, contact your administrator. For information about policies, see [IAM Policies Overview](https://docs.oracle.com/en-us/iaas/Content/Identity/policieshow/Policy_Basics.htm#top "IAM policies govern control of resources in Oracle Cloud Infrastructure \(OCI\) tenancies.").
Customer Secret keys don't expire. Each user can have up to two Customer Secret keys at a time. To create keys using the Console, see [Creating a Customer Secret Key](https://docs.oracle.com/en-us/iaas/Content/Identity/access/to_create_a_Customer_Secret_key.htm#create-customer-secret-key "Use the Console to create a customer secret key."). 
Was this article helpful?
YesNo

