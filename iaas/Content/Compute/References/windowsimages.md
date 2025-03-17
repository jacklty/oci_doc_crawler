Updated 2025-02-11
# Creating Windows Custom Images
You can create a Windows custom image of a bare metal or virtual machine (VM) instance's boot disk and use it to launch other instances. Instances you launch from your image include the customizations, configuration, and software installed when you created the image. For information about custom images, see [Managing Custom Images](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/managingcustomimages.htm#Managing_Custom_Images "You can create a custom image of an instance's boot disk and use it to launch other instances. Instances you launch from your image include the customizations, configuration, and software installed when you created the image."). For information about the licensing requirements for Windows images, see [Microsoft Licensing on Oracle Cloud Infrastructure](https://docs.oracle.com/en-us/iaas/Content/Compute/References/microsoftlicensing.htm#Microsoft_Licensing_on_Oracle_Cloud_Infrastructure).
Windows supports two kinds of images: generalized and specialized. Generalized images are images that have been cleaned of instance-specific information. Specialized images are point-in-time snapshots of the boot disk of a running instance, and are useful for creating backups of an instance. Oracle Cloud Infrastructure supports bare metal and VM instances launched from both generalized and specialized custom Windows images.
**Generalized images**
A generalized image has a generalized OS disk, cleaned of computer-specific information. The images are generalized using Sysprep. Generalized images can be useful in scenarios such as quickly scaling an environment. Generalized images can be configured to preserve the existing `opc` user's account, including the password, at the time the image is created, or configured to recreate the `opc` user account, including generating a new, random password that you retrieve using the API. For background information, see [Sysprep (Generalize) a Windows installation](https://docs.microsoft.com/windows-hardware/manufacture/desktop/sysprep--generalize--a-windows-installation).
**Specialized images**
A specialized image has an OS disk that is already fully installed, and is essentially a copy of the original bare metal or VM instance. Specialized images are intended to be used for backups so that you can recover from a failure. Specialized images are useful when you are testing a task and may need to roll back to known good configuration. Specialized images are not recommended for cloning multiple identical bare metal instances or VMs in the same network because of issues with multiple computers having the same computer name and ID. When creating a specialized image, you must remember the `opc` user's password; a new password is not generated when the instance launches, and it cannot be retrieved from the console or API.
## Creating a Generalized Image 🔗 
**Caution**
  * Creating a generalized image from an instance will render the instance non-functional, so you should first create a custom image from the instance, and then create a new instance from the custom image. The following steps describe how to do this. This is the instance that you'll generalize. Alternatively, you can make a backup image of the instance that you can use to launch a replacement instance if needed.
  * If you upgrade to PowerShell 5.0/WMF 5.0, you might encounter an issue where **Sysprep** fails, which prevents the image generalization process from completing. If this occurs, you might not be able to log into instances launched from the custom image. For more information and steps to work around the issue, see [Unable to log in to instance launched from new generalized Windows custom image](https://docs.oracle.com/en-us/iaas/Content/Compute/known-issues.htm#sysprepfails).


  1. [Connect to the instance](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/connect-to-windows-instance.htm#top "You connect to a Windows instance by using a Remote Desktop connection. Most Windows systems include a Remote Desktop client by default.") by using a Remote Desktop connection and shut down the instance from the operating system.
  2. Create the new image using [Creating Custom Images](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/custom-images-create.htm#listing-custom-images "Create a Compute custom image in an Oracle Cloud Infrastructure compartment.").
  3. Create an instance from the new image using [launching an instance from a custom image](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/managingcustomimages.htm#Managing_Custom_Images__console-custom-image-tasks).
  4. [Connect to the new instance](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/connect-to-windows-instance.htm#top "You connect to a Windows instance by using a Remote Desktop connection. Most Windows systems include a Remote Desktop client by default.") using a Remote Desktop client.
  5. Download the following Windows Sysprep generalize file to the instance:
[oracle-cloud_windows-server_generalize_2022-08-24.SED.EXE](https://docs.oracle.com/iaas/Content/Resources/Assets/oracle-cloud_windows-server_generalize_2022-08-24.SED.EXE)
The file works for all shapes and applies to all Windows Server platform image versions.
  6. Right-click the file, and then click **Run as administrator**.
  7. Extract the files to **C:\Windows\Panther**. The following files are extracted into the Panther folder for all Windows Server versions:
     * Generalize.cmd
     * Specialize.cmd
     * unattend.xml
     * Post-Generalize.ps1
  8. Optional: If you want to preserve the `opc` user account, edit `C:\Program Files\bmcs\imageType.json` and change the `imageType`setting to `custom`. A new password is not created and the password is not retrievable from the console or API.
If you want to configure the generalized image to recreate the `opc` user account when a new instance is launched from the image, leave the `imageType` setting defaulted to `general`. You can retrieve the new account's password through the API using [GetInstanceDefaultCredentials](https://docs.oracle.com/iaas/api/#/en/iaas/latest/InstanceCredentials/GetInstanceDefaultCredentials).
  9. Right-click **Generalize.cmd** , and then click **Run as administrator**. Keep in mind the following outcomes of running this command:
     * Your connection to the Remote Desktop client might immediately be turned off and you will be signed out of the instance. If this does not occur, you should log out of the instance yourself.
     * Because `sysprep generalize` turns off Remote Desktop, you won't be able to sign in to the instance again.
     * Creating a generalized image essentially destroys the instance's functionality.
You should wait for a few minutes before proceeding to the following step to ensure the generalization process has completed.
  10. Create the new image using [Creating Custom Images](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/custom-images-create.htm#listing-custom-images "Create a Compute custom image in an Oracle Cloud Infrastructure compartment.").
  11. After you create an image from an instance that has been generalized, we recommend that you terminate the instance. Although it might appear to be running, it won't be fully operable.


## Creating a Specialized Image 🔗 
**Important** When creating a specialized image, you must remember the `opc` user's password. It cannot be retrieved from the Console or API.
You create a specialized image the same way you create other custom images. For steps, see [Managing Custom Images](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/managingcustomimages.htm#Managing_Custom_Images "You can create a custom image of an instance's boot disk and use it to launch other instances. Instances you launch from your image include the customizations, configuration, and software installed when you created the image.").
Was this article helpful?
YesNo

