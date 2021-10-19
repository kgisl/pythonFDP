# Card

Represents a standard playing card.  
Attributes: suit: integer 0-3 rank: integer 1-13

## Methods

### **init**

#### Parameters

| name | description | default |
| ---- | ----------- | ------- |
| self |             |
| suit |             | 0       |
| rank |             | 2       |

### **str**

Returns a human-readable string representation.

#### Parameters

| name | description | default |
| ---- | ----------- | ------- |
| self |             |

### **eq**

Checks whether self and other have the same rank and suit.  
returns: boolean

#### Parameters

| name  | description | default |
| ----- | ----------- | ------- |
| self  |             |
| other |             |

### **lt**

Compares this card to other, first by suit, then rank.  
returns: boolean

#### Parameters

| name  | description | default |
| ----- | ----------- | ------- |
| self  |             |
| other |             |
