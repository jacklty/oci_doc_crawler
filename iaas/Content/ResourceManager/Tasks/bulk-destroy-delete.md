Updated 2023-01-04
# Bulk Destroying Resources and Deleting Stacks
For the specified compartment, use the following script to delete all the stacks in Resource Manager and destroy all the resources associated with the corresponding stacks.
This script runs [destroy jobs](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/create-job-destroy.htm#top "Create a destroy job in Resource Manager to release \(tear down\) resources associated with a stack and clean up the tenancy. Released resources are eventually deleted by the related OCI service. For example, a released compute instance is eventually deleted by the OCI Compute service.") on all provisioned resources in a compartment and then [deletes](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/delete-stack.htm#top "Delete a stack in Resource Manager. You can't undo the deletion of a stack.") all associated stacks.
  1. Update the compartment OCID in the following script.
[Script for automated destroy jobs and stack deletions](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/bulk-destroy-delete.htm)
Copy
```
#!/bin/bash
echo ""
echo ""
echo ""
echo "This script destroys all provisioned resources and deletes all associated stacks in a compartment. "
echo "Update the compartment OCID before you run the script."
echo " "
echo "**************************************************"
echo "STACK DELETIONS CANNOT BE UNDONE."
echo "**************************************************"
echo ""
echo "Starting to delete stacks from compartment id " $1
echo "Are you sure you want to continue ?"
select yn in "Yes" "No"; do
  case $yn in
    Yes ) break;;
    No ) echo "Exiting...";exit;;
  esac
done
stacks_to_be_deleted=$(oci resource-manager stack list --compartment-id $1 --lifecycle-state=ACTIVE | jq -r ".data[].id")
#stacks_to_be_deleted=$(oci resource-manager stack list -c ocid1.tenancy.oc1..<unique_ID> --lifecycle-state=ACTIVE)
echo "Destroying Stacks"
echo
failedStackArr=()
for stack in $stacks_to_be_deleted
do
    echo "Creating a job to destroy stack : $stack"
    #stack_destroyed=$(oci resource-manager job create-destroy-job --stack-id $stack --execution-plan-strategy AUTO_APPROVED)   
    #echo "oci resource-manager stack delete --force --stack-id $stack.id"
    job_id_destroy_stack=$(oci resource-manager job create-destroy-job --stack-id $stack --execution-plan-strategy AUTO_APPROVED | jq -r ".data.id")
    #poll for the status
    
	echo "Destroy job OCID : $job_id_destroy_stack"
	echo "Destroying resources provisioned by stack : $stack"
    
	#poll for destroy job
    destroy_job_status="STARTED"
    while [ $destroy_job_status != "SUCCEEDED" -a $destroy_job_status != "FAILED" ]
    do
        sleep 5s
        destroy_job_status=$(oci resource-manager job get --job-id $job_id_destroy_stack | jq -r '.data."lifecycle-state"')
    done
    if [ $destroy_job_status == "SUCCEEDED" ]; then
      echo "Stack resources destroyed. Now deleting the stack $stack"
	  echo		
      stack_deleted=$(oci resource-manager stack delete --stack-id $stack --force  | jq -r ".data.id")
    fi
    if [ $destroy_job_status == "FAILED" ]; then
      echo "Not able to destroy resources from stack $stack"
      failedStackArr+=($stack)
    fi
done
if [ ${#failedStackArr[@]} -gt 0 ]; then
	echo "Not able to destroy resources and delete these stacks. Please run destroy jobs and delete stacks manually."
	echo ${failedStackArr[@]}
else
	echo "Success. All resources have been destroyed and associated stacks have been deleted."
fi 
echo "done "
```

  2. Run the script using the following command.
Copy
```
./destroy_delete_stacks_bulk_cloud_shell.sh <compartment_id>
```



Was this article helpful?
YesNo

