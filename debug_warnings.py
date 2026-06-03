from parser import parse_stl_mvp

with open("data/stress_test.awl", encoding="utf-8") as f:
    code = f.read()

result = parse_stl_mvp(code)

print()
print("===== WARNINGS =====")
print()

for warning in result["warnings"][:100]:
    print(warning)