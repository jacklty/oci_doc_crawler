Updated 2024-01-18
# Moving an Image to a Different Compartment
On Compute Cloud@Customer, you can move an image to another compartment using the CLI or API.
Custom images are available to all users authorized for the compartment in which the image was created. Ensure that you move the image to a compartment that has the appropriate authorized users.
  * [Console](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/images/moving-an-image-to-a-different-compartment.htm)
  * [CLI](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/images/moving-an-image-to-a-different-compartment.htm)
  * [API](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/images/moving-an-image-to-a-different-compartment.htm)


  * This task can't be performed using the Console.
  * Use the [oci compute image change-compartment](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/compute/image/change-compartment.html) command and required parameters to move an image to another compartment.
Copy
```
oci compute image change-compartment [OPTIONS]
```

For a complete list of CLI commands, flags, and options, see the [Command Line Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/index.html).
  * Use the [ChangeImageCompartment](https://docs.oracle.com/iaas/api/#/en/iaas/latest/Image/ChangeImageCompartment) operation to move an image to another compartment.
For information about using the API and signing requests, see [REST APIs](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm#REST_APIs) and [Security Credentials](https://docs.oracle.com/iaas/Content/General/Concepts/credentials.htm). For information about SDKs, see [Software Development Kits and Command Line Interface](https://docs.oracle.com/iaas/Content/API/Concepts/sdks.htm#Software_Development_Kits_and_Command_Line_Interface).


Was this article helpful?
YesNo

