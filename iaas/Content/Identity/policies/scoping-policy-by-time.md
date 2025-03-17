Updated 2024-09-30
# Restricting Access to Resources Based on Time Frame
You can use time-based variables in your policies to restrict the access granted in the policy to only certain time frames. 
This feature allows you to restrict actions on resources to particular times. For example, you can create a policy that allows access only through a specified date. A policy like this would be useful if your company hires contractors and you want to ensure access is not allowed past the contract end date. Or, you could allow access to resources only during business hours (for example, Monday-Friday 9:00 AM - 5:00 PM). This restriction can lower the risk of a bad actor making changes when they are more likely to go unnoticed.
The variables that you can use to scope access based on time are:
  * `request.utc-timestamp`
  * `request.utc-timestamp.month-of-year`
  * `request.utc-timestamp.day-of-month`
  * `request.utc-timestamp.day-of-week`
  * `request.utc-timestamp.time-of-day`


Usage for these variables is described in more detail in the following sections. 
## Information for Working with Time-Based Variables 🔗 
You must specify the time the variables using [ISO 8601](https://www.iso.org/iso-8601-date-and-time-format.html) format: YYYY-MM-DDThh:mm:ssZ. Examples of this format are:
  * Date and time with seconds: '2020-04-01T15:00:00Z'
  * Data and time with minutes: '2020-04-01T05:00Z'
  * Date only: '2020-04-01Z'
  * Time only: '05:00:00'


Even though you can specify a time down to seconds, you should allow for a 5 minute time difference between the timestamp on the request and the time the request is evaluated by the IAM service. This time difference can be caused by several factors, therefore be aware of this potential discrepancy when you plan and implement your time-based policies.
The time that you specify is evaluated as Coordinated Universal Time (UTC). This means that you must calculate the correct UTC time for the time zone in which the policy is evaluated. For example, to specify 9:00 AM Pacific Standard Time for the value of a variable, you would enter '17:00:00'. If your locale participates in daylight savings, you'll need to update any policies that refer to a specific hour when the time change goes into effect. 
## Details for Each Time-Based Variable 🔗 
Usage for each variable is described in the following sections:
[request.utc-timestamp](https://docs.oracle.com/en-us/iaas/Content/Identity/policies/scoping-policy-by-time.htm)
**Description:** The time the request is received for authorization. You can write a policy that allows access only before or after a specific date-time timestamp. The timestamp must follow the [ISO 8601](https://www.iso.org/iso-8601-date-and-time-format.html) format: YYYY-MM-DDThh:mm:ssZ and be in Coordinated Universal Time (UTC). 
**Supported operators:** before | after
**Allowed values:** Coordinated Universal Time (UTC) timestamp in [ISO 8601](https://www.iso.org/iso-8601-date-and-time-format.html) format: YYYY-MM-DDThh:mm:ssZ
**Example Values:**
  * '2020-04-01T00:00:00Z'
  * '2020-04-01T00:00Z'


**Example policy:** Allow group, Contractors, to access the `instance-family` resources only until a certain date:
Copy
```
Allow group Contractors to manage instance-family in tenancy where request.utc-timestamp before '2022-01-01T00:00Z'
```

The access granted by the policy to the group Contractors will expire on January 1, 2022, 12:00 AM, UTC.
[request.utc-timestamp.month-of-year](https://docs.oracle.com/en-us/iaas/Content/Identity/policies/scoping-policy-by-time.htm)
**Description:** The month of the year that the request is received for authorization. You can write a policy that allows access only during specific months. 
**Supported operators:** = | != | in
**Allowed values:** Numeric month (matching [ISO 8601](https://www.iso.org/iso-8601-date-and-time-format.html))
**Example Values:** '1', '2', '3', ... '12' 
**Example policy:** Allow group, SummerInterns, to access the `instance-family` resources only during June, July, and August:
Copy
```
Allow group SummerInterns to manage instance-family in tenancy where ANY {request.utc-timestamp.month-of-year in ('6', '7', '8')}
```

The access granted by the policy to the group SummerInterns is only valid during June, July, and August of a given year.
[request.utc-timestamp.day-of-month](https://docs.oracle.com/en-us/iaas/Content/Identity/policies/scoping-policy-by-time.htm)
**Description:** The day of the month that the request is received for authorization. You can write a policy that allows access only for specific days of the month. Keep in mind that the span of the day is calculated based on UTC. For example, suppose you are in Miami, FL, USA, and you enter '1' to indicate the first day of the month. For the month of February, the policy will be in effect for 12:00 AM through 11:59 PM UTC on February 1, which in Miami is 7:00 PM on January 31 through 6:59 PM on February 1.
**Supported operators:** = | != | in
**Allowed values:** Numeric day of month
**Example Values:** '1', '2', '3', ... '31' 
**Example policy:** Allow group, ComplianceAuditors, to read `all-resources` only on the first day of the month.
Copy
```
Allow group ComplianceAuditors to read all-resources in tenancy where request.utc-timestamp.day-of-month = '1'
```

The access granted by the policy to the group ComplianceAuditors is only valid on the first day of each month (the day is defined by UTC time).
[ request.utc-timestamp.day-of-week](https://docs.oracle.com/en-us/iaas/Content/Identity/policies/scoping-policy-by-time.htm)
**Description:** The day of the week that the request is received for authorization. You can write a policy that allows access only for specific days of the week. Note that the span of the day is calculated based on UTC. For example, suppose you are in Miami, FL, USA, and you enter 'monday'. The policy will be in effect for 12:00 AM through 11:59 PM UTC on Monday, which in Miami is 7:00 PM (EST) on Sunday through 6:59 PM on Monday.
**Supported operators:** = | != | in
**Allowed values:** Name of day of week in English
**Example Values:** 'Monday', 'Tuesday', 'Wednesday', etc. 
**Example policy:** Allow group, WorkWeek, to manage`instance-family` only during the company work week.
Copy
```
Allow group WorkWeek to manage instance-family where ANY {request.utc-timestamp.day-of-week in ('monday', 'tuesday', 'wednesday', 'thursday', 'friday')}
```

The access granted by the policy to the group WorkWeek is only valid on the days specified (the day is defined by UTC time).
[request.utc-timestamp.time-of-day](https://docs.oracle.com/en-us/iaas/Content/Identity/policies/scoping-policy-by-time.htm)
**Description:** The time of day that the request is received for authorization. You can write a policy that allows access only for a specific span of time during the day. Note that the time of the day is calculated based on UTC. If you live in a time zone that implements daylight savings, you will need to update the policy when the time changes.
**Supported operators:** between
**Allowed values:** UTC time interval in ISO 8601 format: hh:mm:ssZ
**Example Values:** '01:00:00Z' AND '2:01:00Z'
**Example policies:** Allow group DayShift to manage instances and related resources between the hours of 9:00 AM and 5:00 PM Pacific Standard Time (PST). 
Note that the times are converted to UTC: 
Copy
```
Allow group DayShift to manage instance-family where request.utc-timestamp.time-of-day between '17:00:00Z' and '01:00:00Z'
```

I want to allow group NightShift to manage instances and related resources between 5:00 PM and 9:00 AM PST. 
Copy
```
Allow group NightShift to manage instance-family where request.utc-timestamp.time-of-day between '01:00:00Z' and '17:00:00Z'
```

In both of these examples, the current time is calculated and tested to see if it falls within the provided range or not (ignoring which day the time falls on). 
Was this article helpful?
YesNo

