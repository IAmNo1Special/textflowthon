"""
Example: Glitch Effect (Sync)

This script demonstrates the glitch animation, where characters rapidly flicker through random symbols before settling on the correct letter.
"""
from textflow import TextFlow

def main():
    tc = TextFlow()
    tc.glitch("This is a textflow effect test for glitch (sync)", steps=12, delay=0.04)

if __name__ == "__main__":
    main()
