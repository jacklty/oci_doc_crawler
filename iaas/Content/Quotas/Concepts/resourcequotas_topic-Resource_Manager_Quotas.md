Updated 2023-06-08
# Resource Manager Quotas
Resource Manager quota details.
Family name: `resource-manager`
Name |  Scope |  Description  
---|---|---  
concurrent-job-count | Regional | Number of concurrent Jobs per compartment  
configuration-source-provider-count  | Regional  | Number of configuration source providers per compartment   
private-endpoint-count | Regional | Number of private endpoints per compartment  
stack-count | Regional | Number of stacks per compartment  
template-count | Regional | Number of private templates per compartment  
## Example
Copy
```
set resource-manager quota concurrent-job-count to 1 in compartment MyCompartment
set resource-manager quota configuration-source-provider-count to 5 in compartment MyCompartment
set resource-manager quota private-endpoint-count to 1 in compartment MyCompartment
zero resource-manager quota stack-count in compartment MyCompartment
set resource-manager quota template-count to 3 in compartment MyCompartment
```

Was this article helpful?
YesNo

