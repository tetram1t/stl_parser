from expression_parser import build_expression


def test_simple_expression():
    code = [
        "A(",
        "A Sensor1",
        "O Sensor2",
        ")"
    ]

    tree = build_expression(code)

    assert tree.type == "AND_BLOCK"
    assert len(tree.children) == 2

    assert tree.children[0].type == "AND"
    assert tree.children[0].value == "Sensor1"

    assert tree.children[1].type == "OR"
    assert tree.children[1].value == "Sensor2"