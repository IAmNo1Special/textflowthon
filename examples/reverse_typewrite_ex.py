"""
Example: Reverse Typewriter Effect (Sync)

This script demonstrates the right-to-left typewriter animation in TextFlowThon.
"""
from textflowthon import TextFlowThon

def main():
    tc = TextFlowThon(fg="orange1", bg="black", delay=0.04, cursor="<")
    tc.reverse_typewrite("This is a textflowthon effect test for reverse typewriter (sync)")

if __name__ == "__main__":
    main()
