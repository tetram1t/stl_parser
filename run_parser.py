import json

from parser import parse_stl_mvp

code = """
FOR_LOOP : NOP 0
      AN 'StartCount'
      JC END_FOR
      L "Counter"
      L 1
      <I
      JC END_FOR
      JU FOR_LOOP
END_FOR : R 'StartCount'
"""

result = parse_stl_mvp(code)

print(json.dumps(result, indent=2))