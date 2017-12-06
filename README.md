Project to develop a neural network based chess player

# Glossary
* player side: Side controlled by the software or instance.
* opponent side: The other side.
The game state is stored in a 64 position string representing the board squares
, starting on the left of the player side, advancing to right and then to the
other lines on the opponent direction.

# Data representation
## Basic string representaion
The representation is relative to the player side. In other words, ***the two
players "sees" different representations***.

Each string position can store the following characters:
* ***P*** : Pawn
* ***R*** : Rook
* ***N*** : kNight
* ***B*** : Bishop
* ***Q*** : Queen
* ***K*** : King
* ***.***(period) : Empty square  

Upper case letters means player's pieces

Lower case letters means opponent's pieces

For instance:
The string for white player start board configuration is:
```
RNBQKBNRPPPPPPPP................................pppppppprnbqkbnr
```
which means:
```
rnbqkbnr
pppppppp
........
........
........
........
PPPPPPPP
RNBQKBNR
```
## Compact multiple boards representation
The multiple board representation is used to represent multiple possible locations of a single piece. This representation is made of a tuple:
* Single char piece id
* Board string, where the asterisk are put in all possible piece locations.

For instance:

Starting from this board:
```
rnbqkbnr
p.pppppp
.p......
........
........
...PB...
PPP.PPPP
RN.QKBNR
```
The compact representation of all possible next locations of the e3 bishop is the tuple formed by
* the char 'B'
* and the board
```
rnbqkbnr
p.pppppp
.*.....*
..*...*.
...*.*..
...PB...
PPP*PPPP
RN*QKBNR
```

This tuple in python would look like:
```
('B', 'RN*QKBNRPPP*PPPP...PB......*.*....*...*..*.....*p.pppppprnbqkbnr')
```
