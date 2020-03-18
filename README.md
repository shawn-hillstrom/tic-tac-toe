# Tic Tac Toe

## About

This project implements a simple game of Tic Tac Toe in Python. The purpose of the project is to experiment, using a set of Monte-Carlo trials, with the mechanics of Tic Tac Toe.

There are two modes the game can be run in:
1. Play mode, where one can play the game from the command line as-is.
2. Test mode, where the game runs a set of Monte-Carlo experiments give some initial conditions.

## Versioning

**VERSION:** 1.0

**RELEASE:** N/A

**LAST UPDATED:** January 18th, 2019

## Resources

N/A

## How To Use

After cloning the respository simply run
```bash
python tictactoe.py ...
```
with the one of the following options:

**--play** runs the game in play mode.

**--mc** runs the game in test mode.

Furthermore, one can change the initial state of the board with **--state** where the argument of state must be a string of integers in the set **(0, 1, 2)**. For example: 010002000 will output a board that looks like

```
 _ | X | _ 
 _ | _ | O 
 _ | _ | _ 
```

One can also change the size of the board with the **-n** flag followed by an integer argument. this will produce an nxn board.

## Future Development

There are no plans for future development at this time.
