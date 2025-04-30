# Usage Guide

This guide covers practical usage patterns for TextFlowThon, from basic to advanced.

---

## Basic Synchronous Usage
```python
from textflowthon import TextFlowThon

tc = TextFlowThon()
tc.typewrite("Hello, TextFlowThon!")
```

## Basic Asynchronous Usage
```python
import asyncio
from textflowthon import TextFlowThon

tc = TextFlowThon()
asyncio.run(tc.async_typewrite("Hello from async!"))
```

## Customizing Output
```python
tc = TextFlowThon(width=40, delay=0.02, fg="green", bg="black", cursor="█")
tc.typewrite("Custom style!")
```

## Output to a File
```python
with open("output.txt", "w", encoding="utf-8") as f:
    tc = TextFlowThon()
    tc.typewrite("Writing to a file!", file=f)
```

## Frame-by-Frame Animation
```python
tc = TextFlowThon()
for frame in tc.frames("Frame by frame!"):
    print(frame)
    # Add your own timing or effects
```

## Typewriter Effect (Sync)
```python
from textflowthon import TextFlowThon

tc = TextFlowThon(fg="yellow", cursor="_")
tc.typewrite("Typewriter!")
```

## Typewriter Effect (Async)
```python
import asyncio
from textflowthon import TextFlowThon

tc = TextFlowThon(fg="yellow", cursor="_")
asyncio.run(tc.async_typewrite("Async Typewriter!"))
```

## Reverse Typewriter
```python
from textflowthon import TextFlowThon

tc = TextFlowThon()
tc.reverse_typewrite("Backwards!")
```

## Random Reveal
```python
from textflowthon import TextFlowThon

tc = TextFlowThon()
tc.random_reveal("Surprise!", mask="*")
```

## Glitch Effect
```python
from textflowthon import TextFlowThon

tc = TextFlowThon()
tc.glitch("Glitchy text!", steps=10, delay=0.02)
```

## Glitch Effect (Sync)
```python
from textflowthon import TextFlowThon

tc = TextFlowThon()
tc.glitch("Glitch Effect Example!", steps=12, delay=0.04)
```

## Glitch Effect (Async)
```python
import asyncio
from textflowthon import TextFlowThon

tc = TextFlowThon()
asyncio.run(tc.async_glitch("Async Glitch Effect!", steps=12, delay=0.04))
```

## Matrix-Style Rain (Sync)
```python
from textflowthon import TextFlowThon

tc = TextFlowThon()
tc.matrix_rain(text="NEON GREEN!", width=60, height=18, delay=0.04, duration=3.0, fg="green4", msg_fg="green1")
```

## Matrix-Style Rain (Async)
```python
import asyncio
from textflowthon import TextFlowThon

tc = TextFlowThon()
asyncio.run(tc.async_matrix_rain(text="NEON GREEN!", width=60, height=18, delay=0.04, duration=3.0, fg="green4", msg_fg="green1"))
```

## Novice Type (Sync)
```python
from textflowthon import TextFlowThon

tc = TextFlowThon(fg="yellow", cursor="_")
tc.novice_type("This is a demo of the novice type effect!", error_rate=0.2, max_mistakes=3, correction_delay=0.4, backspace_delay=0.04)
```

## Novice Type (Async)
```python
import asyncio
from textflowthon import TextFlowThon

tc = TextFlowThon(fg="yellow", cursor="_")
asyncio.run(tc.async_novice_type("Async novice typewriter demo!", error_rate=0.2, max_mistakes=3, correction_delay=0.4, backspace_delay=0.04))
```

## Corrupt Effect (Sync)
```python
from textflowthon import TextFlowThon

tc = TextFlowThon(fg="magenta", cursor="_")
tc.corrupt("CORRUPTION IN PROGRESS!", cycles=5, corrupt_sections=4, corrupt_duration=0.18, symbols="@#$%&*?!")
```

## Corrupt Effect (Async)
```python
import asyncio
from textflowthon import TextFlowThon

tc = TextFlowThon(fg="magenta", cursor="_")
asyncio.run(tc.async_corrupt("ASYNC CORRUPTION IN PROGRESS!", cycles=5, corrupt_sections=4, corrupt_duration=0.18, symbols="@#$%&*?!"))
```

## Marquee Effect (Sync & Async)

TextFlowThon's marquee effect provides smooth, in-place scrolling text for the terminal, using Rich Live for maximum compatibility and visual quality. Both synchronous and asynchronous APIs are available, with identical parameters and behavior.

### Parameters
- `text`: The message to scroll
- `file`: Output stream (default: sys.stdout)
- `width`: Width of the visible window
- `delay`: Delay between frames (seconds)
- `padding`: Spaces or characters to pad before/after message
- `loop`: Number of bounce cycles before stopping
- `fg`: Foreground color (Rich color name or hex)
- `bounce`: Enable bidirectional scrolling
- `pad_char`: Character used for padding

