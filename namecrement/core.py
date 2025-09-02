import re
from typing import Iterable, Optional

def namecrement(
    base_name: str,
    existing_names: Iterable[str],
    suffix_format: str = " (%N%)",
    starting_number: Optional[int] = None,
) -> str:
    """
    Generate the next unique name by incrementing base_name using suffix_format.
    - If starting_number is None and base_name is unused => returns base_name.
    - Otherwise returns base_name with the first available %N%.
    """
    if "%N%" not in suffix_format:
        raise ValueError("suffix_format must include '%N%'")

    existing = set(existing_names)

    # If the user didn't force a start and base is free, keep it as-is
    if starting_number is None and base_name not in existing:
        return base_name

    # Build a regex that matches the chosen format for THIS base_name
    # Example: " (%N%)" -> r"^file \((\d+)\)$"
    fmt_regex = re.escape(suffix_format).replace(r"%N%", r"(\d+)")
    pattern = re.compile(rf"^{re.escape(base_name)}{fmt_regex}$")

    # Collect taken numbers that already match the SAME format
    taken = set()
    for name in existing:
        m = pattern.match(name)
        if m:
            taken.add(int(m.group(1)))

    n = starting_number if starting_number is not None else 1
    while n in taken or f"{base_name}{suffix_format.replace('%N%', str(n))}" in existing:
        n += 1

    return f"{base_name}{suffix_format.replace('%N%', str(n))}"