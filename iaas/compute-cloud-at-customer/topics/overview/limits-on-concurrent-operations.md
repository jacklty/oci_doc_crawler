Updated 2024-04-19
# Limits on Concurrent Operations
Find out how many concurrent operations of a specific type Compute Cloud@Customer can manage at any particular time. These limits assume that no other operations of any kind are running at the same time. When a limit is exceeded, an error with code 409 or 429 is displayed.
Resource Type |  Operation |  Concurrency Limit  
---|---|---  
compute instance |  back up or restore an instance |  10  
compute instance |  launch/delete instance |  15  
compute instance |  reset/stop/start instance |  15  
compute instance |  update fault domain (live migration) |  10  
compute image |  create image from instance |  10  
compute image |  import image |  10  
block volume |  create/delete volume |  10  
block volume |  attach/detach boot volume |  15  
block volume |  attach/detach data volume |  15  
block volume |  resize volume |  15  
file system |  create/delete file system |  10  
mount target |  create/delete mount target |  10  
VCN |  create/delete VCN |  10  
VCN gateway | create/delete gateway (all types) |  10  
subnet |  create/delete subnet |  10  
route table |  create/delete route table |  10  
security list |  create/delete security list |  10  
network security group |  create/delete network security group |  10  
VNIC |  attach/detach VNIC |  15  
public IP |  create/delete public IP |  10  
private IP |  create/delete private IP |  10  
all networking resources |  update network resource |  10  
OKE service |  create/update/delete cluster |  10  
OKE service |  create/update/delete node pool |  5  
OKE service |  create/update/delete node |  15  
**Note**
In addition, a system limit on the number of concurrent user sessions:
  * Compute Cloud@Customer Console: 10 users


An authentication error is displayed when the limit is reached. An inactive user session times out after 1 hour.
Was this article helpful?
YesNo

