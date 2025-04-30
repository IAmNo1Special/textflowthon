# TextFlowThon Documentation

Welcome to the official documentation for **TextFlowThon** – a plug-and-play Python library for animating text output in your terminal with a typewriter effect.

---

## Overview
TextFlowThon provides a simple, flexible, and modern API for animating text in both synchronous and asynchronous Python programs. It is ideal for:
- Command-line tools
- AI agents and chatbots
- Demos and interactive scripts
- Any application that wants beautiful animated terminal output

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

To add a new effect, create a new file in `effects/` and wire it up in `core.py`.

---

## Installation

### Recommended: Using `uv`

[`uv`](https://github.com/astral-sh/uv) is a modern Python package and environment manager that is:
- **Extremely fast** (Rust-powered, up to 100x faster than pip)
- **All-in-one** (manages venvs, installs, and dependencies)
- **Reliable** (lockfiles, reproducible builds)
- **Drop-in replacement** for pip/venv

#### Install `uv`:
- With pip:
  ```sh
  pip install uv
  ```
- With Homebrew (macOS/Linux):
  ```sh
  brew install astral-sh/uv/uv
  ```
- Or download from [GitHub Releases](https://github.com/astral-sh/uv/releases)

#### Quickstart:
```sh
uv init # Initialize a new project
uv add textflowthon rich # Install dependencies
uv run your_script.py # Run your script
```

### Manual (pip/venv)

1. Create a virtual environment:
   ```sh
   python -m venv .venv
   ```
2. Activate it:
   - Windows:
     ```sh
     .venv\Scripts\activate
     ```
   - macOS/Linux:
     ```sh
     source .venv/bin/activate
     ```
3. Install dependencies:
   ```sh
   pip install textflowthon rich
   ```
4. Run your scripts as usual:
   ```sh
   python your_script.py
   ```

---

## Quickstart

### Synchronous Usage
```python
from textflowthon import TextFlowThon

tc = TextFlowThon(width=50, delay=0.04, fg="cyan", cursor="▌")
tc.typewrite("Hello, world!")
```

### Asynchronous Usage
```python
import asyncio
from textflowthon import TextFlowThon

tc = TextFlowThon(fg="magenta", delay=0.03)
asyncio.run(tc.async_typewrite("Async hello!"))
```

---

## API Reference

### TextFlowThon
- `TextFlowThon(width=79, delay=0.05, cursor='|', fg='red1', bg=None)`
  - `width`: Maximum line width before wrapping
  - `delay`: Delay between characters (seconds)
  - `cursor`: Cursor character to show during typing
  - `fg`: Foreground color (Rich-compatible)
  - `bg`: Background color (Rich-compatible)

#### Methods
- `typewrite(text, file=None)`
  - Synchronously animates the given text.
- `async_typewrite(text, file=None)`
  - Asynchronously animates the given text (use in async apps).
- `frames(text)`
  - Generator yielding each frame of the animation as a string (for custom rendering/testing).
- `glitch(text, file=None)`
  - Synchronously animates the given text with a glitch effect.
- `async_glitch(text, file=None)`
  - Asynchronously animates the given text with a glitch effect (use in async apps).
- `matrix_rain(text, file=None, msg_fg="#39FF14")`
  - Synchronously animates the given text with a Matrix-style rain effect. Use msg_fg to set neon green message color.
- `async_matrix_rain(text, file=None, msg_fg="#39FF14")`
  - Asynchronously animates the given text with a Matrix-style rain effect (use in async apps). Use msg_fg to set neon green message color.

---

## Usage Guide
See [usage_guide.md](usage_guide.md) for practical usage patterns, from basic to advanced.

## Integration Tips
See [integration.md](integration.md) for integrating TextFlowThon with other libraries and tools.

## Advanced Usage
See [advanced.md](advanced.md) for advanced patterns and power user tips.

## Contributing
See [contributing.md](contributing.md) if you want to help improve TextFlowThon!

---

## Troubleshooting
- Ensure you have the `rich` package installed.
- Use a modern terminal for best color support.
- If you see no animation or color, check your terminal settings.
- For async usage, make sure your event loop is running and not blocked by other code.

---

## Requirements
- Python 3.12+
- [rich](https://github.com/Textualize/rich)
- [uv](https://github.com/astral-sh/uv) (recommended)

---

## License
MIT
