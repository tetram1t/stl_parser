from parser import parse_stl_mvp


# 1. Forward jump (метка объявлена позже)
def test_forward_jump():
    code = """
    JU END_LABEL
    L 1
END_LABEL : NOP 0
"""
    result = parse_stl_mvp(code)

    jumps = [e for e in result["cfg_edges"] if e["kind"] == "jump"]

    assert len(jumps) == 1
    assert jumps[0]["target_label"] == "END_LABEL"
    assert jumps[0]["resolved_target_id"] == 2


# 2. Backward jump (цикл)
def test_backward_jump():
    code = """
LOOP : NOP 0
L 1
JU LOOP
"""
    result = parse_stl_mvp(code)

    jumps = [e for e in result["cfg_edges"] if e["kind"] == "jump"]

    assert len(jumps) == 1
    assert jumps[0]["resolved_target_id"] == 0


# 3. Label without instruction
def test_label_only_line():
    code = """
START :
L 1
"""

    result = parse_stl_mvp(code)

    assert result["instructions"][0]["label"] == "START"
    
    assert result["instructions"][0]["opcode"] is None

    assert result["instructions"][1]["opcode"] == "L"


# 4. Network header (TIA STL export)
def test_network_header():
    code = """
NETWORK
TITLE = Motor Logic

A Sensor1
= Motor1
"""
    result = parse_stl_mvp(code)

    assert isinstance(result, dict)


# 5. CALL FB
def test_call_fb():
    code = """
CALL FB100
"""
    result = parse_stl_mvp(code)

    assert len(result["instructions"]) == 1
    assert result["instructions"][0]["opcode"] == "CALL"


# 6. DB addressing
def test_db_addressing():
    code = """
L DB10.DBW0
"""
    result = parse_stl_mvp(code)

    assert len(result["instructions"]) == 1
    assert result["instructions"][0]["operand"] == "DB10.DBW0"


# 7. Nested boolean expression
def test_nested_boolean_expression():
    code = """
A(
A Sensor1
O Sensor2
)
JC END1
END1 : NOP 0
"""
    result = parse_stl_mvp(code)

    warning_types = {w["type"] for w in result["warnings"]}

    assert "complex_syntax_stub" in warning_types


# 8. Unknown opcode
def test_unknown_opcode():
    code = """
XYZ SomeOperand
"""
    result = parse_stl_mvp(code)

    assert len(result["instructions"]) == 1


# 9. Multiple unresolved jumps
def test_multiple_unresolved_jumps():
    code = """
JC MISSING1
JU MISSING2
"""
    result = parse_stl_mvp(code)

    unresolved = [
        w
        for w in result["warnings"]
        if w["type"] == "unresolved_jump_target"
    ]

    assert len(unresolved) == 2


# 10. Realistic STL fragment
def test_realistic_stl_fragment():
    code = '''
NETWORK
TITLE = Robot Safety

A     "DoorClosed"
AN    "EStop"
JC    STOP

L     MW100
L     1
+I
T     MW100

STOP : R "RobotEnable"
'''

    result = parse_stl_mvp(code)

    labels = result["labels"]

    assert "STOP" in labels

    branches = [
        e
        for e in result["cfg_edges"]
        if e["kind"] == "branch_true"
    ]

    assert len(branches) == 1