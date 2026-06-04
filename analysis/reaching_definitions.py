def build_reaching_definitions(instructions):
    """
    Simple reaching definitions analysis.

    Tracks the latest definition of each variable and
    connects later uses to that definition.
    """

    last_definition = {}
    reaching = []

    for inst in instructions:

        opcode = inst["opcode"]
        operand = inst["operand"]

        if not operand:
            continue

        # Variable read
        if opcode in ["L", "A", "AN", "O", "ON"]:

            reaching.append({
                "instruction": inst["id"],
                "variable": operand,
                "reaches_from": last_definition.get(operand)
            })

        # Variable write
        elif opcode in ["T", "=", "S", "R"]:

            last_definition[operand] = inst["id"]

    return reaching