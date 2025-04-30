"""
Example: Synchronous TextFlowThon Usage
-----------------------------------
This script demonstrates how to use TextFlowThon's synchronous typewriter animation.

It is the default and simplest way to use TextFlowThon.
"""
from textflowthon import TextFlowThon

def main():
    tc = TextFlowThon(width=50, delay=0.04, fg="cyan", cursor="▌")
    tc.typewrite(
        "This is a synchronous typewriter animation (sync).\n"
        "You can use it in any script without worrying about async.\n"
        "---\n"
        "Try changing the width, delay, colors, or cursor!"
    )

if __name__ == "__main__":
    main()
