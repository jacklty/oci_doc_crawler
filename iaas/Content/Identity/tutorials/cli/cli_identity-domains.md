Updated 2025-02-18
# OCI Identity Domains with CLI
In this tutorial, you use the Oracle Cloud Infrastructure command line interface (OCI CLI) to create and manage users in an identity domain.
OCI CLI is built on the Oracle Cloud Infrastructure SDK for Python and runs on Mac, Windows, and Linux. The Python code makes requests to OCI APIs to provide the functionality.
The CLI supports several authentication methods. In this tutorial, you use the API key-based authentication method.
This tutorial covers the following tasks:
  * Generate an API signing key pair
  * Set up the CLI configuration file
  * Install the CLI
  * Get the identity domain URL
  * Create a user
  * Get a user's details
  * Delete a user


This tutorial takes about 30 minutes to complete.
**Note** This tutorial is specific to OCI Identity and Access Management with identity domains.
## Before You Begin 🔗 
To perform this tutorial, you must have the following:
  * An [Oracle Cloud account](https://docs.oracle.com/iaas/Content/GSG/Concepts/get-account.htm).
  * A user account with access to an identity domain and assigned the [user administrator role](https://docs.oracle.com/iaas/Content/Identity/roles/understand-administrator-roles.htm). Ask the identity domain administrator or cloud account administrator if you're not sure whether you have the permissions to create and manage users in an identity domain.
  * The `.oci` directory in your user home directory on the local machine: `~/.oci`
For example, on Windows, you can use PowerShell to create the directory with the following command: `mkdir %HOMEDRIVE%%HOMEPATH%\.oci`
  * A [supported version of Python on a supported operating system](https://docs.oracle.com/iaas/Content/API/Concepts/cliconcepts.htm#Requirements__SupportedPythonVersionsandOperatingSystems).
If you don't already have Python installed on Windows or Linux, later in this tutorial when you run the CLI installation script to install the CLI, you can let the script install Python for you.


## 1. Generate an API signing key pair 🔗 
An RSA key pair in PEM format (minimum 2048 bits) is required for signing API requests.
This task describes how to use the Console to create a key pair.
The following procedure assumes that you have already created the `.oci` directory in your user home directory on the local machine. The `~/.oci` directory is required to store OCI configuration information such as signing credentials and OCID values.
  1. Sign in to the [Oracle Cloud account](http://cloud.oracle.com) using the appropriate tenancy (cloud account name) and identity domain, and your username and password.
If you're signing in for the first time, open the activation email and use the **Activate Your Account** link provided. You're prompted to enter and confirm a password. See [Signing In for the First Time](https://docs.oracle.com/iaas/Content/GSG/Tasks/signingin_topic-Signing_In_for_the_First_Time.htm), if you need more information.
The tenancy, identity domain, and username are provided in the profile password reset email when you activated the user profile in the cloud account.
Contact the cloud account administrator or identity domain administrator if you don't have any of the information you need for signing in. See [Contacting Support](https://docs.oracle.com/iaas/Content/GSG/Tasks/signinginIdentityDomain.htm#contacting_support).
  2. On the Console home page, select the user profile icon and then select your username.
  3. On the user profile page, select **API keys** under **Resources**.
  4. Select **Add API key**.
  5. On the **Add API key** panel, select **Generate API key pair** and then select **Download private key.**
Save the private key to the `~/.oci` directory. Optionally, you can move the key to a subdirectory within the `.oci` directory. 
Note down the private key's filename and path. The following example is for Windows: 
`C:\Users\EXAMPLEUSER\.oci\examplecliuser_2025-01-02T21_18_14.873Z.pem`
  6. (Optional) Select **Download public key.**
You can download the public key but it's not necessary. Both the public and private keys are PEM files. The public key has the string `_public` in the key's filename.
  7. On the **Add API key** panel, select **Add**.
The Console displays the **Configuration file preview** dialog, which shows your user's configuration information for using OCI.
  8. For now, select **Close**.
  9. On the user profile page, verify that the fingerprint for the generated key pair is added under **Fingerprint**. For example:
`11:22:00:aa:33:4b:5c:66:7d:88:99:ee:00:90:80:70`


## 2. Set up the CLI Configuration File 🔗 
The CLI configuration contains the required credentials for working with Oracle Cloud Infrastructure.
This task assumes that you have generated the API key pair for signing API requests.
  1. If not already signed in, sign in to the [Oracle Cloud account](http://cloud.oracle.com) using the appropriate tenancy (cloud account name) and identity domain, and your username and password.
  2. On the Console home page, select the user profile icon and then select your username.
  3. On the user profile page, select **API keys** under **Resources**.
  4. From the Actions menu (![](https://docs.oracle.com/en-us/iaas/Content/libraries/global-images/actions-menu.png)) next to the fingerprint that was added in the task [Generate an API signing key pair](https://docs.oracle.com/en-us/iaas/Content/Identity/tutorials/cli/cli_identity-domains.htm#cli-api-keypair "An RSA key pair in PEM format \(minimum 2048 bits\) is required for signing API requests."), select **View configuration file**.
The Console displays the **Configuration file preview** dialog, which has your user configuration specified in the `DEFAULT` profile.
```
[DEFAULT]
user=ocid1.user.oc1..areallylongstringoflettersandnumbers123498765
fingerprint=11:22:00:aa:33:4b:5c:66:7d:88:99:ee:00:90:80:70
tenancy=ocid1.tenancy.oc1..areallylongstringoflettersandnumbers123498765
region=us-ashburn-1
key_file=<path to your private keyfile>#TODO
```

  5. In the **Configuration file preview** dialog, select **Copy** to copy the configuration file preview content to the clipboard. Then close the dialog.
  6. Open a text editor and paste the preview content from the clipboard into a new file.
  7. Using `config` as the filename, save the file to the `~/.oci` directory.
If a `config` file already exists in the `~/.oci` directory, perform one of the following tasks:
     * Rename the existing configuration file.
     * Open the existing configuration file. If a `DEFAULT` profile is already configured in the existing file, rename the existing `DEFAULT` profile. Then paste the preview `DEFAULT` content from the clipboard into the file.
  8. In the `~/.oci/config` file where you pasted the preview `DEFAULT` profile content, update the `key_file` parameter to the filename and path on the machine's file system where you saved the private key.
The following example is for Windows:
`key_file=C:\Users\EXAMPLEUSER\.oci\examplecliuser_2025-01-02T21_18_14.873Z.pem`
  9. Verify that the `DEFAULT` profile in `~/.oci/config` looks similar to the following:
```
[DEFAULT]
user=ocid1.user.oc1..areallylongstringoflettersandnumbers123498765
fingerprint=11:22:00:aa:33:4b:5c:66:7d:88:99:ee:00:90:80:70
tenancy=ocid1.tenancy.oc1..areallylongstringoflettersandnumbers123498765
region=us-ashburn-1
key_file=C:\Users\EXAMPLEUSER\.oci\examplecliuser_2025-01-02T21_18_14.873Z.pem
```

Unless a specific profile is specified, OCI uses the signing credentials in the `DEFAULT` profile when you run a CLI command.


## 3. Install the CLI 🔗 
You can install OCI CLI on Windows, Linux, or MacOS. 
Before installing the CLI, ensure that a supported Python version is already installed on the machine. The [supported Python versions](https://docs.oracle.com/iaas/Content/API/Concepts/cliconcepts.htm#Requirements__SupportedPythonVersionsandOperatingSystems) section lists the versions that are supported for each OS.
Consider the following:
  * If you already have Python installed on the machine, use the `python --version` command in a command prompt to find out which version is installed.
  * If you don't already have Python installed or you don't have a compatible Python version, the options are:
    * Install a compatible Python version on the machine before installing the CLI.
    * On Windows or Linux: When you run the CLI installation script, you can let the script install Python for you at the same time.
    * On MacOS: The CLI installation script doesn't install Python for you. You must upgrade before you can proceed with the CLI installation.


To install the OCI CLI on a machine:
  1. Follow the [appropriate OS instructions](https://docs.oracle.com/iaas/Content/API/SDKDocs/cliinstall.htm) to install the CLI.
  2. Verify the CLI installation by running the following command in a command prompt.
Copy
```
oci --version
```



## 4. Get the Identity Domain URL 🔗 
This task assumes that you have an Oracle Cloud user account with access to an identity domain.
  1. If not already signed in, sign in to the [Oracle Cloud account](http://cloud.oracle.com) using the appropriate tenancy (cloud account name) and identity domain, and your username and password.
The tenancy, identity domain, and username are provided in the profile password reset email when you activated the user profile in the cloud account.
Contact the cloud account administrator or identity domain administrator if you don't have any of the information you need for signing in. See [Contacting Support](https://docs.oracle.com/iaas/Content/GSG/Tasks/signinginIdentityDomain.htm#contacting_support).
  2. On the Console home page, select the user profile icon and then select the identity domain name.
  3. On the **Domain Information** tab, select **Copy** that's at the end of **Domain URL**. 
  4. Open a text editor and paste the copied URL.
A domain URL looks similar to the following: 
```
https://idcs-01a234bc56d77e0f89898989bg7h06ij.identity.oraclecloud.com
```

Set the copied URL aside. You need it later to construct the `endpoint` parameter in CLI commands.


## 5. Create a User 🔗 
This task assumes that you have generated the API signing key pair, set up the OCI configuration file, and installed the CLI.
You also need to have the identity domain URL to construct CLI commands.
Complex input, such as arrays and objects with more than one value, are passed in JSON format to the CLI. The input can be provided as a JSON file or as inline parameter strings at the command line.
  1. Do one of the following tasks to prepare the input for creating a user:
     * JSON file: Open a text editor. Copy the following JSON and save the file with the extension `.json` in any directory.
Then note down the filename and path, for example in Windows: `C:\examples\clicreateuser.json`
Copy
```
{
 "schemas": [
  "urn:ietf:params:scim:schemas:core:2.0:User"
 ],
 "name": {
	"givenName": "John",
	"familyName": "Doe"
 },
 "userName": "jdoe@cliexample.com",
 "emails": [
	{
	 "value": "john.doe@examplecli.com",
	 "type": "work",
	 "primary": true
	}
 ]
}
```

     * Inline parameter strings: Open a text editor. Copy the following strings and set them aside for later use.
In Windows, enclose each parameter value block in double quotes (`".."`). Within a block, each double quote (`"`) for the key and value strings must be escaped with a backslash (`\`) character.
Copy
```
--user-name jdoe@cliexample.com
--name "{\"givenName\":\"John\",\"familyName\":\"Doe\"}"
--emails "[{\"value\":\"john.doe@examplecli.com\",\"type\":\"work\",\"primary\":true}]"
--schemas "[\"urn:ietf:params:scim:schemas:core:2.0:User\"]" 

```

In MacOS, Linux, or Unix, enclose each parameter value block in single quotes (`'..'`). 
Copy
```
--user-name jdoe@cliexample.com
--name '{"givenName":"John","familyName":"Doe"}'
--emails '[{"value":"john.doe@examplecli.com","type":"work","primary":true}]'
--schemas '["urn:ietf:params:scim:schemas:core:2.0:User"]' 

```

  2. Open a command prompt and enter the CLI command to create a user. 
At the command line, you can specify a JSON file or use inline parameters as the input.
     * Use the JSON file that you created as input.
Windows example:
Copy
```
oci identity-domains user create
 --from-json file://C:\examples\clicreateuser.json
 --endpoint https://idcs-01a234bc56d77e0f89898989bg7h06ij.identity.oraclecloud.com

```

     * Use the inline parameter strings that you prepared as input.
Windows example:
Copy
```
oci identity-domains user create 
--user-name jdoe@cliexample.com 
--name "{\"givenName\":\"John\",\"familyName\":\"Doe\"}" 
--emails "[{\"value\":\"john.doe@examplecli.com\",\"type\":\"work\",\"primary\":true}]" 
--schemas "[\"urn:ietf:params:scim:schemas:core:2.0:User\"]" 
--endpoint https://idcs-01a234bc56d77e0f89898989bg7h06ij.identity.oraclecloud.com

```

MacOS, Linux, or Unix example:
Copy
```
oci identity-domains user create 
--user-name jdoe@cliexample.com
--name '{"givenName":"John","familyName":"Doe"}'
--emails '[{"value":"john.doe@examplecli.com","type":"work","primary":true}]'
--schemas '["urn:ietf:params:scim:schemas:core:2.0:User"]' 
--endpoint https://idcs-01a234bc56d77e0f89898989bg7h06ij.identity.oraclecloud.com

```

The `endpoint` parameter is the domain URL that you copied in the task [Get the Identity Domain URL](https://docs.oracle.com/en-us/iaas/Content/Identity/tutorials/cli/cli_identity-domains.htm#cli-domain-url "This task assumes that you have an Oracle Cloud user account with access to an identity domain.").
  3. In the command response, verify that the user is created.
For example:
```
{
 "data": {
  ...
  "name": {
   "family-name": "Doe",
   "given-name": "John",
   ...
  },
  ...
  "ocid": "ocid1.user.oc1..areallylongstringoflettersandnumbers987654321abcxyz",
  ...
  "user-name": "jdoe@cliexample.com",
  ...
 }
}
```

  4. Copy the OCID of the newly created user.
For example: 
```
ocid1.user.oc1..areallylongstringoflettersandnumbers987654321abcxyz
```



## 6. Get a User 🔗 
This task assumes that you have created a user and obtained the user's OCID.
  1. In a command prompt, enter the CLI command to retrieve the details of a user by providing the user's OCID.
Example:
Copy
```
oci identity-domains user get
 --user-id ocid1.user.oc1..areallylongstringoflettersandnumbers987654321abcxyz
 --endpoint https://idcs-01a234bc56d77e0f89898989bg7h06ij.identity.oraclecloud.com

```

  2. In the command response, verify that the correct user's details are shown.


## 7. Delete a User 🔗 
Delete a user by providing the user's OCID.
  1. In a command prompt, enter the CLI command to delete a user.
Example:
Copy
```
oci identity-domains user delete
 --user-id ocid1.user.oc1..areallylongstringoflettersandnumbers987654321abcxyz
 --endpoint https://idcs-01a234bc56d77e0f89898989bg7h06ij.identity.oraclecloud.com

```

The following response is returned:
`Are you sure you want to delete this resource? [y/N]`
  2. Enter `y`.
The following response is then returned:
```
{
 "opc-next-page": "MQ==",
 "opc-total-items": "1"
}

```

  3. (Optional) You can verify that the user has been deleted by running the CLI command to get a user, as described in [Get a User](https://docs.oracle.com/en-us/iaas/Content/Identity/tutorials/cli/cli_identity-domains.htm#cli-get-user "This task assumes that you have created a user and obtained the user's OCID.").
If the user is deleted, OCI includes the message `"The resource does not exist."` in the response.


## What's Next 🔗 
Explore more about using the CLI in OCI.
  * [Using the CLI](https://docs.oracle.com/iaas/Content/API/SDKDocs/cliconfigure.htm)
  * [Using Interative Mode](https://docs.oracle.com/iaas/Content/API/SDKDocs/cliusing_topic-Using_Interactive_Mode.htm)
  * [Token-based Authentication for the CLI](https://docs.oracle.com/iaas/Content/API/SDKDocs/clitoken.htm)
  * [CLI Environment Variables](https://docs.oracle.com/iaas/Content/API/SDKDocs/clienvironmentvariables.htm)


Was this article helpful?
YesNo

