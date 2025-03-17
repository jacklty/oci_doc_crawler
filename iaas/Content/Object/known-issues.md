Updated 2024-06-28
# Known Issues for Object Storage
These known issues have been identified in Object Storage.
## PAR creation can fail when using long object names 🔗  

Details
    Creating a pre-authenticated request (PAR) can fail when using long object names, resulting in a 500: Internal Server Error error. This failure is because of the size of the metadata associated with longer object names. 

Workaround
    Use shorter object names. The limit depends on implementation-specific details related to the user creating the PAR, so we can't currently give an exact limit. See [Pre-Authenticated Requests](https://docs.oracle.com/en-us/iaas/Content/Object/Tasks/usingpreauthenticatedrequests.htm#pre-auth-req "Learn about how to use the pre-authenticated request feature to give users access a bucket or an object without providing their sign-on credentials.") for more information on that feature.
Was this article helpful?
YesNo

