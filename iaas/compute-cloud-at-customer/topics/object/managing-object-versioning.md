Updated 2023-08-15
# Managing Object Versioning
On Compute Cloud@Customer, object versioning provides data protection against accidental or malicious object update, overwrite, or deletion.
Object versioning is enabled at the bucket level. Versioning directs Object Storage to automatically create an object version each time one of these actions takes place:
  * A new object is uploaded.
  * An existing object is overwritten.
  * When an object is deleted.


You can enable object versioning at bucket creation time or later.
A bucket that is versioning-enabled can have many versions of an object. There is always one latest version of the object and zero or more previous versions.
## Scope and Constraints 🔗 
  * Versioning can be enabled on a bucket in Object Storage.
  * You can rename the latest version of an object, but you can't rename a previous object version. Renaming an object creates a new object.


## Interaction Between Versioning and Other Object Storage Features 🔗 
This section describes some key things you need to know about the interaction between object versioning and other Object Storage features. 
**Copying Objects**
If you copy the latest version of an object to a different bucket, only the object is copied. None of the object's previous versions are copied. You can copy a previous version of an object to another bucket, but that action creates either the latest version of a new object or a new object version in the destination bucket.
**Retention Rules**
  * You can't add retention rules to a bucket that has versioning enabled.
  * You can't enable versioning on a bucket with active retention rules.
  * You can add retention rules to bucket that has versioning suspended. However, you can't resume versioning with active retention rules.


Was this article helpful?
YesNo

