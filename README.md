# SpaceX_by_pygame


## Overview
__Spacex__ is a board game designed after being inspired from snake and ladder but with space theme.
It is a two player dice based game in which player moves forward by the number of tiles as the number received on rolling of the dice.
Each player is competing with one another to reach the final destination i.e. Tile no. 30. The path to tile 30 is full of obstacles like asteroids and blackhole which prevents from reaching the end point while there are few shooting stars which will help you get closer to end point.


## Pygame
The __Pygame__ library is probably the most well known python library when it comes to making games.

## Installation
Use the package manager [pip](https://pip.pypa.io/en/stable/) to install pygame.
```powershell
pip install pygame
```

## Contents
It is written in a file with name SpaceX.py containing both the game logic and required game configurations.
Along with that there are three more folders i.e. Assets consisting all game related images, players_image consisting player’s avatar and music containing all the sounds and music used.
Finally it has a .gitignore file which contains the specific version of the pygame with which the game was developed.

## Execution
On executing the program, the written code executes and a new window opens displaying the starting window followed by the motion of a vector image. The player then enters the main menu by clicking anywhere on the screen. Menu window is provided with different buttons to perform different operations respectively. On clicking new game, one of the menu window’s option, both the players enter the game interface.
Until anyone of the player reaches the end position first i.e. tile 30, the game continues.
On winning a new window is opened to show the result.
The player then get back to the main menu to either play again or to quit the game. 
