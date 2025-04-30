# Installing TextFlow: PyPI vs. Source

TextFlow can be installed in two main ways, depending on your needs:

---

## 1. For Most Users (PyPI)

If you just want to use TextFlow in your own project, install it from PyPI:

- With `uv`:
  ```sh
  uv add textflow
  ```
- With `pip`:
  ```sh
  pip install textflow
  ```

This gives you the latest released version and is the fastest way to get started.

---

## 2. For Contributors/Developers (Source/Editable)

If you want to:
- Run the example scripts in the repo
- Contribute to TextFlow
- Test or develop the library locally

Clone the GitHub repo and install in editable mode:

- With `uv`:
  ```sh
  uv pip install -e . rich
  ```
- With `pip`:
  ```sh
  pip install -e . rich
  ```

This lets you edit the code and see changes immediately, and makes all example scripts runnable.

---

## Why Aren't Example Scripts Included in PyPI Installs?

PyPI packages only include the library code, not the example scripts or full documentation. To access the examples, clone the [GitHub repository](https://github.com/yourusername/textflow).

---

## More Info
- [Quickstart](index.md#quickstart)
- [Usage Guide](usage_guide.md)
- [Contributing](contributing.md)
