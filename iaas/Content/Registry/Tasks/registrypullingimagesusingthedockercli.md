Updated 2025-02-05
# Pulling Images Using the Docker CLI
_Find out how to pull images from Container Registry using the Docker CLI._
You use the Docker CLI to pull images from Oracle Cloud Infrastructure Registry (also known as Container Registry).
Your permissions control the images you can pull from Container Registry (see [Policies to Control Repository Access](https://docs.oracle.com/en-us/iaas/Content/Registry/Concepts/registrypolicyrepoaccess.htm#Policies_to_Control_Repository_Access "Find out how to set up policies to control access to repositories in Container Registry, along with some examples of common policies.")). You can pull images from repositories you've created, from public repositories, and from repositories that the groups to which you belong have been granted access by identity policies. If you belong to the Administrators group, you can pull images from any repository in the tenancy.
**Note**
Container Registry is an [ Open Container Initiative](https://opencontainers.org/)-compliant registry. As a result, you can store any artifacts that conform to Open Container Initiative specifications, such as Docker images, manifest lists (sometimes known as multi-architecture images), and Helm charts. The instructions in this topic assume you are storing Docker images and using the Docker CLI.
To pull images from Container Registry using the Docker CLI:
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
  5. Pull the Docker image from Container Registry to the client machine by entering:
Command
CopyTry It
```
docker pull <registry-domain>/<tenancy-namespace>/<repo-name>:<version>
```

where:
     * `<registry-domain>` includes the region key or region identifier for the Container Registry region you're using. For example, `ocir.us-ashburn-1.oci.oraclecloud.com`. See [registry domain](https://docs.oracle.com/en-us/iaas/Content/Registry/Concepts/registryconcepts.htm#Terminology_Summary__registry-domain).
     * `<tenancy-namespace>` is the auto-generated Object Storage namespace string of the tenancy that owns the repository from which you want to pull the image (as shown on the **Tenancy Information** page). For example, the namespace of the acme-dev tenancy might be `ansh81vru1zp`. Note that for some older tenancies, the namespace string might be the same as the tenancy name in all lower-case letters (for example, `acme-dev`). Note also that your user must have access to the tenancy.
     * `<repo-name>` is the name of a repository from which you want to pull the image (for example, `project01/acme-web-app`). Note that your user must have access to the repository (see [Repositories](https://docs.oracle.com/en-us/iaas/Content/Registry/Concepts/registryconcepts.htm#About_Repositories)).
     * `<version>` is the version identifier of the image that you want to pull from Container Registry (for example, `v2.0.test`).
For example:
Command
CopyTry It
```
docker pull ocir.us-ashburn-1.oci.oraclecloud.com/ansh81vru1zp/project01/acme-web-app:v2.0.test
```

Note that if you don't specify a `<version>` in the `docker pull` command, Docker pulls the image that has the `latest` version identifier.
  6. Confirm that the image has been pulled from Container Registry by entering `docker images` and verifying that the list of images on the client machine now includes the image you just pulled.
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



Was this article helpful?
YesNo

