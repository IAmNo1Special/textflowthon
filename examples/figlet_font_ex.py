"""
Example: Using a FIGlet/ASCII font with TextFlow

This script demonstrates how to animate text in the terminal using a custom FIGlet font.
Requires: pyfiglet
"""
from textflow import TextFlow

def main():
    tc = TextFlow(font="standard", fg="pink3", bg="purple", delay=0.01)
    tc.typewrite("This is a textflow effect test for figlet fonts (sync)")

if __name__ == "__main__":
    main()
