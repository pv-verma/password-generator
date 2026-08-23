import string

from password_generator import (
    build_character_pool,
    calculate_score,
    check_criteria,
    generate_password,
    score_to_label,
)


def test_build_character_pool():
    # lowercase only
    pool = build_character_pool(False, False, False)
    assert pool == string.ascii_lowercase

    # everything included
    pool = build_character_pool(True, True, True)
    assert string.ascii_lowercase in pool
    assert string.ascii_uppercase in pool
    assert string.digits in pool
    assert "!@#$%" in pool


def test_generate_password():
    pool = "abc123"
    password = generate_password(10, pool)

    assert len(password) == 10
    assert all(char in pool for char in password)


def test_check_criteria():
    weak = check_criteria("abc")
    assert weak["length_ok"] is False
    assert weak["has_upper"] is False
    assert weak["has_digit"] is False

    strong = check_criteria("Abcdef1!")
    assert strong["length_ok"] is True
    assert strong["has_upper"] is True
    assert strong["has_lower"] is True
    assert strong["has_digit"] is True
    assert strong["has_symbol"] is True


def test_calculate_score():
    all_true = {"a": True, "b": True, "c": True, "d": True, "e": True}
    assert calculate_score(all_true) == 5

    none_true = {"a": False, "b": False, "c": False, "d": False, "e": False}
    assert calculate_score(none_true) == 0

    mixed = {"a": True, "b": False, "c": True, "d": False, "e": True}
    assert calculate_score(mixed) == 3


def test_score_to_label():
    assert score_to_label(0) == "Weak"
    assert score_to_label(2) == "Weak"
    assert score_to_label(3) == "Medium"
    assert score_to_label(4) == "Strong"
    assert score_to_label(5) == "Very Strong"