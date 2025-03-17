Updated 2024-08-06
# Using Free-Form Tags for Extended Functionality
On Compute Cloud@Customer, you can use free-form tags to extend the functionality of some services.
Use of these tags counts against your tag limit.
The following list describes the special purpose free-form tags:
**Note**
Don't use these tag names for other purposes.
  * `**PCA_no_lm**`**– Control instance live migration.**
Use this tag to instruct the Compute service not to live migrate an instance. The value can be either `True` or `False`.
By default, an instance can be live migrated, such as when you need to evacuate all running instances from a compute node. Live migration can be a problem for some instances. For example, live migration must not be used for instances in a Microsoft Windows cluster. To prevent an instance from being live migrated, set this tag to `True` on the instance.
Specify this tag in the Tagging section of the Create Instance or Edit `**_instance_name_**`dialog, in the`oci compute instance launch` or `oci compute instance             update` command, or using the API.
The following is an example option for the `oci compute instance             launch` command:
```
--freeform-tags '{"PCA_no_lm": "True"}'
```

Setting this tag to True on an instance doesn't prevent the instance from being moved when you change the fault domain. Changing the fault domain isn't a live migration. When you change the fault domain of an instance, the instance is stopped, moved, and restarted.
  * `**PCA_blocksize**`**– Create new volumes with a specific disk block size.**
Use this tag to change the LUN _block size_ used by the underlying storage when a block volume is created. Note – Using this tag doesn't apply to the size of the block volume.
The default block size is 8192 bytes. To specify a different block size, specify the `PCA_blocksize` tag in the Tagging section of the Create Block Volume dialog, in the `oci bv volume create` command, or using the API. Valid values are a power of 2 between 512 and 1M bytes, specified as a string and fully expanded.
The following is an example option for the `oci bv volume create` command:
```
--freeform-tags '{"PCA_blocksize": "65536"}'
```

The block size can't be changed after the volume has been created.


Was this article helpful?
YesNo

