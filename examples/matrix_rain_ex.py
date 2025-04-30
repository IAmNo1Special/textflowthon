from textflow import TextFlow
import sys

if __name__ == "__main__":
    tc = TextFlow()
    multi_line_message = "TYPECAST\nMATRIX\nRAIN!"
    tc.matrix_rain(
        text=multi_line_message,
        width=28,
        height=14,
        delay=0.08,
        duration=3.0,
        fg="green4",
        msg_fg="green1",
        file=sys.stdout
    )
