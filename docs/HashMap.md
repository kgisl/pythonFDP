# HashMap

An implementation of a hashtable using a BetterMap that grows so that the number of items never exceeds the number of LinearMaps.  
The amortized cost of add should be O(1) provided that the implementation of sum in resize is linear.

## Methods

### **init**

Starts with 2 LinearMaps and 0 items.

#### Parameters

| name | description | default |
| ---- | ----------- | ------- |
| self |             |

### get

Looks up the key (k) and returns the corresponding value, or raises KeyError if the key is not found.

#### Parameters

| name | description | default |
| ---- | ----------- | ------- |
| self |             |
| k    |             |

### add

Resize the map if necessary and adds the new item.

#### Parameters

| name | description | default |
| ---- | ----------- | ------- |
| self |             |
| k    |             |
| v    |             |

### resize

Makes a new map, twice as big, and rehashes the items.

#### Parameters

| name | description | default |
| ---- | ----------- | ------- |
| self |             |
