Updated 2025-01-15
# Granting Workloads Access to OCI Resources
_Find out how to use the identity of a workload running on a Kubernetes cluster to grant the workload fine-grained access to other OCI resources using Kubernetes Engine (OKE)._
**Note** You can only use workload identities to grant access to OCI resources when using enhanced clusters. See [Enhanced Clusters](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengcomparingenhancedwithbasicclusters_topic.htm#contengcomparingenhancedwithbasicclusters_topic-enhancedclusters).
In Kubernetes, a workload is an application running on a Kubernetes cluster. A workload can be one application component running inside a single pod, or several application components running inside a set of pods that work together. All the pods in the workload run in the same namespace.
To grant all the pods in a workload access to Kubernetes resources, you can specify that every pod in the workload is to use the same Kubernetes service account. You can then grant Kubernetes cluster role permissions to the service account. It is the service account that binds the pods in the workload to cluster role permissions, and grants the pods access to Kubernetes resources. 
In Oracle Cloud Infrastructure, a workload running on a Kubernetes cluster is considered a resource in its own right. A workload resource is identified by the unique combination of cluster, namespace, and service account. This unique combination is referred to as the workload identity. You can use the workload identity when defining IAM policies to grant fine-grained access to other OCI resources (such as Object Storage buckets). In addition, you can use Oracle Cloud Infrastructure Audit to satisfy compliance requirements by tracking requests made by the workload identity, enabling you to monitor and report unauthorized access and suspicious activity.
To grant all the pods in a workload access to OCI resources:
  * Create a namespace for a service account.
  * Create a service account for the application to use.
  * Define an IAM policy to grant the workload resource access to other OCI resources. 
  * Download and configure the appropriate OCI SDK for the language in which the application is written.
  * Edit the application to specify:
  *     * that workload requests are to be authenticated using the Kubernetes Engine workload identity provider
    * the OCI resources that are to be accessed
  * Update the application's deployment spec to specify that every pod in the workload is to use the service account.


Note the following when using workload identities:
  * You cannot currently use workload identities with dynamic groups.
  * You can only use workload identities with an OCI SDK, not with the Console or the API. 
  * The following OCI SDKs currently support workload identities:
    * Go SDK v65.32.0 (and later)
    * Java SDK v2.54.0 (and later)
    * Python SDK v2.111.0 (and later)
    * .NET SDK v87.3.0 (and later)
    * Ruby SDK v2.19.0 (and later)


## Example: Using the Go SDK to Grant Application Workloads Access to OCI Resources 🔗 
To grant Go application workloads running on a Kubernetes cluster access to other OCI resources:
  1. If you haven't already done so, follow the steps to set up the cluster's kubeconfig configuration file and (if necessary) set the KUBECONFIG environment variable to point to the file. Note that you must set up your own kubeconfig file. You cannot access a cluster using a kubeconfig file that a different user set up. See [Setting Up Cluster Access](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengdownloadkubeconfigfile.htm#Setting_Up_Cluster_Access "Find out about the steps to set up access to the clusters you create using Kubernetes Engine \(OKE\). Having completed the steps, you can start using kubectl to manage the cluster.").
  2. Obtain the OCID of the cluster (for example, using the **Cluster Details** tab in the Console).
  3. Create a namespace for the Kubernetes service account to use by entering:
Command
CopyTry It
```
kubectl create namespace <namespace-name>
```

For example:
Command
CopyTry It
```
kubectl create namespace finance
```

  4. Create a Kubernetes service account for the application to use by entering:
Command
CopyTry It
```
kubectl create serviceaccount <service-account-name> --namespace <namespace-name>
```

For example:
Command
CopyTry It
```
kubectl create serviceaccount financeserviceaccount --namespace finance
```

  5. Define an IAM policy to enable the workload to access the necessary OCI resources: 
    1. Open the **navigation menu** and select **Identity & Security**. Under **Identity** , select **Policies**.
    2. Follow the instructions in [To create a policy](https://docs.oracle.com/iaas/Content/Identity/Tasks/managingpolicies.htm#To_create_a_policy), and give the policy a name (for example, `acme-oke-finance-workload-policy`).
    3. Enter a policy statement to enable the workload to access the necessary OCI resources, in the format:
Copy
```
Allow any-user to <verb> <resource> in <location> where all {
request.principal.type = 'workload',
request.principal.namespace = '<namespace-name>',
request.principal.service_account = '<service-account-name>',
request.principal.cluster_id = '<cluster-ocid>'}
```

where:
       * `<namespace-name>` is the name of the namespace that you created previously.
       * `<service-account-name>` is the name of the service account that you created previously.
       * `<cluster-ocid>` is the cluster's OCID that you obtained previously.
For example:
Copy
```
Allow any-user to manage objects in tenancy where all {
request.principal.type = 'workload',
request.principal.namespace = 'finance',
request.principal.service_account = 'financeserviceaccount',
request.principal.cluster_id = 'ocid1.cluster.oc1.iad.aaaaaaaaaf______jrd'}
```

    4. Click **Create** to create the new policy.
  6. Install the OCI SDK for Go (see [SDK for Go](https://docs.oracle.com/iaas/Content/API/SDKDocs/gosdk.htm#SDK_for_Go)).
  7. In your Go application code, add:
     * the Kubernetes Engine workload identity provider (`OkeWorkloadIdentityConfigurationProvider`)
     * the OCI resource to access
For example, the following code snippet uses the workload identity for authentication, creates a bucket in the Object Storage service in the Pheonix (PHX) region, and uploads a file to the bucket:
```
// ExampleObjectStorage_UploadFile shows how to create a bucket and upload a file using OKE Workload Identity
 
 func ExampleObjectStorage_UploadFile() {
    rp, err := auth.OkeWorkloadIdentityConfigurationProvider()
    if err != nil
    { panic(err) }
    c, clerr := objectstorage.NewObjectStorageClientWithConfigurationProvider(rp)
    c.SetRegion("us-phoenix-1")
    helpers.FatalIfError(clerr)
 
    ctx := context.Background()
    bname := helpers.GetRandomString(8)
    namespace := getNamespace(ctx, c)
     
    createBucket(ctx, c, namespace, bname)
 
    contentlen := 1024 * 1000
    filepath, filesize := helpers.WriteTempFileOfSize(int64(contentlen))  
    filename := path.Base(filepath)
    defer func() {
        os.Remove(filename)
    }()
 
    file, e := os.Open(filepath)
    defer file.Close()
    helpers.FatalIfError(e)
     
    e = putObject(ctx, c, namespace, bname, filename, filesize, file, nil)
    helpers.FatalIfError(e)
 
 
    // Output:
    // get namespace
    // create bucket
    // put object
```

  8. Open the application's deployment spec in a text editor and: 
    1. Add `serviceAccountName` and set it to the name of the service account you created earlier. For example, `serviceAccountName: financeserviceaccount`.
    2. Add `automountServiceAccountToken` and set it to `true`.
For example:
Copy
```
apiVersion: v1
kind: Pod
metadata:
 name: nginx
spec:
 serviceAccountName: financeserviceaccount
 automountServiceAccountToken: true
 containers:
 - name: nginx
  image: nginx:1.14.2
  ports:
   - containerPort: 80
```

  9. Deploy the application by entering:```
kubectl create -f <filename>
```

For example:```
kubectl create -f financeworkloadidentity.yaml
```



## Example: Using the Java SDK to Grant Application Workloads Access to OCI Resources 🔗 
To grant Java application workloads running on a Kubernetes cluster access to other OCI resources:
  1. If you haven't already done so, follow the steps to set up the cluster's kubeconfig configuration file and (if necessary) set the KUBECONFIG environment variable to point to the file. Note that you must set up your own kubeconfig file. You cannot access a cluster using a kubeconfig file that a different user set up. See [Setting Up Cluster Access](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengdownloadkubeconfigfile.htm#Setting_Up_Cluster_Access "Find out about the steps to set up access to the clusters you create using Kubernetes Engine \(OKE\). Having completed the steps, you can start using kubectl to manage the cluster.").
  2. Obtain the OCID of the cluster (for example, using the **Cluster Details** tab in the Console).
  3. Create a namespace for the Kubernetes service account to use by entering:
Command
CopyTry It
```
kubectl create namespace <namespace-name>
```

For example:
Command
CopyTry It
```
kubectl create namespace finance
```

  4. Create a Kubernetes service account for the application to use by entering:
Command
CopyTry It
```
kubectl create serviceaccount <service-account-name> --namespace <namespace-name>
```

For example:
Command
CopyTry It
```
kubectl create serviceaccount financeserviceaccount --namespace finance
```

  5. Define an IAM policy to enable the workload to access the necessary OCI resources: 
    1. Open the **navigation menu** and select **Identity & Security**. Under **Identity** , select **Policies**.
    2. Follow the instructions in [To create a policy](https://docs.oracle.com/iaas/Content/Identity/Tasks/managingpolicies.htm#To_create_a_policy), and give the policy a name (for example, `acme-oke-finance-workload-policy`).
    3. Enter a policy statement to enable the workload to access the necessary OCI resources, in the format:
Copy
```
Allow any-user to <verb> <resource> in <location> where all {
request.principal.type = 'workload',
request.principal.namespace = '<namespace-name>',
request.principal.service_account = '<service-account-name>',
request.principal.cluster_id = '<cluster-ocid>'}
```

where:
       * `<namespace-name>` is the name of the namespace that you created previously.
       * `<service-account-name>` is the name of the service account that you created previously.
       * `<cluster-ocid>` is the cluster's OCID that you obtained previously.
For example:
Copy
```
Allow any-user to manage objects in tenancy where all {
request.principal.type = 'workload',
request.principal.namespace = 'finance',
request.principal.service_account = 'financeserviceaccount',
request.principal.cluster_id = 'ocid1.cluster.oc1.iad.aaaaaaaaaf______jrd'}
```

    4. Click **Create** to create the new policy.
  6. Install the OCI SDK for Java (see [SDK for Java](https://docs.oracle.com/iaas/Content/API/SDKDocs/javasdk.htm#SDK_for_Java)).
  7. In the application's pom.xml, add the `oci-java-sdk-addons-oke-workload-identity` artifact as a dependency:```
<dependency>
<groupId>com.oracle.oci.sdk</groupId>
<artifactId>oci-java-sdk-addons-oke-workload-identity</artifactId>
<version>2.54.0</version>
</dependency>
<dependency>
<groupId>com.oracle.oci.sdk</groupId>
<artifactId>oci-java-sdk-common</artifactId>
<version>2.54.0</version>
</dependency>
```
Note the SDK version must be 2.54.0 or later.
  8. In your Java application code, add:
     * the Kubernetes Engine workload identity provider (`OkeWorkloadIdentityAuthenticationDetailsProvider`)
     * the OCI resource to access
For example, the following code snippet uses the workload identity for authentication, creates a bucket in the Object Storage service in the Pheonix (PHX) region, and uploads a file to the bucket:
Copy
```
import com.oracle.bmc.Region;
import com.oracle.bmc.auth.AuthenticationDetailsProvider;
import com.oracle.bmc.auth.ConfigFileAuthenticationDetailsProvider;
import com.oracle.bmc.auth.okeworkloadidentity.OkeWorkloadIdentityAuthenticationDetailsProvider;
import com.oracle.bmc.objectstorage.ObjectStorage;
import com.oracle.bmc.objectstorage.ObjectStorageClient;
import com.oracle.bmc.objectstorage.model.BucketSummary;
import com.oracle.bmc.objectstorage.requests.GetNamespaceRequest;
import com.oracle.bmc.objectstorage.requests.GetObjectRequest;
import com.oracle.bmc.objectstorage.requests.ListBucketsRequest;
import com.oracle.bmc.objectstorage.requests.ListBucketsRequest.Builder;
import com.oracle.bmc.objectstorage.responses.GetNamespaceResponse;
import com.oracle.bmc.objectstorage.responses.GetObjectResponse;
import com.oracle.bmc.objectstorage.responses.ListBucketsResponse;
import java.io.InputStream;
public class ObjectStorageSyncExample {
  public static void main(String[] args) throws Exception {
    /* Config the Container Engine for Kubernetes workload identity provider */
    final OkeWorkloadIdentityAuthenticationDetailsProvider provider = new OkeWorkloadIdentityAuthenticationDetailsProvider
        .OkeWorkloadIdentityAuthenticationDetailsProviderBuilder()
        .build();
    /* Configure the client to use workload identity provider*/
    ObjectStorage client =
        ObjectStorageClient.builder().region(Region.US_PHOENIX_1).build(provider);
    GetNamespaceResponse namespaceResponse =
        client.getNamespace(GetNamespaceRequest.builder().build());
    String namespaceName = namespaceResponse.getValue();
    System.out.println("Using namespace: " + namespaceName);
    Builder listBucketsBuilder =
        ListBucketsRequest.builder()
            .namespaceName(namespaceName)
            .compartmentId("enter tenancy id");
    String nextToken = null;
    do {
      listBucketsBuilder.page(nextToken);
      ListBucketsResponse listBucketsResponse =
          client.listBuckets(listBucketsBuilder.build());
      for (BucketSummary bucket : listBucketsResponse.getItems()) {
        System.out.println("Found bucket: " + bucket.getName());
      }
      nextToken = listBucketsResponse.getOpcNextPage();
    } while (nextToken != null);
    // fetch the file from the object storage
    String bucketName = null;
    String objectName = null;
    GetObjectResponse getResponse =
        client.getObject(
            GetObjectRequest.builder()
                .namespaceName(namespaceName)
                .bucketName(bucketName)
                .objectName(objectName)
                .build());
    // stream contents should match the file uploaded
    try (final InputStream fileStream = getResponse.getInputStream()) {
      // use fileStream
    } // try-with-resources automatically closes fileStream
    client.close();
  }
}
```

  9. Open the application's deployment spec in a text editor and: 
    1. Add `serviceAccountName` and set it to the name of the service account you created earlier. For example, `serviceAccountName: financeserviceaccount`.
    2. Add `automountServiceAccountToken` and set it to `true`.
For example:
Copy
```
apiVersion: v1
kind: Pod
metadata:
 name: nginx
spec:
 serviceAccountName: financeserviceaccount
 automountServiceAccountToken: true
 containers:
 - name: nginx
  image: nginx:1.14.2
  ports:
   - containerPort: 80
```

  10. Deploy the application by entering:```
kubectl create -f <filename>
```

For example:```
kubectl create -f financeworkloadidentity.yaml
```



## Example: Using the Java SDK to Grant Application Workloads Access to OCI Resources in a Different Compartment 🔗 
To grant Java application workloads running on a Kubernetes cluster in one compartment access to other OCI resources in a different compartment:
  1. If you haven't already done so, follow the steps to set up the cluster's kubeconfig configuration file and (if necessary) set the KUBECONFIG environment variable to point to the file. Note that you must set up your own kubeconfig file. You cannot access a cluster using a kubeconfig file that a different user set up. See [Setting Up Cluster Access](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengdownloadkubeconfigfile.htm#Setting_Up_Cluster_Access "Find out about the steps to set up access to the clusters you create using Kubernetes Engine \(OKE\). Having completed the steps, you can start using kubectl to manage the cluster.").
  2. Obtain the OCID of the cluster (for example, using the **Cluster Details** tab in the Console).
  3. As the cluster administrator, create a namespace for the Kubernetes service account to use by entering:
Command
CopyTry It
```
kubectl create namespace <namespace-name>
```

For example:
Command
CopyTry It
```
kubectl create namespace finance
```

  4. As the cluster administrator, create a Kubernetes service account for the application to use by entering:
Command
CopyTry It
```
kubectl create serviceaccount <service-account-name> --namespace <namespace-name>
```

For example:
Command
CopyTry It
```
kubectl create serviceaccount financeserviceaccount --namespace finance
```

  5. As the tenancy administrator, define an IAM policy to allow a cluster administrator to bind workloads running on a cluster in one compartment, to other OCI resources in a different compartment:
    1. Open the **navigation menu** and select **Identity & Security**. Under **Identity** , select **Policies**.
    2. Follow the instructions in [To create a policy](https://docs.oracle.com/iaas/Content/Identity/Tasks/managingpolicies.htm#To_create_a_policy), and give the policy a name (for example, `acme-oke-finance-workload-policy`).
    3. Enter policy statements to allow a cluster administrator to bind workloads running on a cluster in one compartment, to other OCI resources in a different compartment, in the format:
Copy
```
Allow group cluster-admins to manage cluster-workload-mappings in compartment <compartment-one>
Allow group cluster-admins to {CLUSTER_WORKLOAD_COMPARTMENT_BIND,CLUSTER_WORKLOAD_COMPARTMENT_UNBIND} in compartment <compartment-two>
```

where:
       * `<compartment-one>` is the compartment to which the cluster belongs
       * `<compartment-two>` is the compartment to which the other OCI resources belong
For example:
Copy
```
Allow group cluster-admins to manage cluster-workload-mappings in compartment finance
Allow group cluster-admins to {CLUSTER_WORKLOAD_COMPARTMENT_BIND,CLUSTER_WORKLOAD_COMPARTMENT_UNBIND} in compartment sales
```

Note that if a group is not in the default identity domain, prefix the group name with the identity domain name, in the format `group '<identity-domain-name>'/'group-name'`. You can also specify a group using its OCID, in the format `group id <group-ocid>`.
    4. Click **Create** to create the new policy.
  6. As the cluster administrator, in the compartment to which the cluster belongs, create a workload mapping that maps workloads running on the cluster to the compartment that the other OCI resources belong to:
```
oci ce workload-mapping create --namespace <namespace-name> --mapped-compartment-id <compartment-two-ocid> --cluster-id <cluster-ocid>
```

For example:
```
oci ce workload-mapping create --namespace finance --mapped-compartment-id ocid1.compartment.oc1..aaaaaaaaad______fda --cluster-id ocid1.cluster.oc1.iad.aaaaaaaaaf______jrd
```

  7. As the administrator of the resource in the second compartment, define an IAM policy to enable the workload to access the OCI resources in the compartment:
    1. Open the **navigation menu** and select **Identity & Security**. Under **Identity** , select **Policies**.
    2. Follow the instructions in [To create a policy](https://docs.oracle.com/iaas/Content/Identity/Tasks/managingpolicies.htm#To_create_a_policy), and give the policy a name (for example, `acme-oke-finance-workload-policy`).
    3. Enter a policy statement to enable the workload to access the necessary OCI resources, in the format:
Copy
```
Allow any-user to <verb> <resource> in <location> where all {
request.principal.type = 'workload',
request.principal.namespace = '<namespace-name>',
request.principal.service_account = '<service-account-name>',
request.principal.cluster_id = '<cluster-ocid>'}
```

where:
       * `<namespace-name>` is the name of the namespace that you created previously.
       * `<service-account-name>` is the name of the service account that you created previously.
       * `<cluster-ocid>` is the cluster's OCID that you obtained previously.
For example:
Copy
```
Allow any-user to manage objects in compartment sales where all {
request.principal.type = 'workload',
request.principal.namespace = 'finance',
request.principal.service_account = 'financeserviceaccount',
request.principal.cluster_id = 'ocid1.cluster.oc1.iad.aaaaaaaaaf______jrd'}
```

    4. Click **Create** to create the new policy.
  8. Install the OCI SDK for Java (see [SDK for Java](https://docs.oracle.com/iaas/Content/API/SDKDocs/javasdk.htm#SDK_for_Java)). Note the SDK version must be 2.66.0 or later (or 3.18.0 or later).
  9. In the application's pom.xml, add the `oci-java-sdk-addons-oke-workload-identity` artifact as a dependency:```
<dependency>
<groupId>com.oracle.oci.sdk</groupId>
<artifactId>oci-java-sdk-addons-oke-workload-identity</artifactId>
<version>2.66.0</version>
</dependency>
<dependency>
<groupId>com.oracle.oci.sdk</groupId>
<artifactId>oci-java-sdk-common</artifactId>
<version>2.66.0</version>
</dependency>
```
Note the SDK version must be 2.66.0 or later (or 3.18.0 or later).
  10. In your Java application code, add:
     * the Kubernetes Engine workload identity provider (`OkeWorkloadIdentityAuthenticationDetailsProvider`)
     * the OCI resource to access
For example, the following code snippet uses the workload identity for authentication, creates a bucket in the Object Storage service in the Pheonix (PHX) region, and uploads a file to the bucket:
Copy
```
import com.oracle.bmc.Region;
import com.oracle.bmc.auth.AuthenticationDetailsProvider;
import com.oracle.bmc.auth.ConfigFileAuthenticationDetailsProvider;
import com.oracle.bmc.auth.okeworkloadidentity.OkeWorkloadIdentityAuthenticationDetailsProvider;
import com.oracle.bmc.objectstorage.ObjectStorage;
import com.oracle.bmc.objectstorage.ObjectStorageClient;
import com.oracle.bmc.objectstorage.model.BucketSummary;
import com.oracle.bmc.objectstorage.requests.GetNamespaceRequest;
import com.oracle.bmc.objectstorage.requests.GetObjectRequest;
import com.oracle.bmc.objectstorage.requests.ListBucketsRequest;
import com.oracle.bmc.objectstorage.requests.ListBucketsRequest.Builder;
import com.oracle.bmc.objectstorage.responses.GetNamespaceResponse;
import com.oracle.bmc.objectstorage.responses.GetObjectResponse;
import com.oracle.bmc.objectstorage.responses.ListBucketsResponse;
import java.io.InputStream;
public class ObjectStorageSyncExample {
  public static void main(String[] args) throws Exception {
    /* Config the Container Engine for Kubernetes workload identity provider */
    final OkeWorkloadIdentityAuthenticationDetailsProvider provider = new OkeWorkloadIdentityAuthenticationDetailsProvider
        .OkeWorkloadIdentityAuthenticationDetailsProviderBuilder()
        .build();
    /* Configure the client to use workload identity provider*/
    ObjectStorage client =
        ObjectStorageClient.builder().region(Region.US_PHOENIX_1).build(provider);
    GetNamespaceResponse namespaceResponse =
        client.getNamespace(GetNamespaceRequest.builder().build());
    String namespaceName = namespaceResponse.getValue();
    System.out.println("Using namespace: " + namespaceName);
    Builder listBucketsBuilder =
        ListBucketsRequest.builder()
            .namespaceName(namespaceName)
            .compartmentId("enter tenancy id");
    String nextToken = null;
    do {
      listBucketsBuilder.page(nextToken);
      ListBucketsResponse listBucketsResponse =
          client.listBuckets(listBucketsBuilder.build());
      for (BucketSummary bucket : listBucketsResponse.getItems()) {
        System.out.println("Found bucket: " + bucket.getName());
      }
      nextToken = listBucketsResponse.getOpcNextPage();
    } while (nextToken != null);
    // fetch the file from the object storage
    String bucketName = null;
    String objectName = null;
    GetObjectResponse getResponse =
        client.getObject(
            GetObjectRequest.builder()
                .namespaceName(namespaceName)
                .bucketName(bucketName)
                .objectName(objectName)
                .build());
    // stream contents should match the file uploaded
    try (final InputStream fileStream = getResponse.getInputStream()) {
      // use fileStream
    } // try-with-resources automatically closes fileStream
    client.close();
  }
}
```

  11. Open the application's deployment spec in a text editor and: 
    1. Add `namespace` and set it to the name of the namespace you created earlier. For example, `namespace: finance`.
    2. Add `serviceAccountName` and set it to the name of the service account you created earlier. For example, `serviceAccountName: financeserviceaccount`.
    3. Add `automountServiceAccountToken` and set it to `true`.
For example:
Copy
```
apiVersion: v1
kind: Pod
metadata:
 name: nginx
 namespace: finance
spec:
 serviceAccountName: financeserviceaccount
 automountServiceAccountToken: true
 containers:
  - name: nginx
   image: nginx:1.14.2
   ports:
    - containerPort: 80
```

  12. Deploy the application by entering:```
kubectl create -f <filename>
```

For example:```
kubectl create -f financeworkloadidentity.yaml
```



Was this article helpful?
YesNo

