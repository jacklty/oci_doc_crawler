Updated 2023-12-06
# Creating an Instance Configuration
On Compute Cloud@Customer, you can create an instance configuration from an existing instance (a template instance) or by entering the individual configuration settings.
Avoid entering confidential information in names and tags.
Note the following when you use a template instance to create an instance configuration:
  * The new instance configuration does not include any information from the boot volume of the template instance. For example, installed applications, binaries, and files that are on the template instance are not included in the instance configuration.
Use the following procedure to create an instance configuration that includes the custom setup from the template instance:
    1. Create a custom image from the template instance. See [Creating an Image from an Instance](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/images/creating-an-image-from-an-instance.htm#creating-an-image-from-an-instance "On Compute Cloud@Customer, you can create a custom image of a compute instance's boot disk and use that custom image to create other compute instances. Instances that you create from this image include the customizations, configuration, and software that were installed on the boot disk when you created the image.").
    2. Use the custom image to create a new instance. See [Creating an Instance](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/compute/creating-an-instance.htm#creating-an-instance "On Compute Cloud@Customer, you can create an instance using the Compute Cloud@Customer Console, CLI, and API.").
    3. Use the instance that you created in the preceding step as the template to create the instance configuration.
  * The instance configuration does not include the contents of any block volumes that are attached to the template instance.
  * Instances that are created from this new instance configuration are placed in the same compartment as the template instance.


To include block volumes or secondary VNICs in the configuration, or to specify the compartment where new instances will be created, create the instance configuration as described in [Creating an Instance Configuration by Entering Configuration Values](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/compute/creating-an-instance-configuration-by-entering-configuration-values.htm#updating-an-instance-configuration-by-entering-configuration-values "On Compute Cloud@Customer, you can create an instance configuration by entering values for individual instance configuration settings.").
Was this article helpful?
YesNo

