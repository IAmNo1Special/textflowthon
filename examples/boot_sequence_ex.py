import sys
from textflowthon.effects.boot_sequence import boot_sequence

if __name__ == "__main__":
    boot_sequence(
        message="WELCOME TO TYPECAST OS!",
        file=sys.stdout,
        delay=0.08,
        highlight_color="bright_green",
        bios_color="bright_white",
        mem_color="cyan",
        error_color="bright_red",
        boot_ok=True
    )
