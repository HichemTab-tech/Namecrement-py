# 👥 Contributing to namecrement-py

Thanks for your interest! Contributions make the project better for everyone. 🎉

---

## 🚨 Before You Start

* Check **[existing issues](https://github.com/HichemTab-tech/namecrement-py/issues)** first.
* If it’s not there, **[open a new issue](https://github.com/HichemTab-tech/namecrement-py/issues/new)** with a clear description and examples.

---

## 📄 Code of Conduct

Be respectful, professional, and constructive. Harassment or inappropriate behavior is not tolerated.

---

## ⚙️ Dev Setup

> Requires Python **3.8+**.

### 1) Fork & clone

```sh
git clone https://github.com/YOUR_GITHUB_USERNAME/namecrement-py
cd namecrement-py
```

### 2) Create a virtual env

Using **uv** (recommended):

```sh
uv venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate
```

Or with standard venv:

```sh
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate
```

### 3) Install the package (editable) + dev tools

With **uv**:

```sh
uv pip install -e .
uv pip install pytest ruff black
```

With **pip**:

```sh
pip install -e .
pip install pytest ruff black
```

---

## 🔨 Making Changes

1. Create a feature/bugfix branch from `main`:

   ```sh
   git checkout -b feat/cool-new-thing
   # or
   git checkout -b fix/edge-case-parsing
   ```

2. Write tests (keep them small and clear) in `tests/`.

3. Run checks locally:

   ```sh
   # format & lint
   ruff check .
   black .            # or: ruff format .

   # run tests
   pytest -q
   ```

4. Commit with a clear message (see “Commit Message Guidelines” below) and push:

   ```sh
   git add .
   git commit -m "feat: support custom suffix delimiter via option"
   git push origin feat/cool-new-thing
   ```

---

## 🧪 What to Test

* Happy path: base name taken → next number is returned.
* Keep base when free (no increment).
* Custom `suffix_format` with `%N%` placeholder.
* `starting_number` behavior.
* Ignore other formats when collecting taken numbers (only same format matters).

---

## 📝 Submitting a Pull Request

1. Open a PR from your branch to `main`.
2. In the description, include:

   * **What** changed and **why**.
   * Any **breaking changes**.
   * Linked issues (e.g., **Closes #12**).
3. CI must pass (lint + tests). Maintainers may request changes before merge.

---

## 📌 Commit Message Guidelines

Use **Conventional Commits** to keep history readable and automate changelogs:

```
<type>(optional scope): <short summary>

[optional body]

[optional footer(s)]
```

**Types**:

* `feat`: a new feature
* `fix`: a bug fix
* `docs`: documentation only changes
* `test`: add/adjust tests
* `refactor`: code change that neither fixes a bug nor adds a feature
* `chore`: maintenance, build, or tooling changes
* `ci`: CI/CD workflow changes

**Examples**:

* `feat: add starting_number to override initial increment`
* `fix: handle names ending with space before suffix`
* `docs: clarify suffix_format must include %N%`
* `test: cover gap-filling with mixed formats`
* `chore: bump ruff and black`

---

## 🚢 Releases (maintainers)

* Bump version in `pyproject.toml`.
* Tag and push (e.g., `v0.1.0`). GitHub Actions will build & publish to PyPI via Trusted Publishing.

---

## 🙏 Thanks

Whether it’s a typo fix or a new feature, thanks for helping improve **namecrement-py**!
