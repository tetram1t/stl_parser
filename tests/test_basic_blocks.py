from parser import parse_stl_mvp
from analysis.basic_blocks import build_basic_blocks


def test_basic_blocks():

    code = """
START : NOP 0
A Sensor
JC END

L 1
T MW10

END : R Motor
"""

    parsed = parse_stl_mvp(code)

    blocks = build_basic_blocks(parsed)

    assert len(blocks) >= 3