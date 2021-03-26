# RPS Game
> A simple python project where we are going to build the RPS game using PYGAME module.
### Basic App --> Terminal Game
* [ ✔️ ] Create a python file.
* [  ] import random.
* [ ] Create a class for Game.
	* [ ] init method to initialize values.
		* [ ] Player and AI score
		* [ ] Final points to win the game. 
		* [ ] Different selection options for the AI to choose from the list.
		* [ ] Variables to store the player and AI selection.
	* [ ] Method to start the game { Creating a while loop and running it until the game stops. } .
		* [ ] Display different selection options for the user to choose.
		* [ ] Get the value from the user and store it in a variable.
		* [ ] Using Random.choice select an option from the list as the ai selection.
	* [ ] Method to get the selection of the player.
		* [ ] Convert the selected interger value into corresponding string value and store it in the player selection variable. <br>
		> 1 --> "**rock**" <br> 
		> 2 --> "**paper**"  <br>
		> 3 --> "**scissor**" 
	* [ ] Method to check the winner in the current round.
		* [ ] Compare the selection of the player and the ai.
		* [ ] If they are same declare it as tie
		* [ ] If player wins, declare as "Player won a  point" and increment the player's point by 1.
		* [ ] If AI wins, declare as "AI won a point" and increment the AI's point by 1.
	* [ ] Method to end the game.
		* [ ] If any one the scores equal to the max score, trigger the end game method
		* [ ] Check who has greater score and declare the winner.
	* [ ] Method to display the points whenever required.
		* [ ] Print the player' score and AI score into the terminal.

### RPS Game --> Simple GUI game using pygame