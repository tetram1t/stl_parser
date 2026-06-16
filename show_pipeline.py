from analysis.pipeline import analyze

code = """
L MW10
JU END

T MW20

END:
= Q0.0
"""

ir = analyze(code)

print("\n=== INSTRUCTIONS ===")
print(ir["instructions"])

print("\n=== INSTRUCTION CFG ===")
print(ir["instruction_cfg"])

print("\n=== BLOCKS ===")
print(ir["blocks"])

print("\n=== CFG ===")
print(ir["cfg"])

print("\n=== USE/DEF ===")
print(ir["use_def"])

print("\n=== REACHING ===")
print(ir["reaching"])

result = analyze(code)

print("\n=== DEF-USE ===")
print(result["def_use"])    

print("\n=== DEP GRAPH ===")
print(ir["dep_graph"])