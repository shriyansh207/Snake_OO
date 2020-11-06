# Snake_OO

## Table of Contents
* [Description]
* [Installation]
* [Usage and Instructions]
* [Future imporvements]

## Description
I was tasked with creating a game in Python using the library Pygame. I have created my variation of the classic game by adding extra features. The objective of this game is to eat red apples and try get the highest score. However, there is a twist, green apples spawn in at a random location every 20 seconds. If you eat the green apples and your length is greater than 6, then the snakes length will decrease. However, If you eat the green apple when your length is equal to or greater than 6, then you will die. Bumping into the rocks or eating yourself will also cause you to die.

## Installation
Python can run on Mac, Windows and Linux so the correct version of Python needs to be downloaded onto your OS. Alongside Python,Pip needs to be installed. This allows for an easy install of packages needed to run the game. All this is detailed in the 'requirements.txt' file. Furthemore, the four audio files also need to be downloaded and placed in the same folder as the game code. The audio files are:
* background_music.mp3
* Game_reset.wav
* Score.wav
* Ouch.wav
The game wont run unless the source code and the files above are in the same location on the computer.

## Usage and Instructions
After installing all packages needed to run the game. Open the 'snake_oo.py' file and run it.
The objective of this game is to try get as high of a score as possible. In order to do this, you must navigate the purple snake and have it eat the red apples. When the apple is eaten, the snakes length will increase by 1. However, be wary of the green apples. When they are eaten, if the length of the snake isn't big enough, the snake will die. However, if it is big enough then the snakes size will decrease by a substantial amount (play the game to find out how much.) Having the snake eat itself will also kill it. Lastly, running the snake onto the walls will also kill the snake.

## Future Improvements 
In the future I would like to develop the game to have multiple different levels where the border is changed and can form a pattern on the game screen. Additionally, I want to add extra features like a mystery item that can speed/slow down the snake to make the game a little more exciting and enjoyable. Finally, another addition I want to add to the game is an online scoreboard to get the highest scores of players who have played this game.
