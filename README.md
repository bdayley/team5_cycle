# Cycle
Cycle is a game where the players try to cut each other off using cycles that leave a trail behind them.
# Getting Started
---
Make sure you have Python 3.8.0 or newer and Raylib Python CFFI 3.7 installed and running on your machine. You can install Raylib Python CFFI by opening a terminal and running the following command.
```
python3 -m pip install raylib
```
After you've installed the required libraries, open a terminal and browse to the project's root folder. Start the program by running the following command.```

python3 cycle 
```
You can also run the program from an IDE like Visual Studio Code. Start your IDE and open the 
project folder. Select the main module inside the hunter folder and click the "run" icon.

# Project Structure
---
The project files and folders are organized as follows:

+-- cycle               (source code for game)
  +-- game              (specific game classes)
    +-- casting         (actors in the game)
    +-- directing       (the director class)
    +-- scripting       (controls)
    +--services         (keyboard and video services)
    +-- shared          (color and point)
  +-- __main__.py       (entry point for program)
  +-- constants         (initial values)
+-- README.md           (general info)
```

# Rules
---
  Players can move up, down, left and right.
  * Player one moves using the W, S, A and D keys.
  * Player two moves using the I, K, J and L keys.
  * Each player's trail grows as they move. 
  * Players try to maneuver so the opponent collides with their trail.
  * If a player collides with the opponent the game is over.

# Required Technologies
---
* Python 3.8.0
* Raylib Python CFFI 3.7

# Authors
---
* Carina Aguero (agu21022@byui.edu)\
* Rob Cox (cox21008@byui.edu)\
* Brianna Dayley (col04002@byui.edu)\
* Eduardo Pulido (pul21010@byui.edu)
