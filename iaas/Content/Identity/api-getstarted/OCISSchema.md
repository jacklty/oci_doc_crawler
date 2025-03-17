Updated 2024-04-02
# SCIM Schema Overview
A schema is a collection of attribute definitions that describe the contents of an entire or partial resource, for example, `urn:ietf:params:scim:schemas:core:2.0:User.` The attribute definitions specify the name of the attribute, and metadata such as type (string, binary), cardinality (singular, multi, complex), mutability, and returnability.
## Attribute Notation 🔗 
All identity domain SCIM API operations share a common scheme for referencing simple and complex attributes. In general, attributes are identified by prefixing the attribute name with its schema uniform resource name (URN), separated by a colon (`:`) character. For example, the core User resource attribute `userName` is identified as `urn:ietf:params:scim:schemas:core:2.0:User:userName.`
The identity domains REST API includes the following schema URNs:
  * `urn:ietf:params:scim:schemas:core:2.0`
  * `urn:ietf:params:scim:schemas:extension:enterprise:2.0`
  * `urn:ietf:params:scim:schemas:oracle:idcs:extension`


## Attribute Data Types 🔗 
Attribute data types are derived from JSON and have the following characteristics, unless otherwise specified:
  * optional
  * case insensitive
  * modifiable
  * returned by default
  * not unique
  * of type String


Data Type | Contents  
---|---  
String | A sequence of zero or more Unicode characters encoded using UTF-8.  
Boolean | The literal "true" or "false".  
Decimal | A real number with at least one digit to the left and right of the decimal point.  
Integer | A decimal number with no fractional digits.  
DateTime  | A DateTime value, such as 2024-04-23T04:56:22Z.  
Binary | Arbitrary binary data.  
Complex | A singular or multivalued attribute whose value is a composition of one or more simple Attributes.  
Multivalued | A list of values or subattributes.  
CharArray | An array of characters that contains sensitive attributes, for example, a password.  
Was this article helpful?
YesNo

