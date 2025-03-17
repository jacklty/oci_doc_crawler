Updated 2023-06-02
# Securing the Custom SCIM Gateway
Secure the custom SCIM gateway in an OCI IAM identity domain.
Because you don't want unauthorized users or clients to access your custom SCIM gateway, you must secure it. To secure it, use an authorization token to protect the HTTP(S) endpoints of your gateway. This token validates the user or client to allow them to make appropriate HTTP calls to the gateway endpoints. If the token isn't present or is invalid, then the endpoints return a `401 HTTP` response code because IAM isn't authorized to access the endpoints.
IAM uses the administrator's user name and password, which are configured when you register your custom application, to request an access token from the custom SCIM gateway. IAM can then use this token to access the gateway endpoints as an authorization bearer header.
Was this article helpful?
YesNo

