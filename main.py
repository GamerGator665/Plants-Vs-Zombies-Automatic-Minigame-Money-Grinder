import pyautogui
import random
from pynput import keyboard
import time
import sys
import threading


# ----------------------------------------------------------------------
# Global Variables
# ----------------------------------------------------------------------
running = False
exit_prompt_active = False
captured_coords = {}
coord_labels = ["Minigame/Survival Icon", "Continue", "Money Bag/Trophy"]
capture_index = 0
capture_done = False
listener = None 
# Everything below here is part of that random code I threw together that where I said, and I quote: "I don't know what happened here, but this was the only thing I could figure out to handle Q presses that didn't make the whole program collapse.":
exit_request = threading.Event()  
exit_confirmed = threading.Event()  

# ----------------------------------------------------------------------
# Coordinates Capturing
# ----------------------------------------------------------------------
def on_press_capture(key):
    """Handles keypress during coordinate capture."""
    global capture_index, captured_coords, capture_done

    try:
        if key == keyboard.Key.space:
            x, y = pyautogui.position()
            label = coord_labels[capture_index]
            captured_coords[label] = (x, y)
            print(f"Successfully Captured {label}: ({x}, {y})")
            capture_index += 1

            if capture_index >= len(coord_labels):
                capture_done = True
                print("All coordinates captured successfully!")
                return False
            else:
                print(f"Move your mouse to the {coord_labels[capture_index]} and press SPACE...")

    except AttributeError:
        pass


def get_coordinates_via_spacebar():
    """Prompts the user to capture all 3 coordinates interactively."""
    print("-----------------------------------------------------")
    print("If you have any questions, please refer to the README.txt.")
    print("Please capture coordinates:")
    print("Hover over each target and press Spacebar to capture.")
    print("Once this is done, and I can't stress this enough,")
    print("PLEASE DO NOT MOVE YOUR PVZ WINDOW!")
    print("This will make the script click random objects.")
    print("You will have the option to re-capture these coordinates.")
    print("Targets to capture (in order):")
    for label in coord_labels:
        print(f" • {label}")
    print("Please hover over the Minigame or Survival icon and press Spacebar.")
    print("-----------------------------------------------------")

    while not capture_done:
        with keyboard.Listener(on_press=on_press_capture) as listener:
            listener.join()

    print("Captured Coordinates:")
    for label, (x, y) in captured_coords.items():
        print(f"{label}: ({x}, {y})")

    return captured_coords


# ----------------------------------------------------------------------
# Automation
# ----------------------------------------------------------------------
DELAY_AFTER_CLICK = 0
DELAY_FOR_LOOP = 6


def click_at_position(x, y, label):
    """Moves the mouse to a position and clicks it."""
    if not running:
        return
    print(f"Clicking {label} at ({x}, {y})")
    pyautogui.moveTo(x, y, duration=0)
    pyautogui.click()
    time.sleep(DELAY_AFTER_CLICK)


def automation_logic():
    """Main automation loop."""
    global running

    print("=============================================")
    print("STARTING AUTOMATION LOOP (Press 'Q' to Stop)")

    while running:
        try:
            print("Collecting $500/$1250")

            x_star, y_star = captured_coords["Minigame/Survival Icon"]
            click_at_position(x_star, y_star, "Minigame/Survival Icon")

            x_cont, y_cont = captured_coords["Continue"]
            click_at_position(x_cont, y_cont, "Continue")

            x_bag, y_bag = captured_coords["Money Bag/Trophy"]
            click_at_position(x_bag, y_bag, "Money Bag/Trophy")
            print("Money bag successfully collected.")

            print(f"Pausing for {DELAY_FOR_LOOP} seconds before looping...")
            for _ in range(int(DELAY_FOR_LOOP * 10)):
                if not running:
                    break
                time.sleep(0.1)

        except Exception as e:
            print(f"[ERROR] {e}")
            running = False


# ----------------------------------------------------------------------
# Keybinds
# ----------------------------------------------------------------------

