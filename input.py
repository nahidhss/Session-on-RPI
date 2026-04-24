from gpiozero import Button
from signal import pause

def main():
    # GPIO17 as input with pull-up resistor
    button = Button(17, pull_up=True)

    def pressed():
        print("Button Pressed!")

    def released():
        print("Button Released!")

    button.when_pressed = pressed
    button.when_released = released

    print("Program running... Press Ctrl+C or Enter to exit")

    try:
        input("Press Enter to exit...\n")
    except KeyboardInterrupt:
        pass

if __name__ == "__main__":
    main()
