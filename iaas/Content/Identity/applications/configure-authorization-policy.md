Updated 2025-01-14
# Configuring an SSO Authorization Policy
Create an authorization policy for each resource in your enterprise application and define the conditions in which users are allowed or denied access to the resource.
**Note**
Authorization policies only work for resources that you protect with **Form or Access Token** authentication method in an authentication policy. If your resource is protected with any other authentication method, App Gateway doesn't perform authorization check when users try to access the resource using a web browser.
Authorization policies define under what conditions users are allowed or denied access to application resources. When App Gateway intercepts an HTTP request to a resource endpoint, App Gateway verifies whether the enterprise application in IAM contains authorization policies for the resource. If so, then App Gateway verifies whether the HTTP request matches one of the rules configured to allow or deny access.
For example, you can configure an allow rule to allow all members of the **Employees** group to access the `/myapp/private/home` resource, and configure a deny rule to deny access to this resource for users authenticated by the **My External SAML IDP** identity provider.
  1. Open the **navigation menu** and select **Identity & Security**. Under **Identity** , select **Domains**. 
  2. Click the name of the identity domain that you want to work in. You might need to change the compartment to find the domain that you want. Then, click **Integrated applications**.
  3. Select the enterprise application that you want to modify.
  4. In the **Application details** page, select **SSO configuration** , and then select **Edit SSO configuration**.
  5. In the **Authorization policy** section, select **Time to live (minutes)** to define for how long App Gateway caches any authorization policy evaluation that has been performed.
By caching these policy evaluations, App Gateway doesn't need to communicate with IAM in subsequent HTTP request made by the user for the same resource.
  6. In the **Allow rules** section, select **Add allow rule** , specify a **Rule name** , and then complete the following fields.
Add Allow Rule Options Conditions |  Description  
---|---  
**Resource to include** |  Select one of the resources configured in the enterprise application.  
**HTTP Method** |  Select the HTTP Methods associated with this rule. The rule is valid only for the selected HTTP Methods.  
**Authenticating identity provider** (Optional) |  (Optional) Select from the active identity providers in IAM. If you leave this empty, the other conditions are used for authentication. If the user signs in using one of these identity providers, then App Gateway access to the resource. **Local IDP** refers to users authenticated by IAM.  
**Group membership** |  Select IAM's groups. If the signed in user is a member of one of the selected groups, then App Gateway allows access to the resource.  
**Exclude users** |  Select IAM users. If the signed in user isn't one of the selected users, then App Gateway allows access to the resource.  
**Filter by client IP address** |  Select the IP address range the HTTP request are made from.
     * **Anywhere** : App Gateway doesn't validate the IP address from where the HTTP request was made.
     * **Restrict to the following network perimeters** : Select this option, and then select the network perimeters associated with this rule. If the IP address from where the HTTP request was made is specified in one of the network perimeters, then Access Gateway allows access to the resource.  
**Restrict access time period** |  Select a time of the day (**From** and **To**), select which days of the week, and then the time zone in which the rule is valid. App Gateway allows access to the resource only if the HTTP Request is made within the period configured.  
All the conditions configured for an allow rule must be met so that App Gateway can perform the action configured for the rule.
  7. In the **Actions** section of the **Add allow rule** window, select **+Another Header** , enter the name for the HTTP header and then select a user attribute as value. Repeat this step for all headers you want to configure for this rule.
If the user is allowed access to the resource, App Gateway adds these header variables with the corresponding values to the HTTP request before forwarding the request to the application.
  8. Select **Add allow rule** to add the allow rule.
  9. In the **Deny rules** section, select **Add deny rule** , specify a **Rule name** , and then complete the following fields.
Add Deny Rule Options Conditions |  Description  
---|---  
**Resource to include** |  Select one of the resources configured for the enterprise application.  
**HTTP Method** |  Select the HTTP Methods to associate with this rule.  
**Authenticating identity provider** |  Select identity providers that are active in IAM. If the user is signed in using one of these identity providers, then App Gateway denies access to the resource. **Local IDP** refers to users authenticated by IAM.  
**Group membership** |  Select IAM groups. If the signed in user is member of one of the selected groups, then App Gateway denies access to the resource.  
**Exclude users** |  Select the IAM users. If the signed in user isn't one of the selected users, then App Gateway denies access to the resource.  
**Filter by client IP address** |  Select the IP address range the HTTP request are made from.
     * **Anywhere** : App Gateway doesn't validate the IP address from where the HTTP request was made.
     * **Restrict to the following network perimeters** : Select this option, and then select the network perimeters to associate with this rule. If the IP address from where the HTTP request was made is specified as one of the network perimeters, then Access Gateway denies access to the resource.  
**Restrict access time period** |  Select a time of the day (**From** and **To**), select which days of the week, and then the time zone in which the rule is valid. App Gateway denies access to the resource if the HTTP Request is made within the period configured.  
All the conditions configured for a deny rule must be met so that App Gateway can perform the action configured for the rule.
  10. In the **Actions** section of the **Add deny rule** window, select the action App Gateway must perform when a deny rule condition matches the resource's HTTP request.
     * **Sign out the user** : Logs the user out from IAM.
  11. Select **Add deny rule** to add the deny rule.
  12. Select **Save changes**.


Was this article helpful?
YesNo