### Behavior
- The marquee bounces for `loop` cycles and only stops when the message is perfectly centered in the window.
- No ANSI codes are used; all output is handled by Rich (including color and in-place updates).
- The effect is visually seamless, with no snap or jump at the end.

### Example (Sync)
```python
from textflowthon import TextFlowThon
import sys

tc = TextFlowThon()
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
```

### Example (Async)
```python
import sys
import asyncio
from textflowthon import TextFlowThon

tc = TextFlowThon()

async def main():
    await tc.async_marquee(
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
    asyncio.run(main())
```

### Notes
- For best results, use a modern terminal emulator with full color support.
- See the `examples/` directory for more demos.

---

## Boot Sequence Effect (Sync & Async)

Simulate a retro terminal boot sequence, including BIOS/firmware lines, memory checks, device detection, and a final highlighted message. Both synchronous and asynchronous APIs are available, with identical parameters and behavior.

### Parameters
- `message`: The final message to display, centered and highlighted
- `file`: Output stream (default: sys.stdout)
- `delay`: Delay between BIOS/firmware lines (seconds)
- `bios_lines`: Optional custom list of BIOS/firmware lines
- `highlight_color`: Color for the final message
- `bios_color`: Color for BIOS/firmware lines
- `mem_color`: Color for memory check lines
- `error_color`: Color for error messages
- `boot_ok`: Whether to show a successful or error boot status

### Example (Sync)
```python
from textflowthon import TextFlowThon
import sys

tc = TextFlowThon()
tc.boot_sequence(
    message="WELCOME TO TYPECAST OS!",
    file=sys.stdout,
    delay=0.08,
    highlight_color="bright_green",
    bios_color="bright_white",
    mem_color="cyan",
    error_color="bright_red",
    boot_ok=True
)
```

### Example (Async)
```python
import sys
import asyncio
from textflowthon import TextFlowThon

tc = TextFlowThon()

async def main():
    await tc.async_boot_sequence(
        message="ASYNC BOOT: WELCOME TO TYPECAST OS!",
        file=sys.stdout,
        delay=0.08,
        highlight_color="bright_green",
        bios_color="bright_white",
        mem_color="cyan",
        error_color="bright_red",
        boot_ok=True
    )

if __name__ == "__main__":
    asyncio.run(main())
```

### Behavior
- Animates a full boot sequence, then centers and highlights your message.
- Both sync and async APIs are available with identical parameters and behavior.
- All output is handled by Rich for color and styling.

See `examples/boot_sequence_ex.py` and `examples/async_boot_sequence_ex.py` for full demos.

---

## Matrix Rain

The Matrix Rain effect supports:
- Multi-line message reveal, with vertical and horizontal centering
- Cycling reveal/hide per character as rain falls
- The timer starts after every character is revealed twice
- The final output always fully reveals the message
- The rain color can be customized via the `fg` parameter, and the message color via `msg_fg`. Both accept any Rich color name or hex code. The rain trail uses bold, normal, dimmed, and Matrix-green fades. For example, to make the rain blue and the message yellow, use `fg="blue", msg_fg="yellow"`.

For more advanced patterns, see the [integration](integration.md) and [advanced](advanced.md) guides.

---

### Advanced Usage
- All effects support output to any file-like stream (e.g., open files, StringIO, etc.).
- You can use custom ASCII/FIGlet fonts for typewrite effects via the `font` parameter.
- All effects support both sync and async (asyncio) usage.
- For error handling, invalid color or font names will fall back to defaults and may log a warning.

See the [API documentation](index.md) for more details.

---

## Project Structure

TextFlowThon is modular. All animation effects are implemented as separate modules in the `textflowthon/effects/` directory:

```
textflowthon/
├── __init__.py
├── core.py
├── fonts.py
├── utils.py
├── effects/
│   ├── __init__.py
│   ├── typewrite.py
│   ├── async_typewrite.py
│   ├── reverse_typewrite.py
│   ├── async_reverse_typewrite.py
│   ├── random_reveal.py
│   ├── async_random_reveal.py
│   ├── glitch.py
│   ├── async_glitch.py
│   ├── matrix_rain.py
│   ├── async_matrix_rain.py
├── ...
examples/
├── sync_typewrite_ex.py
├── async_typewrite_ex.py
├── figlet_font_ex.py
├── async_figlet_font_ex.py
├── random_reveal_ex.py
├── async_random_reveal_ex.py
├── reverse_typewrite_ex.py
├── async_reverse_typewrite_ex.py
├── glitch_ex.py
├── async_glitch_ex.py
├── matrix_rain_ex.py
├── async_matrix_rain_ex.py
├── list_effects.py
├── showoff_all_examples.py
├── ...
docs/
├── README.md
├── advanced.md
├── index.md
├── usage_guide.md
├── contributing.md
├── ...
tests/
├── test_core.py
├── test_figlet_font.py
├── test_random_reveal.py
├── test_reverse_typewrite.py
├── test_errors.py
├── ...
pyproject.toml
