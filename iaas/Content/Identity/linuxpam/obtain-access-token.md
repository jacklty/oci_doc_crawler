Updated 2023-05-31
# Obtaining an Access Token
Obtain an access token with Identity Domain Administrator or User Administrator privileges. This allows you to create groups and users with POSIX attributes, or add POSIX attributes to existing groups and users.
In the Linux environment, run the following command:
```
curl -k -X POST -u "client-id:client-secret" -d 
"grant_type=client_credentials&scope=urn:opc:idm:__myscopes__" 
"https://identity-cloud-service-instance-url/oauth2/v1/token"
```

where:
  * `client-id` is the client ID of a confidential application with Identity Domain Administrator or User Administrator privileges
  * `client-secret` is the client secret of a confidential application with administrative privileges
  * `identity-cloud-service-instance-url` is your IAM Instance URL


**Note**
The PAM confidential application `client-id` and `client-secret` are used by the PAM client library to create both groups or POSIX groups.
To create a POSIX group, use the following endpoint with an admin access token.```
/ui/v1/groups
```

Was this article helpful?
YesNo

