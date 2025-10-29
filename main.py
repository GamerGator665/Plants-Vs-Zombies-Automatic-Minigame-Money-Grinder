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
# Handling of exit requests:
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
                print("\nAll coordinates captured successfully!")
                return False
            else:
                print(f"\nMove your mouse to the {coord_labels[capture_index]} and press SPACE...")

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

    print("\nCaptured Coordinates:")
    for label, (x, y) in captured_coords.items():
        print(f"{label}: ({x}, {y})")

    return captured_coords


# ----------------------------------------------------------------------
# 3. AUTOMATION LOGIC
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
    print("= STARTING AUTOMATION LOOP (Press 'Q' to Stop) =")

    while running:
        try:
            print("Collecting $500/$1250")

            # 1. Minigame/Survival Icon
            x_star, y_star = captured_coords["Minigame/Survival Icon"]
            click_at_position(x_star, y_star, "Minigame/Survival Icon")

            # 2. Continue Button
            x_cont, y_cont = captured_coords["Continue"]
            click_at_position(x_cont, y_cont, "Continue")

            # 3. Money Bag
            x_bag, y_bag = captured_coords["Money Bag/Trophy"]
            click_at_position(x_bag, y_bag, "Money Bag/Trophy")
            print("Money bag successfully collected.")

            # Delay between loops
            print(f"Pausing for {DELAY_FOR_LOOP} seconds before looping...")
            for _ in range(int(DELAY_FOR_LOOP * 10)):
                if not running:
                    break
                time.sleep(0.1)

        except Exception as e:
            print(f"[ERROR] {e}")
            running = False


# ----------------------------------------------------------------------
# 4. START / STOP KEYBINDS
# ----------------------------------------------------------------------

def exit_thread_worker():
    """Handles Q presses and waits for ENTER."""
    while True:
        exit_request.wait()  # Wait until Q is pressed
        exit_request.clear()  # Reset for next Q press

        # Show prompt
        try:
            input("\nPress ENTER to fully exit the program...")
        except (EOFError, KeyboardInterrupt):
            pass
        
        # Mark that exit is confirmed
        exit_confirmed.set()

        print("[INFO] Exiting program immediately...")
        sys.exit(0)



def on_press_main(key):
    """Handles M/Q keybinds for automation."""
    global running, exit_prompt_active

    try:
        char = key.char.upper()
    except AttributeError:
        return

    # Start automation
    if char == 'M' and not running:
        running = True
        print("[INFO] Starting automation...")
        t = threading.Thread(target=automation_logic, daemon=True)
        t.start()

    # Clear any pending exit request
        if exit_request.is_set():
            print("[INFO] Automation resumed. Canceling pending exit prompt.")
            exit_request.clear()


    # Stop automation
    elif char == 'Q':
        if running:
            running = False
            print("[INFO] 'Q' key detected. Automation will stop after current action.")
            print("\nPress Enter to terminate the program.")
        else:
            print("[INFO] 'Q' pressed — automation already stopped.")
            print("\nPress Enter to terminate the program.")

        # Always start a new exit thread for each Q press
        exit_request.set()  # Signal the exit thread to show prompt


    # Re-capture coordinates
    elif char == 'C':
        print("[INFO] 'C' key detected. Starting coordinate re-capture...")
        recapture_coordinates()

    # View README file
    elif char == 'R':
        print("[INFO] Loading README file...")
        readme_documentation()


def listen_for_keybinds():
    """Sets up the keyboard listener for M/Q."""
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
    """Re-captures all coordinates (on 'C' press)."""
    global captured_coords, capture_index, capture_done, running

    if running:
        running = False
        print("[INFO] Due to coordinate re-capture, automation has been paused.")

    captured_coords.clear()
    capture_index = 0
    capture_done = False

    new_coords = get_coordinates_via_spacebar()
    captured_coords.update(new_coords)
    print("[INFO] Coordinates successfully updated.")
    listen_for_keybinds()


def readme_documentation():
    """Outputs the README file. That's about it."""
    global running

    if running:
        running = False
        print("[INFO] Due to the execution of the README output, automation has been paused.")

    print("Loading... Please wait...")
    time.sleep(random.uniform(0.5, 1.5))
    print("Well, you found me. Actually someone who wants to read the README...")
    print("Before you go, I just need to tell you that this README was made in Markdown, and therefore has a lot of Markdown formatting.")
    print("If you think there are too many *s, either your terminal is incompatible with Markdown or you haven't installed Rich. Loading README.md in 5 seconds.")
    time.sleep(5)
    try:
        try:
            # Attempt to use rich for nicer Markdown rendering
            from rich.console import Console
            from rich.markdown import Markdown

            console = Console()
            with open("README.md", "r", encoding="utf-8") as f:
                md_content = f.read()

            console.print(Markdown(md_content))

        except (ImportError, FileNotFoundError):
            # If rich isn't installed or README.md is missing, fallback to plain print
            try:
                with open("README.md", "r", encoding="utf-8") as f:
                    print("Rich library not found, falling back to plaintext, there may be a lot of *s.")
                    print(f.read())
            except FileNotFoundError:
                print("Error: README.md file not found.")
            except Exception as e:
                # Catch anything else just in case
                print(f"An error occurred while reading README.md: {e}")

    except Exception as e:
        # Catch any remaining unexpected errors to prevent pynput traceback
        print(f"[ERROR] Could not display README: {e}")


# ----------------------------------------------------------------------
# 5. Execution
# ----------------------------------------------------------------------
if __name__ == "__main__":
    try:
        captured_coords = get_coordinates_via_spacebar()
        listen_for_keybinds()
    except KeyboardInterrupt:
        sys.exit()
