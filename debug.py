from parser import parse_stl_mvp
from pprint import pprint

code = """
A Sensor1
= Motor1
"""

result = parse_stl_mvp(code)

pprint(result["instructions"])