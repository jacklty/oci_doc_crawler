Updated 2025-01-15
# Enforcing the Use of Signed Images from Registry
_Find out how to enforce the use of signed images from Oracle Cloud Infrastructure Registry when deploying applications to a cluster you've created using Kubernetes Engine (OKE)._
For compliance and security reasons, system administrators often want to deploy software into a production system only when they are satisfied that:
  * the software comes from a trusted source
  * the software has not been modified since it was published, compromising its integrity


To meet these requirements, you can sign images stored in Oracle Cloud Infrastructure Registry. Signed images provide a way to verify both the source of an image and its integrity. Oracle Cloud Infrastructure Registry enables users or systems to push images to the registry and then sign them creating an image signature. An image signature associates an image with a master encryption key obtained from Oracle Cloud Infrastructure Vault. 
Users or systems pulling a signed image from Oracle Cloud Infrastructure Registry can be confident both that the source of the image is trusted, and that the image's integrity has not been compromised. For more information, see [Signing Images for Security](https://docs.oracle.com/iaas/Content/Registry/Tasks/registrysigningimages_topic.htm).
To further enhance security, you can configure clusters you've created with Kubernetes Engine to only allow the deployment of images from Oracle Cloud Infrastructure Registry that have been signed by particular master encryption keys. At a high level, these are the steps to follow:
  * Sign images in Oracle Cloud Infrastructure Registry with image signatures that use master encryption keys from Oracle Cloud Infrastructure Vault (see [Signing Images for Security](https://docs.oracle.com/iaas/Content/Registry/Tasks/registrysigningimages_topic.htm)).
  * Create an image verification policy for a cluster that specifies which master encryption key(s) must have been used to sign images.
  * Enable the cluster to use the image verification policy to enforce the use of suitably signed images. 


Note the following:
  * An image in Oracle Cloud Infrastructure Registry can be signed using multiple signatures, each associated with a different master encryption key. Provided a cluster's image verification policy includes at least one of the master encryption keys, the cluster allows the image to be pulled from Oracle Cloud Infrastructure Registry.
  * You can specify up to five master encryption keys in a cluster's image verification policy.
  * If you enable a cluster to use its image verification policy but do not specify the master encryption key(s) that must have been used to sign an image:
    * any signed image can be pulled from Oracle Cloud Infrastructure Registry, regardless of the master encryption keys used to sign it
    * any unsigned image can be pulled from Oracle Cloud Infrastructure Registry
  * If you enable a cluster to use its image verification policy but Kubernetes Engine cannot connect to Oracle Cloud Infrastructure Registry, no images can be pulled from Oracle Cloud Infrastructure Registry.
  * An image in Oracle Cloud Infrastructure Registry is identified by repository, name, and a tag. In addition, each version of an image is given a unique alphanumeric digest. If you enable a cluster to use its image verification policy, in pod specs (and other manifest files) you must reference an image using the image digest rather than the image tag. For example, use:```
image: phx.ocir.io/ansh81vru1zp/project01/ngnix-lb@sha256:ee44b399d______49c775b
```

rather than simply:
```
image: phx.ocir.io/ansh81vru1zp/project01/ngnix-lb:latest
```

Note that you have to modify all existing pod specs (and other manifest files that reference images) to use image digests rather than image tags.
  * Having enabled a cluster to use its image verification policy, you might later have an urgent requirement for a particular pod to pull an image that violates the policy. In this case, you can add the `oracle.image-policy.k8s.io/break-glass: "true"` annotation to the pod spec. Having added the annotation to the pod spec, the pod can pull any signed and unsigned images from Oracle Cloud Infrastructure Registry, regardless of the cluster's image verification policy.
  * A cluster enforces the use of images signed by master encryption keys included in its image verification policy, provided:
    * images are pulled from Oracle Cloud Infrastructure Registry (rather than from other registries)
    * images are signed using master encryption keys obtained from Oracle Cloud Infrastructure Vault


## Required IAM Policies for Enforcing the Use of Signed Images
To enable clusters to include master encryption keys in image verification policies, you must give clusters permission to use keys from Oracle Cloud Infrastructure Vault. For example, to grant this permission to a particular cluster in the tenancy:
```
Allow any-user to use keys in tenancy where request.user.id=<CLUSTER_OCID>
```

To enable clusters to pull signed images from Oracle Cloud Infrastructure Registry, you must give clusters permission to access repositories in Oracle Cloud Infrastructure Registry. For example, to grant this permission to a particular cluster in the tenancy:
```
Allow any-user to read repos in tenancy where request.user.id=<CLUSTER_OCID>
```

For examples of how to create more granular policies, see [Encrypting Kubernetes Secrets at Rest in Etcd](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengencryptingdata.htm#Encrypting_Kubernetes_Secrets_at_Rest_in_Etcd "Find out how to encrypt configuration data stored as Kubernetes secrets in etcd when using Kubernetes Engine \(OKE\).").
## Enforcing the Use of Signed Images
To enable a cluster to allow applications to pull only those images from Oracle Cloud Infrastructure Registry that have been signed using specific master encryption keys:
  1. If you don't already have access to an RSA asymmetric key in Oracle Cloud Infrastructure Vault, create one or more master encryption keys as RSA asymmetric keys. See [Creating a Master Encryption Key](https://docs.oracle.com/iaas/Content/KeyManagement/Tasks/managingkeys_topic-To_create_a_new_key.htm).
  2. Define an image verification policy for the cluster and specify at least one master encryption key that must have been used to sign images:
    1. Open the **navigation menu** and select **Developer Services**. Under **Containers & Artifacts**, select **Kubernetes Clusters (OKE)**.
    2. Choose a **Compartment** you have permission to work in.
    3. On the **Cluster List** page, select the cluster for which you want to define an image verification policy.
    4. Under **Resources** , click **Image Verification**.
    5. Click **Edit Image Verification**.
    6. Select **Enable image verification policies on this cluster** to enable the cluster to use the image verification policy you define. 
    7. Select a master encryption key in Oracle Cloud Infrastructure Vault that must have been used to sign images.
If you want to allow images signed by different keys to be pulled, you can specify multiple master encryption keys. 
Note that if you do specify multiple master encryption keys, an image need only be signed by one of those keys. An image does not have to be signed by all of the master encryption keys you specify. You can specify up to five master encryption keys in the cluster's image verification policy.
    8. Click **Save Image Verification Settings**.
From now on, the cluster allows applications to pull only those images from Oracle Cloud Infrastructure Registry that have been signed using master encryption keys included in the image verification policy. Attempts to pull disallowed images are recorded in application logs (see [Viewing Application Logs on Managed Nodes and Self-Managed Nodes](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengviewingworkernodelogs.htm#Viewing_Worker_Node_Logs "Find out how to view the logs of applications running on managed nodes and self-managed nodes in a Kubernetes cluster you've created using Kubernetes Engine \(OKE\).")).
  3. Sign the images that you want the cluster to allow, using image signatures that associate the images with one or more of the master encryption keys in the image verification policy you've defined. See [Signing Images for Security](https://docs.oracle.com/iaas/Content/Registry/Tasks/registrysigningimages_topic.htm).
  4. (optional) To deploy an application that pulls a signed image from Oracle Cloud Infrastructure Registry, follow the steps in [Pulling Images from Registry during Deployment](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengpullingimagesfromocir.htm#Pulling_Images_from_Registry_during_Deployment "Find out how to create a Docker registry secret, and how to specify the image to pull from Oracle Cloud Infrastructure Registry \(along with the Docker secret to use\) during deployment of an application to a cluster you've created using Kubernetes Engine \(OKE\).") and specify the image in the application's manifest file.


Was this article helpful?
YesNo

