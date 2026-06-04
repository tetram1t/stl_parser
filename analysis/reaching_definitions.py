def build_reaching_definitions(instructions, cfg_edges=None):
    """
    Returns FLAT reaching definitions format for tests.
    """

    if not instructions:
        return []

    # ---- CFG predecessors ----
    preds = {i["id"]: [] for i in instructions}

    if cfg_edges:
        for e in cfg_edges:
            dst = e.get("resolved_target_id")
            if dst is not None:
                preds[dst].append(e["from"])
    else:
        for i in range(1, len(instructions)):
            preds[i].append(i - 1)

    # ---- collect defs ----
    var_defs = {}

    for inst in instructions:
        if inst["opcode"] in ["T", "=", "S", "R"]:
            var = inst.get("operand")
            if var:
                var_defs.setdefault(var, []).append(inst["id"])

    # ---- GEN / KILL ----
    gen = {}
    kill = {}

    for inst in instructions:
        i = inst["id"]
        op = inst["opcode"]
        var = inst.get("operand")

        gen[i] = set()
        kill[i] = set()

        if op in ["T", "=", "S", "R"] and var:
            gen[i].add((var, i))

            for d in var_defs.get(var, []):
                if d != i:
                    kill[i].add((var, d))

    # ---- DATAFLOW ----
    IN = {i["id"]: set() for i in instructions}
    OUT = {i["id"]: set() for i in instructions}

    changed = True

    while changed:
        changed = False

        for inst in instructions:
            i = inst["id"]

            in_new = set()
            for p in preds[i]:
                in_new |= OUT[p]

            out_new = gen[i] | (in_new - kill[i])

            if in_new != IN[i] or out_new != OUT[i]:
                IN[i] = in_new
                OUT[i] = out_new
                changed = True

    # ---- FLATTEN RESULT ----
    result = []

    for inst in instructions:
        i = inst["id"]

        for (var, def_id) in IN[i]:
            result.append({
                "instruction": i,
                "reaches_from": def_id,
                "variable": var
            })

    return result