from parser import parse_stl_mvp


def test_empty_input():
    result = parse_stl_mvp("")

    assert result["instructions"] == []
    assert result["warnings"] == []


def test_duplicate_label():
    code = """
LOOP : NOP 0
LOOP : NOP 0
"""

    result = parse_stl_mvp(code)

    warning_types = {w["type"] for w in result["warnings"]}

    assert "duplicate_label" in warning_types


def test_unresolved_jump():
    code = """
JC UNKNOWN_LABEL
"""

    result = parse_stl_mvp(code)

    warning_types = {w["type"] for w in result["warnings"]}

    assert "unresolved_jump_target" in warning_types