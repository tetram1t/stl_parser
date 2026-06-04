from parser import parse_stl_mvp
from analysis.dataflow import build_use_def


def test_use_def():

    code = """
L MW10
T MW20

A Sensor1
= Motor1
"""

    result = parse_stl_mvp(code)

    df = build_use_def(
        result["instructions"]
    )

    assert "MW10" in df["use"]
    assert "MW20" in df["def"]

    assert "Sensor1" in df["use"]
    assert "Motor1" in df["def"]