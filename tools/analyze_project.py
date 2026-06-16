from collections import Counter
from parser import parse_stl_mvp

with open("data/stress_test.awl", encoding="utf-8") as f:
    code = f.read()

result = parse_stl_mvp(code)

print()
print("===== SUMMARY =====")
print()

print("Instructions :", len(result["instructions"]))
print("Labels       :", len(result["labels"]))
print("CFG edges    :", len(result["cfg_edges"]))
print("Warnings     :", len(result["warnings"]))

print()
print("===== WARNING TYPES =====")

for k, v in Counter(
    w["type"] for w in result["warnings"]
).items():
    print(f"{k}: {v}")

print()
print("===== OPCODE STATS =====")

opcodes = Counter()

for inst in result["instructions"]:
    if inst["opcode"]:
        opcodes[inst["opcode"]] += 1

for op, count in opcodes.most_common(20):
    print(f"{op:10} {count}")