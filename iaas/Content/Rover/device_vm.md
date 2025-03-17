Updated 2023-06-22
# Running CLIs on Device-Hosted Compute Instances
Configure your Roving Edge Infrastructure device to run the command line interface (CLI) on its compute instances.
Follow these guidelines for running CLIs on compute instances hosted by Roving Edge Infrastructure devices.
**Note**
The instructions in this topic are for Oracle Linux host computers.
  * Have the VM go through the following local IP:
`169.254.169.254`
  * Have the VM refer to the Roving Edge Infrastructure device as `otec-console-local`.
  * Employ the following IP Tables rules:
```
{ for i in 19060 8019 12050 21060 22060 23060 22060 12060;do iptables -I 
BareMetalInstanceServices -d 169.254.169.254/32 -p tcp -m tcp --dport $i -m 
comment --comment "Rover service access port" -j ACCEPT;done }
```

See [Service Ports](https://docs.oracle.com/iaas/Content/Rover/device_specifications.htm#ServicePorts) for a list of available ports.


## Unsupported CLI Commands 🔗 
The following CLI commands are currently not supported. Workarounds are provided where available.
  * **Object Storage CLIs** : `oci os list`
You can only use the `oci os list` command when you include the `--fields` option. For example:
```
# oci os object list --bucket-name generic-image --fields name,size,timeCreated,md5,etag
{
"data": [
{
"archival-state": null,
"etag": "b2c123ff0f1231c4c7f41ff92294e4a0-32",
"md5": "ssYx/w8SUcTH9B/5IpTkoA==-32",
"name": "exported-image",
"size": 2132357120,
"storage-tier": null,
"time-created": "2022-03-01T19:50:03.076000+00:00",
"time-modified": null
},  {
   "archival-state": null,
   "etag": "fe5e3c12e12e31de65b86722a6fe29e7-32",
   "md5": "/l48AOleMd5luGcipv4p5w==-32",
   "name": "imported-image-20210830-1542_ocid1.image.oc1.iad..uniqueID.oci",
   "size": 2132224000,
   "storage-tier": null,
   "time-created": "2022-03-01T19:50:59.968000+00:00",
   "time-modified": null
  }
 ],
 "prefixes": []
}
```

  * **Compute CLIs** : `oci compute instance list-vnics`
The `oci compute instance list-vnics` command lists the VNICs that are attached to the specified instance and is often used to get the public IP for a compute node. This CLI is not currently supported in Roving Edge Infrastructure. You can get VNIC information, including IP address associated with a VNIC attached to a compute node, using any of the following methods:
    * **Device Console** : Go to the following location: 
**Compute > Instances > Instance Details > Attached VNICs**
The IP addresses for the VNICs are listed in the dialog box that appears.
    * **CLI** : `oci compute instance list-vnics`
First, run the following command to list all the VNIC's attachments:
```
oci compute vnic-attachment list --instance-id <> --all
```

Next, run the following command for the specific VNIC for which you want to get details:
```
oci network vnic get --vnic-id <>
```

The following example shows these two commands run together with their respective returns:
```
# oci compute vnic-attachment list --instance-id ocid1.instance.orei.orei-1..uniqueID --all
{
 "data": [
  {
   "availability-domain": "orei-1-ad-1",
   "compartment-id": "ocid1.tenancy.orei..uniqueID",
   "display-name": null,
   "id": "ocid1.vnicattachment.orei.orei-1..uniqueID",
   "instance-id": "ocid1.instance.orei.orei-1..uniqueID",
   "lifecycle-state": "ATTACHED",
   "nic-index": 0,
   "subnet-id": "ocid1.subnet.orei.orei-1..uniqueID",
   "time-created": "2022-03-01T21:07:00.937000+00:00",
   "vlan-id": null,
   "vlan-tag": 1,
   "vnic-id": "ocid1.vnic.orei.orei-1..uniqueID"
  }
 ]
}
# oci network vnic get --vnic-id ocid1.vnic.orei.orei-1..uniqueID
{
 "data": {
  "availability-domain": "orei-1-ad-1",
  "compartment-id": "ocid1.tenancy.orei..uniqueID",
  "defined-tags": {},
  "display-name": "test-instance",
  "freeform-tags": {},
  "hostname-label": "test-instance",
  "id": "ocid1.vnic.orei.orei-1..uniqueID",
  "is-primary": true,
  "lifecycle-state": "AVAILABLE",
  "mac-address": "02:00:17:00:04:00",
  "nsg-ids": [],
  "private-ip": "10.0.0.2",
  "public-ip": "10.145.142.128",
  "skip-source-dest-check": false,
  "subnet-id": "ocid1.subnet.orei.orei-1..",
  "time-created": "2022-03-01T21:07:00.155000+00:00",
  "vlan-id": null
 },
 "etag": "2c082d1c"
}
```

If only one VNIC is attached, you can combine these CLI commands with other Linux tools to limit the output to just the public IP address using the following command:
```
oci compute vnic-attachment list --instance-id <> --all|grep -m 1 vnic-id|awk -F'"' '{print $4}'|xargs -I{} oci network vnic get --vnic-id {}|grep public-ip|awk -F'"' '{print $4}'

```

For example:
```
# oci compute vnic-attachment list --instance-id ocid1.instance.orei.orei-1..uniqueID --all|grep -m 1 vnic-id|awk -F'"' '{print $4}'|xargs -I{} oci network vnic get --vnic-id {}|grep public-ip|awk -F'"' '{print $4}'
10.145.142.128
```



Was this article helpful?
YesNo

