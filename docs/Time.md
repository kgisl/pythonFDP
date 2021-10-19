# Time


Represents the time of day.   
attributes: hour, minute, second 

## Methods


### __init__


Initializes a time object.   
hour: int minute: int second: int or float 

#### Parameters
name | description | default
--- | --- | ---
self |  | 
hour |  | 0
minute |  | 0
second |  | 0





### __str__


Returns a string representation of the time. 

#### Parameters
name | description | default
--- | --- | ---
self |  | 





### print_time


Prints a string representation of the time. 

#### Parameters
name | description | default
--- | --- | ---
self |  | 





### time_to_int


Computes the number of seconds since midnight. 

#### Parameters
name | description | default
--- | --- | ---
self |  | 





### is_after


Returns True if t1 is after t2; false otherwise. 

#### Parameters
name | description | default
--- | --- | ---
self |  | 
other |  | 





### __add__


Adds two Time objects or a Time object and a number.   
other: Time object or number of seconds 

#### Parameters
name | description | default
--- | --- | ---
self |  | 
other |  | 





### __radd__


Adds two Time objects or a Time object and a number. 

#### Parameters
name | description | default
--- | --- | ---
self |  | 
other |  | 





### add_time


Adds two time objects. 

#### Parameters
name | description | default
--- | --- | ---
self |  | 
other |  | 





### increment


Returns a new Time that is the sum of this time and seconds. 

#### Parameters
name | description | default
--- | --- | ---
self |  | 
seconds |  | 





### is_valid


Checks whether a Time object satisfies the invariants. 

#### Parameters
name | description | default
--- | --- | ---
self |  | 




