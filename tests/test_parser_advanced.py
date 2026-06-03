from parser import parse_stl_mvp


def test_backward_jump():
    code = """
START : NOP 0
JU START
"""

    result = parse_stl_mvp(code)

    jumps = [e for e in result["cfg_edges"] if e["kind"] == "jump"]

    assert len(jumps) == 1
    assert jumps[0]["resolved_target_id"] == 0