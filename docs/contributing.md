# Contributing to TextFlow

Thank you for your interest in contributing!

## How to Contribute
- **Bug reports:** Open an issue describing the bug and how to reproduce it.
- **Feature requests:** Open an issue describing your idea and its use case.
- **Pull requests:** Fork the repo, make your changes, and submit a PR. Please ensure your code is tested and follows project style.

## Development Setup
1. Clone the repository:
   ```sh
   git clone https://github.com/yourusername/textflow.git
   cd textflow
   ```
2. Create a virtual environment (or use `uv venv`):
   ```sh
   uv venv
   uv pip install -e .
   uv pip install pytest pytest-asyncio
   ```
3. Run tests:
   ```sh
   uv run -m pytest
   ```

## Code Style
- Follow PEP8 conventions.
- Add docstrings for public methods/classes.
- Write and update tests for all features.
- For in-place terminal animations, use only carriage return (\r), space padding, and flush=True. Do not use ANSI escape codes for clearing lines unless you ensure cross-platform support (e.g., via colorama).

## Documentation
- Update or add doc pages for new features.
- Keep examples in sync with the codebase.

## Project Structure

TextFlow is modular. All animation effects are implemented as separate modules in the `textflow/effects/` directory:

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
│   ├── ...
├── examples/
│   ├── sync_ex.py
│   ├── async_ex.py
│   ├── figlet_font_ex.py
│   ├── async_figlet_font_ex.py
│   ├── random_reveal_ex.py
│   ├── async_random_reveal_ex.py
│   ├── reverse_typewrite_ex.py
│   ├── async_reverse_typewrite_ex.py
│   ├── modular_structure_ex.py
│   ├── ...
├── docs/
│   ├── README.md
│   ├── advanced.md
│   ├── index.md
│   ├── usage_guide.md
│   ├── contributing.md
│   ├── ...
├── tests/
│   ├── test_core.py
│   ├── test_figlet_font.py
│   ├── test_random_reveal.py
│   ├── test_reverse_typewrite.py
│   ├── test_errors.py
│   ├── ...
├── pyproject.toml
```

To add a new effect, create a new file in `effects/` and wire it up in `core.py`. All new effects should be added as a separate module in `textflow/effects/` and registered in `core.py`. Ensure new effects use in-place animation with carriage return (\r) and space padding for cross-platform compatibility. Update the README, docs, and add an example script for each new effect.

---

We welcome all contributions—big or small!

- [ ] Glitch effect (sync/async): Add new effect files, wire up in core, add tests and examples.
