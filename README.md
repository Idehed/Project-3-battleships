# Battleships

Battleships is a Python-based terminal game that runs in the Code Institutes mock terminal Heroku.

The user is trying to sink the computer's boats before they do. Whoever sinks all the boats on their opposite board wins!

[Here is a live version of my project]()

![Game in different views](https://github.com/Idehed/Project-3-battleships/assets/146822758/5538260e-ee5a-4486-9436-90207a9f1934)

# How to play

Battleship is a strategy-type guessing game for two players.

It is played on ruled grids (paper or board) on which each player's fleet of warships is marked.
 
The locations of the fleets are concealed from the other player. Players alternate turns calling "shots" at the other player's ships, and the objective of the game is to destroy the opposing player's fleet.

The grid in this battleship game is a 10*10 board with 5 ships that are randomly placed for both the player and the computer.
The guesses that are misses are marked with an "O" and the guesses that are a hits are marked with an "X".

The winner is the one who gets 15 shots at the opposite ships first. 

# Features

## Existing Features

- Welcome message and the information on how to play are displayed. The user will have to put their name in to start the game.


![Welcome/instruction](https://github.com/Idehed/Project-3-battleships/assets/146822758/41139d12-37c1-4038-948a-e388dd64f63f)

- Random board generation
    - 5 ships are randomly put on both the player and the computer's board.
    - The computer board is hidden from the player.
- Play against the computer

![the players board](https://github.com/Idehed/Project-3-battleships/assets/146822758/94a94a68-d097-45ba-a6c0-9bb4b1557b7e)

![computers board](https://github.com/Idehed/Project-3-battleships/assets/146822758/473833a4-6c46-474a-a30f-70b2e07121b5)

- Accepts user inputs
- Maintains and shows the number of hits for both the player and the computer

![two boards](https://github.com/Idehed/Project-3-battleships/assets/146822758/84431e6c-6d87-4eed-914f-b364b01f91d7)

- Invalid user input
    - Error if the user does not enter a row between 1-9.
    - Error if the user does not enter a column between A-I.
    - Cannot guess the same position twice.

![wrong guess](https://github.com/Idehed/Project-3-battleships/assets/146822758/5ff47a21-aed9-4a60-87cf-49a7103a9bdf)

![wrong guess](https://github.com/Idehed/Project-3-battleships/assets/146822758/49735115-e1d9-466c-815c-666bafff2a90)

![already guessed](https://github.com/Idehed/Project-3-battleships/assets/146822758/0968612b-9701-4644-952f-4773f21a1eae)

- User/computer hit-and-miss confirmation 
    - Hit message is displayed in the terminal if the user hits one of the computer ships.
    - The same if the computer's ship is hit.
    - Miss message is displayed if the user missed one of the computer's ships.
    - The same if the computer's ship is missed.

![hit player](https://github.com/Idehed/Project-3-battleships/assets/146822758/a1eb99e7-5617-41ed-b6af-91264a7e45aa)


![hit computer](https://github.com/Idehed/Project-3-battleships/assets/146822758/7d740906-8bd4-4eec-ae7b-444d03336dc4)


![miss player](https://github.com/Idehed/Project-3-battleships/assets/146822758/294c8ac1-d15a-425a-8bd5-472a4e702eb2)

![miss computer](https://github.com/Idehed/Project-3-battleships/assets/146822758/41b9d4fa-c3f8-4331-baba-ab71bc903be8)

- This message is displayed if you win.
- And if you lose this message is displayed "The computer hit all your ships, you lose... "

![player win](https://github.com/Idehed/Project-3-battleships/assets/146822758/6a303fc4-d967-459f-b645-8f4f6ee1ef47)


# Testing
I tested the game manually by doing this:
- I passed my code in the PEP8 Linter. 
- I gave the wrong input, row/column was not in range,  and the same input was twice.
- Tested the in the Heroku terminal and my local terminal.

## Bugs

- When the player hit a ship the counter that was displayed showed "computer: 1", instead of "player: 1".
Needed to changed that in this code : 

            print("\n" + "=" * 40)
            print("Player: {}, Computer: {}".format(
                ship_hit(HIDDEN_COMPUTER), ship_hit(PLAYER_BOARD_SEEN)))
            print("=" * 40 + "\n")

- After changing it worked fine.
## Remaining bugs
- No bugs remaining

## Validator Testing 

PEP8:

- Most of my errors were whitespaces, too many black lines, or line too long. These were easily fixed in the code.
- After fixing them no errors returned.


![pep8](https://github.com/Idehed/Project-3-battleships/assets/146822758/9ac4e5c4-86bf-4a46-b95c-046efd07a0e6)

![pep8](https://github.com/Idehed/Project-3-battleships/assets/146822758/6f01741a-6d79-42a2-a1b7-cf438bbcc131)

![pep8](https://github.com/Idehed/Project-3-battleships/assets/146822758/4f6caed1-446c-4fa8-9266-175261974a99)

---

# Deployment 
This project was deployed using Code Institute's mock terminal for Heroku.

- How to deploy: 
   - Fork or clone this repository.
   - Create/log into a Heroku account.
   - Go to your dashboard and then click New, Create new app.
   - Choose your app name(needs to be unique) and region.
   - Click Create app.
   - Go to settings and add a new config var. Key: PORT ,Value: 8000
   - Then add two new buildpacks, Python and Nodejs. In this order. 
   - Find the forked/cloned repository and connect to it.
   - Click Deploy!


# Credits

- [Garrett Broughten](https://github.com/gbrough/battleship/blob/main/5_ship_types_with_computer.py) Helping me with some of my code.
- [Stackoverflow](https://stackoverflow.com/questions/75696001/battleships-game-python-when-playing-game-no-hits-are-recorded-through-the-ga) Showed me how to hide the computer board.
- [w3schools](https://www.w3schools.com/python/ref_string_format.asp) Learnt how to use the format method for showing the hit counter in the terminal.
- My mentor Ronan Mc for his support and guidance.
