def build_def_use(reaching):
    """
    Converts reaching definitions → def-use chains
    """

    result = {}

    for edge in reaching:
        var = edge["variable"]
        d = edge["reaches_from"]
        u = edge["instruction"]

        if var not in result:
            result[var] = {
                "defs": set(),
                "uses": set()
            }

        result[var]["defs"].add(d)
        result[var]["uses"].add(u)

    # convert sets → lists (для стабильного вывода)
    for var in result:
        result[var]["defs"] = sorted(result[var]["defs"])
        result[var]["uses"] = sorted(result[var]["uses"])

    return result