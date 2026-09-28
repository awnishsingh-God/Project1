#### **# The Hexagon Citadel: Journey of The Syntax Guardian**



* **An immersive, story driven Python game where players plays as the "Syntax Guardian" to face Professor Hexadecimal in a high-stakes number-guessing duel at Mount Abyssus.**



#### \# Overview of the project:



* This Program is based mainly on "Random number generation"...this is attained by an inbuilt module from python library called "Random module"
* There are many uses of random numbers For example OTP generation, captcha, random password generation etc.
* The Hexagon Citadel transforms a classic number-guessing game into a fantasy text adventure. You must guess Professor Hexadecimal's secret number (between 1 and 10) within 5 attempts. The game features interactive and dramatic dialogue, input validation, and a risk-reward hint system where asking for a clue will cost a precious attempts.

#### 

#### \# Features:



* *Story-Driven Narrative:* Lore-driven story and ending depend on the choices the player made
* *Cinematic Pacing:* Intentional Delays using `time.sleep()` to build suspense during the game dialogues and encounters.
* *Input Validation \& Error Handling:* `try-except` blocks to handle non-numeric inputs and out-of-range guesses without crashing **"hence reducing the error chances".**
* *Strategic Hint System:* Players can sacrifice 1 attempt after their #2 attempt to learn whether their guess was too high or too low "Hint system".
* *Dynamic Branching Outcomes:* Custom dramatic win/loss epilogues depending on your success or failure.



#### \# Technologies \& Tools Used:



* Programming Language: Python 3
* Standard Libraries Used: 

&#x20;  `random` – For secret number generation

&#x20;  `time`   – For text pacing and suspense delays



#### \#Steps to Install and run:

* Prerequisites: Install \*\*Python 3.x\*\* from the official site: \[python.org](https://www.python.org/downloads/)
* Execution Steps

&#x20;     1. Download the File:- Download `game.py` into any folder on your computer.



&#x20;     2. Open Terminal / Command Prompt\*\*

&#x20;       - \*\*Windows:\*\* Press `Win + R`, type `cmd`, and press Enter. Navigate to your folder:

&#x20;         ```cmd

&#x20;         cd path\\to\\your\\folder

&#x20;         ```



&#x20;       - \*\*macOS / Linux:\*\* Open Terminal and navigate to your folder:

&#x20;         ```bash

&#x20;         cd path/to/your/folder

&#x20;         ```



&#x20;     3. \*\*Launch the Game\*\*

&#x20;        Run the program using:

&#x20;        ```bash

&#x20;        python main.py



#### \#Instructions for Testing:



To thoroughly test all mechanics in the game:



* ***Test Valid Guesses (Win Scenario)***: Play the game and guess numbers until you hit the secret number. Verify that the win message and ascension to "Grand                          				      Master" trigger properly. 



* ***Test Out-of-Range Inputs***: Enter numbers like 0, 11, or 99. Check the game prompts you to enter a number between 1 and 10 without increasing your try      			     counter.



* ***Test Non-Numeric Input Handling***: Enter letters or special characters (e.g., abc, @#$). Ensure the ValueError catch works and lets you try again.



* ***Test the Hint System***: Fail your first two guesses.

&#x20;

* ***When prompted for a hint***: Type yes to confirm your attempt counter increases by 1 and a high/low clue is displayed. 

&#x20;                            Play again and type no to confirm te hint is skipped smoothly.

* ***Test Loss Scenario***: Intentionally guess incorrectly 5 times to trigger the "Endless Void" game over sequence.



#### \#Screen shots:





#### &#x20;

