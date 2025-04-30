from textflowthon import TextFlowThon
import sys

def main():
    tc = TextFlowThon(fg="cyan")
    tc.marquee(
        "TYPECAST MARQUEE EFFECT!",
        file=sys.stdout,
        width=40,
        delay=0.07,
        padding=40,
        loop=2,
        fg="red",
        bounce=True,
        pad_char="-"
    )

if __name__ == "__main__":
    main()
