import re
from typing import Iterable, Optional

def namecrement(
    proposed_name: str,
    existing_names: Iterable[str],
    suffix_format: str = " (%N%)",
    starting_number: Optional[int] = None,
) -> str:
    """
    Python port of the JS namecrement:
    - Keeps base if it's free and no starting_number is provided.
    - Otherwise appends the smallest positive integer using suffix_format.
    - If proposed_name already ends with the same-format suffix, strip it first.
    """
    if "%N%" not in suffix_format:
        raise ValueError('suffix_format must contain "%N%"')

    escape = re.escape

    # Build a "(\\d+)"-style regex from the provided format
    format_regex = escape(suffix_format).replace("%N%", r"(\d+)")

    # If proposed already ends with that suffix, drop it → base
    # JS: /(.*)<format>$/
    suffix_re = re.compile(rf"(.*){format_regex}$")
    m = suffix_re.search(proposed_name)
    base = m.group(1) if m else proposed_name

    # Match either: ^base<format>$  OR  ^base$
    matcher = re.compile(rf"^(?:{escape(base)}{format_regex}|{escape(base)})$")

    # Collect used numbers; 0 means the bare base is taken
    used: set[int] = set()
    for name in existing_names:
        m2 = matcher.match(name)
        if m2:
            used.add(int(m2.group(1)) if m2.group(1) else 0)

    # If the base itself is free and no explicit starting number → return base
    if 0 not in used and starting_number is None:
        return base

    # Else find the smallest available starting from starting_number or 1
    counter = 1 if starting_number is None else starting_number
    while counter in used:
        counter += 1

    return f"{base}{suffix_format.replace('%N%', str(counter))}"