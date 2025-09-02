# Namecrement (Python)

<p align="center">

![Tests](https://github.com/HichemTab-tech/Namecrement-py/workflows/Test/badge.svg)
[![License](https://img.shields.io/badge/license-MIT-green.svg)](https://github.com/HichemTab-tech/Namecrement-py/blob/main/LICENSE)
[![PyPI Version](https://img.shields.io/pypi/v/namecrement.svg)](https://pypi.org/project/namecrement/)

</p>

**Smart and simple unique name generator.**
If a name already exists, Namecrement automatically increments it,
like `"file"` → `"file (1)"`, `"file (2)"`, and so on.

---

## ✨ Features

* Automatically avoids naming collisions
* Smart incremental naming (`(1)`, `(2)`, etc.)
* Lightweight and dependency-free (single function)
* Works for filenames, labels, identifiers, and more

---

### 📦 Also Available

* JavaScript: [Namecrement](https://github.com/HichemTab-tech/Namecrement)
* PHP: [Namecrement-php](https://github.com/HichemTab-tech/Namecrement-php)

---

## 📦 Installation

```bash
pip install namecrement
```

or (with uv):

```bash
uv add namecrement
```

---

## 🚀 Usage

```python
from namecrement import namecrement

# Example list of existing names
existing = ["file", "file (1)", "file (2)"]

# Generate a unique name
new_name = namecrement("file", existing)

print(new_name)  # -> "file (3)"
```

---

## 🧠 Advanced Usage

```python
from namecrement import namecrement

namecrement("file", ["file", "file -1-", "file -2-"], " -%N%-")
# -> "file -3-"
```

You can customize how numbers are added by using the `%N%` placeholder in a `suffix_format`:

| Format Example | Output     |
| -------------- | ---------- |
| `" (%N%)"`     | `file (1)` |
| `"-%N%"`       | `file-1`   |
| `"_v%N%"`      | `file_v1`  |
| `"<%N%>"`      | `file<1>`  |

---

### ✅ Format Guard

`suffix_format` **must** include the `%N%` placeholder, otherwise the function raises a `ValueError`.
This ensures every generated name contains the incremented number in your format.

```python
namecrement("log", ["log", "log_1"], "_%N%_")
# -> "log_2"
```

---

## 📚 API

### `namecrement(base_name: str, existing_names: Iterable[str], suffix_format: str = " (%N%)", starting_number: int | None = None) -> str`

| Parameter         | Type            | Description                                               |
| ----------------- | --------------- | --------------------------------------------------------- |
| `base_name`       | `str`           | The proposed name                                         |
| `existing_names`  | `Iterable[str]` | The list of names to check against                        |
| `suffix_format`   | `str`           | The format for the incremented name (default: `" (%N%)"`) |
| `starting_number` | `int \| None`   | Optional starting number override (default: `None`)       |

Returns a **unique** name based on the proposed one.

* If `starting_number` is `None` and `base_name` is unused → returns `base_name`.
* Otherwise returns `base_name` with the first available `%N%`.

---

## 🛠️ Examples

```python
from namecrement import namecrement

namecrement("report", ["report", "report (1)"])
# -> "report (2)"

namecrement("image", ["photo", "image", "image (1)", "image (2)"])
# -> "image (3)"

namecrement("new", [])
# -> "new"

namecrement("document", ["document", "document -1-", "document (2)"], " -%N%-")
# -> "document -2-"

namecrement("file", [], " (%N%)", 5)
# -> "file (5)"
```

---

## 📄 License

MIT License © 2025 Hichem Taboukouyout
