"""
Example: Random Reveal Effect with TextFlowThon

This script demonstrates the random reveal animation, where characters are revealed in random order.
"""
from textflowthon import TextFlowThon

def main():
    tc = TextFlowThon(fg="yellow", bg="black", delay=0.05, cursor="_")
    tc.random_reveal("This is a textflowthon effect test for random reveal (sync)", mask="*")

if __name__ == "__main__":
    main()
