from analysis.pipeline import analyze
from exporters.graphviz_export import export_cfg_dot


code = """
L MW10
JU END

T MW20

END:
= Q0.0
"""

ir = analyze(code)

dot = export_cfg_dot(ir["instruction_cfg"])

with open("cfg.dot", "w", encoding="utf-8") as f:
    f.write(dot)

print("CFG exported to cfg.dot")