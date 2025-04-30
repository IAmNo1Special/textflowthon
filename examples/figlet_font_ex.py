"""
Example: Using a FIGlet/ASCII font with TextFlowThon

This script demonstrates how to animate text in the terminal using a custom FIGlet font.
Requires: pyfiglet
"""
from textflowthon import TextFlowThon

def main():
    tc = TextFlowThon(font="standard", fg="pink3", bg="purple", delay=0.01)
    tc.typewrite("This is a textflowthon effect test for figlet fonts (sync)")

if __name__ == "__main__":
    main()
