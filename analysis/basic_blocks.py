def build_basic_blocks(parsed):
    """
    Build basic blocks from instruction list.

    Block starts:
    - first instruction
    - jump target
    - instruction after JC
    """

    instructions = parsed["instructions"]

    if not instructions:
        return []

    leaders = {0}

    # jump targets
    for edge in parsed["cfg_edges"]:
        target = edge["resolved_target_id"]

        if target is not None:
            leaders.add(target)

    # instruction after conditional branch
    for inst in instructions:
        if inst["opcode"] == "JC":
            if inst["id"] + 1 < len(instructions):
                leaders.add(inst["id"] + 1)

    leaders = sorted(leaders)

    blocks = []

    for i, start in enumerate(leaders):

        end = (
            leaders[i + 1]
            if i + 1 < len(leaders)
            else len(instructions)
        )

        block = {
            "id": len(blocks),
            "start": start,
            "end": end - 1,
            "instructions": instructions[start:end]
        }

        blocks.append(block)

    return blocks