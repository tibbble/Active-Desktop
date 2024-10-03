import math
import time
import argparse
from pynput import keyboard
from pynput.mouse import Controller


def circular_motion(*, t: float, radius: float, step_degrees: float, mouse: Controller):
    mouse_relative_x = math.cos(math.radians(t * step_degrees)) * radius
    mouse_relative_y = math.sin(math.radians(t * step_degrees)) * radius
    mouse.move(mouse_relative_x, mouse_relative_y)


def on_press(key, running, end_time):
    if key in [keyboard.Key.esc, keyboard.Key.enter, keyboard.KeyCode.from_char("q")]:
        running["value"] = False
        return False
    elif key == keyboard.KeyCode.from_char("t"):
        remaining_time = (end_time - time.time()) / 3600  # Convert to hours
        print(f"Time remaining: {remaining_time:.2f} hours")



def main(sleep_time, circle_radius, circle_step_degrees, duration_hours):
    t = 0
    running = {"value": True}
    start_time = time.time()
    end_time = start_time + (duration_hours * 3600)  # Convert hours to seconds

    print("Circular mouse movement started.")
    print(f"Program will run for {duration_hours} hours.")
    print("Press 'q', 'Enter', or 'Esc' to stop the program early.")
    print("Press 't' to check the remaining time.")

    with keyboard.Listener(on_press=lambda key: on_press(key, running, end_time)) as listener:
        try:
            mouse = Controller()

            while running["value"] and time.time() < end_time:
                circular_motion(
                    mouse=mouse,
                    t=t,
                    radius=circle_radius,
                    step_degrees=circle_step_degrees,
                )
                t += 1
                time.sleep(sleep_time)

                # Optional: Print remaining time every 10 minutes
                elapsed_time = time.time() - start_time
                if elapsed_time % 600 < sleep_time:  # Check if 10 minutes have passed
                    remaining_time = (end_time - time.time()) / 3600  # Convert to hours
                    print(f"Approximately {remaining_time:.2f} hours remaining.")

        except Exception as e:
            print(f"An error occurred: {e}")
        finally:
            if time.time() >= end_time:
                print("Program completed its scheduled duration.")
            print("Mouse movement stopped.")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Move the mouse in a circular pattern."
    )
    parser.add_argument(
        "--sleep",
        type=float,
        default=1,
        help="Sleep time between movements (default: 1s)",
    )
    parser.add_argument(
        "--radius", type=int, default=2, help="Radius of the circle (default: 2)"
    )
    parser.add_argument(
        "--step",
        type=int,
        default=5,
        help="Step in degrees for each movement (default: 5)",
    )
    parser.add_argument(
        "--duration",
        type=float,
        default=3.0,
        help="Maximum duration to run the program in hours (default: 3.0)",
    )
    args = parser.parse_args()

    main(args.sleep, args.radius, args.step, args.duration)
