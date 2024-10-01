import pyautogui
import time

print("Press Ctrl+C to stop.")

try:
    while True:
        # Get the current mouse position
        x, y = pyautogui.position()
        # Print the current position
        print(f'Mouse Position: X={x}, Y={y}', end='\r')
        # Sleep for a short time to avoid flooding the console
        time.sleep(0.1)
except KeyboardInterrupt:
    print("\nMouse tracking stopped.")
