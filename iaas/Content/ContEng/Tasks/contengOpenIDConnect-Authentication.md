Updated 2025-02-26
# Authenticating Cluster Users using an External OpenID Connect (OIDC) Identity Provider
_Find out about using external OpenID Connect (OIDC) identity providers to authenticate users of clusters you create with Kubernetes Engine (OKE)._
By default, clusters you create with Kubernetes Engine use Oracle Cloud Infrastructure Identity and Access Management (OCI IAM) to authenticate users. OCI IAM and the Kubernetes RBAC Authorizer work together to enable users who have been successfully authorized by at least one of them to complete the requested Kubernetes operation. See [About Access Control and Kubernetes Engine (OKE)](https://docs.oracle.com/en-us/iaas/Content/ContEng/Concepts/contengaboutaccesscontrol.htm#About_Access_Control_and_Container_Engine_for_Kubernetes "Find out about the permissions required to access clusters you've created using Kubernetes Engine \(OKE\).").
In addition to OCI IAM, you can specify that clusters you create with Kubernetes Engine use an external OpenID Connect (OIDC) identity provider (IdP) to authenticate users. You can specify a different OIDC identity provider for different clusters. Using an external OIDC identity provider (such as Keycloak) for user authentication enables you to leverage existing identity providers that your organization already maintains, rather than creating new user accounts in OCI IAM. And because users are not defined in OCI IAM, they can only access the cluster and do not have access to other OCI resources.
Having enabled a cluster for OIDC authentication, the cluster uses an OIDC authenticator plugin to authenticate users with a designated OIDC identity provider. In summary, the authentication flow is as follows:
  1. User logs in to the OIDC identity provider to obtain an id_token.
  2. User issues a kubectl command to the cluster, passing the id_token as an argument.
  3. The Kubernetes API server running on the cluster validates the id_token using information from the OIDC identity provider.
  4. The Kubernetes API server performs Kubernetes RBAC authorization.
  5. If the user is authorized, the Kubernetes API server performs the requested operation, and kubectl returns a response to the user.


For a complete description of the OIDC authentication flow in Kubernetes, see [OpenID Connect Tokens](https://kubernetes.io/docs/reference/access-authn-authz/authentication/#openid-connect-tokens) in the Kubernetes documentation.
If you enable a cluster for OIDC authentication, you can also use the Kubernetes RBAC Authorizer to enforce additional fine-grained access control for users on specific clusters . You can set up Kubernetes RBAC roles and clusterroles in the same way that you would if you were using OCI IAM authentication, as described in [About Access Control and Kubernetes Engine (OKE)](https://docs.oracle.com/en-us/iaas/Content/ContEng/Concepts/contengaboutaccesscontrol.htm#About_Access_Control_and_Container_Engine_for_Kubernetes "Find out about the permissions required to access clusters you've created using Kubernetes Engine \(OKE\)."). However, when defining a Kubernetes RBAC rolebinding or clusterrolebinding to map a role or clusterrole to a user or group, instead of specifying an OCID defined in OCI IAM, you specify the name of the user or group defined in the external OIDC identity provider. 
Note the following:
  * You can specify an OIDC identity provider for clusters with virtual nodes, managed nodes, and self-managed nodes.
  * OCI IAM authentication is always enabled, even when OIDC authentication is enabled. So OCI IAM users and OIDC users can both be authenticated by the same cluster, and perform operations on that cluster for which they are authorized.
  * Kubernetes Engine does not implement an OIDC client. It is your responsibility to set up and maintain user authentication details in the external OIDC identity provider, and to obtain an id_token from the identity provider. 
  * Use the kubernetes-apiserver log to troubleshoot issues with initiating the OIDC authenticator plugin, and issues with token validation. For more information, see [Viewing Kubernetes Engine (OKE) Service Logs](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengviewingservicelogs.htm#contengviewingservicelogs "Find out how to view the logs of Kubernetes processes \(such as kube-scheduler, kube-controller-manager, cloud-controller-manager, and kube-apiserver\) running on the control plane of clusters you've created using Kubernetes Engine \(OKE\).").


## Prerequisites for OIDC authentication
Note the following prerequisites for enabling a cluster for OIDC authentication:
  * The cluster must be an enhanced cluster. OIDC authentication is not supported for basic clusters.
  * The cluster must be a new cluster, or a "VCN-native cluster". That is, a cluster that has its Kubernetes API endpoint integrated into your own VCN (see [Migrating to VCN-Native Clusters](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengmigratingclusters.htm#migrating_clusters_to_native_vcns "Find out how to migrate a cluster to integrate its Kubernetes API endpoint into your own VCN, using Kubernetes Engine \(OKE\).")). OIDC authentication is not supported for clusters with Kubernetes API endpoints that are not integrated into your own VCN.
  * The cluster must be running Kubernetes version 1.21 (or later).


Note the following prerequisites for accessing an OIDC-enabled cluster:
  * User authentication details must exist in the external OIDC identity provider.
  * An egress rule must exist for the cluster's Kubernetes API endpoint subnet that allows traffic to the IP address and port number of the external OIDC identity provider:
State: | Destination | Protocol / Dest. Port | Description:  
---|---|---|---  
Stateful | Identity provider's IP address | Identity provider-dependent |  Allow traffic to external OIDC identity provider.  


## Enabling a Cluster for OIDC Authentication 🔗 
To enable a cluster you create with Kubernetes Engine to authenticate users with an OIDC identity provider, you must set the cluster's **OIDC issuer URL** and **OIDC client ID** properties at a minimum. 
In addition, you can optionally set other properties to control OIDC authentication. For a full list of properties, see [Configuring the API Server](https://kubernetes.io/docs/reference/access-authn-authz/authentication/#configuring-the-api-server) in the Kubernetes documentation.
### Using the CLI to Specify an External OpenID Connect (OIDC) Identity Provider 🔗 
For information about using the CLI, see [Command Line Interface (CLI)](https://docs.oracle.com/iaas/Content/API/Concepts/cliconcepts.htm). For a complete list of flags and options available for CLI commands, see the [Command Line Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/). 
#### Creating A Cluster and Specifying a Single External OpenID Connect (OIDC) Identity Provider
To use the CLI to create an enhanced cluster that uses a single external OpenID Connect (OIDC) identity provider, use the `oci ce cluster create` command and include at least the following parameters required for OIDC configuration:
  * `--open-id-connect-auth-enabled` set to `true`
  * `--oidc-issuer-url` set to the base public URL of the identity provider that allows the Kubernetes API server to discover public signing keys. This is typically the identity provider's OIDC discovery URL, changed to have an empty path. For example, if the issuer's OIDC discovery URL is `https://accounts.provider.example/.well-known/openid-configuration`, specify `https://accounts.provider.example`
  * `--oidc-client-id` set to a client ID for which all tokens must be issued. For example, `kubernetes`


For example: 
Copy
```
oci ce cluster create \
--compartment-id ocid1.compartment.oc1..aaaaaaaa______n5q \
--name sales \
--vcn-id ocid1.vcn.oc1.phx.aaaaaaaa______lhq \
--type ENHANCED_CLUSTER \
--kubernetes-version v1.25.4 \
--service-lb-subnet-ids "[\"ocid1.subnet.oc1.phx.aaaaaaaa______g7q"]" \
--endpoint-subnet-id ocid1.subnet.oc1.phx.aaaaaaaa______sna \
--endpoint-public-ip-enabled true \
--endpoint-nsg-ids "[\"ocid1.networksecuritygroup.oc1.phx.aaaaaaaa______5qq\"]" \
--cluster-pod-network-options '[{"cniType":"OCI_VCN_IP_NATIVE"}]' \
--open-id-connect-auth-enabled true
--oidc-issuer-url https://accounts.provider.example
--oidc-client-id kubernetes
```

In addition to the cluster's **OIDC issuer URL** and **OIDC client ID** properties, you can optionally set other properties to control OIDC authentication. For a full list of properties, see [Configuring the API Server](https://kubernetes.io/docs/reference/access-authn-authz/authentication/#configuring-the-api-server) in the Kubernetes documentation.
#### Updating A Cluster and Specifying a Single External OpenID Connect (OIDC) Identity Provider
To use the CLI to update an existing enhanced cluster to use a single external OpenID Connect (OIDC) identity provider:
  1. Using your preferred JSON editor, create a new file in JSON format to update the cluster's external OIDC identity provider configuration, and include at least the following parameters required for the configuration:
Copy
```
{
"options": {
  "openIdConnectTokenAuthenticationConfig": {
   "isOpenIdConnectAuthEnabled": true,
   "issuerUrl": "<idp-base-url>",
   "clientId": "<client-id>"
   ]
  }
  }
}
```

where:
     * `isOpenIdConnectAuthEnabled` is set to `true`
     * `"issuerUrl": "<idp-base-url>"` is the base public URL of the identity provider that allows the Kubernetes API server to discover public signing keys. This is typically the identity provider's OIDC discovery URL, changed to have an empty path. For example, if the issuer's OIDC discovery URL is `https://accounts.provider.example/.well-known/openid-configuration`, specify `https://accounts.provider.example`
     * `"clientId": "<client-id>"` is the client ID for which all tokens must be issued. For example, `kubernetes`
For example:
Copy
```
{
"options": {
  "openIdConnectTokenAuthenticationConfig": {
   "isOpenIdConnectAuthEnabled": true,
   "issuerUrl": "https://accounts.provider.example",
   "clientId": "kubernetes"
   ]
  }
  }
}
```

In addition to the cluster's **OIDC issuer URL** and **OIDC client ID** properties, you can optionally set other properties to control OIDC authentication. For example:```
{
"options": {
  "openIdConnectTokenAuthenticationConfig": {
   "clientId": "kubernetes",
   "usernameClaim": "sub",
   "issuerUrl": "https://token.actions.githubusercontent.com",
   "isOpenIdConnectAuthEnabled": true,
   "usernamePrefix": "actions-oidc:",
   "requiredClaim": [
    "repository=GH_ACCOUNT/REPO", 
    "ref=refs/heads/main"
   ]
  }
  }
}
```

For a full list of properties, see [Configuring the API Server](https://kubernetes.io/docs/reference/access-authn-authz/authentication/#configuring-the-api-server) in the Kubernetes documentation.
  2. Save the JSON file containing the external OpenID Connect (OIDC) identity provider configuration, with a name and in a location of your choice. For example, as `/users/jdoe/update-oidc-config`
  3. Use the `oci ce cluster update` command to update the existing cluster:```
oci ce cluster update --cluster-id <cluster-ocid> --from-json file://<path-to-file>
```

For example:
```
oci ce cluster update --cluster-id ocid1.cluster.oc1.iad.aaaaaaaaaf______jrd --from-json file:///users/jdoe/update-oidc-config
```



#### Creating A Cluster and Specifying Multiple External OpenID Connect (OIDC) Identity Providers
To use the CLI to create an enhanced cluster that uses multiple external OpenID Connect (OIDC) identity providers (available for clusters running Kubernetes version 1.30 and later):
  1. Create a new Kubernetes authentication configuration file as .yaml file, to contain details of the identity providers. For more information about authentication configuration files, see [Authentication configuration from a file](https://kubernetes.io/docs/reference/access-authn-authz/authentication/#using-authentication-configuration) in the Kubernetes documentation.
  2. For each identity provider:
    1. Set the `jwt.issuer.url` field to the base public URL of the identity provider that allows the Kubernetes API server to discover public signing keys. This is typically the identity provider's OIDC discovery URL, changed to have an empty path. For example, if the issuer's OIDC discovery URL is `https://accounts.provider.example/.well-known/openid-configuration`, specify `https://accounts.provider.example`
    2. Optionally set other fields to control OIDC authentication. Note that when using an authentication configuration file, any OIDC configuration must be specified in this file. For more information about the fields in an authentication configuration file, see [Authentication configuration from a file](https://kubernetes.io/docs/reference/access-authn-authz/authentication/#using-authentication-configuration) in the Kubernetes documentation.
For example:
```
apiVersion: apiserver.config.k8s.io/v1beta1
kind: AuthenticationConfiguration
jwt:
 - issuer:
   url: https://accounts.google.com
   audiences:
    - 838763820337-6vt12pbavkteafx08f32z48u7gpll6on.apps.googleusercontent.com
    - 838763820337-elyce7g28ep5b7uzq4dt1uzh1h86jki9.apps.googleusercontent.com
   audienceMatchPolicy: MatchAny
  claimMappings:
   username:
    claim: "sub"
    prefix: ""
   groups:
    claim: "groups"
    prefix: ""
   uid:
    claim: "sub"
 - issuer:
   url: https://dev-dx7mdewuu7xhb4mw.us.auth0.com/
   audiences:
    - 7w7qJsa3brl5OHV6uljAAYhfknVTsVAw
   audienceMatchPolicy: MatchAny
  claimMappings:
   username:
    claim: "sub"
    prefix: ""
   groups:
    claim: "groups"
    prefix: ""
   uid:
    claim: "sub"
```

  3. Convert the authentication configuration .yaml file to a Base64 encoded string.
  4. Use the `oci ce cluster create` command and include the following parameters:
     * `--open-id-connect-auth-enabled` set to `true`
     * `--configuration-file` set to the Base64 encoded string that you created from the authentication configuration file.
For example: 
Copy
```
oci ce cluster create \
--compartment-id ocid1.compartment.oc1..aaaaaaaa______n5q \
--name sales \
--vcn-id ocid1.vcn.oc1.phx.aaaaaaaa______lhq \
--type ENHANCED_CLUSTER \
--kubernetes-version v1.30.1 \
--service-lb-subnet-ids "[\"ocid1.subnet.oc1.phx.aaaaaaaa______g7q"]" \
--endpoint-subnet-id ocid1.subnet.oc1.phx.aaaaaaaa______sna \
--endpoint-public-ip-enabled true \
--endpoint-nsg-ids "[\"ocid1.networksecuritygroup.oc1.phx.aaaaaaaa______5qq\"]" \
--cluster-pod-network-options '[{"cniType":"OCI_VCN_IP_NATIVE"}]' \
--open-id-connect-auth-enabled true
--configuration-file <base64-encoded-config-file>
```

Note that having set the `--configurationFile` parameter, do not use other parameters of the `oci ce cluster create` command to configure OIDC authentication. Only use fields in the authentication configuration file to control OIDC authentication.


### Using the API to Specify an External OpenID Connect (OIDC) Identity Provider 🔗 
#### Creating A Cluster and Specifying a Single External OpenID Connect (OIDC) Identity Provider
To use the API to create a cluster that uses a single external OpenID Connect (OIDC) identity provider, use the [CreateCluster](https://docs.oracle.com/iaas/api/#/en/containerengine/latest/Cluster/CreateCluster) operation to create a cluster, and specify values for the attributes of the `openIdConnectTokenAuthenticationConfig` property, including at least the following required attributes:
  * `isOpenIdConnectAuthEnabled` set to `true`
  * `issuerUrl` set to the base public URL of the identity provider that allows the Kubernetes API server to discover public signing keys. This is typically the identity provider's OIDC discovery URL, changed to have an empty path. For example, if the issuer's OIDC discovery URL is `https://accounts.provider.example/.well-known/openid-configuration`, specify `https://accounts.provider.example`
  * `clientId` set to a client ID for which all tokens must be issued. For example, `kubernetes`


In addition to the `issuerURL` and `clientId` attributes, you can optionally set other `openIdConnectTokenAuthenticationConfig` attributes to control OIDC authentication. For a full list of attributes, see [openIdConnectTokenAuthenticationConfig Reference](https://docs.oracle.com/iaas/api/#/en/containerengine/latest/datatypes/OpenIdConnectTokenAuthenticationConfig)
#### Creating A Cluster and Specifying Multiple External OpenID Connect (OIDC) Identity Providers
To use the API to create a cluster that uses multiple external OIDC identity providers (available for clusters running Kubernetes version 1.30 and later):
  1. Create a new Kubernetes authentication configuration file as .yaml file, to contain details of the identity providers. For more information about authentication configuration files, see [Authentication configuration from a file](https://kubernetes.io/docs/reference/access-authn-authz/authentication/#using-authentication-configuration) in the Kubernetes documentation.
  2. For each identity provider:
    1. Set the `jwt.issuer.url` field to the base public URL of the identity provider that allows the Kubernetes API server to discover public signing keys. This is typically the identity provider's OIDC discovery URL, changed to have an empty path. For example, if the issuer's OIDC discovery URL is `https://accounts.provider.example/.well-known/openid-configuration`, specify `https://accounts.provider.example`
    2. Optionally set other fields to control OIDC authentication. Note that when using an authentication configuration file, any OIDC configuration must be specified in this file. For more information about the fields in an authentication configuration file, see [Authentication configuration from a file](https://kubernetes.io/docs/reference/access-authn-authz/authentication/#using-authentication-configuration) in the Kubernetes documentation.
For example:
```
apiVersion: apiserver.config.k8s.io/v1beta1
kind: AuthenticationConfiguration
jwt:
 - issuer:
   url: https://accounts.google.com
   audiences:
    - 838763820337-6vt12pbavkteafx08f32z48u7gpll6on.apps.googleusercontent.com
    - 838763820337-elyce7g28ep5b7uzq4dt1uzh1h86jki9.apps.googleusercontent.com
   audienceMatchPolicy: MatchAny
  claimMappings:
   username:
    claim: "sub"
    prefix: ""
   groups:
    claim: "groups"
    prefix: ""
   uid:
    claim: "sub"
 - issuer:
   url: https://dev-dx7mdewuu7xhb4mw.us.auth0.com/
   audiences:
    - 7w7qJsa3brl5OHV6uljAAYhfknVTsVAw
   audienceMatchPolicy: MatchAny
  claimMappings:
   username:
    claim: "sub"
    prefix: ""
   groups:
    claim: "groups"
    prefix: ""
   uid:
    claim: "sub"
```

  3. Convert the authentication configuration .yaml file to a Base64 encoded string.
  4. Use the [CreateCluster](https://docs.oracle.com/iaas/api/#/en/containerengine/latest/Cluster/CreateCluster) operation to create the cluster, and specify values for the following attributes of the `openIdConnectTokenAuthenticationConfig` property:
     * `isOpenIdConnectAuthEnabled` set to `true`
     * `configurationFile` set to the Base64 encoded string that you created from the authentication configuration file.
Note that having set the `configurationFile` attribute, do not set other attributes of the `openIdConnectTokenAuthenticationConfig` property to configure OIDC authentication. Only use fields in the authentication configuration file to control OIDC authentication.


## Accessing an OIDC-Enabled Cluster 🔗 
One way to access a cluster that authenticates users with an external OIDC identity provider is to use the OIDC Authenticator. To use the OIDC Authenticator to access an OIDC-enabled cluster, you have to enter details for the user, the OIDC identity provider, and the OIDC token in the kubeconfig file, as described in this section. Alternatively, you can access an OIDC-enabled cluster by including a token directly in kubectl commands, using the `--token` option. For more information about using either the OIDC Authenticator or the kubectl the `--token` option, see [OpenID Connect Tokens](https://kubernetes.io/docs/reference/access-authn-authz/authentication/#openid-connect-tokens) in the Kubernetes documentation. 
Note that there are other ways to access OIDC-enabled clusters. For example, by using a kubectl plugin such as kubelogin (for more information, see the [kubelogin documentation on GitHub](https://github.com/int128/kubelogin)).
To use the OIDC Authenticator to access an OIDC-enabled cluster:
  1. Log in to the external OIDC identity provider.
  2. Make a note of the `id_token` and the `refresh_token` that the OIDC identity provider provides. 
  3. Set up a kubeconfig file to access the OIDC-enabled cluster by following the instructions in [Setting Up Cloud Shell Access to Clusters](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengdownloadkubeconfigfile.htm#cloudshelldownload) or [Setting Up Local Access to Clusters](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengdownloadkubeconfigfile.htm#localdownload) as appropriate, depending on how you want to access the cluster.
  4. Define a user in the kubeconfig file that is to be authenticated with the external OIDC identity provider by running the following command:
Copy
```
kubectl config set-credentials <username> \
  --auth-provider=oidc \
  --auth-provider-arg=idp-issuer-url=<base-url> \
  --auth-provider-arg=client-id=<client-name> \
  --auth-provider-arg=client-secret=<client-secret> \
  --auth-provider-arg=refresh-token=<refresh-token> \
  --auth-provider-arg=id-token=<id-token> \
  --auth-provider-arg=extra-scopes=groups
```

where:
     * `<username>` of the user to authenticate with the external OIDC identity provider. For example, `oidc-admin-user`
     * `idp-issuer-url=<base-url>` is the base public URL of the external OIDC identity provider that allows the Kubernetes API server to discover public signing keys. This is typically the identity provider's OIDC discovery URL, changed to have an empty path. For example, if the issuer's OIDC discovery URL is `https://accounts.provider.example/.well-known/openid-configuration`, then specify `https://accounts.provider.example`
     * `client-id=<client-name>` is a string identifier associated with your OIDC client that forms part of the client credentials. For example, `client-id=kubernetes`
     * `client-secret=<CLIENT_SECRET>` is a secret string, effectively the password for the client credentials.
     * `refresh-token=<refresh-token>` is the OAuth 2.0 refresh token provided by the external OIDC identity provider after authentication. 
     * `id-token=<id-token>` is the OAuth 2.0 id_token provided by the external OIDC identity provider after authentication. The id_token represents the IdP user to which you want to allow cluster access through OIDC authentication.
     * `extra-scopes=groups` is a list of additional OAuth 2.0 scopes to request from the external OIDC identity provider when tokens are refreshed.
For example:
Copy
```
kubectl config set-credentials oidc-admin-user \
  --auth-provider=oidc \
  --auth-provider-arg=idp-issuer-url=https://accounts.provider.example \
  --auth-provider-arg=client-id=kubernetes \
  --auth-provider-arg=client-secret=1db158______c5 \
  --auth-provider-arg=refresh-token=q1b______KtQA= \
  --auth-provider-arg=id-token=eyJr______4knw \
  --auth-provider-arg=extra-scopes=groups
```

  5. Define a context in the kubeconfig file for the new user that is to be authenticated using the external OIDC identity provider, by running the following command:```
kubectl config set-context <context-name> --cluster=<cluster-name> --user=<oidc-username>
```

where:
     * `<context-name>` is a name of your choice for the context. For example, `OIDC-auth`
     * `--cluster=<cluster-name>` is the name of the OIDC-enabled cluster. For example, `OIDC-development`
     * `--user=<oidc-username>` is the name of the user to authenticate with the external OIDC identity provider. For example, `oidc-admin-user`
For example:
```
kubectl config set-context OIDC-auth --cluster=OIDC-development --user=oidc-admin-user
```



Was this article helpful?
YesNo

