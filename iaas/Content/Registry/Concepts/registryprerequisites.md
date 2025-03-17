Updated 2025-01-10
# Preparing for Container Registry
_Find out about the prerequisites you have to meet before you can use Container Registry._
Before you can push and pull Docker images to and from Oracle Cloud Infrastructure Registry (also known as Container Registry):
  * You must have access to an Oracle Cloud Infrastructure tenancy. The tenancy must be subscribed to one or more of the regions in which Container Registry is available (see [Availability by Region](https://docs.oracle.com/en-us/iaas/Content/Registry/Concepts/registryprerequisites.htm#regional-availability)).
  * You must have access to the Docker CLI (for example, to push and pull images on a local machine, you'll need to have installed Docker on the local machine).
  * You must either belong to a group to which a policy grants the appropriate permissions, or belong to the tenancy's Administrators group. See [Policies to Control Repository Access](https://docs.oracle.com/en-us/iaas/Content/Registry/Concepts/registrypolicyrepoaccess.htm#Policies_to_Control_Repository_Access "Find out how to set up policies to control access to repositories in Container Registry, along with some examples of common policies."). 
  * You must have an Oracle Cloud Infrastructure auth token. If you don't have an auth token already, see [Getting an Auth Token](https://docs.oracle.com/en-us/iaas/Content/Registry/Tasks/registrygettingauthtoken.htm#Getting_an_Auth_Token "Find out how to create a new auth token for use with Container Registry.").


## Availability by Region 🔗 
Container Registry is available in the Oracle Cloud Infrastructure regions listed at [Regions and Availability Domains](https://docs.oracle.com/iaas/Content/General/Concepts/regions.htm). Refer to that topic to see region identifiers, region keys, and availability domain names.
Note that Container Registry fully implements a Docker protocol that enables you to use the Docker Registry HTTP API (as well as the Oracle Cloud Infrastructure API) to manage images at the regional endpoints below. See the [Docker documentation](https://docs.docker.com/registry/spec/api/) for information about using the Docker Registry HTTP API.
Region Name | Available Endpoints  
---|---  
South Africa Central (Johannesburg)  | 
  * `https://af-johannesburg-1.ocir.io` (OC1 realm only)
  * `https://jnb.ocir.io` (OC1 realm only)
  * `https://artifacts.af-johannesburg-1.oci.oraclecloud.com`

  
Australia Southeast (Melbourne)  | 
  * `https://ap-melbourne-1.ocir.io` (OC1 realm only)
  * `https://mel.ocir.io` (OC1 realm only)
  * `https://artifacts.ap-melbourne-1.oci.oraclecloud.com`

  
India South (Hyderabad)  | 
  * `https://ap-hyderabad-1.ocir.io` (OC1 realm only)
  * `https://hyd.ocir.io` (OC1 realm only)
  * `https://artifacts.ap-hyderabad-1.oci.oraclecloud.com`

  
India West (Mumbai)  | 
  * `https://ap-mumbai-1.ocir.io` (OC1 realm only)
  * `https://bom.ocir.io` (OC1 realm only)
  * `https://artifacts.ap-mumbai-1.oci.oraclecloud.com`

  
Japan Central (Osaka)  | 
  * `https://ap-osaka-1.ocir.io` (OC1 realm only)
  * `https://kix.ocir.io` (OC1 realm only)
  * `https://artifacts.ap-osaka-1.oci.oraclecloud.com`

  
Singapore (Singapore)  | 
  * `https://ap-singapore-1.ocir.io` (OC1 realm only)
  * `https://sin.ocir.io` (OC1 realm only)
  * `https://artifacts.ap-singapore-1.oci.oraclecloud.com`

  
Singapore West (Singapore)  | 
  * `https://ap-singapore-2.ocir.io` (OC1 realm only)
  * `https://xsp.ocir.io` (OC1 realm only)
  * `https://artifacts.ap-singapore-2.oci.oraclecloud.com`

  
South Korea Central (Seoul)  | 
  * `https://ap-seoul-1.ocir.io` (OC1 realm only)
  * `https://icn.ocir.io` (OC1 realm only)
  * `https://artifacts.ap-seoul-1.oci.oraclecloud.com`

  
South Korea North (Chuncheon)  | 
  * `https://ap-chuncheon-1.ocir.io` (OC1 realm only)
  * `https://yny.ocir.io` (OC1 realm only)
  * `https://artifacts.ap-chuncheon-1.oci.oraclecloud.com`

  
Australia East (Sydney)  | 
  * `https://ap-sydney-1.ocir.io` (OC1 realm only)
  * `https://syd.ocir.io` (OC1 realm only)
  * `https://artifacts.ap-sydney-1.oci.oraclecloud.com`

  
Japan East (Tokyo)  | 
  * `https://ap-tokyo-1.ocir.io` (OC1 realm only)
  * `https://nrt.ocir.io` (OC1 realm only)
  * `https://artifacts.ap-tokyo-1.oci.oraclecloud.com`

  
Canada Southeast (Montreal)  | 
  * `https://ca-montreal-1.ocir.io` (OC1 realm only)
  * `https://yul.ocir.io` (OC1 realm only)
  * `https://artifacts.ca-montreal-1.oci.oraclecloud.com`

  
Canada Southeast (Toronto)  | 
  * `https://ca-toronto-1.ocir.io` (OC1 realm only)
  * `https://yyz.ocir.io` (OC1 realm only)
  * `https://artifacts.ca-toronto-1.oci.oraclecloud.com`

  
Netherlands Northwest (Amsterdam)  | 
  * `https://eu-amsterdam-1.ocir.io` (OC1 realm only)
  * `https://ams.ocir.io` (OC1 realm only)
  * `https://artifacts.eu-amsterdam-1.oci.oraclecloud.com`

  
Germany Central (Frankfurt)  | 
  * `https://eu-frankfurt-1.ocir.io` (OC1 realm only)
  * `https://fra.ocir.io` (OC1 realm only)
  * `https://artifacts.eu-frankfurt-1.oci.oraclecloud.com`

  
Spain Central (Madrid)  | 
  * `https://eu-madrid-1.ocir.io` (OC1 realm only)
  * `https://mad.ocir.io` (OC1 realm only)
  * `https://artifacts.eu-madrid-1.oci.oraclecloud.com`

  
France South (Marseille)  | 
  * `https://eu-marseille-1.ocir.io` (OC1 realm only)
  * `https://mrs.ocir.io` (OC1 realm only)
  * `https://artifacts.eu-marseille-1.oci.oraclecloud.com`

  
Italy Northwest (Milan)  | 
  * `https://eu-milan-1.ocir.io` (OC1 realm only)
  * `https://lin.ocir.io` (OC1 realm only)
  * `https://artifacts.eu-milan-1.oci.oraclecloud.com`

  
France Central (Paris)  | 
  * `https://eu-paris-1.ocir.io` (OC1 realm only)
  * `https://cdg.ocir.io` (OC1 realm only)
  * `https://artifacts.eu-paris-1.oci.oraclecloud.com`

  
Sweden Central (Stockholm)  | 
  * `https://eu-stockholm-1.ocir.io` (OC1 realm only)
  * `https://arn.ocir.io` (OC1 realm only)
  * `https://artifacts.eu-stockholm-1.oci.oraclecloud.com`

  
Switzerland North (Zurich)  | 
  * `https://eu-zurich-1.ocir.io` (OC1 realm only)
  * `https://zrh.ocir.io` (OC1 realm only)
  * `https://artifacts.eu-zurich-1.oci.oraclecloud.com`

  
Israel Central (Jerusalem) | 
  * `https://il-jerusalem-1.ocir.io` (OC1 realm only)
  * `https://mtz.ocir.io` (OC1 realm only)
  * `https://artifacts.il-jerusalem-1.oci.oraclecloud.com`

  
UAE Central (Abu Dhabi)  | 
  * `https://me-abudhabi-1.ocir.io` (OC1 realm only)
  * `https://auh.ocir.io` (OC1 realm only)
  * `https://artifacts.me-abudhabi-1.oci.oraclecloud.com`

  
UAE East (Dubai)  | 
  * `https://me-dubai-1.ocir.io` (OC1 realm only)
  * `https://dxb.ocir.io` (OC1 realm only)
  * `https://artifacts.me-dubai-1.oci.oraclecloud.com`

  
Saudi Arabia Central (Riyadh)  | 
  * `https://me-riyadh-1.ocir.io` (OC1 realm only)
  * `https://ruh.ocir.io` (OC1 realm only)
  * `https://artifacts.me-riyadh-1.oci.oraclecloud.com`

  
Saudi Arabia West (Jeddah)  | 
  * `https://me-jeddah-1.ocir.io` (OC1 realm only)
  * `https://jed.ocir.io` (OC1 realm only)
  * `https://artifacts./me-jeddah-1.oci.oraclecloud.com`

  
Serbia Central (Jovanovac)  | 
  * `https://ocir.eu-jovanovac-1.oci.oraclecloud20.com` (OC1 realm only) 
  * `https://artifacts.eu-jovanovac-1.oci.oraclecloud.com`

  
Mexico Central (Queretaro)  | 
  * `https://mx-queretaro-1.ocir.io` (OC1 realm only)
  * `https://qro.ocir.io` (OC1 realm only)
  * `https://artifacts.mx-queretaro-1.oci.oraclecloud.com`

  
Mexico Northeast (Monterrey)  | 
  * `https://mx-monterrey-1.ocir.io` (OC1 realm only)
  * `https://mty.ocir.io` (OC1 realm only)
  * `https://artifacts.mx-monterrey-1.oci.oraclecloud.com`

  
Chile Central (Santiago)  | 
  * `https://sa-santiago-1.ocir.io` (OC1 realm only)
  * `https://scl.ocir.io` (OC1 realm only)
  * `https://artifacts.sa-santiago-1.oci.oraclecloud.com`

  
Chile West (Valparaiso)  | 
  * `https://sa-valparaiso-1.ocir.io` (OC1 realm only)
  * `https://vap.ocir.io` (OC1 realm only)
  * `https://artifacts.sa-valparaiso-1.oci.oraclecloud.com`

  
Colombia Central (Bogota)  | 
  * `https://sa-bogota-1.ocir.io` (OC1 realm only)
  * `https://bog.ocir.io` (OC1 realm only)
  * `https://artifacts.sa-bogota-1.oci.oraclecloud.com`

  
Brazil East (Sao Paulo)  | 
  * `https://sa-saopaulo-1.ocir.io` (OC1 realm only)
  * `https://gru.ocir.io` (OC1 realm only)
  * `https://artifacts.sa-saopaulo-1.oci.oraclecloud.com`

  
Brazil Southeast (Vinhedo)  | 
  * `https://sa-vinhedo-1.ocir.io` (OC1 realm only)
  * `https://vcp.ocir.io` (OC1 realm only)
  * `https://artifacts.sa-vinhedo-1.oci.oraclecloud.com`

  
UK South (London)  | 
  * `https://uk-london-1.ocir.io` (OC1 realm only)
  * `https://lhr.ocir.io` (OC1 realm only)
  * `https://artifacts.uk-london-1.oci.oraclecloud.com`

  
UK West (Newport)  | 
  * `https://uk-cardiff-1.ocir.io` (OC1 realm only)
  * `https://cwl.ocir.io` (OC1 realm only)
  * `https://artifacts.uk-cardiff-1.oci.oraclecloud.com`

  
US East (Ashburn)  | 
  * `https://us-ashburn-1.ocir.io` (OC1 realm only)
  * `https://iad.ocir.io` (OC1 realm only)
  * `https://artifacts.us-ashburn-1.oci.oraclecloud.com`

  
US Midwest (Chicago)  | 
  * `https://us-chicago-1.ocir.io` (OC1 realm only)
  * `https://ord.ocir.io` (OC1 realm only)
  * `https://artifacts.us-chicago-1.oci.oraclecloud.com`

  
US West (Phoenix)  | 
  * `https://us-phoenix-1.ocir.io` (OC1 realm only)
  * `https://phx.ocir.io` (OC1 realm only)
  * `https://artifacts.us-phoenix-1.oci.oraclecloud.com`

  
US West (San Jose)  | 
  * `https://us-sanjose-1.ocir.io` (OC1 realm only)
  * `https://sjc.ocir.io` (OC1 realm only)
  * `https://artifacts.us-sanjose-1.oci.oraclecloud.com`

  
Was this article helpful?
YesNo

