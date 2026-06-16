from parser import parse_stl_mvp
from analysis.instruction_cfg import build_instruction_cfg


def test_instruction_cfg_jump():

    code = """
L MW10
JU END

T MW20

END:
= Q0.0
"""

    ir = parse_stl_mvp(code)

    cfg = build_instruction_cfg(ir)

    assert cfg == [
        {"from": 0, "to": 1, "kind": "fallthrough"},
        {"from": 1, "to": 3, "kind": "jump"},
        {"from": 2, "to": 3, "kind": "fallthrough"},
        {"from": 3, "to": 4, "kind": "fallthrough"},
    ]