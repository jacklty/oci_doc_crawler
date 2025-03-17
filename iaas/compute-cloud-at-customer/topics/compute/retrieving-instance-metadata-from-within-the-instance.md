Updated 2024-10-07
# Retrieving Instance Metadata from Within the Instance
On Compute Cloud@Customer, the Instance Metadata Service (IMDS) serves information about a running instance to users who are logged in to that instance. IMDS also provides information to cloud-init that you can use for various system initialization tasks.
**Note**
To access IMDS metadata, use an instance image that's provided by Oracle.
The IMDS metadata includes instance information such as the following:
  * The SSH public key that enables users to log in to the instance
  * Instance attached VNICs, VNIC IDs
  * Instance CIDR blocks


In general, the IMDS instance metadata includes the following information:
  * The same information that you see on the details page of an instance in the Compute Cloud@Customer Console and in the output of the instance `get` CLI.
  * Custom information that you add to an instance by using the `--metadata`, `--extended-metadata`, `--ssh-authorized-keys-file`, and `--user-data-file` options of the instance `launch` command. This metadata can't be updated after instance launch. For a user logged into the instance, the instance metadata is read-only.


## Upgrading to IMDS Version 2 Endpoints 🔗 
The Instance Metadata Service is available in two versions: version 1 and version 2.
**Important**
To increase the security of metadata requests, upgrade all applications to use the IMDS version 2 endpoints, if supported by the image. Then disable use of IMDS version 1 endpoints.
IMDS version 2 endpoints (IMDSv2) are supported on the Oracle Linux images listed in [Guest Operating Systems](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/overview/guest-operating-systems.htm#guest-operating-systems "On Compute Cloud@Customer, you can use choose to create instances from various images. Each image provides a particular instance guest OS. This section lists the types of guest OSs you can use."). Other platform images and most other images don't support IMDSv2.
For each instance, perform the following steps to upgrade to IMDSv2:
  1. Identify applications that are making IMDSv1 requests.
For example, `cloud-init` makes requests to `/v#` instance endpoints.
  2. Migrate the identified applications to support IMDSv2 endpoints.
When you use `/v2` endpoints, you must include the "Authorization: Bearer Oracle" header. See the examples in [Retrieving IMDS Instance Metadata](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/compute/retrieving-instance-metadata-from-within-the-instance.htm#retrieving-instance-metadata-from-within-the-instance__get-imds-md).
  3. Disable IMDSv1 endpoints.
Perform one of the following steps, as described in [Creating an Instance](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/compute/creating-an-instance.htm#creating-an-instance "On Compute Cloud@Customer, you can create an instance using the Compute Cloud@Customer Console, CLI, and API.").
     * On the details page of an instance, under Instance Details, check the value of Legacy Instance Metadata Service Endpoints. If the value of Legacy Instance Metadata Service Endpoints is Enabled, click Edit on the Controls menu, and check the box for Legacy Instance Metadata Service Endpoints Disabled.
     * In the output from `instance list` or `instance                   get`, under `instance-options`, check the value of `are-legacy-imds-endpoints-disabled`. If the value of `are-legacy-imds-endpoints-disabled` is `null` or `false`, use the `instance update` command to specify the following option:
```
--instance-options '{"areLegacyImdsEndpointsDisabled": true}'
```

Future requests to legacy (`v1`) endpoints will be rejected with a 404 not found error.


## Retrieving IMDS Instance Metadata 🔗 
To retrieve the IMDS instance metadata, follow these steps:
  1. Log in to the instance.
  2. Use a cURL command to retrieve the metadata information from the HTTP endpoint.
Information is provided through an HTTP endpoint that listens on 169.254.169.254. If an instance has multiple VNICs, you must send the request using the primary VNIC.
Use the `instance` command to retrieve the instance metadata. Use the `vnics` command to retrieve the VNIC data.
If you are using `/v2` endpoints, as shown in the following examples, then you must include the "Authorization: Bearer Oracle" header.
Example: Instance Metadata
```
$ curl -H "Authorization: Bearer Oracle" -L http://169.254.169.254/opc/v2/instance/
{
  "availabilityDomain": "AD-1",
  "faultDomain": "FAULT-DOMAIN-1",
  "compartmentId": "ocid1.compartment.**_unique_ID_**",
  "displayName": "dev1",
  "hostname": "**_hostname_**",
  "id": "ocid1.instance.**_unique_ID_**",
  "image": "ocid1.image.**_unique_ID_**",
  "metadata": {
    "ssh_authorized_keys": "public_SSH_key"
  },
  "region": "PCA",
  "canonicalRegionName": "PCA",
  "ociAdName": "PCA",
  "regionInfo": null,
  "shape": "VM.PCAStandard.E5.Flex",
  "state": "RUNNING",
  "timeCreated": 1634943279000,
  "agentConfig": null
}
```

To retrieve a single value, specify the key name as shown in the following example.
Example: VNIC Metadata
```
$ curl -H "Authorization: Bearer Oracle" -L http://169.254.169.254/opc/v2/vnics/
[
  {
    "vnicId": "ocid1.vnic.**_unique_ID_**",
    "privateIp": "**_privateIp_**",
    "vlanTag": 0,
    "macAddr": "00:13:97:9f:16:32",
    "virtualRouterIp": "**_virtualRouterIp_**",
    "subnetCidrBlock": "**_subnetCidrBlock_**"
  }
]
```

You can view all the data for one of multiple VNICs by specifying the array index for that VNIC data, or you can retrieve a single value for that specified VNIC:
```
$ curl -H "Authorization: Bearer Oracle" -L http://169.254.169.254/opc/v2/vnics/0/privateIp
**_privateIp_**
```



Was this article helpful?
YesNo

