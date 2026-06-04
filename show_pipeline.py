from analysis.pipeline import analyze

code = """
L MW10
T MW20

A Sensor1
= Motor1
"""

result = analyze(code)

print("\n=== INSTRUCTIONS ===")
print(result["instructions"])

print("\n=== BLOCKS ===")
print(result["blocks"])

print("\n=== BLOCK CFG ===")
print(result["block_cfg"])

print("\n=== USE/DEF ===")
print(result["use_def"])

print("\n=== REACHING ===")
print(result["reaching"])

print("\n=== DEF-USE ===")
print(result["def_use"])