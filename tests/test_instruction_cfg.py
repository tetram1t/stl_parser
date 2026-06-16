from parser import parse_stl_mvp
from analysis.instruction_cfg import build_instruction_cfg


def test_instruction_cfg():

    code = """
L MW10
T MW20
A Sensor1
= Motor1
"""

    ir = parse_stl_mvp(code)

    cfg = build_instruction_cfg(ir["instructions"])

    assert cfg == [
        {"from": 0, "to": 1, "kind": "fallthrough"},
        {"from": 1, "to": 2, "kind": "fallthrough"},
        {"from": 2, "to": 3, "kind": "fallthrough"},
    ]