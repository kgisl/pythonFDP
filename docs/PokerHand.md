# PokerHand


Represents a poker hand. 

## Methods


### make_histograms


Computes histograms for suits and hands.   
Creates attributes:   
suits: a histogram of the suits in the hand. ranks: a histogram of the ranks. sets: a sorted list of the rank sets in the hand. 

#### Parameters
name | description | default
--- | --- | ---
self |  | 





### has_highcard


Returns True if this hand has a high card. 

#### Parameters
name | description | default
--- | --- | ---
self |  | 





### check_sets


Checks whether self.sets contains sets that are at least as big as the requirements in t.   
t: list of int 

#### Parameters
name | description | default
--- | --- | ---
self |  | 





### has_pair


Checks whether this hand has a pair. 

#### Parameters
name | description | default
--- | --- | ---
self |  | 





### has_twopair


Checks whether this hand has two pair. 

#### Parameters
name | description | default
--- | --- | ---
self |  | 





### has_threekind


Checks whether this hand has three of a kind. 

#### Parameters
name | description | default
--- | --- | ---
self |  | 





### has_fourkind


Checks whether this hand has four of a kind. 

#### Parameters
name | description | default
--- | --- | ---
self |  | 





### has_fullhouse


Checks whether this hand has a full house. 

#### Parameters
name | description | default
--- | --- | ---
self |  | 





### has_flush


Checks whether this hand has a flush. 

#### Parameters
name | description | default
--- | --- | ---
self |  | 





### has_straight


Checks whether this hand has a straight. 

#### Parameters
name | description | default
--- | --- | ---
self |  | 





### in_a_row


Checks whether the histogram has n ranks in a row.   
hist: map from rank to frequency n: number we need to get to 

#### Parameters
name | description | default
--- | --- | ---
self |  | 
ranks |  | 
n |  | 5





### has_straightflush


Checks whether this hand has a straight flush.   
Clumsy algorithm. 

#### Parameters
name | description | default
--- | --- | ---
self |  | 





### has_straightflush


Checks whether this hand has a straight flush.   
Better algorithm (in the sense of being more demonstrably correct). 

#### Parameters
name | description | default
--- | --- | ---
self |  | 





### classify


Classifies this hand.   
Creates attributes: labels: 

#### Parameters
name | description | default
--- | --- | ---
self |  | 




