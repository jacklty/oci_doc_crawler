Updated 2025-01-15
# Creating Cloud-init Scripts for Self-managed Nodes
_Find out how to create the cloud-init script for a self-managed node that you want to add to an enhanced cluster created with Kubernetes Engine._
When creating a self-managed node to add to an enhanced cluster, you have to provide a cloud-init script that specifies the cluster's Kubernetes API private endpoint and base64-encoded CA certificate.
To create the cloud-init script for a self-managed node:
  1. Obtain the Kubernetes API private endpoint of the enhanced cluster to which you want to add the self- managed node using the Console or the CLI:
     * Using the Console:
       1. Open the **navigation menu** and select **Developer Services**. Under **Containers & Artifacts**, select **Kubernetes Clusters (OKE)**.
       2. On the **Cluster List** page, click the name of the enhanced cluster to which you want to add the self-managed node.
On the **Cluster Details** page, the **Kubernetes API private endpoint** is shown, including the port number. For example, `10.0.103.170:6443`
       3. Make a note of the cluster's Kubernetes API private endpoint, without the port number. For example, `10.0.103.170`
     * Using the CLI:
       1. Enter:
Command
CopyTry It
```
oci ce cluster create-kubeconfig --cluster-id <cluster-ocid> --region <region-identifier> --kube-endpoint PRIVATE_ENDPOINT --file - \
| grep -oE "https://[0-9\.]+:6443" \
| sed -E 's^https://([0-9\.]+):.*^\1^' 
```

The `grep` command extracts the URL of the cluster endpoint from the output of the `ce cluster create-kubeconfig` command. The `sed` command removes the protocol and port information from the cluster endpoint's URL to leave just the IP address.
       2. Make a note of the cluster's Kubernetes API private endpoint. For example, `10.0.103.170`
  2. Obtain the cluster's base64-encoded CA certificate from the cluster's kubeconfig file using the Console or the CLI:
     * Using the Console:
       1. On the **Cluster Details** page, make a note of the cluster's OCID. For example, `ocid1.cluster.oc1.phx.aaaaaaaa______ivq`
       2. Click **Access Cluster**.
       3. In the **Access Your Cluster** dialog, click **Cloud Shell Access** , and click **Launch Cloud Shell**.
       4. In the Cloud Shell window, enter the following command:
Command
CopyTry It
```
oci ce cluster create-kubeconfig --cluster-id <cluster-ocid> --region <region-identifier> --file - | grep -oE "LS0t.*"
```

where:
          * `<cluster-ocid>` is the value of the `--cluster-id` parameter shown in step 2 in the **Access Your Cluster** dialog.
          * `<region-identifier>` is the value of the `--region` parameter shown in step 2 in the **Access Your Cluster** dialog.
For example:
Command
CopyTry It
```
oci ce cluster create-kubeconfig --cluster-id ocid1.cluster.oc1.phx.aaaaaaaa______ivq --region us-phoenix-1 --file - | grep -oE "LS0t.*"
```

The base64-encoded CA certificate is shown in the Cloud Shell window as a long alphanumeric string starting with the characters `LS0t`.
       5. Make a note of the cluster's base64-encoded CA certificate.
     * Using the CLI:
       1. Enter:
Command
CopyTry It
```
oci ce cluster create-kubeconfig --cluster-id <cluster-ocid> --region <region-identifier> --file - | grep -oE "LS0t.*"
```

The base64-encoded CA certificate is shown in the Cloud Shell window as a long alphanumeric string starting with the characters `LS0t`.
       2. Make a note of the cluster's base64-encoded CA certificate.
  3. Create the cloud-init script as follows:
    1. In a text editor of your choice, create a new text file.
    2. Copy and paste the following script into the file:
Copy
```
#!/usr/bin/env bash
bash /etc/oke/oke-install.sh \
 --apiserver-endpoint "<cluster-endpoint>" \
 --kubelet-ca-cert "<base64-encoded-certificate>"
```

where:
       * `<cluster-endpoint>` is the cluster's Kubernetes API private endpoint that you obtained earlier (without the port number). For example, `10.0.103.170`
       * `<base64-encoded-certificate>` is the cluster's base64-encoded CA certificate that you obtained earlier (starting with the characters `LS0t`).
For example:
Copy
```
#!/usr/bin/env bash
bash /etc/oke/oke-install.sh \
 --apiserver-endpoint "10.0.103.170" \
 --kubelet-ca-cert "LS0t______UtLS0tLQo="
```

    3. Save the text file for use when you create the self-managed node.


Was this article helpful?
YesNo

