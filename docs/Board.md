# Board

Board class to represent the game board

## Methods

### **init**

#### Parameters

| name | description | default |
| ---- | ----------- | ------- |
| self |             |
| m    |             |
| n    |             |
| init |             |

### **str**

return the **str** representation of a Board object \* represents a live cell, and a space represents a dead one

#### Parameters

| name | description | default |
| ---- | ----------- | ------- |
| self |             |

### population

population — the number of live cells on the board

#### Parameters

| name | description | default |
| ---- | ----------- | ------- |
| self |             |

### count_live_neighbours

count the live neighbours of a cell

#### Parameters

| name | description | default |
| ---- | ----------- | ------- |
| self |             |
| x    |             |
| y    |             |

### next_cell_state

#### Parameters

| name | description | default |
| ---- | ----------- | ------- |
| self |             |
| x    |             |
| y    |             |

### next_board_state

return board configuration for the next state

#### Parameters

| name | description | default |
| ---- | ----------- | ------- |
| self |             |

### advance_state

update the board configuration with the config for the next state

#### Parameters

| name | description | default |
| ---- | ----------- | ------- |
| self |             |

### has_live_cells

return whether there are any live cells or not

#### Parameters

| name | description | default |
| ---- | ----------- | ------- |
| self |             |
