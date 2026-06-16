def export_cfg_dot(instruction_cfg):
    """
    Export instruction CFG to Graphviz DOT format.
    """

    lines = []

    lines.append("digraph CFG {")
    lines.append("    rankdir=TB;")

    for edge in instruction_cfg:
        src = edge["from"]
        dst = edge["to"]

        lines.append(f"    {src} -> {dst};")

    lines.append("}")

    return "\n".join(lines)