def exit_thread_worker():
    """I don't know what happened here, but this was the only thing I could figure out to handle Q presses that didn't make the whole program collapse."""
    while True:
        exit_request.wait()  
        exit_request.clear()  

        try:
            input("Press ENTER to fully exit the program...")
        except (EOFError, KeyboardInterrupt):
            pass
        
        exit_confirmed.set()

        sys.exit(0)



def on_press_main(key):
    """Handles M/Q keybinds for automation."""
    global running, exit_prompt_active

    if hasattr(key, 'char') and key.char is not None:
        char = key.char.upper()

        if char == 'M' and not running:
            running = True
            print("Starting automation...")
            t = threading.Thread(target=automation_logic, daemon=True)
            t.start()

        elif char == 'Q':
            if running:
                running = False
                print("Automation will stop after current action.")
                print("Press Enter to terminate the program.")
            else:
                print("Automation already stopped.")
                print("Press Enter to terminate the program.")

            exit_request.set()

        elif char == 'C':
            print("Starting coordinate re-capture...")
            recapture_coordinates()

        elif char == 'R':
            print("Loading README file...")
            readme_documentation()

    elif key == keyboard.Key.enter:
        if not running:
            print("Terminating program... Please wait...")
            time.sleep(random.uniform(1.5,5))
            os._exit(0)

def listen_for_keybinds():
    """Sets up the keyboard listener for M/Q/C/R."""
    global listener
    print("-----------------------------------------------------")
    print("Automation Controls:")
    print("Press 'M' to START automation.")
    print("Press 'Q' to STOP automation (then press ENTER to exit).")
    print("Press 'C' to RECAPTURE the coordinates of the UI elements.")
    print("Press 'R' to view the README.")
    print("Why am I giving you the power to get infinite PvZ money?")
    print("Because I'm CRAZY!")
    print("-----------------------------------------------------")

    listener = keyboard.Listener(on_press=on_press_main)
    listener.start()
    listener.join()


def recapture_coordinates():
    """Re-captures all coordinates)."""
    global captured_coords, capture_index, capture_done, running

    if running:
        running = False
        print(" Due to coordinate re-capture, automation has been paused.")

    captured_coords.clear()
    capture_index = 0
    capture_done = False

    new_coords = get_coordinates_via_spacebar()
    captured_coords.update(new_coords)
    print(" Coordinates successfully updated.")
    listen_for_keybinds()


def readme_documentation():
    """Outputs the README file. That's about it."""
    global running

    if running:
        running = False
        print("Due to the execution of the README output, automation has been paused.")

    print("Loading... Please wait...")
    time.sleep(random.uniform(0.5, 1.5))
    print("Well, you found me. Actually someone who wants to read the README...")
    print("Before you go, I just need to tell you that this README was made in Markdown, and therefore has a lot of Markdown formatting.")
    print("If you think there are too many *s, either your terminal is incompatible with Markdown or you haven't installed Rich. Loading README.md in 5 seconds.")
    time.sleep(5)
    try:
        try:
            from rich.console import Console
            from rich.markdown import Markdown

            console = Console()
            with open("README.md", "r", encoding="utf-8") as f:
                md_content = f.read()

            console.print(Markdown(md_content))

        except (ImportError, FileNotFoundError):
            try:
                with open("README.md", "r", encoding="utf-8") as f:
                    print("Rich library not found, falling back to plaintext, there may be a lot of *s.")
                    print(f.read())
            except FileNotFoundError:
                print("Error: README.md file not found.")
            except Exception as e:
                print(f"An error occurred while reading README.md: {e}")

    except Exception as e:
        print(f"[ERROR] Could not display README: {e}")


# ----------------------------------------------------------------------
# This is practically the main code. That's the power of subroutines!
# ----------------------------------------------------------------------
if __name__ == "__main__":
    try:
        captured_coords = get_coordinates_via_spacebar()
        listen_for_keybinds()
    except KeyboardInterrupt:
        sys.exit()



