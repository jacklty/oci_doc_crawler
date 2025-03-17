Updated 2023-08-28
# Creating Access Policy
A tenancy's administrator group users can manage API keys for any user. To allow other users to create and manage Object Storage API keys for themselves, create a policy using the following statement in the root compartment.
Copy
```
allow any-user to {USER_INSPECT, USER_READ, USER_UPDATE, 
USER_APIKEY_ADD, USER_APIKEY_REMOVE} in tenancy where request.principal.id = target.user.id
```

Was this article helpful?
YesNo

