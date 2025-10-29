=========================================================

PvZ Automatic Minigame Money Grinder (PVZ-AMMG) - README

=========================================================



Version: 1.0



This Python script automates the process of grinding money in Plants vs. Zombies (PvZ) by repeatedly collecting a money bag at the end of a minigame.



This script uses the pyautogui library to control your mouse and pynput to listen for your keyboard commands (Start, Stop, Recapture), meaning that this program is not suitable for use with other programs simultaneously.



=================================

\*\*!! CRITICAL DISCLAIMER !!\*\*

=================================



This script takes \*\*FULL CONTROL\*\* of your mouse. Once you press 'M' to start, it will continuously click the coordinates you have set.



* Like I said before, \*\*DO NOT\*\* attempt to use your computer for other tasks while the script is running.
* &nbsp;To stop the script, press 'Q'. This will pause the automation. You can then press 'ENTER' to fully terminate the program when focused on the window.
* &nbsp;The author would like to say that this code is fully coordinate-based and cannot automatically relocate the coordinates if you move the game window! (Yes, I'm looking at people like Code Bullet who don't know how to use a failsafe in a script that uses their mouse, but still does weird stuff with it anyway!) 







==================================

Step 1: Minigame Farming Setup

==================================



This script is specifically designed for the minigame money-farming strategy. For example, if the minigame used is "Last Stand", the loop it automates is:



1\.  \*\*On the "Minigame" screen:\*\* Clicks the "Last Stand" icon.

2\.  \*\*On the "Continue Game?" screen:\*\* Clicks the "Continue" button.

3\.  \*\*On the lawn:\*\* Clicks the Money Bag or Trophy to collect the coins.

4\.  \*\*During the cutscene\*\* Waits for 6 seconds before looping, to avoid complications caused by clicking during the cutscene.



\*\*REQUIREMENTS:\*\* For this to work, you must have \*already completed\* a minigame so that a money bag/trophy is waiting for you on the lawn. The script does not play the game; it only collects the reward you've already earned.

\*\*SETUP:\*\* To set it up, all you need to do is create a save state of the money bag/trophy on the lawn. To do this, complete a minigame. Before picking up the reward, click "Menu" and then "Main Menu". Choose to leave when prompted, and then when you go back to the minigame, the reward should still be on the lawn.



=================

2\. Requirements

=================



\* \*\*Python 3:\*\* This script is written for Python 3.

\* \*\*PvZ:\*\* Pretty obvious. I recommend Windowed mode, since the script can then be easily closed if problems occur.

\* \*\*Required Python Libraries:\*\* pyautogui and pynput.





=================

2a. Installation 

=================

Please note, I use Windows, and I am unaware of how to do this on Mac/Linux.



Before running the script, you must install the required libraries.

Assuming you have Python installed:



1\.  Open PowerShell.

2\.  Run the following commands:



&nbsp;   `py -m pip install pyautogui`

&nbsp;   `py -m pip install pynput`



The script should now be able to run, assuming you have Python installed.

----------------

3\. How to Use (Step-by-Step)

----------------



Follow these instructions \*exactly\* to ensure the script works.



\### Step 1: Game Setup



1\.  Launch Plants vs. Zombies.

2\.  Go to the "Minigames" screen.

3\.  Ensure you have a reward (money bag or trophy) waiting for you on a minigame. If you don't have any, play one round and save the reward (Check back to the end of Section 1 for instructions on how to do this!).



\### Step 2: Run the Script



Open the 'main.py' file. It's seriously that simple. (If you have the default app set to open a python file as something other than Python (e.g. VS Code), then open with Python.)



\### Step 3: Capturing Coordinates



The terminal will now ask you to capture three coordinates. You must press the Spacebar to capture the mouse's current position for each target.



\*\*IMPORTANT! PLEASE DO NOT MOVE YOUR GAME WINDOW DURING THIS PROCESS!\*\*



1\.  \*\*Target 1: "Minigame/Survival Icon"\*\*

&nbsp;   \* Go to your PvZ window (which should be on the Minigame selection screen).

&nbsp;   \* Move your mouse cursor to point directly over the chosen minigame icon.

&nbsp;   \* Press the Spacebar once.



2\.  \*\*Target 2: "Continue"\*\*

&nbsp;   \* \*\*BEFORE YOU PRESS SPACE:\*\* Manually \*\*click\*\* the "Last Stand" icon to proceed to the "Continue Game?" screen.

&nbsp;   \* Once the "Continue Game?" screen loads, move your mouse cursor over the \*\*"Continue" button\*\*.

&nbsp;   \* Press the Spacebar once.



3\.  \*\*Target 3: "Money Bag/Trophy"\*\*

&nbsp;   \* \*\*BEFORE YOU PRESS SPACE:\*\* Manually \*\*click\*\* the "Continue" button to proceed to the lawn.

&nbsp;   \* Move your mouse cursor directly over the \*\*money bag\*\* (or trophy) that you click to collect coins.

&nbsp;   \* Press the Spacebar once.



Once done, the terminal will confirm "All coordinates captured successfully!"



\*\*!!! FINAL WARNING !!!\*\*

Once the coordinates are captured, \*\*DO NOT MOVE OR RESIZE THE PLANTS VS. ZOMBIES WINDOW.\*\* The script clicks specific (X, Y) pixels on your screen. If you move the window, the coordinates will be wrong, and the script will click in the wrong places.



\### Step 4: Run the Automation



The script is now ready and waiting for your command.



\* \*\*Press 'M' to START\*\*



\*\*NOTE! Before pressing M, please ensure that you are on the Minigame screen!\*\*

&nbsp;   \* The automation loop will begin. You will see messages in the terminal describing the current state.

&nbsp;   \* Your mouse will move and click automatically.



\* \*\*Press 'Q' to STOP\*\*

&nbsp;   \* The automation will stop after its current action.

&nbsp;   \* You can press the Enter key to close the script.





============

4\. Controls

============



\* \*\*'M' (For Money):\*\* Begins the automation loop.

\* \*\*'Q' (For Quit):\*\* Stops the automation loop and prompts you to exit.

\* \*\*'ENTER' (After 'Q'):\*\* Confirms and exits the entire program.

\* \*\*'C' (For (re)Capture):\*\* Stops automation (if running) and restarts the coordinate capture process (Step 3). Use this if you accidentally move the game window.

\* \*\*'R' (Readme):\*\* Well, this is awkward.





==========================

5\. FAQ (Will be updated)

==========================



\* \*\*Q: The mouse is clicking in the wrong spot!\*\*

&nbsp;   \* \*\*A:\*\* You 99% most likely moved or resized the game window after capturing coordinates. Press `Q` (then `ENTER`) to stop the script. Relaunch it, or press `C` to restart the coordinate capture process.



\* \*\*Q: The script fails or throws an error.\*\*

&nbsp;   \* \*\*A:\*\* Make sure you have installed the required libraries: pyautogui and pynput.



\* \*\*Q: The script runs, but it gets stuck or doesn't work.\*\*

&nbsp;   \* \*\*A:\*\* You likely did not set up the game state correctly. Remember, the script only \*collects\* the reward; it doesn't \*earn\* it for you.



\* \*\*Q: My question isn't here!\*\*

&nbsp;   \* \*\*A:\*\* Submit a bug report on GitHub.

