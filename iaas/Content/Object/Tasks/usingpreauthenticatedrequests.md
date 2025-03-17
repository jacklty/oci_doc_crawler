Updated 2025-01-22
# Object Storage Pre-Authenticated Requests 
Learn about how to use the pre-authenticated request feature to give users access a bucket or an object without providing their sign-on credentials.
Pre-authenticated requests provide a way to let users access a bucket or an object without having their own credentials. Users continue to have access to the bucket or object as long as the creator of the request has permissions to access those resources. For example, you can create a request that lets an operations support user upload backups to a bucket without owning API keys. Or, you can create a request that lets a business partner access all your quarterly financial reports in a bucket without owning API keys.
When you create a pre-authenticated request, a unique URL is generated. Anyone you provide this URL to can access the Object Storage resources identified in the pre-authenticated request, using standard HTTP tools such as curl and wget.
**Important**
Assess the business requirement for pre-authenticated access to a bucket or objects. A pre-authenticated request URL gives anyone who has the URL access to the targets identified in the request. Carefully manage the distribution of the URL.
## Pre-Authenticated Request Tasks 🔗 
You can perform the following pre-authenticated request tasks:
  * [List the pre-authenicated requests for a bucket.](https://docs.oracle.com/en-us/iaas/Content/Object/Tasks/usingpreauthenticatedrequests_topic-To_list_preauthenticated_requests.htm#top "View a list of the pre-authenticated requests in a bucket.")
  * [Create a pre-authenticated request.](https://docs.oracle.com/en-us/iaas/Content/Object/Tasks/usingpreauthenticatedrequests_topic-To_create_a_preauthenticated_request_for_all_objects_in_a_bucket.htm#top "Create a pre-authenticated request for all the objects in an Object Storage bucket or for a specific object.")
  * [Access and copy the pre-authenticated request's ID number for future use.](https://docs.oracle.com/en-us/iaas/Content/Object/Tasks/usingpreauthenticatedrequests_topic-To_copy_a_preauthenticated_request_ID.htm#top "Get access to your pre-authenticated request ID.")
  * [Display a list of the pre-authenticated request in a bucket.](https://docs.oracle.com/en-us/iaas/Content/Object/Tasks/usingpreauthenticatedrequests_topic-To_list_preauthenticated_requests.htm#top "View a list of the pre-authenticated requests in a bucket.")
  * [View the details of a pre-authenticated request.](https://docs.oracle.com/en-us/iaas/Content/Object/Tasks/usingpreauthenticatedrequests_topic-To_get_a_preauthenticated_request.htm#top "View the details of a pre-authenticated request in a bucket.")
  * [Remove a pre-authenticated request from a bucket.](https://docs.oracle.com/en-us/iaas/Content/Object/Tasks/usingpreauthenticatedrequests_topic-To_delete_a_preauthenticated_request.htm#top "Delete a pre-authenticated request from a bucket.")


## Required Permissions 🔗 
### Creating a Pre-Authenticated Request
To create or manage pre-authenticated requests, you need `PAR_MANAGE` permission to the target bucket.
While you only need `PAR_MANAGE` permission to create a pre-authenticated request, you must also have the appropriate permissions for the access type that you're granting. For example:
  * If you're creating a pre-authenticated request for uploading objects to a bucket, you need `OBJECT_CREATE` and `OBJECT_OVERWRITE` permissions in addition to `PAR_MANAGE`.
  * If you're creating a pre-authenticated request for read/write access to objects in a bucket, you need `OBJECT_READ`, `OBJECT_CREATE`, and `OBJECT_OVERWRITE` permissions in addition to `PAR_MANAGE`.


**Important** If the creator of a pre-authenticated request is deleted or loses the required permissions after they created the request, the request no longer works.
### Using a Pre-Authenticated Request
Permissions of the pre-authenticated request creator are checked each time you use a pre-authenticated request. The pre-authenticated request no longer works when any of the following occurs:
  * Permissions of the pre-authenticated request creator have changed.
  * User who created the pre-authenticated request is deleted.
  * Federated user who created the pre-authenticated request has lost the user capabilities that they had when they created the request.
  * Pre-authenticated request has expired or has been deleted.


## Options 🔗 
You can create a pre-authenticated request that grants read, write, or read/write access to one of the following:
  * All objects in the bucket.
  * A specific object in the bucket.
  * All objects in the bucket that have a specified prefix.


For requests that apply to several objects, you can also decide whether you want to let users list those objects.
## Scope and Constraints 🔗 
Understand the following scope and constraints regarding pre-authenticated requests:
  * You can create an unlimited number of pre-authenticated requests.
  * The maximum length for a pre-authenticated request, including the object name, is 3500 bytes.
  * A pre-authenticated request created for all objects in a bucket lets request users upload any number of objects to the bucket.
  * Expiration date is required, but has no limits. You can set them as far out in the future as you want.
  * You can't edit a pre-authenticated request. To change user access options or enable object listing in response to changing requirements, you must create a new pre-authenticated request.
  * By default, pre-authenticated requests for a bucket or objects with prefix can't be used to list objects. You can explicitly enable object listing when you create a pre-authenticated request.
  * When you create a pre-authenticated request that limits scope to objects with a specific prefix, request users can only `GET` and `PUT` objects with the prefix name specified in the request. Trying to `GET` or `PUT` an object without the specified prefix or with a different prefix fails.
  * The target and actions for a pre-authenticated request are based on the creator's permissions. The request isn't, however, bound to the creator's account sign-in credentials. If the creator's sign-in credentials change, a pre-authenticated request isn't affected.
  * Deleting a pre-authenticated request revokes user access to the associated bucket or object.
  * Pre-authenticated requests can't be used to delete buckets or objects.
  * You can't delete a bucket that has a pre-authenticated request associated with that bucket or with an object in that bucket.


Was this article helpful?
YesNo

