"""
Example: Reverse Typewriter Effect (Sync)

This script demonstrates the right-to-left typewriter animation in TextFlow.
"""
from textflow import TextFlow

def main():
    tc = TextFlow(fg="orange1", bg="black", delay=0.04, cursor="<")
    tc.reverse_typewrite("This is a textflow effect test for reverse typewriter (sync)")

if __name__ == "__main__":
    main()
