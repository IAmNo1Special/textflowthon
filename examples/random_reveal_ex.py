"""
Example: Random Reveal Effect with TextFlow

This script demonstrates the random reveal animation, where characters are revealed in random order.
"""
from textflow import TextFlow

def main():
    tc = TextFlow(fg="yellow", bg="black", delay=0.05, cursor="_")
    tc.random_reveal("This is a textflow effect test for random reveal (sync)", mask="*")

if __name__ == "__main__":
    main()
