Updated 2024-04-02
# Token Exchange Grant Type Two-Legged Authorization Flow Example
Use the following examples to create your Token Exchange grant type requests.
Each of these examples requires a signed request. To learn how to create signature header requests, see [Request Signatures](https://docs.oracle.com/iaas/Content/API/Concepts/signingrequests.htm).
## Request Example: Exchange an API Key for an Identity Domain Access Token
Use the API Key of a User to make a signed request to obtain an access token for the user who owns that API Key.```
  curl -X POST -sS https://<domainURL>/oauth2/v1/token -i 
  -H 'date: Mon, 20 Nov 2023 00:32:02 GMT' 
  -H 'x-content-sha256: 5AfZSV0021K+QUDAdfV7g4wwqBsF2rgVOQWRMIrTa9Q=' 
  -H 'content-type: application/x-www-form-urlencoded;charset=utf-8' 
  -H 'content-length: 185' 
  -H 'Authorization: Signature version="1",keyId="<key-id>",algorithm="rsa-sha256",headers="(request-target) date host x-content-sha256 content-type content-length",signature="<signature>"' 
  -d 'grant_type=urn:ietf:params:oauth:grant-type:token-exchange&scope=http://www.ocisampleservice.com/resume&requested_token_type=urn:ietf:params:oauth:token-type:access_token'

```

## Request Example: Exchange a User Principal for an Identity Domain Access Token
Use a User Principal to make a signed request to obtain an access token for that user.```
  curl -X POST -sS https://<domainURL>/oauth2/v1/token -i 
  -H 'date: Mon, 20 Nov 2023 23:51:18 GMT' 
  -H 'x-content-sha256: n0NyZzoYSrKNC6r6f3mrNxYCtZOuG1zK2TY/r+N676Y=' 
  -H 'content-type: application/x-www-form-urlencoded;charset=utf-8' 
  -H 'content-length: 163' 
  -H 'Authorization: Signature version="1",keyId="<key-id>",algorithm="rsa-sha256",headers="(request-target) date host x-content-sha256 content-type content-length",signature="<signature>"' 
  -d 'grant_type=urn:ietf:params:oauth:grant-type:token-exchange&scope=http://www.ocisampleservice.com/resume&requested_token_type=urn:ietf:params:oauth:token-type:access_token'
```

The following additional scopes can also be used:
  * `offline_access`
  * `urn:opc:resource:consumer:tokengenerator:appid::<appId>`
  * `urn:opc:resource:consumer:<scopeExtension>::<scopeQualifier>`


The following is request example using the `offline_access` scope.```
  curl -X POST -sS https://<domainURL>/oauth2/v1/token -i 
  -H 'date: Mon, 20 Nov 2023 18:58:49 GMT' 
  -H 'x-content-sha256: 7zRa1qI4iIQouzn2TCTisZKi1CSoXRDe1pUJ58IFyVk=' 
  -H 'content-type: application/x-www-form-urlencoded;charset=utf-8' 
  -H 'content-length: 284' 
  -H 'Authorization: Signature version="1",keyId="<key-id>",algorithm="rsa-sha256",headers="(request-target) date host x-content-sha256 content-type content-length",signature="<signature>"' 
  -d 'grant_type=urn:ietf:params:oauth:grant-type:token-exchange&client_id=<client-id>&scope=http://www.docservice.com/report offline_access&isCLI=true&requested_token_type=urn:ietf:params:oauth:token-type:access_token???
```

When this scope is included, both an access token and a refresh token are produced. The refresh token format is listed in the response example below.```
{
  "access_token": "<access-token>",
  "token_type": "Bearer",
  "expires_in": 3600
  "refresh_token": "<refresh token>"
}
```

## Request Example: Exchange an Instance Principal (IPST) for an Identity Domain Access Token
Use an Instance Principal to make a signed request to obtain an access token for that instance.```
  curl -X POST -sS https://<domainURL>/oauth2/v1/token -i 
  -H 'date: Mon, 20 Nov 2023 12:07:10 GMT' 
  -H 'x-content-sha256: t7NyZzoWSrKNC6r6f3mrNxYCtZOuG1zK2TY/r+N676Y=' 
  -H 'content-type: application/x-www-form-urlencoded;charset=utf-8' 
  -H 'content-length: 170' 
  -H 'Authorization: Signature version="1",keyId="<key-id>",algorithm="rsa-sha256",headers="(request-target) date host x-content-sha256 content-type content-length",signature="<signature>"' 
  -d 'grant_type=urn:ietf:params:oauth:grant-type:token-exchange&scope=http://www.ocisampleservice.com/resume&requested_token_type=urn:ietf:params:oauth:token-type:access_token'

```

## Request Example: Exchanging Resource Principal (RPST) for an Identity Domain Access Token
Use a Resource Principal to make a signed request to obtain an access token for that resource.```
  curl -X POST -sS https://<domainURL>/oauth2/v1/token -i 
  -H 'date: Mon, 20 Nov 2023 01:17:33 GMT' 
  -H 'x-content-sha256: t7NyZzoWSrKNC6r6f3mrNxYCtZOuG1zK2TY/r+N676Y=' 
  -H 'content-type: application/x-www-form-urlencoded;charset=utf-8' 
  -H 'content-length: 197' 
  -H 'Authorization: Signature version="1",keyId="<key-id>",algorithm="rsa-sha256",headers="(request-target) date host x-content-sha256 content-type content-length",signature="<signature>"' 
  -d 'grant_type=urn:ietf:params:oauth:grant-type:token-exchange&scope=http://www.ocisampleservice.com/resume&requested_token_type=urn:ietf:params:oauth:token-type:access_token'
```

## Response Example
The following example shows the contents of the response body in JSON format when you use the Token Exchange grant type to obtain an access token for all 2-legged flow requests.```
{
  "access_token": "<access-token>",
  "token_type": "Bearer",
  "expires_in": 3600
}
```

Was this article helpful?
YesNo

