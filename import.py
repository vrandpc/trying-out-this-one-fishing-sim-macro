import pyautogui
import time

print("Press Ctrl+C to stop.")

try:
    while True:
        # Get the current mouse position
        x, y = pyautogui.position()
        
        # Ensure that coordinates fit within the console and are accurate
        # Format the output to be more readable, aligning with the screen resolution
        print(f'Mouse Position: X={x:<4} Y={y:<4} (Width: 1920, Height: 1080)', end='\r')
        
        # Sleep for a short time to avoid flooding the console
        time.sleep(0.1)
except KeyboardInterrupt:
    print("\nMouse tracking stopped.")
