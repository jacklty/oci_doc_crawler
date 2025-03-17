Updated 2024-12-16
# Managing Boot Volumes
On Oracle Cloud Infrastructure, when you launch an instance, a new boot volume for the instance is created in the same compartment and attached to the instance. 
You can accept the image's default boot volume size, or you can specify a larger size, up to 16 TB. If you specify a size smaller than the default boot volume size, your request is ignored and the boot volume is the default size.
The boot volume is associated with the instance until you terminate the instance. When you terminate the instance, you can preserve and reuse the boot volume and its data.
Boot volumes are encrypted by default.
You can list, detach, reattach, back up, clone, and delete boot volumes.
For Linux-based images, the custom boot volume size must be at least the image's default boot volume size or 50 GB, whichever is larger. 
For Microsoft Windows-based images, the custom boot volume size must be at least the image's default boot volume size or 256 GB, whichever is larger. The minimum size requirement for Microsoft Windows images is to ensure that enough space is available for patches and updates.
If you specify a custom boot volume size, extend the volume to take advantage of the larger size.
Was this article helpful?
YesNo

