Updated 2023-08-15
# Using Preauthenticated Requests
On Compute Cloud@Customer, preauthenticated requests provide a way to let users access a bucket or an object without having their own credentials, as long as the request creator has permissions to access those objects.
For example, you can create a request that lets an operations support user upload backups to a bucket without owning API keys. Or, you can create a request that lets a business partner update shared data in a bucket without owning API keys.
When you create a preauthenticated request, a unique URL is generated. Anyone you provide this URL to can access the Object Storage resources identified in the preauthenticated request, using standard HTTP tools like curl and wget.
**Important**
Assess the business requirement for and the security ramifications of preauthenticated access to a bucket or objects.
A preauthenticated request URL gives anyone who has the URL access to the targets identified in the request. Carefully manage the distribution of the URL.
## Required Permissions 🔗 
**To Create a Preauthenticated Request**
You need the `PAR_MANAGE` permission to the target bucket or object.
You must also have the appropriate permissions for the access type that you are granting. For example:
  * If you are creating a preauthenticated request for uploading objects to a bucket, you need the `OBJECT_CREATE` and `OBJECT_OVERWRITE` permissions.
  * If you are creating a preauthenticated request for read/write access to objects in a bucket, you need the `OBJECT_READ`, `OBJECT_CREATE`, and `OBJECT_OVERWRITE` permissions.


**Important**
If the creator of a preauthenticated request is deleted or loses the required permissions after they created the request, the request will no longer work.
**To Use a Preauthenticated Request**
Permissions of the preauthenticated request creator are checked each time you use a preauthenticated request. 
The preauthenticated request no longer works when any of the following occurs:
  * Permissions of the preauthenticated request creator have changed.
  * The user who created the preauthenticated request is deleted.
  * A Federated user who created the preauthenticated request has lost the user capabilities that they had when they created the request.
  * Preauthenticated request has expired.


## Types of Preauthenticated Requests 🔗 
When creating a preauthenticated request, you have the following options:
  * You can specify the name of a bucket that a preauthenticated request user has write access to and can upload one or more objects to. 
  * You can specify the name of an object that a preauthenticated request user can read from, write to, or read from and write to.


## Scope and Constraints 🔗 
Understand the following scope and constraints regarding preauthenticated requests:
  * Users can't list bucket contents.
  * You can create an unlimited number of preauthenticated requests.
  * There is no time limit to the expiration date that you can set.
  * You can't edit a preauthenticated request. If you want to change user access options in response to changing requirements, you must create a new preauthenticated request.
  * The target and actions for a preauthenticated request are based on the creator's permissions. The request isn't, however, bound to the creator's account login credentials. If the creator's login credentials change, a preauthenticated request isn't affected. 
  * You can't delete a bucket that has a preauthenticated request associated with that bucket or with an object in that bucket.


**Important**
The unique URL provided by the system when you create a preauthenticated request is the only way a user can access the bucket or object specified as the request target. Copy the URL to durable storage. The URL is displayed only at the time of creation and can't be retrieved later. 
Was this article helpful?
YesNo

