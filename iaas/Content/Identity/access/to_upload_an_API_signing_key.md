Updated 2025-02-18
# Adding an API Signing Key
Generate and add a signing key from the Console.
You can use the Console to generate the private/public key pair for you. If you already have a key pair, you can choose to upload the public key. When you use the Console to add the key pair, the Console also generates a configuration file preview snippet for you.
The following procedures work for a regular user or an administrator. Administrators can manage API keys for either another user or themselves.
**About the Configuration File Snippet**
When you use the Console to add the API signing key pair, a configuration file preview snippet is generated with the following information:
  * `user` - the OCID of the user for whom the key pair is being added.
  * `fingerprint` - the fingerprint of the key that was just added.
  * `tenancy` - your tenancy's OCID.
  * `region` - the currently selected region in the Console.
  * `key_file`- the path to your downloaded private key file. You must update this value to the path on your file system where you saved the private key file. 


If your configuration file already has a DEFAULT profile, you'll need to do one of the following:
  * Replace the existing profile and its contents.
  * Rename the existing profile.
  * Rename this profile to a different name after pasting it into the configuration file.


You can copy this snippet into your configuration file, to help you get started. If you don't already have a configuration file, see [SDK and CLI Configuration File](https://docs.oracle.com/iaas/Content/API/Concepts/sdkconfig.htm) for details on how to create one.
[Generating an API Signing Key Pair](https://docs.oracle.com/en-us/iaas/Content/Identity/access/to_upload_an_API_signing_key.htm)
**Prerequisite:** Before you generate a key pair, create the `.oci` directory in your home directory to store the credentials. See [SDK and CLI Configuration File](https://docs.oracle.com/iaas/Content/API/Concepts/sdkconfig.htm) for more details.
  1. View the user's details:
     * If you're adding an API key for _yourself_ : 
Open the **Profile** menu, and then click **My Profile**.
     * If you're an administrator adding an API key for _another user_ : Open the **navigation menu** and select **Identity & Security**. Under **Identity** , select **Domains**. Select the name of the identity domain that you want to work in. You might need to change the compartment to find the domain that you want. Then, select **Users**. Locate the user in the list, and then click the user's name to view the details.
  2. Under **Resources** , click **API keys**.
  3. Click **Add API key**.
  4. In the dialog, click **Generate API key pair**.
  5. Click **Download private key** and save the key to your `.oci` directory. In most cases, you do not need to download the public key.
**Note** : If your browser downloads the private key to a different directory, be sure to move it to your `.oci` directory.
  6. Click **Add**. 
The key is added and the **Configuration file preview** is displayed. The file snippet includes required parameters and values you'll need to create your configuration file. Copy and paste the configuration file snippet from the text box into your `~/.oci/config` file. (If you have not yet created this file, see [SDK and CLI Configuration File](https://docs.oracle.com/iaas/Content/API/Concepts/sdkconfig.htm) for details on how to create one.) 
After you paste the file contents, you'll need to update the `key_file` parameter to the location where you saved your private key file.
If your configuration file already has a DEFAULT profile, you'll need to do one of the following:
     * Replace the existing profile and its contents.
     * Rename the existing profile.
     * Rename this profile to a different name after pasting it into the configuration file.
  7. Update the permissions on your downloaded private key file so that only you can view it:
    1. Go to the `.oci` directory where you placed the private key file.
    2. Use the command `chmod go-rwx ~/.oci/<oci_api_keyfile>.pem` to set the permissions on the file.


[Uploading or Pasting an API Key](https://docs.oracle.com/en-us/iaas/Content/Identity/access/to_upload_an_API_signing_key.htm)
**Prerequisite:** You have generated a public **RSA key in PEM format (minimum 2048 bits)**. The PEM format looks something like this:
Copy
```
-----BEGIN PUBLIC KEY-----
MIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEAoTFqF...
...
-----END PUBLIC KEY——
```

  1. View the user's details:
     * If you're adding an API key for _yourself_ : 
Open the **Profile** menu, and then click **My Profile**.
     * If you're an administrator adding an API key for _another user_ : Open the **navigation menu** and select **Identity & Security**. Under **Identity** , select **Domains**. Select the name of the identity domain that you want to work in. You might need to change the compartment to find the domain that you want. Then, select **Users**. Locate the user in the list, and then click the user's name to view the details.
  2. Under **Resources** , click **API keys**.
  3. Click **Add API key**.
  4. In the dialog, select **Choose public key file** to upload your file, or **Paste a public key** , if you prefer to paste it into the **Public key** text box.
  5. After you upload the file or paste the key into the text box, click **Add**.
The key is added and the **Configuration file preview** is displayed. The file snippet includes required parameters and values you'll need to create your configuration file. Copy and paste the configuration file snippet from the text box into your `~/.oci/config` file. (If you have not yet created this file, see [SDK and CLI Configuration File](https://docs.oracle.com/iaas/Content/API/Concepts/sdkconfig.htm) for details on how to create one.) 
After you paste the file contents, you'll need to update the `key_file` parameter to the location where you saved your private key file.
If your configuration file already has a DEFAULT profile, you'll need to do one of the following:
     * Replace the existing profile and its contents.
     * Rename the existing profile.
     * Rename this profile to a different name after pasting it into the configuration file.


## API Signing Keys 🔗 
A user who needs to make API requests must have an **RSA public key in PEM format (minimum 2048 bits)** added to their IAM user profile and sign the API requests with the corresponding private key (see [Required Keys and OCIDs](https://docs.oracle.com/iaas/Content/API/Concepts/apisigningkey.htm)). 
**Important** A user automatically can generate and manage _their own_ API keys in the Console or API. An administrator doesn't need to write a policy to give the user that ability. Remember that a user can't use the API to change or delete their own credentials until they save a key in the Console, or an administrator adds a key for that user in the Console or the API.
If you have a system that needs to make API requests, an administrator needs to create a user for that system and then add a public key to the IAM service for the system. There's no need to generate a Console password for the user.
For instructions on generating an API key, see [Adding an API Signing Key](https://docs.oracle.com/en-us/iaas/Content/Identity/access/to_upload_an_API_signing_key.htm#upload-API-signing-key "Generate and add a signing key from the Console.").
We recommend that you add a label at the end of a private key. For example, ```
-----END PRIVATE KEY-----
 OCI_PRIVATE_KEY
```

Was this article helpful?
YesNo

