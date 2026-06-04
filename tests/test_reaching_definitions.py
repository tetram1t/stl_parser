from parser import parse_stl_mvp
from analysis.reaching_definitions import (
    build_reaching_definitions
)


def test_reaching_definitions():

    code = """
L MW10
T MW20

L MW20
T MW30
"""

    result = parse_stl_mvp(code)

    reaching = build_reaching_definitions(
        result["instructions"]
    )

    mw20_use = [
        x
        for x in reaching
        if x["variable"] == "MW20"
    ][0]

    assert mw20_use["reaches_from"] == 1