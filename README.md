# YouFastEnough_PyGame
Game Code used to compete in the 2024 ENCMP 100 Programming Contest hosted by Dr Dileepan Joseph

"You Fast Enough? - Aaron Bernard-(https://www.linkedin.com/in/aaron-bernard-8bab28213/) and Harshavardan Maheskumar-(https://www.linkedin.com/in/harsha-vardan/)

Contest required a submission that would later be uploaded onto YouTube: https://www.youtube.com/watch?v=Ih0zuZ7bIUk
Programming and Voice-over done by: Aaron Bernard (voice is sped up to meet submission limit of 5 mins - might sound different)
Video editing done by (among other media related things refer References): Harshavardan Maheskumar

## YouTube Description: 
"
Dive into a "Subway Surfers"-like mini-game, where the entire point of the game is no point at all!
Inspired by games like mobile game "Subway Surfers", "Flappy Bird" and our all time guilty pleasure, the 
"Chrome T-Rex Game", we strive to offer the user another game to pass time with; an 'Infinite Runner'.

Involving the game mechanic/idea that the game is 'infinite', i.e. the game is played for as long as the user 
wishes to play, attaining the highest score they possibly can. Similar to the player controlling the 'subway surfer'
for as far as they can make it past all the trains at increasing speeds; or the increased objects and increased speeds the
Dino/T-Rex (player) has to adapt to and dodge for the highest possible score they may score - in a practical setting.

The game itself, unlike those mentioned above, is a memory-game instead, where a randomly-generated string of characters are 
generated to the screen.
You, a player, choose between 3 different game modes, allowing for different difficulties, similar to increased 
'surfer' speed in "Subway Surfers". 
Each mode increasing in difficulty in terms of the amount of time left for you to answer (Timer Difficulty), 
the number of blanks to answer (Character-Input Difficulty) and whether the character input (Character Difficulty) 
is: alphabet-only (upper and lowercase), numerical-integer-only (single digits 0-9), or alphanumeric (a combination of 
upper/lowercase alphabets and single-digit integer numbers from 0-9).

Regardless of game mode (easy, medium or hard) a typical attempt will seem as such: 
- the player chooses a game mode;
- start the game at the player's free will;
- the randomly-generated string characters will then be hidden from the player;
- have a timer count down, representing how long the player has to attempt as many 'game attempts' as they can, using keyboard inputs;
- when they have successfully answered a 'randomly-generated' string, a new string will be generated, showing for a short 
period of time (2 seconds) before being hidden from the player to continue the gameplay;
(each successful entry adds 5 seconds to the timer as well as adds 10 points to your current score of that game mode)
- unsuccessful attempts display a red box, indicating a wrong entry, and will continue as is with a cleared input area, 
allowing the user to continue inputing values till their time's up;
- a 'hint's button exists, allowing the player to temporarily see the generated string of characters after it has been
generated and the player needs help;
- once the time runs out, the game is over, and a 'game over' screen is displayed to the user;
- the user is then allowed to either -> 'play again' or 'quit' the game altogether;
- 'quit' quits the game
- 'play again' takes the user back to the main menu where they will be allowed to play the game again.
And the process will repeat wherein the player will choose a preferred game mode, start, submit entries and so on and so forth

Instructions for the game as well as the player's highest score across all 3 game modes are displayed in the main menu.
"



## Cautions/Program Flow:
- choose a game mode from the main menu (suggested game mode: Easy or Medium; Hard has a smaller amount of time as well as more inputs
and is alphanumeric in input). play the game (using the 'menu' button you can leave anytime (except when the 'game over' screen comes
up), even during the game itself, and everything will reset).

- 'hint's reveal the hidden string of characters 

- 'game over' screen has a 'play again' (takes you back to the main menu to play the game again) and 'quit' button completely terminates
the code and exits

- (imp) if you backspace too fast, the value will be removed from the array as expected, but the display may be delayed in updating 
the display and removing the backspaced value and may also not even remove the displayed value at all - even though it has been
correctly backspaced from the list holding all inputted values. A debugging print statement was used to observe if the array holding
the inputted values was being correctly '.pop()' when the backspace was clicked - you can observe if you backspace (even faster 
than normal pace) you will remove the value from the array but the display may not follow suit and may still exist on the display. 
This could be amounted to the Spyder IDE itself for the delay, or worse, incorrect display screen



## References:
**All media related work: presentation; video-recording; video-editing --> done by Harshavardan Maheskumar**
Video Editing Software: “Final Cut Pro FX” 

Dictionary Revision: https://www.w3schools.com/python/python_dictionaries.asp
Random – Randint: https://www.w3schools.com/python/module_random.asp 

All pygame references:
-	Timer: https://www.youtube.com/watch?v=bdblBxRsik4 – Sam Whitby Coding
-	Input : https://www.youtube.com/watch?v=7ZR-XIDbZag – Coding with Russ
-	“How to create a menu”: https://www.youtube.com/watch?v=2iyx8_elcYg – Coding with Russ
-	Getting-started: https://www.youtube.com/watch?v=y9VG3Pztok8 – Coding with Russ
-	Event handler: https://www.youtube.com/watch?v=KR2zP6yuWAs – Coding with Russ
-	Keyboard input: https://www.youtube.com/watch?v=Hujzny-gkEk – Coding with Russ
-	Mouse input: https://www.youtube.com/watch?v=YbouZ2X8fGk – Coding with Russ
-	Displaying text: https://www.youtube.com/watch?v=ndtFoWWBAoE – Coding with Russ
-	Displaying shapes: https://www.youtube.com/watch?v=YDP1Hk7uZFA – Coding with Russ
-	Buttons-text: https://www.youtube.com/watch?v=jyrP0dDGqgY  – Coding with Russ
-	Buttons-images: https://www.youtube.com/watch?v=G8MYGDf_9ho  – Coding with Russ

Downloaded Font Style: “TechnoRaceItalic-eZRWe.otf” by Nirmana Visual. 
Downloaded from “Font Space” - https://www.fontspace.com/category/gaming

All code structures and learning are credited to those above.
