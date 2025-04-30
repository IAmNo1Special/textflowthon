from textflowthon import TextFlowThon
import sys

def main():
    tc = TextFlowThon(fg="yellow", cursor="_")
    tc.novice_type(
        "This is a demo of the novice type effect!",
        file=sys.stdout,
        error_rate=0.2,
        max_mistakes=3,
        correction_delay=0.4,
        backspace_delay=0.04
    )

if __name__ == "__main__":
    main()
