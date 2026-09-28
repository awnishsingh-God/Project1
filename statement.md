#### **#Problem Statement: The Hexagon Citadel Castle**



* Project Name: ***The Hexagon Citadel: Journey of The Syntax Guardian***
* Language: (Python 3.13.14)
* Genre: Interactive Text-Based CLI Adventure / Number Guessing Game



#### \#1. Overview \& Background



* You play as the \*\*Syntax Guardian\*\*, a fearless programmer trained by High Sorcerer Ajeet Singh. Sent to the treacherous Mount Abyssus, you must scale the Hexagon Citadel Castle and defeat the undefeated \*\*Professor Hexadecimal\*\* in a duel of logic. To survive and achieve the title of \*Grand Master of the Python Realm\*, you must guess the secret number before you are cast into the Endless Void.



#### \#2. Game Rules \& Constraints



* NUMBER RANGE :-1 TO 10 inclusive
* ATTEMPT LIMIT:- 5 attempts (4 if you have taken the hint)
* INPUT VALIDATION :- Range error checks (`1-10`) and `ValueError` handling for non-integer inputs.



#### \#3. Program Specifications



* \~\~\~INPUT\~\~\~
* 1\. Player Name: String input converted to uppercase to match the introduction body .
* 2\. Player Guesses: Integer values ranging strictly between `1` and `10` if input out of the range then it ask for repeated input.
* 3\. Hint Choice: Optional `YES` or `NO` text input on attempt 2 which will cost the player 1 attempt.
* 
* \~\~\~Output \& Flow\~\~\~
* 1\. Prologue: Dramatic story narrative introducing the characters with timed delays (`time.sleep()`).
* 2\. Game Loop:
* &#x20;   - Prompts for player input with input validation.
* &#x20;   - Evaluates input against `secret\_number`.
* &#x20;   - Offers a hint option on attempt #2 (WHICH WILL TELL THAT THE NUMBER ENTERED IN 2ND ATTEMPT IS GREATER OR LESSER THAN THE SECRET NUMBER).
* 3\. End States:
* &#x20;   - Victory State: Displays the victory text, unlocks the \*Gates of Knowledge\*, and terminates the loop.
* &#x20;   - Defeat State: Triggered after 5 failed attempts, resulting in a \*Game Over\* scene and a dramatic ending.
* 4\. Execution Example
* ```text


Enter your name:-SYNTAX GUARDIAN



&#x20;                   ONCE UPON A TIME THERE LIVED A MAN\~ THE SYNTAX GUARDIAN\~ NAMED SYNTAX GUARDIAN A FEARLESS PROGRAMMER.....AFRAID OF NOTHING...

&#x20;                     He was sent on a mission by his master HIGH SORCERER AJEET SINGH to defeat THE UNDEFEATED PROFFESOR HEXADECIMAL.





&#x20;                 So he packed his PC and went to the GREAT MOUNT ABYSSUS....a mountaion which was directly attached to an endless DARK VOID

&#x20;                                           On the top of the mountain sat the HEXAGON CITADEL CASTLE of the Proffesor....







==========================================================WELCOME TO THE HEXAGON CITADEL CASTLE============================================================



&#x20;                   HALT, Tarnished one! I am THE PROFFESOR HEXADECIMAL !!!!! Your master sent you to learn Python ? \[Laughs mockingly]

&#x20;                                    but your journey ends here! Guess my secret number, Tarnished One, or fall into the Void!





&#x20;                 I will be generous with you by giving you 5 ATTEMPTS.....THE NUMBER I AM THINKING WILL BE IN BETWEEN OF 1 TO 10.........

&#x20;                            BEWARE!!!!!! TARNISHED ONE.. DO NOT GUESS BLINDLY , THINK BEFORE MAKING YOUR NEXT CHOICE......



&#x20;                                         OR ELSE YOU WILL BE PUSHED IN AN ENDLESS VOID AND FALL FOR ETERNITY







\~\~\~\~\~\~\~\~\~\~\~\~\~\~\~\~\~\~\~\~\~\~\~\~\~\~\~\~\~\~\~\~\~\~\~\~\~\~\~\~\~\~\~\~\~\~\~\~\~\~\~\~\~\~\~\~\~LETS START...... GOOD LUCK TARNISHED ONE\~\~\~\~\~\~\~\~\~\~\~\~\~\~\~\~\~\~\~\~\~\~\~\~\~\~\~\~\~\~\~\~\~\~\~\~\~\~\~\~\~\~\~\~\~\~\~\~\~\~\~\~\~\~\~\~\~\~\~



OKAY TARNISHED WHATS YOUR GUESS??:-1



&#x20;       TARNISHED ONE the number you entered is not correct ..........





&#x20;       Try AGAIN Tarnished one \[PROFFESOR LAUGHING AND MOCKING YOU]........



OKAY TARNISHED WHATS YOUR GUESS??:-5



&#x20;       TARNISHED ONE your guess is incorrect once again...I FEEL PITY FOR YOU..........





&#x20;       OKAY TARNISHED ONE..... WOULD YOU LIKE TO HAVE A HINT ????

&#x20;           BUT IT WILL REDUSE YOUR 1 TRY.. CHOOSE WISELY.......



Enter yes or no:-YES



&#x20;               TARNISHED ONE ..... YOU HAVE CHOSEN TO SACRIFICE YOUR 1 TRY TO GET A HINT........





&#x20;               TARNISHED ONE .....THE NUMBER YOU ENTERED NOW WAS LESSER THAN THE NUMBER I WAS THINKING........




&#x20;               TARNISHED ONE i expected more from the student of THE HIGH SORCEROR ............. '''

