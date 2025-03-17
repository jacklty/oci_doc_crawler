Updated 2024-02-05
# Upgrade Window Recurrence Patterns
Examples of RFC 5545 recurrence pattern definitions. Use these when setting upgrade windows.
## Any time 🔗 
The upgrade can occur anytime. This is the same functionality as not having an upgrade schedule.
```
FREQ=WEEKLY;BYDAY=SU,MO,TU,WE,TH,FRI,SA
```

## Weekly, on Tuesdays and Fridays
```
FREQ=WEEKLY;BYDAY=TU,FR
```

## Monthly, on the first Sunday of the month
```
FREQ=MONTHLY;BYDAY=1SU
```

## Every third month on the last Wednesday of the month
```
FREQ=MONTHLY;INTERVAL=3;BYDAY=-1WE
```

## Every 10 days
```
FREQ=DAILY;INTERVAL=10
```

## Yearly, in April
The day is obtained from the first start date/time.
```
FREQ=YEARLY;BYMONTH=4
```

For more information on the format required, see [RFC 5545](https://datatracker.ietf.org/doc/html/rfc5545).
Was this article helpful?
YesNo

