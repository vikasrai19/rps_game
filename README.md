# RPS Game
> A simple python project where we are going to build the RPS game using PYGAME module.

-- --
### Basic App -> Terminal Game
* [x] Create a python file.
* [x] import random.
* [x] Create a class for Game.
	* [x] init method to initialize values.
		* [x] Player and AI score
		* [x] Final points to win the game. 
		* [x] Different selection options for the AI to choose from the list.
		* [x] Variables to store the player and AI selection.
	* [ ] Method to start the game { Creating a while loop and running it until the game stops. } .
		* [x] Display different selection options for the user to choose.
		* [x] Get the value from the user and store it in a variable.
		* [x] Using Random.choice select an option from the list as the ai selection.
	* [x] Method to get the selection of the player.
		* [x] Convert the selected interger value into corresponding string value and store it in the player selection variable. <br>
		> 1 --> "**rock**" <br> 
		> 2 --> "**paper**"  <br>
		> 3 --> "**scissor**" 
	* [x] Method to check the winner in the current round.
		* [x] Compare the selection of the player and the ai.
		* [x] If they are same declare it as tie
		* [x] If player wins, declare as "Player won a  point" and increment the player's point by 1.
		* [x] If AI wins, declare as "AI won a point" and increment the AI's point by 1.
	* [x] Method to end the game.
		* [x] If any one the scores equal to the max score, trigger the end game method
		* [x] Check who has greater score and declare the winner.
	* [x] Method to display the points whenever required.
		* [x] Print the player' score and AI score into the terminal.
----

### RPS Game -> Simple GUI game using pygame
* [x] Install pygame module
```python
# pygame installation command
# Windows 
pip install pygame

# maco and linux
pip3 install pygame
```
* [x] Importing modules. pygame, random, os
* [x] Intialize the pygame module.
* [x] Import all the images that are required by the game.
-- -- 
* [ ] Create a game class
	* [ ] init method and initialize values.
	* [ ] start method
		* [x] Check for different pygame events
			* [x] quit event
			* [x] Mouse click event
	  	* [x] create quit button to quit the game
		* [x] Display the player and ai score
		* [x] Create 3 buttons for the player to choose
			* [x] Check for the mouse clicks on these buttons
		* [x] Display the player selection with the appropriate images. <br />
		<br />
	* [x] ai_selection method
		* [x] using Random.choice method select a random value from the list and store it as ai_selected option.
	    * [x] Display the AI selection with the appropriate images.
		<br><br>
	* [x] check_round_winner method
		* [x] Compare the player and ai selection.
			* [x] If both are equal, display the result as tie
			* [x] If player won the round, display "player won a point" and increment player score by 1
			* [x] If ai won the round, display "ai won a point" and increment ai points by 1.
		* [x] If either player points or ai points is equal to the max points, declare them as winner.
	<br><br>
	* [ ] restart game method
		* [ ] Set player and ai score to 0
		* [ ] Set player selection image and ai selection image to None
	