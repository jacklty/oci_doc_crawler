Updated 2025-02-05
# Container Registry Concepts
_Find out about the key concepts you need to understand before using Container Registry._
This topic describes key concepts you need to understand when using Oracle Cloud Infrastructure Registry (also known as Container Registry).
## Images 🔗 
Container Registry is an [ Open Container Initiative](https://opencontainers.org/)-compliant registry. As a result, you can store any artifacts that conform to Open Container Initiative specifications, such as Docker images, manifest lists (sometimes known as multi-architecture images), and Helm charts. The instructions in this documentation assume you are storing and retrieving Docker container images using the Docker CLI. Docker container images are commonly referred to as Docker images, or simply as images.
A Docker image is a read-only template with instructions for creating a Docker container. A Docker image holds the application that you want Docker to run as a container, along with any dependencies. To create a Docker image, you first create a Dockerfile to describe that application. You then build the Docker image from the Dockerfile. Having created a Docker image, you store it in a Docker registry such as Container Registry.
Typically, you'll group together different versions of the same Docker image into a named repository in the registry (for example, into a repository named 'project01/acme-web-app'), and give each image version a different identifier (for example, '4.6.3'). So each image in the registry is uniquely identified by the combination of its repository name and its version identifier (for example, 'project01/acme-web-app:4.6.3', 'project01/acme-web-app:4.6.4', and so on).
## Repositories 🔗 
A repository is a meaningfully named collection of related images grouped together for convenience in Container Registry. Typically, you'll group together different versions of the same source image into the same repository (for example, into a repository named `project01/acme-web-app`), and give each image version a different identifier (for example, `4.6.3`). So each image in the registry is uniquely identified by the combination of its repository name and its version identifier (for example,` project01/acme-web-app:4.6.3`, `project01/acme-web-app:4.6.4`, and so on).
Repositories can be private or public. Any user with internet access and knowledge of the appropriate URL can pull images from a public repository in Container Registry. 
A repository exists within a particular tenancy, region, and compartment. When referring to the tenancy that owns a repository, you specify the tenancy's namespace. The tenancy namespace is an auto-generated random string of alphanumeric characters. For example, the namespace of the `acme-dev` tenancy might be `ansh81vru1zp`. Note that for some older tenancies, the namespace string might be the same as the tenancy name in all lower-case letters (for example, `acme-dev`). To find out the tenancy namespace of the current tenancy, open the **Profile** menu and select **Tenancy**. 
You must belong to the tenancy's Administrators group or have been granted the REPOSITORY_MANAGE permission to:
  * create a new public repository
  * change an existing repository into a public repository
  * change an existing public repository into a private repository


If you make a repository private, you (along with users belonging to the tenancy's Administrators group) will be able to perform any operation on the repository. You can use identity policies to allow other users to perform other operations on repositories (both public and private) that you create. 
Usually, before pushing any images, you'll create an empty repository in a compartment and give the repository a name (for example, `project01/acme-web-app`). If you belong to the tenancy's Administrators group or have been granted the REPOSITORY_MANAGE permission, you can also specify whether the repository is to be private or public (see [Policies to Control Repository Access](https://docs.oracle.com/en-us/iaas/Content/Registry/Concepts/registrypolicyrepoaccess.htm#Policies_to_Control_Repository_Access "Find out how to set up policies to control access to repositories in Container Registry, along with some examples of common policies.")). Having created the repository, images you subsequently push to Container Registry that include the repository name are pushed to that repository. 
For example, for convenience you might want to group together multiple versions of an image in the acme-dev tenancy in the Ashburn region into the repository called `project01/acme-web-app`. First, you create the `project01/acme-web-app` repository. Then, you include the name of the repository when you push the image, in the format `<registry-domain>/<tenancy-namespace>/<repo-name>:<version>`. For example, `ocir.us-ashburn-1.oci.oraclecloud.com/ansh81vru1zp/project01/acme-web-app:4.6.3`.
Note that creating an empty repository in advance of pushing an image is almost certainly going to be your normal workflow. And if you're only authorized to manage repositories in compartments and not in the tenancy's root compartment, you'll always have to create a repository before pushing an image. However, if you're in the unusual position of mostly intending to push images to the root compartment, creating an empty repository in advance is not strictly necessary. For more information, see [Creating a Repository](https://docs.oracle.com/en-us/iaas/Content/Registry/Tasks/registrycreatingarepository.htm#top "Find out how to create a repository in Container Registry.").
## Terminology Summary 🔗 
When working with repositories in Container Registry, you'll find it helpful to have a clear understanding of the following terms and how they relate to each other. 

repository path
    
A repository path (sometimes referred to as `<repo-path>` in this documentation) is the fully-qualified path to a repository in Container Registry. A repository path has the format `<registry-domain>/<tenancy-namespace>/<repo-name>`.
For example:
  * `ocir.us-ashburn-1.oci.oraclecloud.com/ansh81vru1zp/project01/acme-web-app`
  * `iad.ocir.io/ansh81vru1zp/project01/acme-web-app`
  * `us-phoenix-1.ocir.io/cbujx0t3wa3r/my-hello-app`



registry domain
    
A Container Registry registry domain includes a Container Registry region key or region identifier. A Container Registry registry domain has one of the following formats:
  * (recommended) `ocir.<region-identifier>.oci.oraclecloud.com`
  * `<region-key>.ocir.io` (OC1 realms only)
  * `<region-identifier>.ocir.io` (OC1 realms only)


For example:
  * `ocir.us-ashburn-1.oci.oraclecloud.com`
  * `iad.ocir.io/ansh81vru1zp`
  * `us-phoenix-1.ocir.io`


For the list of region identifiers and region keys, see [Availability by Region](https://docs.oracle.com/en-us/iaas/Content/Registry/Concepts/registryprerequisites.htm#regional-availability). 

region identifier
    
A region identifier (sometimes referred to as `<region-identifier>` in this documentation) identifies the Container Registry region you're using.
For example:
  * `us-ashburn-1`
  * `us-phoenix-1`


For the list of region identifiers, see [Availability by Region](https://docs.oracle.com/en-us/iaas/Content/Registry/Concepts/registryprerequisites.htm#regional-availability). 

region key
    
A region key (sometimes referred to as `<region-key>` in this documentation) identifies the Container Registry region you're using.
For example:
  * `iad`
  * `phx`


For the list of region keys, see [Availability by Region](https://docs.oracle.com/en-us/iaas/Content/Registry/Concepts/registryprerequisites.htm#regional-availability). 

tenancy namespace
    
A tenancy namespace (sometimes referred to as `<tenancy-namespace>` in this documentation) is an auto-generated, random, and immutable string of alphanumeric characters. For example, the namespace of the `acme-dev` tenancy might be `ansh81vru1zp`. 
Note that for some older tenancies, the namespace string might be the same as the tenancy name in all lower-case letters (for example, `acme-dev`). To find out the tenancy namespace of the current tenancy, open the **Profile** menu and select **Tenancy**. The tenancy namespace is shown in the **Object Storage Namespace** field. 

repository name
    
A repository name (sometimes referred to as `<repo-name>` in this documentation) is the name of a repository in Container Registry, to and from which you can push and pull images. Repository names can include one or more slash characters, and are unique across all compartments in the entire tenancy.
For example:
  * `project01/acme-web-app`
  * `project01/my-test-app`
  * `my-hello-app`
  * `project01/acme-web-app/component1`
  * `project01/acme-web-app/component2`
  * `project01/acme-web-app/component1/subcomponent1`


Note that although a repository name can include slash characters, the slash does not represent a hierarchical directory structure. It is simply one character in a string of characters. As a convenience, you might choose to start the names of several different repositories with the same string, perhaps ending in a slash (such as `project01/`). Such a string is sometimes called a 'repository name prefix'. But a repository named `project01/acme-web-app` need not have any relationship with a repository named `project01/my-test-app`. Using the same repository name prefix for some repositories simply makes it easier to organize and control access to them in Container Registry, which can contain many other repositories. 

registry identifier
    
A registry identifier includes a Container Registry registry domain and a tenancy namespace, in the format `<registry-domain>/<tenancy-namespace>`
For example:
  * `ocir.us-ashburn-1.oci.oraclecloud.com/ansh81vru1zp`
  * `iad.ocir.io/ansh81vru1zp/project01`
  * `us-phoenix-1.ocir.io/cbujx0t3wa3r`



image path
    
An image path is the fully-qualified path to a particular image in a registry. It extends the repository path by adding the version identifier associated with the image. An image path has the format `<registry-domain>/<tenancy-namespace>/<repo-name>:<version>`
For example:
  * `ocir.us-ashburn-1.oci.oraclecloud.com/ansh81vru1zp/project01/acme-web-app:v2.0.test`
  * `iad.ocir.io/ansh81vru1zp/project01/acme-web-app:v2.0.test`
  * `us-phoenix-1.ocir.io/cbujx0t3wa3r/my-hello-app:latest`



version identifier
    
A version identifier (sometimes referred to as `<version>` in this documentation) is a string used to refer to a particular image version in a known repository. For example:
  * `4.6.3`
  * `4.6.4`
  * `v2.0.test`



image name
    
The term 'image name' is sometimes used as a short-hand way to refer to a particular image in a particular repository. In this context, an image name has the structure:
```
<repo-name>:<version>
```

For example:
  * `project01/acme-web-app`:`4.6.3`
  * `project01/acme-web-app`:`4.6.4`
  * `my-hello-app:latest`


Was this article helpful?
YesNo

