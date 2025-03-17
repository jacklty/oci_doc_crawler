Updated 2025-02-05
# Pushing Images Using the Docker CLI
_Find out how to push images to Container Registry using the Docker CLI._
You use the Docker CLI to push images to Oracle Cloud Infrastructure Registry (also known as Container Registry).
To push an image, you first use the `docker tag` command to create a copy of the local source image as a new image (the new image is actually just a reference to the existing source image). As a name for the new image, you specify the fully qualified path to the target location in Container Registry where you want to push the image, including the name of a repository. 
For example, assume you have a local image named `acme-web-app:latest` (the image name comprising the repository name of `acme-web-app`, and the image tag of `latest`). Let's say you want to push this image to Container Registry into a repository called `project01/acme-web-app` with a version identifier of `v2.0.test`, in the Ashburn region of the acme-dev tenancy. When you use the `docker tag` command, you'd name the new image with the fully qualified path to its destination, in the format `<registry-domain>/<tenancy-namespace>/<repo-name>:<version>`. So in this case, you'd name the new image `ocir.us-ashburn-1.oci.oraclecloud.com/ansh81vru1zp/project01/acme-web-app:v2.0.test`. Subsequently, when you use the `docker push` command, the image's name ensures it is pushed to the correct destination.
Your permissions control the images you can push to Container Registry (see [Policies to Control Repository Access](https://docs.oracle.com/en-us/iaas/Content/Registry/Concepts/registrypolicyrepoaccess.htm#Policies_to_Control_Repository_Access "Find out how to set up policies to control access to repositories in Container Registry, along with some examples of common policies.")). You can push images to repositories you've created (see [Creating a Repository](https://docs.oracle.com/en-us/iaas/Content/Registry/Tasks/registrycreatingarepository.htm#top "Find out how to create a repository in Container Registry.")). You can also push images to repositories that the groups to which you belong have been granted access by appropriate identity policies. If you belong to the Administrators group, you can push images to any repository in the tenancy. 
Note that the instructions in this topic assume that the repository to which you want to push images already exists. That will usually be the case, but need not always be so (see [Creating a Repository](https://docs.oracle.com/en-us/iaas/Content/Registry/Tasks/registrycreatingarepository.htm#top "Find out how to create a repository in Container Registry.")).
**Note**
Container Registry is an [ Open Container Initiative](https://opencontainers.org/)-compliant registry. As a result, you can store any artifacts that conform to Open Container Initiative specifications, such as Docker images, manifest lists (sometimes known as multi-architecture images), and Helm charts. The instructions in this topic assume you are storing Docker images and using the Docker CLI.
To push images to Container Registry using the Docker CLI:
  1. If you already have an auth token, go to the next step. Otherwise:
    1. In the top-right corner of the Console, open the **Profile** menu, and then select **User settings** (or **My Profile** or your account name) to view the details.
    2. On the **Auth Tokens** page, select **Generate Token**.
    3. Enter a friendly description for the auth token. Avoid entering confidential information.
    4. Select **Generate Token**. The new auth token is displayed.
    5. Copy the auth token immediately to a secure location from where you can retrieve it later, because you won't see the auth token again in the Console.
    6. Close the **Generate Token** dialog.
  2. In a terminal window on the client machine running Docker, log in to Container Registry by entering `docker login <registry-domain>`, where `<registry-domain>` includes a region key or region identifier for the Container Registry region you're using. For example, `docker login ocir.us-ashburn-1.oci.oraclecloud.com`. See [Availability by Region](https://docs.oracle.com/en-us/iaas/Content/Registry/Concepts/registryprerequisites.htm#regional-availability).
  3. When prompted for a username, enter your username in the format `<tenancy-namespace>/<username>`, where `<tenancy-namespace>` is the auto-generated Object Storage namespace string of your tenancy (as shown on the **Tenancy Information** page). For example, `ansh81vru1zp/jdoe@acme.com`. If your tenancy is federated with Oracle Identity Cloud Service, use the format `<tenancy-namespace>/oracleidentitycloudservice/<username>`.
  4. When prompted for a password, enter the auth token you copied earlier.
  5. Find the image on the client machine that you want to push:
    1. In a terminal window on your client machine, enter `docker images` to list the available images.
For example:
Copy
```
  
$ docker images
REPOSITORY    TAG       IMAGE ID   CREATED    SIZE
acme-web-app   latest      8e0506e14874 2 hours ago  162.6 MB
acme-web-app   v1.0       7d9495d03763 2 hours ago  162.6 MB
<none>      <none>      6ebd328f833d 5 hours ago  162.6 MB
hello-world    latest      80b84820d442 5 weeks ago  890 B
					
```

    2. Find the local image on the client machine that you want to push to Container Registry.
In the output of the `docker images` command, look for the specific image that you want to push. You'll need to uniquely identify this image later, in one of the following ways:
       * Using its id.
       * Using its image name (its repository name and image tag separated by a colon).
For example, on the client machine you might have an acme-web-app image. In the output of the `docker                 images` command, look for the specific acme-web-app image that you want to push. You can uniquely identify that particular image in one of the following ways:
       * Using its id (for example, `8e0506e14874`).
       * Using its image name (its repository name and image tag separated by a colon, for example `acme-web-app:latest`).
    3. Use the `docker tag` command to create a copy of the original image as a new image (the new image is actually just a reference to the existing original image). As a name (or tag) for the new image, you specify the fully qualified path to the target location in Container Registry where you want to push the image, by entering:
Command
CopyTry It
```
docker tag <image-identifier> <target-tag>
```

where:
       * `<image-identifier>` uniquely identifies the original image, either using the image's id (for example, `8e0506e14874`), or the image's name (its original repository name and image tag separated by a colon, for example `acme-web-app:latest`).
       * `<target-tag>` is the fully qualified path to the target location in Container Registry where you want to push the image, in the format `<registry-domain>/<tenancy-namespace>/<repo-name>:<version>` where:
         * `<registry-domain>` includes the region key or region identifier for the Container Registry region you're using.. For example, `ocir.us-ashburn-1.oci.oraclecloud.com`. See [registry domain](https://docs.oracle.com/en-us/iaas/Content/Registry/Concepts/registryconcepts.htm#Terminology_Summary__registry-domain).
         * `<tenancy-namespace>` is the auto-generated Object Storage namespace string of the tenancy that owns the repository to which you want to push the image (as shown on the **Tenancy Information** page). For example, the namespace of the acme-dev tenancy might be `ansh81vru1zp`. Note that for some older tenancies, the namespace string might be the same as the tenancy name in all lower-case letters (for example, `acme-dev`). Note also that your user must have access to the tenancy.
         * `<repo-name>` is the name of the target repository to which you want to push the image (for example, `project01/acme-web-app`). Note that you'll usually specify a repository that already exists, but that need not always be the case (see [Creating a Repository](https://docs.oracle.com/en-us/iaas/Content/Registry/Tasks/registrycreatingarepository.htm#top "Find out how to create a repository in Container Registry.")).
         * `<version>` is a version identifier you want to give the image in Container Registry (for example, `v2.0.test`).
For example, combining the previous examples, you might enter:
Command
CopyTry It
```
docker tag 8e0506e14874 ocir.us-ashburn-1.oci.oraclecloud.com/ansh81vru1zp/project01/acme-web-app:v2.0.test
```

  6. Confirm that the Docker image has been correctly tagged on the client machine by entering `docker images` and verifying that the list of images includes an image with the tag you specified. 
For example:
Copy
```

$ docker images
REPOSITORY                                TAG          IMAGE ID   CREATED    SIZE
ocir.us-ashburn-1.oci.oraclecloud.com/ansh81vru1zp/project01/acme-web-app v2.0.test       8e0506e14874 1 minute ago 162.6 MB
acme-web-app                               latest        8e0506e14874 2 hours ago  162.6 MB
acme-web-app                               v1.0         7d9495d03763 2 hours ago  162.6 MB
<none>                                  <none>        6ebd328f833d 5 hours ago  162.6 MB
hello-world                                latest        80b84820d442 5 weeks ago  890 B
					
```

  7. Push the Docker image from the client machine to Container Registry by entering:
Command
CopyTry It
```
docker push <target-tag>
```

where `<target-tag>` is in the format `<registry-domain>/<tenancy-namespace>/<repo-name>:<version>` where:
     * `<registry-domain>` includes the region key or region identifier for the Container Registry region you're using. For example, `ocir.us-ashburn-1.oci.oraclecloud.com`. See [registry domain](https://docs.oracle.com/en-us/iaas/Content/Registry/Concepts/registryconcepts.htm#Terminology_Summary__registry-domain).
     * `<tenancy-namespace>` is the auto-generated Object Storage namespace string of the tenancy that owns the repository to which you want to push the image (as shown on the **Tenancy Information** page). For example, the namespace of the acme-dev tenancy might be `ansh81vru1zp`. Note that for some older tenancies, the namespace string might be the same as the tenancy name in all lower-case letters (for example, `acme-dev`). Note also that your user must have access to the tenancy.
     * `<repo-name>` is the name of the target repository to which you want to push the image (for example, `project01/acme-web-app`). Note that you'll usually specify a repository that already exists, but that need not always be the case (see [Creating a Repository](https://docs.oracle.com/en-us/iaas/Content/Registry/Tasks/registrycreatingarepository.htm#top "Find out how to create a repository in Container Registry.")).
     * `<version>` is the version identifier you want to give the image in Container Registry (for example, `v2.0.test`).
For example:
Command
CopyTry It
```
docker push ocir.us-ashburn-1.oci.oraclecloud.com/ansh81vru1zp/project01/acme-web-app:v2.0.test
```



Was this article helpful?
YesNo

