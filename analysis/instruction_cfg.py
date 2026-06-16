def build_instruction_cfg(instructions):
    """
    Build instruction-level CFG.

    Returns:
    [
        {"from": 0, "to": 1, "kind": "fallthrough"},
        ...
    ]
    """

    edges = []

    if not instructions:
        return edges

    for idx in range(len(instructions) - 1):
        current = instructions[idx]
        nxt = instructions[idx + 1]

        edges.append({
            "from": current["id"],
            "to": nxt["id"],
            "kind": "fallthrough"
        })

    return edges