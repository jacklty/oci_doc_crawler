Updated 2025-01-10
# Pulling Images from Container Registry during Kubernetes Deployment
_Find out how to create a Docker registry secret. Also find out how to specify the image to pull from Container Registry (along with the Docker secret to use) during deployment of an application to a cluster._
During the deployment of an application to a Kubernetes cluster, you'll typically want one or more images to be pulled from a Docker registry. In the application's manifest file you specify the images to pull, the registry to pull them from, and the credentials to use when pulling the images. The manifest file is commonly also referred to as a pod spec, or as a deployment.yaml file (although other filenames are allowed).
If you want the application to pull images that reside in Oracle Cloud Infrastructure Registry (also known as Container Registry), you have to perform two steps:
  * You have to use kubectl to create a Docker registry secret. The secret contains the Oracle Cloud Infrastructure credentials to use when pulling the image. When creating secrets, Oracle strongly recommends you use the latest version of kubectl (see the [kubectl documentation](https://kubernetes.io/docs/tasks/tools/install-kubectl/)).
  * You have to specify the image to pull from Container Registry, including the repository location and the Docker registry secret to use, in the application's manifest file.


**Note** Container Registry is an [ Open Container Initiative](https://opencontainers.org/)-compliant registry. As a result, you can store any artifacts that conform to Open Container Initiative specifications, such as Docker images, manifest lists (sometimes known as multi-architecture images), and Helm charts. The instructions in this topic assume you are storing Docker images and using the Docker CLI.
To create a Docker registry secret:
  1. If you haven't already done so, follow the steps to set up the cluster's kubeconfig configuration file and (if necessary) set the KUBECONFIG environment variable to point to the file. Note that you must set up your own kubeconfig file. You cannot access a cluster using a kubeconfig file that a different user set up. See [Setting up Cluster Access](https://docs.oracle.com/iaas/Content/ContEng/Tasks/contengdownloadkubeconfigfile.htm). 
  2. In a terminal window, enter:
Command
CopyTry It
```
kubectl create secret docker-registry <secret-name> --docker-server=<registry-domain> --docker-username=<tenancy-namespace>/<oci-username> --docker-password='<oci-auth-token>' --docker-email=<email-address>
```

where:
     * `<secret-name>` is a name of your choice, that you will use in the manifest file to refer to the secret . For example, `ocirsecret`
     * `<registry-domain>` includes a region key or region identifier for the Container Registry region you're using. For example, `ocir.us-ashburn-1.oci.oraclecloud.com`. See [registry domain](https://docs.oracle.com/en-us/iaas/Content/Registry/Concepts/registryconcepts.htm#Terminology_Summary__registry-domain).
     * `<tenancy-namespace>` is the auto-generated Object Storage namespace string of the tenancy containing the repository from which the application is to pull the image (as shown on the **Tenancy Information** page). For example, the namespace of the acme-dev tenancy might be `ansh81vru1zp`. Note that for some older tenancies, the namespace string might be the same as the tenancy name in all lower-case letters (for example, `acme-dev`).
     * `<oci-username>` is the username to use when pulling the image. The username must have access to the tenancy specified by `<tenancy-namespace>`. For example, `jdoe@acme.com` . If your tenancy is federated with Oracle Identity Cloud Service, use the format `oracleidentitycloudservice/<oci-username>`
     * `'<oci-auth-token>'` is the auth token of the user specified by `<oci-username>`. For example, `k]j64r{1sJSSF-;)K8` . If the auth token contains some special characters (such as the parenthesis in this example), which is often the case, surround the auth token with single quotes. Otherwise, single quotes are not required.
     * `<email-address>` is an email address. An email address is required, but it doesn't matter what you specify. For example, `jdoe@acme.com`
Note that strings containing some special characters (such as parentheses) must be surrounded by single quotes.
For example, combining the previous examples, you might enter:
Command
CopyTry It
```
kubectl create secret docker-registry ocirsecret --docker-server=ocir.us-ashburn-1.oci.oraclecloud.com --docker-username=ansh81vru1zp/jdoe@acme.com --docker-password='k]j64r{1sJSSF-;)K8' --docker-email=jdoe@acme.com
```

Having created the Docker secret, you can now refer to it in the application manifest file.


To specify the image to pull from Container Registry, along with the Docker secret to use, during deployment of an application to a cluster:
  1. Open the application's manifest file in a text editor.
  2. Add the following sections to the manifest file:
    1. Add a `containers` section that specifies the name and location of the container you want to pull from Container Registry, along with other deployment details. 
    2. Add an `imagePullSecrets` section to the manifest file that specifies the name of the Docker secret you created to access the Container Registry. 
Here's an example of what the manifest might look like when you've added the `containers` and `imagePullSecrets` sections:
Copy
```

apiVersion: v1
kind: Pod
metadata:
 name: ngnix-image
spec:
 containers:
  - name: ngnix
   image: ocir.us-ashburn-1.oci.oraclecloud.com/ansh81vru1zp/project01/ngnix-lb:latest
   imagePullPolicy: Always
   ports:
   - name: nginx
    containerPort: 8080
    protocol: TCP
 imagePullSecrets:
  - name: ocirsecret
```

  3. Save and close the manifest file.


Was this article helpful?
YesNo

