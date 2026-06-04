def build_basic_blocks(parsed):
    """
    Build classic compiler-style basic blocks.

    Block leaders:
    1. First instruction
    2. Jump targets
    3. Instruction after conditional branch
    """

    instructions = parsed["instructions"]

    if not instructions:
        return []

    leaders = {0}

    # Jump targets only
    for edge in parsed["cfg_edges"]:

        if edge["kind"] not in (
            "jump",
            "branch_true",
        ):
            continue

        target = edge["resolved_target_id"]

        if target is not None:
            leaders.add(target)

    # Instruction after conditional branch
    for inst in instructions:

        if inst["opcode"] == "JC":

            next_id = inst["id"] + 1

            if next_id < len(instructions):
                leaders.add(next_id)

    leaders = sorted(leaders)

    blocks = []

    for idx, start in enumerate(leaders):

        if idx + 1 < len(leaders):
            end = leaders[idx + 1]
        else:
            end = len(instructions)

        blocks.append({
            "id": idx,
            "start": start,
            "end": end - 1,
            "instructions": instructions[start:end]
        })

    return blocks