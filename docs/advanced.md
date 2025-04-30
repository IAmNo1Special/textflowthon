# Advanced Usage

Here are advanced patterns and power user tips for TextFlow.

---

## Project Structure

TextFlow is organized for maintainability and extensibility. All animation effects are implemented as separate modules in the `textflow/effects/` directory:

```
textflow/
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
├── sync_ex.py
├── async_ex.py
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
├── test_glitch.py
├── test_matrix_rain.py
├── ...
pyproject.toml
```

To add a new effect, create a new file in `effects/` and register it in `core.py`.

---

## Real-Time Agents or Chatbots
Use the async API to animate output in bots or assistants without blocking:
```python
import asyncio
from textflow import TextFlow

async def agent():
    tc = TextFlow(fg="green", delay=0.02)
    await tc.async_typewrite("AI: How can I help you today?")

asyncio.run(agent())
```

## Multiple Animations Concurrently
Run several typewriter effects in parallel:
```python
import asyncio
from textflow import TextFlow

tc1 = TextFlow(fg="yellow", cursor="|")
tc2 = TextFlow(fg="magenta", cursor="█")

async def animate1():
    await tc1.async_typewrite("Bot 1: Hello!")

async def animate2():
    await tc2.async_typewrite("Bot 2: Hi there!")

async def main():
    await asyncio.gather(animate1(), animate2())

asyncio.run(main())
```

## Output to Files or Custom Streams
```python
from textflow import TextFlow

with open("output.txt", "w", encoding="utf-8") as f:
    tc = TextFlow(fg="cyan")
    tc.typewrite("This will be written to a file with animation frames.", file=f)
```

## Dynamic Style Changes
```python
tc = TextFlow()
tc.fg = "red"
tc.delay = 0.01
tc.cursor = "_"
tc.typewrite("Now in red and faster!")
```

## Custom Fonts (ASCII/FIGlet)

TextFlow supports custom ASCII/FIGlet fonts via the `pyfiglet` library. This allows you to animate text in a variety of fun styles directly in your terminal.

### Usage

Pass the `font` argument to `TextFlow`:

```python
from textflow import TextFlow

tc = TextFlow(font="slant")
tc.typewrite("Hello, world!")
```

- You can use any built-in pyfiglet font name (see [pyfiglet font list](https://github.com/pwaller/pyfiglet/blob/master/pyfiglet/fonts.py)).
- To use a custom `.flf` (FIGlet font) file, place it in a directory and specify its path:

```python
tc = TextFlow(font="path/to/customfont.flf")
tc.typewrite("Custom font!")
```

If the font cannot be loaded, TextFlow will fall back to normal text and print an error message.

**Note:** Only ASCII/FIGlet fonts are supported. Vector fonts like `.otf` or `.ttf` are not supported for terminal rendering.

### Where to Find FIGlet Fonts
- [FIGlet Font Archive](http://www.figlet.org/fontdb.cgi)
- [pyfiglet GitHub](https://github.com/pwaller/pyfiglet/tree/master/pyfiglet/fonts)
- Or create your own with [FIGlet font editors](http://www.jave.de/figlet/fonts.html)

## Random Reveal Effect

TextFlow supports a random reveal animation, where characters are revealed in random order. This effect is available in both synchronous and asynchronous forms, and you can specify the mask character for unrevealed positions.

### Synchronous Example
```python
from textflow import TextFlow

tc = TextFlow(fg="yellow", bg="black", delay=0.05, cursor="_")
tc.random_reveal("Random Reveal Example!", mask="*")
```

### Asynchronous Example
```python
import asyncio
from textflow import TextFlow

tc = TextFlow(fg="bright_cyan", bg="black", delay=0.04, cursor="*")
asyncio.run(tc.async_random_reveal("Async Random Reveal!", mask="*"))
```

- The `mask` argument can be any single character (default: `_`).
- Colors and cursor styles are fully supported.

## Reverse Typewriter Effect

TextFlow supports a reverse typewriter animation, where text appears one character at a time from right to left. This effect is available in both synchronous and asynchronous forms.

### Synchronous Example
```python
from textflow import TextFlow

tc = TextFlow(fg="orange1", bg="black", delay=0.04, cursor="<")
tc.reverse_typewrite("Reverse Typewriter Animation!")
```

### Asynchronous Example
```python
import asyncio
from textflow import TextFlow

tc = TextFlow(fg="deep_sky_blue1", bg="black", delay=0.03, cursor="<")
asyncio.run(tc.async_reverse_typewrite("Async Reverse Typewriter!"))
```

- Both methods use the same styling and cursor options as other TextFlow effects.

## Glitch Effect

TextFlow supports a glitch animation, where text appears with a glitchy effect. This effect is available in both synchronous and asynchronous forms.

### Synchronous Example
```python
from textflow import TextFlow

tc = TextFlow(fg="red", bg="black", delay=0.05, cursor="_")
tc.glitch("Glitch Effect Example!")
```

### Asynchronous Example
```python
import asyncio
from textflow import TextFlow

tc = TextFlow(fg="bright_cyan", bg="black", delay=0.04, cursor="*")
asyncio.run(tc.async_glitch("Async Glitch Effect!"))
```

- Colors and cursor styles are fully supported.

## Matrix-Style Rain Effect

TextFlow supports a Matrix-style rain animation, where characters fall down the screen in columns, similar to the Matrix movie. This effect is available in both synchronous and asynchronous forms. You can reveal a message in bright neon green (msg_fg="#39FF14") for maximum visibility.

### Synchronous Example
```python
from textflow import TextFlow

tc = TextFlow()
tc.matrix_rain(text="NEON GREEN!", width=60, height=18, delay=0.04, duration=3.0, msg_fg="#39FF14")
```

### Asynchronous Example
```python
import asyncio
from textflow import TextFlow

tc = TextFlow()
asyncio.run(tc.async_matrix_rain(text="NEON GREEN!", width=60, height=18, delay=0.04, duration=3.0, msg_fg="#39FF14"))
```

## Animation Best Practices

- All effects that animate in-place (e.g., typewrite, glitch, reverse, random reveal) use only carriage return (\r), space padding, and flush=True for maximum terminal compatibility. This avoids issues with ANSI escapes on Windows.

## Integration with Rich Ecosystem
TextFlow is compatible with the [rich](https://github.com/Textualize/rich) library. You can combine it with progress bars, tables, and more for interactive UIs.

---

For more, see the [usage guide](usage_guide.md), [integration](integration.md), or [contributing](contributing.md) pages.
