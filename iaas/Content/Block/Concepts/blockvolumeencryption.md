Updated 2024-02-13
# Block Volume Encryption
All block volumes and boot volumes are encrypted at-rest by Block Volume.
There is no option for unencrypted volumes at-rest. Encryption at-rest doesn't impact the performance of the volume and doesn't incur additional cost. Block Volume also provides in-transit encryption. In-transit encryption for block volumes attached to VMs is optional, and you can enable or disable it as needed for these volumes. In-transit encryption for bare metal instances is supported and enabled and you can't disable it for the following shapes:
  * BM.Standard.E3.128
  * BM.Standard.E4.128
  * BM.DenseIO.E4.128


To confirm support for other Linux-based custom images and for more information, contact [Oracle support](https://support.oracle.com/).
By default, Oracle-provided encryption keys are used for encryption. You have the option to override or specify your own keys stored in the Vault service. Block Volume uses the encryption key configured for the volume for both at-rest and in-transit encryption. For more information, see [Block Volume Encryption Keys](https://docs.oracle.com/en-us/iaas/Content/Block/Concepts/blockvolumeencryption-Encryption_Keys.htm#encryptionKeys "Block Volume encrypts resources such as block volumes, boot volumes, and volume backups by using the Advanced Encryption Standard \(AES\) algorithm with 256-bit encryption.").
## Custom Encryption
You can opt to perform your own custom encryption at the operating system level using third-party software such as devicemapper crypt (`dm-crypt`), BitLocker Drive Encryption, etc. This encryption is in addition to the standard encryption provided by Oracle for volumes. This means that volumes are double encrypted, first by the software at the operating system level, and then by Oracle using Oracle managed keys.
When you use a custom encryption mode, you incur no additional cost, but you could see a degradation in overall performance of the volume. This encryption uses host CPU cycles, and the volume performance depends on the actual shape of the Compute instance.
Was this article helpful?
YesNo

