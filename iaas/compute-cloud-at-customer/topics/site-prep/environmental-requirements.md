Updated 2023-08-15
# Environmental Requirements
Follow these important environmental requirements to ensure the optimal environment for Oracle Compute Cloud@Customer.
Use the information in this section along with the [Environmental Checklist](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/site-prep/site-checklists.htm#site_checklists__environmental-checklist) to prepare your site.
## **Temperature and Humidity Requirements** 🔗 
Airflow through the Oracle Compute Cloud@Customer rack is from front to back. For information, see [Ventilation and Cooling Requirements](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/site-prep/environmental-requirements.htm#environmental-requirements__ventilation-cooling). 
Studies have shown that temperature increases of 10 degrees Celsius (18 degrees Fahrenheit) above 20 degrees Celsius (68 degrees Fahrenheit) reduce long-term electronics reliability by 50 percent. Excessive internal temperatures might result in full or partial shutdown of the rack. 
Condition  |  Operating Requirement  |  Non-operating Requirement  |  Optimum   
---|---|---|---  
Temperature  |  5 ° to 32 ° Celsius (41 ° to 89.6 ° Fahrenheit)  |  -40 ° to 68 ° Celsius (-40 ° to 154 ° Fahrenheit)  |  For optimal rack cooling, data center temperatures from 21 ° to 23 ° Celsius (69.8 ° to 73.4 ° Fahrenheit)   
Relative humidity  |  10 to 90 percent relative humidity, non-condensing  |  Up to 93 percent relative humidity  |  For optimal data center rack cooling, 45 to 50 percent non-condensing   
Altitude  |  3,000 meters (9,840 feet) maximum  |  12,000 meters (39,370 feet)  |  Ambient temperature is reduced by 1 ° Celsius per 300 meters above 900 meters altitude above sea level   
Set conditions to the optimal temperature and humidity ranges to minimize the chance of downtime because of component failure. Operating a rack for extended periods at or near the operating range limits, or installing it in an environment when it remains at or near non-operating range limits could significantly increase hardware component failure. 
The ambient temperature range of 21 ° to 23 ° Celsius (69.8 ° to 73.4 ° Fahrenheit) is optimal for server reliability and operator comfort. Most computer equipment can operate in a wide temperature range, but near 22 ° Celsius (71.6 ° Fahrenheit) is preferable because it is easier to maintain safe humidity levels. Operating in this temperature range provides a safety buffer in the event that the air conditioning system goes down for a period of time. 
The ambient relative humidity range of 45 to 50 percent is suitable for safe data processing operations. Most computer equipment can operate in a wide range (20 to 80 percent), but the range of 45 to 50 percent is recommended for the following reasons: 
  * Optimal range helps protect computer systems from corrosion problems associated with high humidity levels. 
  * Optimal range provides the greatest operating time buffer in the event of air conditioner control failure. 
  * This range helps to avoid failures or temporary malfunctions caused by intermittent interference from static discharges that may occur when relative humidity is too low. 


**Note**
Electrostatic discharge (ESD) is easily generated, and hard to dissipate in areas of low relative humidity, such as below 35 percent. ESD becomes critical when humidity drops below 30 percent. It is not difficult to maintain humidity in a data center because of the high-efficiency vapor barrier and low rate of air changes normally present. 
## **Ventilation and Cooling Requirements** 🔗 
Always provide adequate space in front of and behind the rack to allow for proper ventilation. Do not obstruct the front or rear of the rack with equipment or objects that might prevent air from flowing through the rack. Rack-mountable servers and equipment typically draw cool air in through the front of the rack and let warm air out the rear of the rack. There is no airflow requirement for the left and right sides because of front-to-back cooling. 
If the rack is not completely filled with components, then cover the empty sections will filler panels. Gaps between components can adversely affect airflow and cooling within the rack. 
Relative humidity is the percentage of the total water vapor that can exist in the air without condensing, and is inversely proportional to air temperature. Humidity goes down when the temperature rises, and goes up when the temperature drops. For example, air with a relative humidity of 45 percent at a temperature of 24 ° Celsius (75.2 ° Fahrenheit) has a relative humidity of 65 percent at a temperature of 18 ° Celsius (64.4 ° Fahrenheit). As the temperature drops, the relative humidity rises to more than 65 percent, and water droplets are formed. 
Air conditioning facilities usually don't precisely monitor or control temperature and humidity throughout an entire computer room. Generally, monitoring is done at individual points corresponding to multiple exhaust vents in the main unit, and other units in the room. Special consideration should be paid to humidity when using underfloor ventilation. When underfloor ventilation is used, monitoring is done at each point close to an exhaust vent. Distribution of the temperature and humidity across the entire room is uneven. 
The rack has been designed to function while installed in a natural convection air flow. The following requirements must be followed to meet the environmental specification: 
  * Ensure that there is adequate airflow through the system. 
  * Ensure that the system has front-to-back cooling. The air intake is at the front of the system, and the air outlet is at the rear of the system. 
  * Allow a minimum clearance of 1219.2 mm (48 inches) at the front of the system, and 914 mm (36 inches) at the rear of the system for ventilation. 


**Optional Raised Floor Installations**
For installations on optional raised floors, use perforated tiles, approximately 400 CFM/tile, in front of the rack for cold air intake. The tiles can be arranged in any order in front of the rack, as long as cold air from the tiles can flow into the rack. Inadequate cold airflow could result in a higher intake temperature in the system because of exhaust air recirculation. The following is the recommended number of floor tiles: 
  * Four floor tiles for a rack with up to 12 compute nodes (fully loaded) 
  * Three floor tiles for a rack with up to 6 compute nodes (half loaded) 
  * One floor tile for a rack with 3 compute nodes (quarter loaded) 


Was this article helpful?
YesNo

