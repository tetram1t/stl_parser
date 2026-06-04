def build_use_def(instructions):
    """
    Build USE / DEF maps.

    USE:
        Variable is read.

    DEF:
        Variable is written.
    """

    use_map = {}
    def_map = {}

    for inst in instructions:

        opcode = inst["opcode"]
        operand = inst["operand"]

        if not operand:
            continue

        # Read operations
        if opcode in [
            "A",
            "AN",
            "O",
            "ON",
            "L"
        ]:
            use_map.setdefault(
                operand,
                []
            ).append(inst["id"])

        # Write operations
        elif opcode in [
            "T",
            "=",
            "S",
            "R"
        ]:
            def_map.setdefault(
                operand,
                []
            ).append(inst["id"])

    return {
        "use": use_map,
        "def": def_map
    }