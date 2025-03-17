Updated 2024-08-14
# Generated Worker Node Name Formats
_Find out about the format of the names that Kubernetes Engine (OKE) gives to worker nodes in the clusters it creates._
Regardless of how you create a cluster, Kubernetes Engine gives names to worker nodes. The format depends on the type of node:
  * **Managed nodes:** Names have the following format:
`oke-c<part-of-cluster-OCID>-n<part-of-node-pool-OCID>-s<part-of-subnet-OCID>-<slot>`
where:
    * `oke` is the standard prefix for all worker nodes created by Kubernetes Engine
    * `c<part-of-cluster-OCID`> is a portion of the cluster's OCID, prefixed with the letter `c`
    * `n<part-of-node-pool-OCID>` is a portion of the node pool's OCID, prefixed with the letter `n`
    * `s<part-of-subnet-OCID>` is a portion of the subnet's OCID, prefixed with the letter `s`
    * `<slot>` is an ordinal number of the node in the subnet (for example, `0`, `1`) 
For example, if you specified a cluster is to have two nodes in a node pool, the two nodes might be named:
    * `oke-cywiqripuyg-nsgagklgnst-st2qczvnmba-0`
    * `oke-cywiqripuyg-nsgagklgnst-st2qczvnmba-1`
  * **Virtual nodes:** Names are the same as the node's private IP address. For example, `10.0.5.207`.


Do not change the auto-generated names that Kubernetes Engine gives to worker nodes.
Was this article helpful?
YesNo

