Updated 2025-01-14
# OCI Identity Domains with Postman
In this tutorial, you make REST application programming interface (API) calls to an identity domain using Postman, a software that's typically used for REST API tests.
The identity domains REST APIs provide a way to integrate identity domains with REST clients to manage users, groups, applications, and settings, and perform federated single sign-on (SSO) and authorization in the cloud. The APIs support OAuth 2.0, OpenID Connect, and System for Cross-Domain Identity Management (SCIM).
In this tutorial, you:
  * Register an OAuth client application
  * Set the environment parameters in Postman
  * Import the identity domains Postman collection
  * Request an OAuth access token
  * Create a user
  * Get a user
  * Delete a user


This tutorial takes about 20 minutes to complete.
**Note** This tutorial is specific to OCI Identity and Access Management with identity domains.
## Before You Begin 🔗 
To perform this tutorial, you must have the following:
  * Access to an identity domain with the [identity domain administrator role](https://docs.oracle.com/iaas/Content/Identity/roles/understand-administrator-roles.htm). Ensure that you have the following values:
    * The tenancy name, identity domain name, and the credentials (user name and password) to [sign in](https://docs.oracle.com/iaas/Content/GSG/Tasks/signinginIdentityDomain.htm) to a tenancy in the Oracle Cloud Infrastructure Console with an identity domain.
    * The domain URL that's shown on the identity domain details page after signing in. For example, `https://<idcs-letterandnumberstring>.identity.oraclecloud.com`. If you need help to find the domain URL, see [Finding an Identity Domain URL](https://docs.oracle.com/iaas/Content/Identity/api-getstarted/locate-identity-domain-url.htm) in the documentation. The identity domain URL is used to construct a REST request.
  * Familiarity with the [REST architecture style](https://en.wikipedia.org/wiki/Representational_state_transfer)
  * The [Postman desktop app](https://www.postman.com/downloads/) installed.
    * Familiarity with Postman is not necessary.
    * [Create a Postman account](https://learning.postman.com/docs/getting-started/installation/postman-account/#sign-up-for-a-postman-account). An account is required to use environment variables.
    * (Optional) [Create a workspace](https://learning.postman.com/docs/collaborating-in-postman/using-workspaces/create-workspaces/) in Postman.


## 1. Register a Client Application 🔗 
To authenticate a REST API call to an identity domain, register an OAuth client application in the identity domain.
This task is required to obtain the credentials (client ID and client secret) that are used for authentication. The credentials are equivalent to service credentials (ID and password) that the client uses to communicate with an identity domain. This task also helps you determine which requests are authorized through the REST API. 
  1. Open the **navigation menu** and select **Identity & Security**. Under **Identity** , select **Domains**.
  2. Select the name of the identity domain that you want to work in. You might need to change the compartment to find the domain that you want. 
  3. On the domain details page, select **Integrated applications**. 
  4. Select **Add application.**
  5. In the **Add application** dialog, select **Confidential Application** , and then select **Launch workflow**. 
  6. On the **Add application details** step of the workflow, enter an application name and description, and then select **Next**. 
  7. On the **Configure OAuth** step, perform the following actions:
    1. In the **Client configuration** box, select **Configure this application as a client now**.
The box expands, showing more options.
    2. Under **Authorization** , select only **Client Credentials** as the allowed grant type. 
    3. Scroll down to the end of the box. Select **Add app roles** and then select **Add roles**. 
    4. In the **Add app roles** panel, select **Identity Domain Administrator** , and then select **Add**.
  8. On the **Configure OAuth** step, select **Next** and then select **Finish**. 
You can skip the policy configuration step in this tutorial.
When the application is created, its initial state is **Inactive**.
  9. On the application details page, select **Activate**. Then select **Activate application** to confirm activation of this application.
  10. On the application details page, scroll down to **General Information** and follow these steps to copy the client ID and client secret values. 
    1. Highlight the value that's displayed next to **Client ID** and copy the value to a text file.
    2. Under **Client Secret** , select **Show secret**. In the dialog that appears, select **Copy** and then select **Close**. The value is copied to the clipboard. Paste the value in a text file.
    3. Store the client ID and client secret values that you copied in a safe place.


## 2. Set the Environment Parameters in Postman 🔗 
To successfully perform this tutorial in Postman, import the `idcs-rest-clients` REST variable samples and set the environment parameters.
  1. Open the Postman desktop app and sign in using your account. If you have a workspace, select **Workspace** and select the workspace. Otherwise, you can use the default workspace.
  2. In the workspace, select **Import**. 
  3. In the **Import** dialog, paste the following GitHub environment variables URL into the field. ```
https://github.com/oracle/idm-samples/raw/master/idcs-rest-clients/example_environment.json
```

Postman starts importing as soon as you paste the URL. When import is complete, select **Dismiss** to close the message box.
  4. In the sidebar on the left, select **Environments**. Then right-click **Oracle Identity Cloud Service Example Environment with Variables** and select **Duplicate**.
  5. In the list of environments, right-click **Oracle Identity Cloud Service Example Environment with Variables Copy** that appears below the original environment and select **Rename**. In the field, type `Environment A for REST API Testing` and press **Enter**.
  6. To update the variables in the renamed environment, enter the following values in the **Initial Value** and **Current Value** fields.
     * **HOST:** The domain URL that you obtained from the identity domain details page after signing in to the Oracle Cloud Infrastructure Console. For example, `https://<idcs-letterandnumber123string>.identity.oraclecloud.com`. If you need help to find the domain URL, see [Finding an Identity Domain URL](https://docs.oracle.com/iaas/Content/Identity/api-getstarted/locate-identity-domain-url.htm) in the documentation. 
     * **CLIENT_ID and CLIENT_SECRET:** The client ID and the client secret that you copied into a text file from the identity domain's trusted application, as described in the tutorial task [Register a Client Application](https://docs.oracle.com/en-us/iaas/Content/Identity/tutorials/rest/rest_postman.htm#prepare "To authenticate a REST API call to an identity domain, register an OAuth client application in the identity domain.").
     * **USER_LOGIN and USER_PW:** Your login user name and password 
![Modified Postman environment variables](https://docs.oracle.com/en-us/iaas/Content/Identity/tutorials/images/modify_environment_variables.png)
  7. Select **Save**.
  8. In the list of environments, select the check mark on the name `Environment A for REST API Testing` to make it the active environment.
The active environment is shown in the environment selector at the top-right corner of the workbench.


## 3. Import the Identity Domains Postman Collection 🔗 
To successfully perform this tutorial in Postman, import the `REST_API_for_Oracle_Identity_Cloud_Service` collection, which contains sample API requests that can be used to make calls.
  1. In the Postman workspace, select **Import**. 
  2. In the **Import** dialog, paste the following URL into the field to import the identity domains REST API Postman collection.```
https://github.com/oracle/idm-samples/raw/master/idcs-rest-clients/REST_API_for_Oracle_Identity_Cloud_Service.postman_collection.json
```

Postman starts importing as soon the collection as you paste the URL. When import is complete, you can select **Dismiss** to close the message box.
  3. In the sidebar on the left, select **Collections**.
  4. Select the name **REST_API_for_Oracle_Identity_Cloud_Service**.
The requests in the collection are organized in folders.
![The collection appears beneath the Collections tab.](https://docs.oracle.com/en-us/iaas/Content/Identity/tutorials/images/collection_in_left_panel.png)


## 4. Request an Access Token 🔗 
To make API calls to an identity domain, you must authenticate the client against the identity domain, and then obtain an OAuth access token.
The access token provides a session between a client (in this tutorial, Postman) and the identity domain.
**Note** By default, an access token has a timeout interval of 60 minutes. To perform REST API calls beyond the interval, you must request a new access token.
  1. In the sidebar on the left, select **Collections**. Expand **REST_API_for_Oracle_Identity_Cloud_Service** , if it's not expanded.
  2. Expand **OAuth** , and then expand **Tokens**.
  3. Under **Tokens** , select **POST Obtain access_token (client credentials)**.
The API's `POST` tab appears in the workbench. The request pane of the API is separated from the response pane by a line. You can drag the separator line to show more or less of each pane.
In the request pane, the URL field shows: `POST {{HOST}}/oauth2/v1/token`
The variables for `{{HOST}}`, signing in, and authentication credentials are already set when you completed the tutorial task [Set the Environment Parameters in Postman](https://docs.oracle.com/en-us/iaas/Content/Identity/tutorials/rest/rest_postman.htm#_02-iam-postman-set-env-var "To successfully perform this tutorial in Postman, import the idcs-rest-clients REST variable samples and set the environment parameters."). 
  4. Select **Send**.
In the response viewer, confirm that the status `200 OK` appears and that the access token is returned in the response body. An access token is a very long string of letters and numbers.
  5. To assign the access token value to an environment variable, use the following steps.
    1. In the response, highlight the access token content that's between the quotation marks and right-click. In the shortcut menu, select **Set: Environment A for REST API Testing** and then select **access_token** in the secondary menu to assign the highlighted content as the access token environment value.
![Access token in the response and context menus](https://docs.oracle.com/en-us/iaas/Content/Identity/tutorials/images/assign_access_token_variable.png)
    2. In the upper-right of the workbench, select the icon to open the variables pane.
The assigned `access_token` value is shown under **All variables**.
![Access token variable in Variables pane](https://docs.oracle.com/en-us/iaas/Content/Identity/tutorials/images/variables_pane.png)
  6. To close the variables pane, select **X** in the upper-right of the pane or select the variables icon. 


If you send the next REST API call to the identity domain before the token expires, the API call contains the access token and other information related to the request. REST information is sent through a request Universal Resource Identifier, a header, parameters, or JSON code, and varies according to the REST API call and method that you request.
## 5. Create a User 🔗 
This task assumes that you requested an access token within the past hour.
If necessary, [request a new token](https://docs.oracle.com/en-us/iaas/Content/Identity/tutorials/rest/rest_postman.htm#_04-iam-postman-request-acccess-token "To make API calls to an identity domain, you must authenticate the client against the identity domain, and then obtain an OAuth access token.") before creating a user.
  1. In the sidebar on the left, select **Collections**. Expand **Users** and then expand **Create**.
  2. Under **Create** , select **Create a user**.
The API's `POST` tab appears in the workbench.
  3. Select the **Body** tab.
The sample uses raw mode and JSON format for the body data.
![Body tab with JSON code](https://docs.oracle.com/en-us/iaas/Content/Identity/tutorials/images/modify_request_body_content.png)
  4. Select **Send**.
     * In the response viewer, confirm that the status `201 Created` appears and that the response body contains details about the user that was successfully created in the identity domain.
     * If the status `401 Unauthorized` appears, with the error message `Proper authorization is required for this area`, [request a new access token](https://docs.oracle.com/en-us/iaas/Content/Identity/tutorials/rest/rest_postman.htm#_04-iam-postman-request-acccess-token "To make API calls to an identity domain, you must authenticate the client against the identity domain, and then obtain an OAuth access token.") and try creating the user again.
  5. In the response body of a successful creation, scroll down to line 40, which has the OCID value for the user that's created.
For example: `ocid1.user.oc1..aabaaacaaaq7xxxxxx`
  6. Highlight the OCID value that's between the double quotation marks. In the shortcut menu, select **Set: Environment A for REST API Testing** and then select **userid** in the secondary menu.
  7. In the upper-right of the workbench, select the icon to open the variables pane.
The assigned `userid` value is shown under **All variables**. 


## 6. Get a User 🔗 
This task retrieves the details of a specific user by using the `userid` variable.
The following procedure assumes that you have completed the preceding task [Create a User](https://docs.oracle.com/en-us/iaas/Content/Identity/tutorials/rest/rest_postman.htm#_05-iam-postman-create-user "This task assumes that you requested an access token within the past hour.").
  1. In the sidebar on the left, select **Collections**. Expand **Users** and then expand **Search**.
  2. Under **Search** , select **Get a specific user**.
The API's `GET` tab appears in the workbench.
  3. Select **Send**.
     * If successful, confirm that the status `200 OK` appears in the response viewer. You should also see details about that specific user in the **Body** tab.
     * If you see the status `401 Unauthorized` with the error message `Proper authorization is required for this area`, [request a new access token](https://docs.oracle.com/en-us/iaas/Content/Identity/tutorials/rest/rest_postman.htm#_04-iam-postman-request-acccess-token "To make API calls to an identity domain, you must authenticate the client against the identity domain, and then obtain an OAuth access token.") and try retrieving the specific user again.


## 7. Delete a User 🔗 
This task deletes a user that's specified by the `userid` variable.
The following procedure assumes that you have completed the tutorial tasks [Create a User](https://docs.oracle.com/en-us/iaas/Content/Identity/tutorials/rest/rest_postman.htm#_05-iam-postman-create-user "This task assumes that you requested an access token within the past hour.") and [Get a User](https://docs.oracle.com/en-us/iaas/Content/Identity/tutorials/rest/rest_postman.htm#_06-iam-postman-get-user "This task retrieves the details of a specific user by using the userid variable.").
If necessary, [request a new access token](https://docs.oracle.com/en-us/iaas/Content/Identity/tutorials/rest/rest_postman.htm#_04-iam-postman-request-acccess-token "To make API calls to an identity domain, you must authenticate the client against the identity domain, and then obtain an OAuth access token.") before performing this task.
  1. In the sidebar on the left, select **Collections**. Expand **Users** and then expand **Delete**.
  2. Select **Delete user**.
The API's `DELETE` tab appears in the workbench.
  3. In the upper-right of the workbench, select the icon to open the variables pane.
Under **All variables** , confirm that the `userid` variable still shows the same OCID value that was used to retrieve the user's details. 
  4. Select **Send**.
     * If successful, confirm that the status `204 No content` appears in the response viewer. The **Body** tab is blank because no response body is returned for a `DELETE` operation.
     * If you see the status `401 Unauthorized` with the error message `Proper authorization is required for this area`, [request a new access token](https://docs.oracle.com/en-us/iaas/Content/Identity/tutorials/rest/rest_postman.htm#_04-iam-postman-request-acccess-token "To make API calls to an identity domain, you must authenticate the client against the identity domain, and then obtain an OAuth access token.") and try deleting the specific user again.
  5. When deletion is successful, select the **GET a specific user** tab in the workbench. Then select **Send**.
In the response viewer, confirm that the status `404 Not found` appears, which indicates that the user has been deleted.


## What's Next 🔗 
To explore guidelines for building requests and typical use cases using the OCI identity domains REST APIs, see:
  * [Structuring Resource Requests](https://docs.oracle.com/en-us/iaas/Content/Identity/api-getstarted/RequestResponse.htm#RequestResponse "Learn the guidelines for building send requests in an identity domain.")
  * [API Use Cases](https://docs.oracle.com/en-us/iaas/Content/Identity/api-getstarted/api-use-cases.htm "Step through typical use cases using the IAM identity domain REST APIs.")


Was this article helpful?
YesNo

