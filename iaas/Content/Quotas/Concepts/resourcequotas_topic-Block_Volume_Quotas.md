Updated 2023-06-08
# Block Volume Quotas
Block Volume quota details.
Family name: `block-storage`
Name |  Scope |  Description  
---|---|---  
backup-count | Regional | Total number of block and boot volume backups  
total-storage-gb | Availability domain  |  Maximum storage space of block and boot volumes, in GB  
volume-count | Availability domain  |  Total number of block and boot volumes  
## Example
Copy
```
set block-storage quota volume-count to 10 in compartment MyCompartment
```

Was this article helpful?
YesNo

