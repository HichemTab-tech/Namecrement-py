import pytest

from namecrement import namecrement


# ---------------------------
# namecrement (default format)
# ---------------------------

def test_returns_proposed_name_if_unique():
    result = namecrement("file", ["file (1)", "file (2)"])
    assert result == "file"

def test_appends_paren_1_if_taken():
    result = namecrement("file", ["file"])
    assert result == "file (1)"

def test_finds_smallest_unused_suffix():
    result = namecrement("file", ["file", "file (1)", "file (2)"])
    assert result == "file (3)"

def test_handles_names_that_already_have_suffix():
    # NOTE: requires stripping an existing suffix from the proposed name
    result = namecrement("file (1)", ["file", "file (1)", "file (2)"])
    assert result == "file (3)"

def test_fills_in_gaps_between_suffixes():
    result = namecrement("file", ["file", "file (1)", "file (3)"])
    assert result == "file (2)"

def test_escapes_special_characters_in_base_name():
    result = namecrement("file.name", ["file.name", "file.name (1)"])
    assert result == "file.name (2)"


# -------------------------------
# namecrement (custom suffix fmt)
# -------------------------------

def test_supports_dash_format():
    result = namecrement("file", ["file", "file -1-", "file -2-"], " -%N%-")
    assert result == "file -3-"

def test_supports_simple_numeric_suffix():
    result = namecrement("log", ["log", "log1"], "%N%")
    assert result == "log2"

def test_uses_custom_suffix_even_if_proposed_has_similar_suffix():
    # NOTE: requires stripping existing suffix from the proposed name
    result = namecrement("item 1", ["item", "item 1", "item 2"], " %N%")
    assert result == "item 3"

def test_returns_base_if_not_in_existing_even_with_custom_format():
    result = namecrement("report", ["report -1-"], " -%N%-")
    assert result == "report"

def test_handles_special_chars_with_custom_format():
    result = namecrement("file.name", ["file.name", "file.name_1_"], "_%N%_")
    assert result == "file.name_2_"


# -------------------------------------
# namecrement with starting_number opt
# -------------------------------------

def test_starts_from_starting_number_if_base_available():
    result = namecrement("file", [], " (%N%)", 2)
    assert result == "file (2)"

def test_starts_from_starting_number_even_if_base_taken():
    result = namecrement("file", ["file"], " (%N%)", 2)
    assert result == "file (2)"

def test_finds_next_available_from_starting_number():
    result = namecrement("file", ["file", "file (2)"], " (%N%)", 2)
    assert result == "file (3)"

def test_handles_starting_number_zero_when_free():
    result = namecrement("file", [], " (%N%)", 0)
    assert result == "file (0)"

def test_handles_starting_number_zero_when_taken():
    result = namecrement("file", ["file (0)"], " (%N%)", 0)
    assert result == "file (1)"

def test_ignores_starting_number_when_not_passed_and_base_unique():
    result = namecrement("file", ["file (1)"])
    assert result == "file"

def test_uses_starting_number_when_passed_even_if_base_unique():
    result = namecrement("file", ["file (1)"], " (%N%)", 5)
    assert result == "file (5)"

def test_handles_case_where_starting_number_is_occupied():
    result = namecrement("file", ["file (5)"], " (%N%)", 5)
    assert result == "file (6)"


# -------------------------
# Suffix format validation
# -------------------------

def test_allows_valid_suffix_formats_with_placeholder():
    result = namecrement("file", [], " -%N%-")
    assert result == "file"

def test_throws_if_suffix_format_missing_placeholder():
    with pytest.raises(ValueError) as e:
        namecrement("file", [], " -X-")
    assert str(e.value) == "suffix_format must contain \"%N%\""


# -----------------------------
# Edge cases & stress tests
# -----------------------------

def test_handles_multi_digit_suffixes():
    result = namecrement("file", ["file", "file (1)", "file (10)"])
    assert result == "file (2)"

def test_ignores_names_that_dont_match_suffix_pattern():
    result = namecrement("file", ["file [1]", "file_1", "file (x)"])
    assert result == "file"

def test_treats_numeric_looking_names_correctly_if_not_matching_format():
    result = namecrement("file1", ["file1", "file1 (1)"])
    assert result == "file1 (2)"

def test_handles_special_characters_in_base():
    result = namecrement("file[1].$^", ["file[1].$^", "file[1].$^ (1)"])
    assert result == "file[1].$^ (2)"

def test_does_not_falsely_match_suffix_in_middle():
    result = namecrement("file (1) backup", ["file (1) backup", "file (1) backup (1)"])
    assert result == "file (1) backup (2)"

def test_treats_suffix_like_middle_as_distinct_base():
    result = namecrement("archive (1) final", ["archive (1) final", "archive (1) final (1)"])
    assert result == "archive (1) final (2)"

def test_fills_large_gaps_correctly():
    result = namecrement("file", ["file", "file (1)", "file (99)", "file (100)"])
    assert result == "file (2)"

def test_handles_deeply_nested_suffix_correctly():
    # NOTE: requires stripping: "file (99)" -> base "file"
    result = namecrement("file (99)", ["file", "file (1)", "file (99)"])
    assert result == "file (2)"

def test_handles_complex_custom_format_with_angle_brackets():
    result = namecrement("version", ["version", "version<v1>", "version<v2>"], "<v%N%>")
    assert result == "version<v3>"

def test_handles_numeric_only_base_names():
    result = namecrement("2023", ["2023", "2023 (1)", "2023 (2)"])
    assert result == "2023 (3)"
