"""
Example: Synchronous TextFlow Usage
-----------------------------------
This script demonstrates how to use TextFlow's synchronous typewriter animation.

It is the default and simplest way to use TextFlow.
"""
from textflow import TextFlow

def main():
    tc = TextFlow(width=50, delay=0.04, fg="cyan", cursor="▌")
    tc.typewrite(
        "This is a synchronous typewriter animation (sync).\n"
        "You can use it in any script without worrying about async.\n"
        "---\n"
        "Try changing the width, delay, colors, or cursor!"
    )

if __name__ == "__main__":
    main()
