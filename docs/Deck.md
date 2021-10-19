# Deck


Represents a deck of cards.   
Attributes: cards: list of Card objects. 

## Methods


### __init__


Initializes the Deck with 52 cards.  

#### Parameters
name | description | default
--- | --- | ---
self |  | 





### __str__


Returns a string representation of the deck.  

#### Parameters
name | description | default
--- | --- | ---
self |  | 





### add_card


Adds a card to the deck.   
card: Card 

#### Parameters
name | description | default
--- | --- | ---
self |  | 
card |  | 





### remove_card


Removes a card from the deck or raises exception if it is not there.   
card: Card 

#### Parameters
name | description | default
--- | --- | ---
self |  | 
card |  | 





### pop_card


Removes and returns a card from the deck.   
i: index of the card to pop; by default, pops the last card. 

#### Parameters
name | description | default
--- | --- | ---
self |  | 
i |  | 





### shuffle


Shuffles the cards in this deck. 

#### Parameters
name | description | default
--- | --- | ---
self |  | 





### sort


Sorts the cards in ascending order. 

#### Parameters
name | description | default
--- | --- | ---
self |  | 





### move_cards


Moves the given number of cards from the deck into the Hand.   
hand: destination Hand object num: integer number of cards to move 

#### Parameters
name | description | default
--- | --- | ---
self |  | 
hand |  | 
num |  | 




