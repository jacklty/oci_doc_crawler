Updated 2025-01-14
# Configuring SSO Resources
Create resources individually by adding one resource for each of your application's URLs, or use regular expression to create a resource which represents a collection of URLs for your application.
A resource represents a URL or URL Pattern for which you want to restrict access or intend to give anyone to access. You need the list of resources of your application. See [Enterprise Applications](https://docs.oracle.com/en-us/iaas/Content/Identity/applications/enterprise-applications.htm#enterprise-applications "Enterprise applications are web applications that require App Gateway to integrate with IAM for authentication and authorization purposes.")
Policy mapping is hierarchical in App Gateway. So, order of the resources defined is important. See the following example:
If the user is accessing a resource `/myapp/logout.html`, and we have authentication policy in below order: 
  1. `/.*` (public)
  2. `/.*/logout.html` (Form+logout)

Then policy match stops at step #1 (`/.*`) and the same policy is applied which is "public" in this case.
Similarly, if user is accessing a resource `/myapp/logout.html` and we have authentication policy in below order.
  1. `/.*/logout.html` (Form+logout)
  2. `/.* `(public)

In this case, policy match stops at point 1 (`/.*/logout.html`) and same policy is applied which is "Form+logout".
Something else to be aware of is that applications which do their own login integrations can run into problems when their integrations accessed static resources during login, but the resources weren't made public. This causes the login process to fail. To avoid this happening, you should use the `public` authentication method for your public static resources such as CSS, JavaScript, image files as follows:
  * Group all public static resources together, for example under `/myapp/public/resources`.
  * State that these directories should use the `public` authentication method using a regex such as `/myapp/public/.*`.


To configure resources:
  1. Open the **navigation menu** and select **Identity & Security**. Under **Identity** , select **Domains**. 
  2. Click the name of the identity domain that you want to work in. You might need to change the compartment to find the domain that you want. Then, click **Integrated applications**. 
  3. Select the enterprise application that you want to modify.
  4. In the **Application details** page, select **SSO configuration** , and then select **Edit SSO configuration**. In the **Resources** section, select **Add resource** to add a resource.
  5. In **Add resource** , provide a name and description for the resource and the resource URL. Optionally, add a **URL query string**. If you want to use a regular expression, then select **Regex** , so that App Gateway evaluates the **Resource URL** value as a pattern.
For example, if you want to protect the application endpoint `http://myapp.internal.example.com:3266/private/home`, you can enter `/private/home` as the value for **Resource URL**. If you want to protect any page under the `/private` context, then enter `/private/.*` as value for **Resource URL** , and select **Regex**.
See [Using Regular Expressions](https://docs.oracle.com/en-us/iaas/Content/Identity/applications/use-regular-expressions.htm#use-regular-expressions "Use regular expressions \(regex\) to define a URL pattern which represents more than one URL of your enterprise application and for which you can apply the same authentication policy and the same authorization policy.").
  6. Select **Add resource**. 
  7. Select **Save changes**.


Was this article helpful?
YesNo

