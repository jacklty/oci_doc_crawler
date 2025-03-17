Updated 2025-01-10
# Extend Console Pages Using Schema Documents
Review requirements, supported types, and examples for schema documents used with Terraform configurations in Resource Manager.
Schema documents are recommended for Terraform configurations when using Resource Manager. Including a schema document allows you to extend pages in the Oracle Cloud Infrastructure Console. Facilitate variable entry in the **Create stack** page by surfacing SSH key controls and by naming, grouping, dynamically prepopulating values, and more. Define text in the **Application Information** tab of the **Stack details** page that opens for a created stack.
## Requirements for Schema Documents 🔗 
Schema documents for Resource Manager have the following requirements:
  * YAML format.
  * Data types must be consistent with the associated [Terraform configuration](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Concepts/authoring-configurations.htm#top "Write a Terraform configuration to describe infrastructure using the HashiCorp Configuration Language format \(HCL\).").
For example, let's say that you declare the type `number` for the `availability` variable in the schema. In this situation, `availability` must have the same declared type (`number`) in the associated Terraform configuration. (By default, variables with no declared type use `string`.)
  * Placement under the root folder of the Resource Manager Terraform configuration. (By default, the schema document assumes that the root folder is the working directory.)


## Supported Types (Dynamic Prepopulation and Controls) 🔗 
This section lists the types supported by Resource Manager for [dynamic prepopulation](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Concepts/terraformconfigresourcemanager_topic-schema.htm#console-howto__prepop) and controls.
Most types require the compartment OCID (`dependsOn: required: compartmentId`). Some types have additional required or optional items. To determine required and optional items for a type, see [Meta Schema for Validation](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Concepts/terraformconfigresourcemanager_topic-schema.htm#metaschema).
Optionally filter dynamically prepopulated lists by other variables using `dependsOn`. For example, filter subnets by VCN. For more information, see [Dynamic prepopulation](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Concepts/terraformconfigresourcemanager_topic-schema.htm#console-howto__prepop).
**Note**
Descriptions in `schema.yaml` files are HTML encoded in the output.
When defined in the Terraform configuration, the following variables automatically prepopulate with values on the Console pages used to [create and edit the stack](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/create-stack.htm#top "Create a stack in Resource Manager. You can optionally postpone variables and other stack settings until after the stack is created."). The stack's values are used when you select the Terraform actions [Plan](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/create-job-plan.htm#top "Create a plan job in Resource Manager."), [Apply](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/create-job-apply.htm#top "Create an apply job in Resource Manager."), and [Destroy](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/create-job-destroy.htm#top "Create a destroy job in Resource Manager to release \(tear down\) resources associated with a stack and clean up the tenancy. Released resources are eventually deleted by the related OCI service. For example, a released compute instance is eventually deleted by the OCI Compute service.").
  * `tenancy_ocid` (tenancy OCID)
  * `compartment_ocid` (compartment OCID)
  * `region` (region)
  * `current_user_ocid` (OCID of the current user)


Type (rendered as a [dynamically prepopulated](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Concepts/terraformconfigresourcemanager_topic-schema.htm#console-howto__prepop) dropdown field unless otherwise noted) | Resource identifier | Comments  
---|---|---  
`file` | -- | Surfaces a control for adding a single file by dropping or browsing. When this control is surfaced, a user can upload a file of any extension, such as a license key or certificate. For more information, see [File control](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Concepts/terraformconfigresourcemanager_topic-schema.htm#console-howto__file).  
`oci:apm:domain:id` | [Application Performance Monitoring (APM) domain](https://docs.oracle.com/iaas/application-performance-monitoring/doc/create-apm-domain.html) OCID  
`oci:blockstorage:policies:id` | [Volume backup policy](https://docs.oracle.com/iaas/Content/Block/Tasks/schedulingvolumebackups.htm#Oracle)  
`oci:container:cluster:id` | [Kubernetes Clusters](https://docs.oracle.com/iaas/Content/ContEng/Concepts/contengclustersnodes.htm#kubernetes_clusters) OCID  
`oci:core:image:id` | [Image](https://docs.oracle.com/iaas/Content/Compute/Concepts/computeoverview.htm#one) OCID  
`oci:core:instanceshape:name` | [Instance shape](https://docs.oracle.com/iaas/Content/Compute/References/computeshapes.htm) name  
`oci:core:natgateway:id` | [NAT gateway](https://docs.oracle.com/iaas/Content/Network/Tasks/NATgateway.htm) OCID  
`oci:core:nsg:id` | [Network security group](https://docs.oracle.com/iaas/Content/Network/Concepts/networksecuritygroups.htm) OCID  
`oci:core:servicegateway:id` | [Service gateway](https://docs.oracle.com/iaas/Content/Network/Tasks/servicegateway.htm) OCID  
`oci:core:ssh:publickey` | -- | Surfaces a control for adding one or more public SSH keys by dropping files or pasting key values. For more information, see [SSH key control](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Concepts/terraformconfigresourcemanager_topic-schema.htm#console-howto__ssh).  
`oci:core:subnet:id` | [Subnet](https://docs.oracle.com/iaas/Content/Network/Tasks/managingVCNs.htm) OCID  
`oci:core:vcn:id` | [VCN](https://docs.oracle.com/iaas/Content/Network/Tasks/managingVCNs.htm) OCID  
`oci:database:autonomouscontainerdatabase:id` | [Autonomous Container Database](https://docs.oracle.com/en/cloud/paas/autonomous-database/dedicated/adbaa/index.html#ADBAA-GUID-268B36E1-87D8-4649-A370-226E2AE3FC5C) OCID  
`oci:database:autonomousdatabase:id` | [Autonomous Database](https://docs.oracle.com/en/cloud/paas/autonomous-database/dedicated/adbaa/index.html#ADBAA-GUID-B5518C12-0362-4A98-AB35-3CB84AC83F31) OCID  
`oci:database:autonomousdatabaseversion:id` | [Autonomous Database](https://docs.oracle.com/en/cloud/paas/autonomous-database/dedicated/adbaa/index.html#ADBAA-GUID-B5518C12-0362-4A98-AB35-3CB84AC83F31) version  
`oci:database:database:id` | Database OCID for a [Base Database](https://docs.oracle.com/en/cloud/paas/base-database/index.html) service database, or an [Exadata Database Service on Dedicated Infrastructure](https://docs.oracle.com/en/engineered-systems/exadata-cloud-service/ecscm/index.html) database.  
`oci:database:dbhome:id` | DB home OCID (applies to [Base Database](https://docs.oracle.com/en/cloud/paas/base-database/index.html) and [Exadata Database Service on Dedicated Infrastructure](https://docs.oracle.com/en/engineered-systems/exadata-cloud-service/ecscm/index.html))  
`oci:database:dbsystem:id` | DB system OCID (applies to [Base Database](https://docs.oracle.com/en/cloud/paas/base-database/index.html))  
`oci:identity:availabilitydomain:name` | [Availability domain](https://docs.oracle.com/iaas/Content/General/Concepts/regions.htm) name  
`oci:identity:compartment:id` | [Compartment](https://docs.oracle.com/iaas/Content/GSG/Concepts/concepts-account.htm#conceptcompartment) OCID  
`oci:identity:domains:id` | [Identity domain](https://docs.oracle.com/iaas/Content/Identity/domains/overview.htm) OCID |  Specify the tenancy OCID as `compartmentId`. See [ListDomains](https://docs.oracle.com/iaas/api/#/en/identity/latest/DomainSummary/ListDomains).  
`oci:identity:dynamicgroups:id` | [Dynamic group](https://docs.oracle.com/iaas/Content/Identity/dynamicgroups/managingdynamicgroups.htm) OCID |  Specify the tenancy OCID as `compartmentId`. See [ListDynamicGroups](https://docs.oracle.com/iaas/api/#/en/identity/latest/DynamicGroup/ListDynamicGroups).  
`oci:identity:faultdomain:name` | [Fault domain](https://docs.oracle.com/iaas/Content/General/Concepts/regions.htm#fault) name  
`oci:identity:groups:id` | [Group](https://docs.oracle.com/iaas/Content/Identity/groups/managinggroups.htm) OCID |  Specify the tenancy OCID as `compartmentId`. See [ListGroups](https://docs.oracle.com/iaas/api/#/en/identity/latest/Group/ListGroups).  
`oci:identity:region:name` | [Region](https://docs.oracle.com/iaas/Content/General/Concepts/regions.htm) name  
`oci:identity:tag:value` | [Tag key name from tag namespace](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm); see [TagSummary](https://docs.oracle.com/iaas/api/#/en/identity/latest/TagSummary) | Surfaces a control for adding defined and freeform tags. For more information, see [Tagging control](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Concepts/terraformconfigresourcemanager_topic-schema.htm#console-howto__tag).  
`oci:kms:key:id` | [Vault key](https://docs.oracle.com/iaas/Content/KeyManagement/Tasks/managingkeys.htm) OCID; see [ListKeys](https://docs.oracle.com/iaas/api/#/en/key/latest/KeySummary/ListKeys)  
`oci:kms:secret:id` | [Vault secret](https://docs.oracle.com/iaas/Content/KeyManagement/Tasks/managingsecrets.htm) OCID; see [ListSecrets](https://docs.oracle.com/iaas/api/#/en/secretmgmt/latest/SecretSummary/ListSecrets)  
`oci:kms:vault:id` | [Vault](https://docs.oracle.com/iaas/Content/KeyManagement/Concepts/keyoverview.htm) OCID  
`oci:kubernetes:versions:id` | See [GetClusterOptions](https://docs.oracle.com/iaas/api/#/en/containerengine/latest/ClusterOptions/GetClusterOptions)  
`oci:loadbalancer:loadbalancer:id` | [load balancer](https://docs.oracle.com/iaas/Content/Balance/Concepts/balanceoverview.htm) OCID  
`oci:ods:project:id` | [Data Science project](https://docs.oracle.com/iaas/data-science/using/manage-projects.htm) OCID  
`oci:resourcemanager:privateendpoint:id` | [Resource Manager private endpoint](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/private-endpoints.htm#top "Create, edit, and delete private endpoints in Resource Manager.") OCID | Specify a compartment (`compartmentId`) and a VCN (`vcnId`) for listing private endpoints. For an example, see [Example declaration for private endpoints](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Concepts/terraformconfigresourcemanager_topic-schema.htm#console-howto__private-endpoints) on this page.  
## Meta Schema for Validation 🔗 
Use the following meta schema file to confirm that your schema document is using supported variable types.
[Meta Schema](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Concepts/terraformconfigresourcemanager_topic-schema.htm)
Copy
```
# Meta JSON Schema.
#
# This is used to validate the Schema file when the package is uploaded/loaded into Resource Manager.
# For marketplace, it is also used to validate the package when the package artifact is created in Partner Portal.
#
# NOTE: additionalProperties are set to true explicitly even though this is the default. It must be set to true in
# cases where we use the allOf. This is a quirk of JSON Schema. During validation, allOf means it has to match all of
# the individual definitions separately. It doesn't mean it has to match a Union of the individual definitions. This
# is a known issue with JSON Schema.
title: Schema
type: object
required:
 - variables
 - schemaVersion
additionalProperties: true
properties:
 title:
  type: string
 description:
  type: string
 stackDescription:
  type: string
 packageVersion:
  type: string
 version:
  type: string
 schemaVersion:
  type: string
  enum:
   - 1.0.0
   - 1.1.0
 locale:
  $ref: "#/definitions/locale"
 logoUrl:
  $ref: "#/definitions/url"
 source:
  $ref: "#/definitions/source"
 informationalText:
  type: string
 instructions:
  type: string
 troubleshooting:
  type: string
 allowViewState:
  type: boolean
 variables:
  $ref: "#/definitions/variables"
 # Deprecated - use variableGroups instead
 groupings:
  $ref: "#/definitions/variableGroups"
 variableGroups:
  $ref: "#/definitions/variableGroups"
 outputs:
  $ref: "#/definitions/outputs"
 outputGroups:
  $ref: "#/definitions/outputGroups"
 primaryOutputButton:
  type: string
  format: variablereference
definitions:
 source:
  type: object
  properties:
   type:
    enum:
     - marketplace
     - quickstart
     - web
   reference:
    type:
     - string
     - number
  additionalProperties: false
 variableGroups:
  type: array
  items:
   $ref: "#/definitions/variableGroup"
 variableGroup:
  type: object
  required:
   - title
   - variables
  properties:
   title:
    type: string
   variables:
    type: array
    items:
     type: string
     format: variablereference
   visible:
    $ref: "#/definitions/booleanStatement"
  additionalProperties: true
 locale:
  enum:
   - en
  default: en
 url:
  type: string
  pattern: ^https?:\/\/(www\.)?[-a-zA-Z0-9@:%._\+~#=]{2,256}\.[a-z]{2,4}\b([-a-zA-Z0-9@:%_\+.~#?&//=]*)$
 ocid:
  type: string
  pattern: ^ocid1\.([a-z0-9_-]{1,32})\.([a-z0-9_-]{1,15})\.([a-z0-9]{0,24})\.([a-z0-9]{60})$
 variables:
  type: object
  additionalProperties:
   $ref: "#/definitions/variable"
 variable:
  oneOf:
   - $ref: "#/definitions/staticVariable"
   - $ref: "#/definitions/dynamicVariable"
 baseVariable:
  type: object
  properties:
   title:
    type: string
    minLength: 1
   description:
    type: string
   required:
    type: boolean
    default: false
   visible:
    $ref: "#/definitions/booleanStatement"
 booleanStatement:
  oneOf:
   - type: boolean
   - type: string
   - $ref: "#/definitions/equality"
   - $ref: "#/definitions/greaterThanOrEqual"
   - $ref: "#/definitions/lessThanOrEqual"
   - $ref: "#/definitions/greaterThan"
   - $ref: "#/definitions/lessThan"
   - $ref: "#/definitions/booleanOr"
   - $ref: "#/definitions/booleanAnd"
   - $ref: "#/definitions/booleanNot"
 equality:
  type: object
  properties:
   eq:
    type: array
    items:
     - type: [string, number]
     - type: [string, number]
    additionalItems: false
  additionalProperties: false
 greaterThanOrEqual:
  type: object
  properties:
   ge:
    type: array
    items:
     - type: [string, number]
     - type: [string, number]
    additionalItems: false
  additionalProperties: false
 lessThanOrEqual:
  type: object
  properties:
   le:
    type: array
    items:
     - type: [string, number]
     - type: [string, number]
    additionalItems: false
  additionalProperties: false
 greaterThan:
  type: object
  properties:
   gt:
    type: array
    items:
     - type: [string, number]
     - type: [string, number]
    additionalItems: false
  additionalProperties: false
 lessThan:
  type: object
  properties:
   lt:
    type: array
    items:
     - type: [string, number]
     - type: [string, number]
    additionalItems: false
  additionalProperties: false
 booleanOr:
  type: object
  properties:
   or:
    type: array
    items:
     - $ref: "#/definitions/booleanStatement"
     - $ref: "#/definitions/booleanStatement"
    additionalItems: false
  additionalProperties: false
 booleanAnd:
  type: object
  properties:
   and:
    type: array
    items:
     - $ref: "#/definitions/booleanStatement"
     - $ref: "#/definitions/booleanStatement"
    additionalItems: false
  additionalProperties: false
 booleanNot:
  type: object
  properties:
   not:
    type: array
    items:
     - $ref: "#/definitions/booleanStatement"
    additionalItems: false
  additionalProperties: false
 dependsOnCompartment:
  allOf:
   - $ref: "#/definitions/baseVariable"
   - required:
     - dependsOn
    properties:
     dependsOn:
      type: object
      required:
       - compartmentId
      properties:
       compartmentId:
        type: string
        format: variablereference
      additionalProperties: false
    additionalProperties: true
 staticVariable:
  oneOf:
   - $ref: "#/definitions/arrayVariable"
   - $ref: "#/definitions/booleanVariable"
   - $ref: "#/definitions/enumVariable"
   - $ref: "#/definitions/integerVariable"
   - $ref: "#/definitions/numberVariable"
   - $ref: "#/definitions/stringVariable"
   - $ref: "#/definitions/multilineVariable"
   - $ref: "#/definitions/fileVariable"
   - $ref: "#/definitions/passwordVariable"
   - $ref: "#/definitions/datetimeVariable"
 dynamicVariable:
  oneOf:
   - $ref: "#/definitions/imageVariable"
   - $ref: "#/definitions/identityDomainVariable"
   - $ref: "#/definitions/instanceShapeVariable"
   - $ref: "#/definitions/subnetVariable"
   - $ref: "#/definitions/vcnVariable"
   - $ref: "#/definitions/availabilityDomainVariable"
   - $ref: "#/definitions/compartmentVariable"
   - $ref: "#/definitions/faultDomainVariable"
   - $ref: "#/definitions/regionVariable"
   - $ref: "#/definitions/dbSystemVariable"
   - $ref: "#/definitions/dbHomeVariable"
   - $ref: "#/definitions/dbHomeVersionVariable"
   - $ref: "#/definitions/databaseVariable"
   - $ref: "#/definitions/autonomousDatabaseVariable"
   - $ref: "#/definitions/autonomousDatabaseVersionVariable"
   - $ref: "#/definitions/autonomousContainerDBVariable"
   - $ref: "#/definitions/kmsVaultVariable"
   - $ref: "#/definitions/containerClusterVariable"
   - $ref: "#/definitions/volumeBackupPoliciesVariable"
   - $ref: "#/definitions/loadBalancerVariable"
   - $ref: "#/definitions/serviceGatewayVariable"
   - $ref: "#/definitions/kubernetesVersionsVariable"
   - $ref: "#/definitions/instanceVariable"
   - $ref: "#/definitions/natGatewayVariable"
   - $ref: "#/definitions/tagVariable"
   - $ref: "#/definitions/nsgVariable"
   - $ref: "#/definitions/mountTargetsVariable"
   - $ref: "#/definitions/kmsKeyVariable"
   - $ref: "#/definitions/kmsSecretVariable"
   - $ref: "#/definitions/odsProjectVariable"
   - $ref: "#/definitions/instanceShapeVariableWithFlex"
   - $ref: "#/definitions/groupsVariable"
   - $ref: "#/definitions/dynamicGroupsVariable"
   - $ref: "#/definitions/logAnalyticsLogGroup"
   - $ref: "#/definitions/logAnalyticsLogEntities"
   - $ref: "#/definitions/logAnalyticsScheduledTasks"
   - $ref: "#/definitions/logAnalyticsEntityTypes"
   - $ref: "#/definitions/managementAgents"
   - $ref: "#/definitions/logAnalyticsSources"
   - $ref: "#/definitions/privateEndpointVariable"
   - $ref: "#/definitions/apmDomainVariable"
 nonNegativeInteger:
  type: integer
  minimum: 0
 nonNegativeIntegerDefault0:
  allOf:
   - $ref: "#/definitions/nonNegativeInteger"
   - default: 0
 arrayVariable:
  allOf:
   - $ref: "#/definitions/baseVariable"
   - required: [type]
    properties:
     type:
      enum: [array]
     items:
      $ref: "#/definitions/variable"
     maxItems:
      $ref: "#/definitions/nonNegativeInteger"
     minItems:
      $ref: "#/definitions/nonNegativeIntegerDefault0"
     uniqueItems:
      type: boolean
      default: false
     contains:
      $ref: "#/definitions/variable"
    additionalProperties: true
 booleanVariable:
  allOf:
   - $ref: "#/definitions/baseVariable"
   - required: [type]
    properties:
     type:
      enum: [boolean]
     default:
      $ref: "#/definitions/booleanStatement"
      default: false
    additionalProperties: true
 enumVariable:
  allOf:
   - $ref: "#/definitions/baseVariable"
   - required: [type]
    properties:
     type:
      enum: [enum]
     enum:
      type: array
      items:
       type: string
     default:
      $ref: "#/definitions/booleanStatement"
     allowMultiple:
      type: boolean
      default: false
    additionalProperties: true
 integerVariable:
  allOf:
   - $ref: "#/definitions/baseVariable"
   - required: [type]
    properties:
     type:
      enum: [integer]
     default:
      type: integer
     multipleOf:
      type: number
      exclusiveMinimum: 0
     minimum:
      type: number
     maximum:
      type: number
     exclusiveMinimum:
      type: number
     exclusiveMaximum:
      type: number
    additionalProperties: true
 numberVariable:
  allOf:
   - $ref: "#/definitions/baseVariable"
   - required: [type]
    properties:
     type:
      enum: [number]
     default:
      type: number
     multipleOf:
      type: number
      exclusiveMinimum: 0
     minimum:
      type: number
     maximum:
      type: number
     exclusiveMinimum:
      type: number
     exclusiveMaximum:
      type: number
    additionalProperties: true
 stringVariable:
  allOf:
   - $ref: "#/definitions/baseVariable"
   - required: [type]
    properties:
     type:
      enum: [string]
     default:
      $ref: "#/definitions/booleanStatement"
     pattern:
      type: string
     maxLength:
      $ref: "#/definitions/nonNegativeInteger"
     minLength:
      $ref: "#/definitions/nonNegativeIntegerDefault0"
    additionalProperties: true
 multilineVariable:
  allOf:
   - $ref: "#/definitions/baseVariable"
   - required: [type]
    properties:
     type:
      enum: [text]
     default:
      $ref: "#/definitions/booleanStatement"
     pattern:
      type: string
     multiline:
      type: boolean
     maxLength:
      $ref: "#/definitions/nonNegativeInteger"
     minLength:
      $ref: "#/definitions/nonNegativeIntegerDefault0"
    additionalProperties: true
 fileVariable:
  allOf:
   - $ref: "#/definitions/baseVariable"
   - required: [type]
    properties:
     type:
      enum: [file]
    additionalProperties: true
 passwordVariable:
  allOf:
   - $ref: "#/definitions/baseVariable"
   - required: [type]
    properties:
     type:
      enum: [password]
     default:
      $ref: "#/definitions/booleanStatement"
     confirmation:
      $ref: "#/definitions/booleanStatement"
    additionalProperties: true
 datetimeVariable:
  allOf:
   - $ref: "#/definitions/baseVariable"
   - required: [type]
    properties:
     type:
      enum: [datetime]
     default:
      $ref: "#/definitions/booleanStatement"
    additionalProperties: true
 identityDomainVariable:
  allOf:
   - $ref: "#/definitions/baseVariable"
   - required:
     - type
     - dependsOn
    properties:
     type:
      enum: [oci:identity:domains:id]
     pattern:
      type: string
     dependsOn:
      type: object
      required:
       - compartmentId
      properties:
       compartmentId:
        type: string
        format: variablereference
      additionalProperties: false
    additionalProperties: true
 
 imageVariable:
  allOf:
   - $ref: "#/definitions/baseVariable"
   - required:
     - type
     - dependsOn
    properties:
     type:
      enum: [oci:core:image:id]
     pattern:
      type: string
     dependsOn:
      type: object
      required:
       - compartmentId
      properties:
       compartmentId:
        type: string
        format: variablereference
       shape:
        type: string
        format: variablereference
       operatingSystem:
        type: string
        format: variablereference
       operatingSystemVersion:
        type: string
        format: variablereference
      additionalProperties: false
    additionalProperties: true
 instanceShapeVariableWithFlex:
  allOf:
   - $ref: "#/definitions/baseVariable"
   - required:
     - type
     - dependsOn
    properties:
     type:
      enum: [oci:core:instanceshapewithflex:name]
     pattern:
      type: string
     dependsOn:
      type: object
      required:
       - compartmentId
      properties:
       imageId:
        type: string
        format: variablereference
       compartmentId:
        type: string
        format: variablereference
       availabilityDomain:
        type: string
        format: variablereference
      additionalProperties: false
    additionalProperties: true
 instanceShapeVariable:
  allOf:
   - $ref: "#/definitions/baseVariable"
   - required:
     - type
     - dependsOn
    properties:
     type:
      enum: [oci:core:instanceshape:name]
     pattern:
      type: string
     dependsOn:
      type: object
      required:
       - compartmentId
      properties:
       imageId:
        type: string
        format: variablereference
       compartmentId:
        type: string
        format: variablereference
       availabilityDomain:
        type: string
        format: variablereference
      additionalProperties: false
    additionalProperties: true
 natGatewayVariable:
  allOf:
   - $ref: "#/definitions/baseVariable"
   - required:
     - type
     - dependsOn
    properties:
     type:
      enum: [oci:core:natgateway:id]
     dependsOn:
      type: object
      required:
       - compartmentId
      properties:
       vcnId:
        type: string
        format: variablereference
       compartmentId:
        type: string
        format: variablereference
      additionalProperties: false
    additionalProperties: true
 instanceVariable:
  allOf:
   - $ref: "#/definitions/baseVariable"
   - required:
     - type
     - dependsOn
    properties:
     type:
      enum: [oci:core:instance:id]
     dependsOn:
      type: object
      required:
       - compartmentId
      properties:
       compartmentId:
        type: string
        format: variablereference
      additionalProperties: false
    additionalProperties: true
 subnetVariable:
  allOf:
   - $ref: "#/definitions/baseVariable"
   - required:
     - type
     - dependsOn
    properties:
     type:
      enum: [oci:core:subnet:id]
     dependsOn:
      type: object
      required:
       - vcnId
       - compartmentId
      properties:
       vcnId:
        type: string
        format: variablereference
       compartmentId:
        type: string
        format: variablereference
       hidePublicSubnet:
        $ref: "#/definitions/booleanStatement"
       hidePrivateSubnet:
        $ref: "#/definitions/booleanStatement"
       hideRegionalSubnet:
        $ref: "#/definitions/booleanStatement"
       hideAdSubnet:
        $ref: "#/definitions/booleanStatement"
      additionalProperties: false
    additionalProperties: true
 serviceGatewayVariable:
  allOf:
   - $ref: "#/definitions/baseVariable"
   - required:
     - type
     - dependsOn
    properties:
     type:
      enum: [oci:core:servicegateway:id]
     dependsOn:
      type: object
      required:
       - compartmentId
      properties:
       vcnId:
        type: string
        format: variablereference
       compartmentId:
        type: string
        format: variablereference
      additionalProperties: false
    additionalProperties: true
 logAnalyticsLogGroup:
  allOf:
   - $ref: "#/definitions/baseVariable"
   - required:
     - type
     - dependsOn
    properties:
     type:
      enum: [oci:logan:loggroup:id]
     dependsOn:
      type: object
      required:
       - compartmentId
      properties:
       compartmentId:
        type: string
        format: variablereference
      additionalProperties: false
    additionalProperties: true
 logAnalyticsScheduledTasks:
  allOf:
   - $ref: "#/definitions/baseVariable"
   - required:
     - type
     - dependsOn
    properties:
     type:
      enum: [oci:logan:scheduledtask:id]
     dependsOn:
      type: object
      required:
       - compartmentId
       - taskType
      properties:
       compartmentId:
        type: string
        format: variablereference
       taskType:
        type: string
      additionalProperties: false
    additionalProperties: true
 logAnalyticsLogEntities:
  allOf:
   - $ref: "#/definitions/baseVariable"
   - required:
     - type
     - dependsOn
    properties:
     type:
      enum: [oci:logan:logentity:id]
     dependsOn:
      type: object
      required:
       - compartmentId
      properties:
       compartmentId:
        type: string
        format: variablereference
      additionalProperties: false
    additionalProperties: true
 logAnalyticsEntityTypes:
  allOf:
   - $ref: "#/definitions/baseVariable"
   - required:
     - type
    properties:
     type:
      enum: [oci:logan:entitytype:id]
    additionalProperties: true
 managementAgents:
  allOf:
   - $ref: "#/definitions/baseVariable"
   - required:
     - type
     - dependsOn
    properties:
     type:
      enum: [oci:mgmt:agent:id]
     dependsOn:
      type: object
      required:
       - compartmentId
      properties:
       compartmentId:
        type: string
        format: variablereference
      additionalProperties: false
    additionalProperties: true
 logAnalyticsSources:
  allOf:
   - $ref: "#/definitions/baseVariable"
   - required:
     - type
     - dependsOn
    properties:
     type:
      enum: [oci:logan:source:id]
     dependsOn:
      type: object
      required:
       - compartmentId
      properties:
       compartmentId:
        type: string
        format: variablereference
      additionalProperties: false
    additionalProperties: true
 nsgVariable:
  allOf:
   - $ref: "#/definitions/baseVariable"
   - required:
     - type
     - dependsOn
    properties:
     type:
      enum: [oci:core:nsg:id]
     dependsOn:
      type: object
      required:
       - compartmentId
      properties:
       vcnId:
        type: string
        format: variablereference
       compartmentId:
        type: string
        format: variablereference
      additionalProperties: false
    additionalProperties: true
 vcnVariable:
  allOf:
   - $ref: "#/definitions/dependsOnCompartment"
   - required: [type]
    properties:
     type:
      enum: [oci:core:vcn:id]
    additionalProperties: true
 availabilityDomainVariable:
  allOf:
   - $ref: "#/definitions/dependsOnCompartment"
   - required: [type]
    properties:
     type:
      enum: [oci:identity:availabilitydomain:name]
    additionalProperties: true
 compartmentVariable:
  allOf:
   - $ref: "#/definitions/baseVariable"
   - required: [type]
    properties:
     type:
      enum: [oci:identity:compartment:id]
     default:
      $ref: "#/definitions/booleanStatement"
    additionalProperties: true
 faultDomainVariable:
  allOf:
   - $ref: "#/definitions/baseVariable"
   - required:
     - type
     - dependsOn
    properties:
     type:
      enum: [oci:identity:faultdomain:name]
     dependsOn:
      type: object
      required:
       - compartmentId
       - availabilityDomainName
      properties:
       compartmentId:
        type: string
        format: variablereference
       availabilityDomainName:
        type: string
        format: variablereference
      additionalProperties: false
    additionalProperties: true
 regionVariable:
  allOf:
   - $ref: "#/definitions/baseVariable"
   - required: [type]
    properties:
     type:
      enum: [oci:identity:region:name]
     default:
      $ref: "#/definitions/booleanStatement"
      default: ${session.region}
    additionalProperties: true
 dbSystemVariable:
  allOf:
   - $ref: "#/definitions/dependsOnCompartment"
   - required: [type]
    properties:
     type:
      enum: [oci:database:dbsystem:id]
    additionalProperties: true
 dbHomeVariable:
  allOf:
   - $ref: "#/definitions/baseVariable"
   - required:
     - type
     - dependsOn
    properties:
     type:
      enum: [oci:database:dbhome:id]
     dependsOn:
      type: object
      required:
       - dbSystemId
       - compartmentId
      properties:
       dbSystemId:
        type: string
        format: variablereference
       compartmentId:
        type: string
        format: variablereference
      additionalProperties: false
    additionalProperties: true
 dbHomeVersionVariable:
  allOf:
   - $ref: "#/definitions/baseVariable"
   - required:
     - type
     - dependsOn
    properties:
     type:
      enum: [oci:database:dbhome:dbversion]
     dependsOn:
      type: object
      required:
       - dbHomeId
      properties:
       dbHomeId:
        type: string
        format: variablereference
      additionalProperties: false
    additionalProperties: true
 databaseVariable:
  allOf:
   - $ref: "#/definitions/baseVariable"
   - required:
     - type
     - dependsOn
    properties:
     type:
      enum: [oci:database:database:id]
     dependsOn:
      type: object
      required:
       - dbHomeId
       - compartmentId
      properties:
       dbHomeId:
        type: string
        format: variablereference
       compartmentId:
        type: string
        format: variablereference
      additionalProperties: false
    additionalProperties: true
 autonomousDatabaseVariable:
  allOf:
   - $ref: "#/definitions/baseVariable"
   - required:
     - type
     - dependsOn
    properties:
     type:
      enum: [oci:database:autonomousdatabase:id]
     dependsOn:
      type: object
      required:
       - compartmentId
      properties:
       compartmentId:
        type: string
        format: variablereference
       dbWorkload:
        type: string
        format: variablereference
      additionalProperties: false
    additionalProperties: true
 autonomousDatabaseVersionVariable:
  allOf:
   - $ref: "#/definitions/baseVariable"
   - required:
     - type
     - dependsOn
    properties:
     type:
      enum: [oci:database:autonomousdatabaseversion:id]
     dependsOn:
      type: object
      properties:
       compartmentId:
        type: string
        format: variablereference
       dbWorkload:
        type: string
        format: variablereference
       additionalProperties: false
    additionalProperties: true
 autonomousContainerDBVariable:
  allOf:
   - $ref: "#/definitions/dependsOnCompartment"
   - required: [type]
    properties:
     type:
      enum: [oci:database:autonomouscontainerdatabase:id]
    additionalProperties: true
 kmsVaultVariable:
  allOf:
   - $ref: "#/definitions/dependsOnCompartment"
   - required: [type]
    properties:
     type:
      enum: [oci:kms:vault:id]
    additionalProperties: true
 kmsKeyVariable:
  allOf:
   - $ref: "#/definitions/baseVariable"
   - required:
     - type
     - dependsOn
    properties:
     type:
      enum: [oci:kms:key:id]
     dependsOn:
      type: object
      required:
       - compartmentId
       - vaultId
      properties:
       compartmentId:
        type: string
        format: variablereference
       vaultId:
        type: string
        format: variablereference
       protectionMode:
        type: string
        format: variablereference
       algorithm:
        type: string
        format: variablereference
       length:
        type: number
        format: variablereference
       curveId:
        type: string
        format: variablereference
      additionalProperties: false
    additionalProperties: true
 kmsSecretVariable:
  allOf:
   - $ref: "#/definitions/baseVariable"
   - required:
     - type
     - dependsOn
    properties:
     type:
      enum: [oci:kms:secret:id]
     dependsOn:
      type: object
      required:
       - compartmentId
      properties:
       compartmentId:
        type: string
        format: variablereference
       vaultId:
        type: string
        format: variablereference
       name:
        type: string
        format: variablereference
      additionalProperties: false
    additionalProperties: true
 containerClusterVariable:
  allOf:
   - $ref: "#/definitions/dependsOnCompartment"
   - required: [type]
    properties:
     type:
      enum: [oci:container:cluster:id]
    additionalProperties: true
 sshPublicKeyVariable:
  allOf:
   - $ref: "#/definitions/baseVariable"
   - required: [type]
    properties:
     type:
      enum: [oci:core:ssh:publickey]
    additionalProperties: true
 kubernetesVersionsVariable:
  allOf:
   - $ref: "#/definitions/baseVariable"
   - required:
     - type
     - dependsOn
    properties:
     type:
      enum: [oci:kubernetes:versions:id]
     dependsOn:
      type: object
      required:
       - clusterOptionId
       - compartmentId
      properties:
       clusterOptionId:
        type: string
        format: variablereference
       compartmentId:
        type: string
        format: variablereference
      additionalProperties: false
    additionalProperties: true
 volumeBackupPoliciesVariable:
  allOf:
   - $ref: "#/definitions/baseVariable"
   - required: [type]
    properties:
     type:
      enum: [oci:blockstorage:policies:id]
     dependsOn:
      type: object
      properties:
       compartmentId:
        type: string
        format: variablereference
      additionalProperties: false
    additionalProperties: true
 groupsVariable:
  allOf:
   - $ref: "#/definitions/dependsOnCompartment"
   - required: [type]
    properties:
     type:
      enum: [oci:identity:groups:id]
    additionalProperties: true
 dynamicGroupsVariable:
  allOf:
   - $ref: "#/definitions/dependsOnCompartment"
   - required: [type]
    properties:
     type:
      enum: [oci:identity:dynamicgroups:id]
    additionalProperties: true
 loadBalancerVariable:
  allOf:
   - $ref: "#/definitions/dependsOnCompartment"
   - required: [type]
    properties:
     type:
      enum: [oci:loadbalancer:loadbalancer:id]
     pattern:
      type: string
    additionalProperties: true
 mountTargetsVariable:
  allOf:
   - $ref: "#/definitions/baseVariable"
   - required:
     - type
     - dependsOn
    properties:
     type:
      enum: [oci:mount:target:id]
     dependsOn:
      type: object
      required:
       - compartmentId
       - availabilityDomain
      properties:
       availabilityDomain:
        type: string
        format: variablereference
       compartmentId:
        type: string
        format: variablereference
      additionalProperties: false
    additionalProperties: true
 tagVariable:
  allOf:
   - $ref: "#/definitions/dependsOnCompartment"
   - required: [type]
    properties:
     type:
      enum: [oci:identity:tag:value]
    additionalProperties: true
 odsProjectVariable:
  allOf:
   - $ref: "#/definitions/dependsOnCompartment"
   - required: [type]
    properties:
     type:
      enum: [oci:ods:project:id]
    additionalProperties: true
 privateEndpointVariable:
  allOf:
   - $ref: "#/definitions/baseVariable"
   - required: [type]
    properties:
     type:
      enum: [oci:resourcemanager:privateendpoint:id]
     dependsOn:
      type: object
      required:
       - compartmentId
       - vcnId
      properties:
       compartmentId:
        type: string
        format: variablereference
       vcnId:
        type: string
        format: variablereference
      additionalProperties: false
    additionalProperties: true
 apmDomainVariable:
  allOf:
   - $ref: "#/definitions/dependsOnCompartment"
   - required: [type]
    properties:
     type:
      enum: [oci:apm:domain:id]
    additionalProperties: true
 outputs:
  type: object
  additionalProperties:
   $ref: "#/definitions/output"
 output:
  oneOf:
   - $ref: "#/definitions/booleanOutput"
   - $ref: "#/definitions/numberOutput"
   - $ref: "#/definitions/stringOutput"
   - $ref: "#/definitions/copyableStringOutput"
   - $ref: "#/definitions/linkOutput"
   - $ref: "#/definitions/ocidOutput"
   - $ref: "#/definitions/mapOutput"
   - $ref: "#/definitions/jsonOutput"
   - $ref: "#/definitions/listOutput"
   - $ref: "#/definitions/csvOutput"
 outputGroups:
  type: array
  items:
   $ref: "#/definitions/outputGroup"
 outputGroup:
  type: object
  required:
   - title
   - outputs
  properties:
   title:
    type: string
   outputs:
    type: array
    items:
     type: string
  additionalProperties: true
 baseOutput:
  type: object
  properties:
   title:
    type: string
   description:
    type: string
   sensitive:
    type: boolean
    default: false
   format:
    type: string
   visible:
    type: boolean
    default: true
  additionalProperties: true
 booleanOutput:
  allOf:
   - $ref: "#/definitions/baseOutput"
   - required: [type]
    properties:
     type:
      enum: [boolean]
     value:
      type: boolean
    additionalProperties: true
 numberOutput:
  allOf:
   - $ref: "#/definitions/baseOutput"
   - required: [type]
    properties:
     type:
      enum: [number]
     value:
      type: number
    additionalProperties: true
 stringOutput:
  allOf:
   - $ref: "#/definitions/baseOutput"
   - required: [type]
    properties:
     type:
      enum: [string]
     value:
      type: string
    additionalProperties: true
 copyableStringOutput:
  allOf:
   - $ref: "#/definitions/baseOutput"
   - required: [type]
    properties:
     type:
      enum: [copyableString]
     value:
      type: string
    additionalProperties: true
 mapOutput:
  allOf:
   - $ref: "#/definitions/baseOutput"
   - required: [type]
    properties:
     type:
      enum: [map]
     value:
      type: object
    additionalProperties: true
 jsonOutput:
  allOf:
   - $ref: "#/definitions/baseOutput"
   - required: [type]
    properties:
     type:
      enum: [json]
     value:
      type: object
    additionalProperties: true
 listOutput:
  allOf:
   - $ref: "#/definitions/baseOutput"
   - required: [type]
    properties:
     type:
      enum: [list]
     value:
      type: array
    additionalProperties: true
 csvOutput:
  allOf:
   - $ref: "#/definitions/baseOutput"
   - required: [type]
    properties:
     type:
      enum: [csv]
     value:
      type: array
    additionalProperties: true
 linkOutput:
  allOf:
   - $ref: "#/definitions/baseOutput"
   - required: [type]
    properties:
     type:
      enum: [link]
     displayText:
      type: string
      minLength: 3
      maxLength: 45
     value:
      $ref: "#/definitions/url"
    additionalProperties: true
 ocidOutput:
  allOf:
   - $ref: "#/definitions/baseOutput"
   - required: [type]
    properties:
     type:
      enum: [ocid]
     value:
      $ref: "#/definitions/ocid"
    additionalProperties: true
```

## Example Schema Document 🔗 
Following is an example schema document.
[Example](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Concepts/terraformconfigresourcemanager_topic-schema.htm)
Copy
```
# Title shown in Application Information tab.
title: Sample input variable schema
# Sub Title shown in Application Information tab.
description: Sample description...
informationalText: Sample informational text to display in tab...
schemaVersion: 1.1.0
version: "20190304"
# URL of Logo Icon used on Application Information tab. Logo must be 130x130 pixels.
# (Optional)
logoUrl: https://cloudmarketplace.oracle.com/marketplace/content?contentId=53066708
# Used in Application Information tab to Hyperlink Title and Logo to the Marketplace
# Listing.
# Also used to link to Listing Usage section for "View Instructions".
# (Optional) If it is missing, Application Information uses the
# "marketplace-listing-id" tag for the same purpose.
source:
 type: marketplace
 reference: 16132843
locale: "en"
variableGroups:
 - title: "Node Configuration"
  variables:
   - targetCompartment
   - ${nodeCount}
   - ${nodeShapes}
   - ${availability}
 - title: "Application Details"
  variables:
   - ${username}
   - ${password}
   - ${dnsServers}
 - title: "Subnet"
  variables:
   - ${vcnCompartment}
   - ${myVcn}
   - ${subnetCompartment}
   - ${mySubnet}
   - ${mySubnetWithFilter}
   - ${hide_public_subnet}
   - ${hide_private_subnet}
   - ${hide_regional_subnet}
   - ${hide_ad_subnet}
 - title: "Network Configuration"
  variables:
   - ${service_gateway}
   - ${nat_gateway}
   - ${load_balancer}
   - ${myNsg}
   - ${Kubernetes_version}
   - ${backup_policies}
   - ${mount_target}
 - title: "Existing Groups"
  variables:
   - ${iam_groups_use_existing}
 - title: "Identity"
  variables:
   - ${iam_groups}
   - ${iam_dynamic_groups}
   - ${iam_domains}
 - title: "Database"
  variables:
   - ${dbCompartment}
   - ${myDbSystem}
   - ${myDbHome}
   - ${myDb}
   - ${myAutonomousDB}
   - ${myAutonomousDBVersion}
 - title: "Advanced"
  variables:
   - ${myImageId}
   - ${myInstance}
   - ${myShape}
   - ${myCompatibleShape}
   - ${myCompatibleShapeBasedOnAd}
   - ${multilineText}
  visible: true
 - title: "Hidden"
  variables:
   - ${myRegion}
  visible: false
 - title: "Existing Vcn"
  variables:
   - ${myVcn}
  visible:
   or:
    - ${useExistingVcn}
    - and:
      - and:
        - true
        - true
      - not:
        - false
 - title: "Password can't be 'password'!"
  variables:
   - ${password}
 - title: "Complex Conditional Section"
  variables:
   - ${myVcn}
  visible:
   or:
    - ${useExistingVcn}
    - and:
      - and:
        - true
        - true
      - not:
        - false
 - title: "Equality Conditional Section"
  variables:
   - ${myVcn}
  visible:
   eq:
    - ${objectStorageTier}
    - standard
 - title: "Less than Conditional Section"
  variables:
   - ${myVcn}
  visible:
   lt:
    - ${availability}
    - 5
 - title: "Less than or Equal Conditional Section"
  variables:
   - ${myVcn}
  visible:
   le:
    - ${availability}
    - 4
 - title: "Greater than Conditional Section"
  variables:
   - ${myVcn}
  visible:
   gt:
    - ${availability}
    - 5
 - title: "Greater than or Equal Conditional Section"
  variables:
   - ${myVcn}
  visible:
   ge:
    - ${availability}
    - 4
 - title: "Vault section"
  variables:
   - ${myVault}
   - ${myVaultKey}
   - ${mode}
   - ${myCompatibleKey}
   - ${algo}
   - ${myCompatibleKeyBasedOnAlgo}
   - ${mySecret}
   - ${myVaultSecret}
 - title: "DataScience"
  variables:
   - ${ods_project_ocid}
 - title: "Generic File"
  variables:
   - ${generic_file}
 - title: "Resource Tagging"
  variables:
   - ${tag}
 - title: "Resource Manager Section"
  variables:
   - ${private_endpoint_ocid}
 - title: "APM Domain Selection"
  variables:
   - ${apmDomain}
variables:
 # string field
 username:
  type: string
  minLength: 1
  maxLength: 255
  pattern: "^[a-z][a-zA-Z0-9]+$"
  # title is used as the label if present
  title: Username
  # description used as the tooltip if present
  description: Enter your username
  default: admin
  required: true
 # password field
 password:
  description: Really Bad Password Field
  type: password
  pattern: "^[a-zA-z]{1,8}$"
  required: true
 # integer field
 nodeCount:
  type: integer
  description: Number of Nodes
  minimum: 3
  maximum: 12
  multipleOf: 3
 # non-integer number field
 availability:
  type: number
  default: 99.7
  maximum: 100
  minimum: 0
 # string enum
 objectStorageTier:
  type: enum
  enum:
   - archive
   - standard
  allowMultiple: false
 # input a list, each element must be an ip addresses
 dnsServers:
  type: array
  items:
   type: string
   pattern: "^(?:(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\\.){3}(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)$"
  minItems: 1
  uniqueItems: true
  default: [8.8.8.8, 8.8.4.4]
 # datetime picker
 expireDate:
  type: datetime
 # compartmentId dynamic dropdown, targetCompartment present in input variables
 targetCompartment:
  type: oci:identity:compartment:id
 # ---- subnet picker ---- #
 useExistingVcn:
  type: boolean
 vcnCompartment:
  type: oci:identity:compartment:id
  visible: ${useExistingVcn}
 myVcn:
  type: oci:core:vcn:id
  dependsOn:
   compartmentId: ${vcnCompartment}
  visible:
   or:
    - ${useExistingVcn}
    - and:
      - and:
        - true
        - true
      - not:
        - false
 subnetCompartment:
  type: oci:identity:compartment:id
  visible: ${useExistingVcn}
 mySubnet:
  type: oci:core:subnet:id
  dependsOn:
   compartmentId: ${subnetCompartment}
   vcnId: ${myVcn}
  visible: ${useExistingVcn}
 mySubnetWithFilter:
  type: oci:core:subnet:id
  dependsOn:
   compartmentId: ${subnetCompartment}
   vcnId: ${myVcn}
   hidePublicSubnet: ${hide_public_subnet}
   hidePrivateSubnet: ${hide_private_subnet}
   hideRegionalSubnet: ${hide_regional_subnet}
   hideAdSubnet: ${hide_ad_subnet}
  visible: ${useExistingVcn}
 hide_public_subnet:
  type: boolean
  default: false
 hide_private_subnet:
  type: boolean
  default: false
 hide_regional_subnet:
  type: boolean
  default: false
 hide_ad_subnet:
  type: boolean
  default: false
 load_balancer:
  type: oci:loadbalancer:loadbalancer:id
  pattern: ^(10)Mbps.*$
  title: Existing LBaaS for "Application" Evaluation
  required: true
  dependsOn:
   compartmentId: ${vcnCompartment}
 Kubernetes_version:
  type: oci:kubernetes:versions:id
  title: Kubernetes version
  description: The Oracle cloud kubernetes version for tenancy.
  required: true
  visible: true
  dependsOn:
   compartmentId: ${vcnCompartment}
   clusterOptionId: "all"
 backup_policies:
  type: oci:blockstorage:policies:id
  title: Backup Policy
  description: The Oracle Cloud Backup Policy for tenancy.
  required: true
 mount_target:
  type: oci:mount:target:id
  title: Mount target
  description: The Oracle Cloud mount target
  dependsOn:
   compartmentId: ${targetCompartment}
   availabilityDomain: ${myAvailabilityDomain}
 myNsg:
  type: oci:core:nsg:id
  title: "Network Security Group"
  description: "Network Security Group description"
  dependsOn:
   compartmentId: ${vcnCompartment}
 service_gateway:
  type: oci:core:servicegateway:id
  title: NAT Gateway
  dependsOn:
   compartmentId: ${vcnCompartment}
   vcnId: ${myVcn}
 nat_gateway:
  type: oci:core:servicegateway:id
  title: NAT Gateway
  dependsOn:
   compartmentId: ${vcnCompartment}
   vcnId: ${myVcn}
 iam_groups_use_existing:
  type: boolean
  title: Use existing Groups
  required: true
  default: false
 iam_groups:
  type: oci:identity:groups:id
  title: Group Name
  dependsOn:
   compartmentId: ${targetCompartment}
  visible:
   or:
    - ${iam_groups_use_existing}
    - and:
      - and:
        - true
        - true
      - not:
        - false
 iam_dynamic_groups:
  type: oci:identity:dynamicgroups:id
  title: Dynamic Group Name
  dependsOn:
   compartmentId: ${targetCompartment}
  visible:
   or:
    - ${iam_groups_use_existing}
    - and:
      - and:
        - true
        - true
      - not:
        - false
 
 iam_domains:
  type: oci:identity:domains:id
  title: Domain Name
  dependsOn:
   compartmentId: ${targetCompartment}
  visible:
   or:
    - ${iam_groups_use_existing}
    - and:
      - and:
        - true
        - true
      - not:
        - false
 myRegion:
  type: oci:identity:region:name
  visible: false
 myImageId:
  type: oci:core:image:id
  dependsOn:
   compartmentId: ${targetCompartment}
 myShape:
  type: oci:core:instanceshape:name
  dependsOn:
   compartmentId: ${targetCompartment}
 myInstance:
  type: oci:core:instance:id
  dependsOn:
   compartmentId: ${targetCompartment}
 myCompatibleShape:
  type: oci:core:instanceshape:name
  dependsOn:
   compartmentId: ${targetCompartment}
   imageId: ${myImageId}
  visible:
   or:
    - ${useExistingVcn}
    - and:
      - and:
        - true
        - true
      - not:
        - false
 myCompatibleShapeBasedOnAd:
  type: oci:core:instanceshape:name
  dependsOn:
   compartmentId: ${targetCompartment}
   availabilityDomain: ${myAvailabilityDomain}
  visible:
   or:
    - ${useExistingVcn}
    - and:
      - and:
        - true
        - true
      - not:
        - false
 myAvailabilityDomain:
  type: oci:identity:availabilitydomain:name
  dependsOn:
   compartmentId: ${targetCompartment}
  visible: complexExpression
 myFaultdomain:
  type: oci:identity:faultdomain:name
  dependsOn:
   compartmentId: ${targetCompartment}
   availabilityDomainName: ${myAvailabilityDomain}
 dbCompartment:
  type: oci:identity:compartment:id
 myDbSystem:
  type: oci:database:dbsystem:id
  dependsOn:
   compartmentId: ${dbCompartment}
 myDbHome:
  type: oci:database:dbhome:id
  dependsOn:
   dbSystemId: ${myDbSystem}
   compartmentId: ${dbCompartment}
 myDbHomeVersion:
  type: oci:database:dbhome:dbversion
  dependsOn:
   dbHomeId: ${myDbHome}
 myDb:
  type: oci:database:database:id
  dependsOn:
   dbHomeId: ${myDbHome}
   compartmentId: ${dbCompartment}
 myAutonomousDB:
  type: oci:database:autonomousdatabase:id
  dependsOn:
   compartmentId: ${dbCompartment}
   dbWorkload: "DW"
 myAutonomousDBVersion:
  type: oci:database:autonomousdatabaseversion:id
  title: AutonomousDatabaseVersionTitle
  description: AutonomousDatabaseVersionDescription
  required: true
  default: "19c"
  dependsOn:
   compartmentId: ${compartment_ocid}
   dbWorkload: "AJD"
 container_cluster_ocid:
  type: oci:container:cluster:id
  required: true
  title: OKE Cluster
  description: Kubernetes cluster managed by OCI Container Engine for Kubernetes
  dependsOn:
   compartmentId: ${compartment_ocid}
 myVault:
  type: oci:kms:vault:id
  title: "vault"
  description: "vault"
  dependsOn:
   compartmentId: ${targetCompartment}
 myVaultKey:
  type: oci:kms:key:id
  title: "key"
  description: "key"
  dependsOn:
   compartmentId: ${targetCompartment}
   vaultId: ${myVault}
 mode:
  type: enum
  enum:
   - Hsm
   - Software
  allowMultiple: false
 myCompatibleKey:
  type: oci:kms:key:id
  title: "key"
  description: "key"
  dependsOn:
   compartmentId: ${targetCompartment}
   vaultId: ${myVault}
   protectionMode: ${mode}
 algo:
  type: enum
  enum:
   - AES
   - RSA
   - ECDSA
  allowMultiple: true
 myCompatibleKeyBasedOnAlgo:
  type: oci:kms:key:id
  title: "key"
  description: "key"
  dependsOn:
   compartmentId: ${targetCompartment}
   vaultId: ${myVault}
   protectionMode: ${mode}
   algorithm: ${algo}
 mySecret:
  type: "oci:kms:secret:id"
  title: "secret"
  description: "secret"
  dependsOn:
   compartmentId: ${targetCompartment}
 myVaultSecret:
  type: "oci:kms:secret:id"
  title: "secret"
  description: "secret"
  dependsOn:
   compartmentId: ${targetCompartment}
   vaultId: ${myVault}
 ods_project_ocid:
  type: oci:ods:project:id
  required: true
  title: odsProject
  description: "Select ods project from list"
  dependsOn:
   compartmentId: ${targetCompartment}
 generic_file:
  type: file
  required: true
  title: GenericFile
  description: "Drop a raw file (stored as base64 string data)"
 tag:
  type: oci:identity:tag:value
  required: true
  title: Tagging
  description: Tag value for resource created
  dependsOn:
   compartmentId: ${targetCompartment}
 private_endpoint_ocid:
  type: oci:resourcemanager:privateendpoint:id
  required: true
  title: privateEndpoint
  description: "Resource Manager Private Endpoint for Private Access"
  dependsOn:
   compartmentId: ${targetCompartment}
   vcnId: ${vcnId}
 multilineText:
  type: text
  required: false
  multiline: true
  title: Multi-line value
  description: Multi-line value
  default: "First line\nSecond line\nThird line"
 apmDomainVariable:
  type: oci:apm:domain:id
  title: "APM Domain"
  description: "APM Domain"
  dependsOn:
   compartmentId: ${targetCompartment}
# Used to present outputs with more refinement on the Application Information tab.
# The Application Information tab is only shown if the schema has a "title",
# "description", and at least one output in this "outputs" section.
#
# type:
#  - boolean
#  - string
#  - number
#  - link - contains url that can be hyperlinked. If type is not specified and the
#      value is a proper url, this type is assumed.
#  - ocid - contains an OCID. An attempt is made to hyperlink it to the designated
#      resource in the console.
#  - csv - synonym for list. Array of values converted to a comma separated list.
#  - json - synonym for map. Map of key / values converted to JSON.
#  - list - array of values converted to a comma separated list.
#  - map - map of key / values converted to JSON.
#
# displayText: used in links to give text displayed instead of value
# title: friendly label
# visible: if false, this ouptut is not shown in the outputs section of Application Information.
#     It can still be used as the primaryOutputButton.
outputs:
 controlCenterUrl:
  type: link
  title: Control Center
  displayText: Control Center
  visible: false
 schemaRegistryUrl:
  type: link
  title: Schema Registry
  displayText: Schema Registry
 schemaRegistryPublicIps:
  type: csv
  title: Public IPs
 schemaRegistryLoadBalancer:
  type: ocid
  title: Load Balancer
 brokerPublicIps:
  type: csv
 connectUrl:
  type: link
  title: Connect
  displayText: Connect
 connectPublicIps:
  type: csv
  title: Public IPs
 restUrl:
  type: link
  title: Rest API
# primaryOutputButton is a reference to a link output that creates a primary button
# on the Application Information tab.
# (Optional) if not provided, no primary button is shown. Also if the output
# referenced is not a link output, no button is shown.
primaryOutputButton: ${controlCenterUrl}
# Used to group Outputs. Any outputs not included in these defined groups, are
# included in a default group labelled "Outputs".
# (Optional) if not groups are given, outputs are not grouped at all.
outputGroups:
 - title: Schema Registry
  outputs:
   - ${schemaRegistryUrl}
   - ${schemaRegistryPublicIps}
   - ${schemaRegistryInstances}
   - ${schemaRegistryLoadBalancer}
 - title: Broker / Connect
  outputs:
   - ${brokerPublicIps}
   - ${brokerInstances}
   - ${connectUrl}
   - ${connectPublicIps}
   - ${restUrl}
```

## How to Control Console Items 🔗 
Use a schema document to control the display of stack variables and other items on stack details pages in the Console.
This display control is available for stacks created from a Terraform configuration file. Using a schema document, you can define how variables look and behave during stack creation and what text is displayed in the **Application information** tab for a created stack.
Following are Console display items that the schema document controls. To see relevant instructions and examples, expand a display item that you're interested in.
[Field label and description](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Concepts/terraformconfigresourcemanager_topic-schema.htm)
To render a field label and description for a variable:
  * Add the lines `title: <field_label>` and `description: <field_description>`.


Example image for a variable field label and description:
[![Advanced logging field with description "Enable or disable advanced logging \(VCN flow logs and/or audit logs\)."](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Images/resourcemanager_var-fieldlabeldescr.png)](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Images/resourcemanager_var-fieldlabeldescr.png)
Example declaration for a variable field label and description:
```
 advanced_logging_option:
  type: enum
  description: "Enable or disable advanced logging (VCN flow logs and/or audit logs)."
  title: "Advanced logging"
```

[Default value](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Concepts/terraformconfigresourcemanager_topic-schema.htm)
To render a variable with a default value:
  * Add the line `default:                 <default-value>`.


Example image for a variable with a default value:
[![Default value "DataScienceGroup" for variable Group name for security policies.](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Images/resourcemanager_var-default.png)](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Images/resourcemanager_var-default.png)
Example declaration for a default value:
```
 ods_group_name:
  type: string
  title: ${Messages.solutionsHub.solutions.dataScience.variables.ods_group_name.title()}
  description: ${Messages.solutionsHub.solutions.dataScience.variables.ods_group_name.description()}
  required: true
 # provide a default value
  default: "DataScienceGroup"
```

[Multiline text field](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Concepts/terraformconfigresourcemanager_topic-schema.htm)
To render a variable as a multiline text field:
  * Add the line `multiline: true`.


To declare a default value with multiple lines:
  * Separate each line with `\n`.


Example image for a variable rendered as a multiline text field, with two lines of text entered:
[![Multiline text field, with two lines of text entered.](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Images/resourcemanager_var-multiline.png)](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Images/resourcemanager_var-multiline.png)
Example declaration for a multiline text field:
```
 otherNames:
  type: text
  required: false
  multiline: true
  title: "Other Names"
  description: "Enter one name per line."
  default: "Name1\nName2"
```

[Group and order](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Concepts/terraformconfigresourcemanager_topic-schema.htm)
To render a group (box) of variables, with the variables in a prescribed sequence:
  * Add a `variableGroups` block.
  * Add a `title` line to this block.
  * Add a `variables` block to `variableGroups`.
  * Add variables to the `variables` block in the order that you want.


Example image for a group of variables:
[![Variable group WordPress configuration containing fields for username and password.](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Images/resourcemanager_var-group.png)](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Images/resourcemanager_var-group.png)
Example declaration for a group of variables with a prescribed order:
```
variableGroups:
 - title: "WordPress configuration"
  variables:
  - wp_admin_user
  - wp_admin_password
```

[SSH key control](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Concepts/terraformconfigresourcemanager_topic-schema.htm)
To render a variable as an SSH key control:
  * Add the line `type: oci:core:ssh:publickey`.


Example image for an SSH key control:
[![SSH key control.](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Images/resourcemanager_var-ssh.png)](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Images/resourcemanager_var-ssh.png)
Example declaration for an SSH key control:
```
 ssh_public_key:
  title: SSH public key
  description: Public SSH key to be included in the ~/.ssh/authorized_keys file for the default user on the instance
  # renders variable as an SSH key control
  type: oci:core:ssh:publickey
  additionalProps:
   allowMultiple: true
  required: false
  default: [""]
  pattern: "((^(ssh-rsa AAAAB3NzaC1yc2|ecdsa-sha2-nistp256 AAAAE2VjZHNhLXNoYTItbmlzdHAyNT|ecdsa-sha2-nistp384 AAAAE2VjZHNhLXNoYTItbmlzdHAzODQAAAAIbmlzdHAzOD|ecdsa-sha2-nistp521 AAAAE2VjZHNhLXNoYTItbmlzdHA1MjEAAAAIbmlzdHA1Mj|ssh-ed25519 AAAAC3NzaC1lZDI1NTE5|ssh-dss AAAAB3NzaC1kc3)[0-9A-Za-z+\/]+[=]{0,3})( [^,]*)?)(,((ssh-rsa AAAAB3NzaC1yc2|ecdsa-sha2-nistp256 AAAAE2VjZHNhLXNoYTItbmlzdHAyNT|ecdsa-sha2-nistp384 AAAAE2VjZHNhLXNoYTItbmlzdHAzODQAAAAIbmlzdHAzOD|ecdsa-sha2-nistp521 AAAAE2VjZHNhLXNoYTItbmlzdHA1MjEAAAAIbmlzdHA1Mj|ssh-ed25519 AAAAC3NzaC1lZDI1NTE5|ssh-dss AAAAB3NzaC1kc3)[0-9A-Za-z+\/]+[=]{0,3})( [^,]*)?)*$"
```

[File control](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Concepts/terraformconfigresourcemanager_topic-schema.htm)
To render a variable as a file control:
  * Add the line `type: file`.
**Note** The uploaded file is stored in Base64 format. To use the file, decode the output. For example, add the following code to an `outputs.tf` file in the Terraform configuration.```
output "generic_file_raw" {
 value = base64decode(var.generic_file)
}
```



Example image for a file control:
[![File control.](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Images/resourcemanager_var-file.png)](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Images/resourcemanager_var-file.png)
Example declaration for a file control:
```
 generic_file:
  type: file
  title: generic_file
  description: Drop any file or browse
  required: true
```

[Tagging control](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Concepts/terraformconfigresourcemanager_topic-schema.htm)
To render a variable as a tagging control:
  * Add the line `type: oci:identity:tag:value`.
**Note** To prepopulate tag values in the Console, access the values from the Terraform configuration. For example, add the following code to a `main.tf` file in the Terraform configuration.```
resource "oci_logging_log_group" "sample_log_group" {
 compartment_id = var.compartment_ocid
 display_name  = "sample_log_group"
 description  = "Prepopulated tag values"
 freeform_tags = var.tag_value.freeformTags
 defined_tags  = var.tag_value.definedTags
}
```



Example image for a tagging control:
[![Tagging control.](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Images/resourcemanager_var-tag.png)](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Images/resourcemanager_var-tag.png)
Example declaration for a tagging control:
```
 tag_value:
  type: oci:identity:tag:value
  title: Tags
  required: true
```

[Dynamic prepopulation](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Concepts/terraformconfigresourcemanager_topic-schema.htm)
To dynamically prepopulate variables with values based on dependencies:
  * Add the lines `type:                 <supported-type>` and `dependsOn:                   <other_variable>`.
<supported-type> is a type listed at [Supported Types (Dynamic Prepopulation and Controls)](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Concepts/terraformconfigresourcemanager_topic-schema.htm#types).


Example image for a dynamically prepopulated variable:
[![Pre-populated values for Virtual cloud network \(VCN\) field.](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Images/resourcemanager_var-prepop.png)](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Images/resourcemanager_var-prepop.png)
Example declaration for a dynamically prepopulated variable:
```
  vcn_ocid:
  "title": "Virtual cloud network (VCN)",
  "description": "The virtual cloud network to use with the compute instance. You can use the subnets template to create a VCN."
  # prepopulates available values for VCN
   type: oci:core:vcn:id
  # determines values for prepopulation from selected compartment
   dependsOn:
    compartmentId: compartment_ocid
   required: true
   default: ""
```

Example declaration for private endpoints:
```
 private_endpoint_ocid:
  type: oci:resourcemanager:privateendpoint:id
  required: true
  title: "Resource Manager Private Endpoint"
  description: "Resource Manager Private Endpoint for Private Access"
  dependsOn:
   compartmentId: ${privateEndpointCompartmentOCID}
   vcnId: ${privateEndpointVCNOCID}
```

Example declarations for VCN depending on compartment, with subnet depending on both compartment and VCN:
```
 vcnCompartment:
  # prepopulates available values for compartment
  type: oci:identity:compartment:id
 
myVcn:
  # prepopulates available values for VCN
  type: oci:core:vcn:id
  # determines values for VCN prepopulation from selected compartment
  dependsOn:
   compartmentId: ${vcnCompartment}
 
subnetCompartment:
  # prepopulates available values for compartment
  type: oci:identity:compartment:id
 
mySubnet:
  # prepopulates available values for subnet
  type: oci:core:subnet:id
  # determines values for subnet prepopulation from selected compartment and VCN
  dependsOn:
   compartmentId: ${subnetCompartment}
   vcnId: ${myVcn}
```

Image example declaration 1, where image depends on compartment only (the one mandatory `dependsOn` field):
```
 instance_image:  
  title: Image  
  description: Image  
  type: oci:core:image:id  
  required: true  
  dependsOn:   
    compartmentId: ${compartment_ocid}
```

Image example declaration 2, where image depends on compartment, operating system, operating system version, and shape:
```
 instance_image:  
  title: Image  
  description: Image  
  type: oci:core:image:id  
  required: true  
  dependsOn:   
    compartmentId: ${compartment_ocid}   
    operatingSystem: "Oracle Linux"   
    operatingSystemVersion: "7.8"
    shape: "<shape name>"
```

[Enumerated values (single value selection)](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Concepts/terraformconfigresourcemanager_topic-schema.htm)
To render enumerated values for a variable (allowing selection of one value):
  * Add the lines `type: enum` and add an `enum` block.


Example image for a variable with enumerated values that allow selection of a single value:
[![Enumerated values for the Advanced logging field.](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Images/resourcemanager_var-enum.png)](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Images/resourcemanager_var-enum.png)
Example declaration for a variable with enumerated values:
```
 advanced_logging_option:
  title: "Advanced logging"
  description: "Enable or disable advanced logging (VCN flow logs and/or audit logs)."
  type: enum
  # enumerated values
  enum:
  - AUDIT_LOGS
  - FLOW_LOGS
  - BOTH
  - NONE
  default: NONE
  required: true
```

[Enumerated values (multiple value selection)](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Concepts/terraformconfigresourcemanager_topic-schema.htm)
To render enumerated values for a variable (allowing selection of multiple values):
  * Add the lines `type: enum` and add an `enum` block.
  * Add the lines `additionalProps:` and add a `allowMultiple:true` block.


Example image for a variable with enumerated values that allow selection of multiple values:
[![This image shows a variable with enumerated values, where multiple values can be selected.](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Images/resourcemanager-schema-enum-multiselect-atttachment-type.png)](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Images/resourcemanager-schema-enum-multiselect-atttachment-type.png)
Example declaration for a variable with enumerated values (multiple value selection):
```
  attachment_type:
   type: enum
   title: "Attachment type"
   additionalProps:
    allowMultiple: true
   default: "iscsi"
   # enumerated values (multiple value selection)
   enum:
    - "iscsi"
    - "paravirtualized"
```

[Check box](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Concepts/terraformconfigresourcemanager_topic-schema.htm)
To render a variable as a check box:
  * Add the line `type: boolean`.


Example image for a check box variable:
[![Check box rendering for Enable vault support? variable.](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Images/resourcemanager_var-checkbox.png)](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Images/resourcemanager_var-checkbox.png)
Example declaration for a check box variable:
```
 ods_vcn_use_existing:
  # renders variable as a check box
  type: boolean
  title: "Enable vault support?"
  description: "Use a vault to store secrets and manage encrypted resources."
  required: true
  default: false
```

[Visibility dependency](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Concepts/terraformconfigresourcemanager_topic-schema.htm)
**Note**
Groups have higher priority than the groups' constituent variables. For example, if a variable is visible within a group that isn't visible, then the entire group isn't visible.
Supported operations: 
  * `and`
  * `eq` (equal)
  * `ge` (greater than or equal)
  * `gt` (greater than)
  * `le` (less than or equal)
  * `lt` (less than)
  * `not`
  * `or`


To hide or show variables or variable groups depending on other variables:
  * Add the line `visible: <other_variable>`. 


Example of variable **Use existing vault?** , whose visibility depends on the user selection for the variable **Enable vault support?** :
[![Use existing vault? is visible only when Enable vault support? is selected.](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Images/resourcemanager_var-checkbox-hide.png)](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Images/resourcemanager_var-checkbox-hide.png)
Example declarations that show the "Application Name" and "API Gateway Name" fields (`functions_app_name` and `apigateway_name`) only when the "Provision Functions and API Gateway?" check box (`enable_functions_apigateway`) is selected:
```
 enable_vault:
  type: boolean
  title: "Enable vault support?"
  description: "Use a vault to store secrets and manage encrypted resources."
  required: true
  default: false
 ods_use_existing_vault:
  type: boolean
  title: "Use existing vault?"
  description: "Use a pre-existing vault in the current compartment."
  required: true
  default: false
 # show only when enable_vault variable is selected
  visible: enable_vault
```

[Password](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Concepts/terraformconfigresourcemanager_topic-schema.htm)
To render a variable as a password:
  * Add the line `type: password`. 


To require re-entry for confirmation of the entered password:
  * Add the line `confirmation: true`. 


Example image for a password variable that requires confirmation:
[![Confirmation prompt for a password \(WordPress administrator password\).](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Images/resourcemanager_var-passwordconfirm.png)](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Images/resourcemanager_var-passwordconfirm.png)
Example declaration for a password variable, requiring confirmation:
```
 wp_admin_password:
  title: "WordPress administrator password"
  description: "The password must be more than 8 characters and include at least one uppercase letter, one lowercase letter, one number, and one of the following special characters: !@#%^*_+-:?.,[]{}"
  # renders variable as a password field
  type: password
  # renders a second field to re-enter the password for confirmation
  confirmation: true
  pattern: "^(?=.*[!@#%^*_+\\-:?.,\\[\\]\\{\\}])(?=.*[0-9])(?=.*[a-z])(?=.*[A-Z])(?!.*[$\\(\\)]).{8,32}$"
  required: true
```

[Required variables](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Concepts/terraformconfigresourcemanager_topic-schema.htm)
To require a value for a variable:
  * Add the line `required: true`.


Example image for a required variable, with validation warning:
[![Validation warning for a required variable \(Virtual cloud network \(VCN\)\) that wasn't populated.](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Images/resourcemanager_var-required.png)](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Images/resourcemanager_var-required.png)
Example declaration for a required variable:
```
  vcn_ocid:
  "title": "Virtual cloud network (VCN)",
  "description": "The virtual cloud network to use with the compute instance. You can use the subnets template to create a VCN."
   type: oci:core:vcn:id
   dependsOn:
    compartmentId: compartment_ocid
  # displays validation warning if no value is selected or entered
   required: true
   default: ""
```

[Optional variable](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Concepts/terraformconfigresourcemanager_topic-schema.htm)
To mark a variable as optional:
  * Add the line `required: false`.


Example image for an optional variable:
[!["Optional" marking displayed to the right of the variable's title: Private IP.](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Images/resourcemanager_var-optional.png)](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Images/resourcemanager_var-optional.png)
Example declaration for an optional variable:
```
  private_ip:
   title: "Private IP"
   description: "Private IP address of your choice to assign to the VNICs."
   type: string
   # displays "Optional" marking to right of field label
   required: false
   default: ""
```

[Validation pattern](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Concepts/terraformconfigresourcemanager_topic-schema.htm)
To validate the value entered for a variable against a regular expression pattern:
  * Add the line `pattern: <regular-expression>`.
<regular-expression> is the validation pattern specific to the value that you want to validate. 
Hyperlink pattern example: `^https?:\/\/(www\.)?[-a-zA-Z0-9@:%._\+~#=]{2,256}\.[a-z]{2,4}\b([-a-zA-Z0-9@:%_\+.~#?&//=]*)$`


Example image for a validation error for an entered value:
[![Validation error for an entered value \(WordPress administrator password\).](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Images/resourcemanager_var-pattern.png)](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Images/resourcemanager_var-pattern.png)
Example declaration for a variable with a validation pattern:
```
 wp_admin_password:
  title: "WordPress administrator password"
  description: "The password must be more than 8 characters and include at least one uppercase letter, one lowercase letter, one number, and one of the following special characters: !@#%^*_+-:?.,[]{}"
  type: password
  confirmation: true
  # validate entered value against alphanumeric regular expression
  pattern: "^(?=.*[!@#%^*_+\\-:?.,\\[\\]\\{\\}])(?=.*[0-9])(?=.*[a-z])(?=.*[A-Z])(?!.*[$\\(\\)]).{8,32}$"
  required: true
```

[Sensitive variables (Outputs tab, Application information tab)](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Concepts/terraformconfigresourcemanager_topic-schema.htm)
The output of a sensitive-marked variable displays as **< sensitive>** with [an **Unlock** option](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Concepts/terraformconfigresourcemanager_topic-schema.htm#console-interact__sensitive) in the **Application information** tab. This tab is visible in the **Job details** and **Stack details** pages.
Example image for a sensitive-marked variable (**Generated SSH private key**) on the **Application information** tab:
[![Sensitive-marked variable in Application information tab.](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Images/resourcemanager-sensitive-app-unlock.png)](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Images/resourcemanager-sensitive-app-unlock.png)
For more information about the Terraform sensitive argument, see [sensitive - Suppressing Values in CLI Output](https://developer.hashicorp.com/terraform/language/values/outputs#sensitive-suppressing-values-in-cli-output).
To mark a variable as sensitive:
  * Add the line `sensitive: true`.


Example declaration for a sensitive-marked variable:
```
 ssh_private_key:
  title: Generated SSH private key
  # marks variable as sensitive
  sensitive: true
```

[Application information tab](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Concepts/terraformconfigresourcemanager_topic-schema.htm)
To display the **Application information** tab for a stack created from your Terraform configuration:
  * Add lines for the schema `title` and `description`.
  * Optionally add a line for a blue informational text box: `informationalText`.
  * Add at least one output in the `outputs` section, optionally grouped using `outputGroups`.


To allow copying of an output value displayed in the **Application information** tab:
  * Set the type: Add the line `type: copyableString`.


Example image for the **Application information** tab:
[![Application information tab.](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Images/resourcemanager_var-appinfo.png)](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Images/resourcemanager_var-appinfo.png)
Example declaration for a schema title, description, and outputs:
```
# heading under Application Information tab
title: "Deploy a WordPress instance"
# text under heading
description: "Create your own website or blog using WordPress."
...
# output variable groups
outputGroups:
- title: "Service endpoints"
 outputs:
  - wordpress_public_ip
- title: "Generated passwords"
 outputs:
  - generated_ssh_private_key
...
# output variable field names and values
outputs:
 wordpress_public_ip:
  type: link
  title: "Your WordPress website"
 generated_ssh_private_key:
  title: "Generated SSH private key"
  sensitive: true
```

## How to Interact with Console Items 🔗 
This section describes how to interact with schema-controlled display of stack information in the Oracle Cloud Infrastructure Console.
Stack information is affected by the schema document (if any) that you include in the Terraform configuration for creating the stack. The schema document affects how variables look and behave during stack creation and what text is displayed in the **Application Information** tab for a created stack.
[Unlock sensitive variables](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Concepts/terraformconfigresourcemanager_topic-schema.htm)
An **Unlock** option on the **Application information** tab indicates a [sensitive-marked variable](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Concepts/terraformconfigresourcemanager_topic-schema.htm#console-howto__sensitive). This option switches between **Unlock** and **Lock**.
  * To view the value, select **Unlock**.
  * To hide the value, select **Lock**.


Example image for a sensitive-marked variable (**Generated SSH private key**) on the **Application information** tab:
[![Screenshot of Application information tab with a sensitive-marked variable \(Generated SSH private key\).](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Images/resourcemanager-sensitive-app-unlock.png)](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Images/resourcemanager-sensitive-app-unlock.png)
Was this article helpful?
YesNo

